Strategy = [
  {
    "name": "20:50",
    "active": True,
    "condition": "({46553} ( latest ema( latest close , 20 ) > latest ema( latest close , 50 ) and latest ema( latest close , 50 ) > latest ema( latest close , 200 ) and latest open <= latest ema( latest close , 20 ) and latest close > latest ema( latest close , 20 ) and latest rsi( 14 ) >= 55 ))"
  }
]
