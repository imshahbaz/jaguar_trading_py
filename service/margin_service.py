import os
import warnings
import sys
from constants import Margins
import requests
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
                df = pd.concat([df, pd.DataFrame.from_dict(item,orient='index').T],ignore_index = True)
            
    return df

def get_data(strategy):
    data = GetDataFromChartink(strategy["condition"])
    message = ""
    final_list=[]
    if len(data) > 0:
        list= data["nsecode"]
        for stock in list:
            if Margins.get(stock) != None:
                final_list.append(Margins.get(stock))
                
    if len(final_list)>0:
        final_list.sort(key=lambda x:x["percent"],reverse=True)
        message+=  "Strategy : "+ strategy["name"]+"\n"
        for stock in final_list:
            message+= ("\n%s ( %s ) %d\n"%(stock.get("name"),stock.get("symbol"),stock.get("percent")))
                        
    if message != "":
        formdata = {"stocks":message}
        requests.post(api,data=formdata)

    return message


def publish_message():
    for strategy in Strategy:
        get_data(strategy=strategy)

    return "Success"    
