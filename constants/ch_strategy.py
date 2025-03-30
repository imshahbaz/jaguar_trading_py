Strategy = [
    {
        "name": "20:50",
        "active": False,
        "condition": "({46553} ( latest ema( latest close , 20 ) > latest ema( latest close , 50 ) and latest ema( latest close , 50 ) > latest ema( latest close , 200 ) and latest open <= latest ema( latest close , 20 ) and latest close > latest ema( latest close , 20 ) and latest rsi( 14 ) >= 55 ))"
    },
    {
        "name": "Super Rsi",
        "active": True,
        "condition": "( {46553} ( latest close > latest open and latest close > latest supertrend( 10 , 3 ) and latest rsi( 14 ) > 60 and 1 day ago  rsi( 14 ) <= 60 ) )"
    }
    , {
        "name": "Vollinger",
        "active": False,
        "condition": "( {46553} ( latest close > latest open and latest close > latest sma( latest close , 20 ) and latest volume > 1 day ago volume and latest low <= latest sma( latest close , 20 ) and latest close >= ( ( latest high - latest low ) * 0.7 ) + latest low ) )"
    },
    {
        "name": "521",
        "active": True,
        "condition": "( {46553} ( latest close > latest open and latest ema( latest close , 5 ) > latest ema( latest close , 10 ) and latest ema( latest close , 10 ) > latest ema( latest close , 21 ) and latest low <= latest ema( latest close , 5 ) and latest low > latest ema( latest close , 10 ) ) )"
    }
]
