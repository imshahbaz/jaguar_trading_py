Strategy = [
    {"name": "SuperBull", "active": False,
     "condition": "( {46553} ( latest adx di positive( 14 ) > latest adx di negative( 14 ) and latest close > latest open and latest close >= ( ( ( latest high - latest low ) * .8 ) + latest low ) and latest open <= ( ( ( latest high - latest low ) * .2 ) + latest low ) and latest close > latest supertrend( 10 , 3 ) and 1 day ago close < ( 1.01 * 2 days ago close ) ) )"},
    {"name": "RSE", "active": True,
     "condition": "( {46553} ( latest rsi( 14 ) > 55 and 1 day ago  rsi( 14 ) <= 55 and latest close > latest supertrend( 10 , 3 ) and latest ema( latest close , 3 ) > latest ema( latest close , 30 ) and latest close > latest open ) )"}
    , {
        "name": "Rollinger", "active": True,
        "condition": "( {46553} ( latest low <= latest sma( latest close , 20 ) and latest close > latest open and latest close > latest supertrend( 10 , 3 ) and latest close > latest sma( latest close , 20 ) and latest high < latest upper bollinger band( 20 , 2 ) and latest rsi( 14 ) > 50 and latest close >= ( ( latest high - latest low ) * .7 ) + latest low ) )"
    }
]
