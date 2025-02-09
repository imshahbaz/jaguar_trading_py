import datetime
import os
import sys
import warnings

import pytz
from nselib import capital_market

from constants import Margins
from constants.ch_strategy import Strategy

warnings.filterwarnings("ignore")

try:
    import xlwings as xw
except (ModuleNotFoundError, ImportError):
    print("xlwings module not found")
    os.system(f"{sys.executable} -m pip install -U xlwings")
finally:
    import xlwings as xw

try:
    import requests
except (ModuleNotFoundError, ImportError):
    print("requests module not found")
    os.system(f"{sys.executable} -m pip install -U requests")
finally:
    import requests

try:
    import pandas as pd
except (ModuleNotFoundError, ImportError):
    print("pandas module not found")
    os.system(f"{sys.executable} -m pip install -U pandas")
finally:
    import pandas as pd

try:
    from bs4 import BeautifulSoup
except (ModuleNotFoundError, ImportError):
    print("BeautifulSoup module not found")
    os.system(f"{sys.executable} -m pip install -U beautifulsoup4")
finally:
    from bs4 import BeautifulSoup

Charting_Link = "https://chartink.com/screener/"
Charting_url = 'https://chartink.com/screener/process'
api = "https://apiway.ai/webhooks/catch/661b9ad15daec/webhooks-app"


def GetDataFromChartink(payload):
    payload = {'scan_clause': payload}

    with requests.Session() as s:
        r = s.get(Charting_Link)
        soup = BeautifulSoup(r.text, "html.parser")
        csrf = soup.select_one("[name='csrf-token']")['content']
        s.headers['x-csrf-token'] = csrf
        r = s.post(Charting_url, data=payload)

        df = pd.DataFrame()
        for item in r.json()['data']:

            if len(item) > 0:
                df = pd.concat([df, pd.DataFrame.from_dict(item, orient='index').T], ignore_index=True)

    return df


def get_data(strategy, gsheet_margin):
    data = GetDataFromChartink(strategy["condition"])
    message = ""
    final_list = []
    if len(data) > 0:
        stock_names = data["nsecode"]
        for stock in stock_names:
            if gsheet_margin.get(stock) is not None:
                final_list.append(gsheet_margin.get(stock))

    if len(final_list) > 0:
        final_list.sort(key=lambda x: x["percent"], reverse=True)
        message += "Strategy : " + strategy["name"] + "\n"
        for stock in final_list:
            message += ("\n%s ( %s ) %d\n" % (stock.get("name"), stock.get("symbol"), stock.get("percent")))

    if message != "":
        formdata = {"stocks": message}
        requests.post(api, data=formdata)

    return message


def publish_message():
    utc_now = datetime.datetime.utcnow()

    indian_timezone = pytz.timezone('Asia/Kolkata')
    indian_now = utc_now.astimezone(indian_timezone)

    indian_day_string = indian_now.strftime("%A")

    if indian_day_string == "Saturday" or indian_day_string == "Sunday":
        return "Weekend"

    gsheet_margin = get_g_sheet()
    for strategy in Strategy:
        if strategy['active']:
            get_data(strategy=strategy, gsheet_margin=gsheet_margin)

    return "Success"


async def get_hist_data(symbol: str, fromDate: str, toDate: str):
    return capital_market.price_volume_and_deliverable_position_data(symbol=symbol, from_date=fromDate, to_date=toDate)


def get_g_sheet():
    try:
        url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTb4OSG_m0d7SoEaVL70BwiO0VgwHKVLIXNOClkkJkXefRp33tYVOUAU_DXfwuLmFfJ-PmRI_qfIsHW/pub?output=csv"
        response = requests.get(url)
        response.raise_for_status()

        open('dataset.csv', 'wb').write(response.content)
        df = pd.read_csv('dataset.csv')
        g_sheet_margin = {}
        for row in df.itertuples():
            if row.percent >= 60:
                g_sheet_margin[row.symbol] = {"name": row.name, "symbol": row.symbol, "percent": row.percent}

        return g_sheet_margin

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

    finally:
        os.remove('dataset.csv')
