Strategy = [
  {
    "name": "20:50",
    "active": True,
    "condition": "({46553} ( latest ema( latest close , 20 ) > latest ema( latest close , 50 ) and latest ema( latest close , 50 ) > latest ema( latest close , 200 ) and latest open <= latest ema( latest close , 20 ) and latest close > latest ema( latest close , 20 ) and latest rsi( 14 ) >= 55 ))"
  },
  
  {
    "name": "Dual Rsi",
    "active": True,
    "condition": "({46553} ( weekly rsi( 7 ) > 60 and latest rsi( 7 ) > 40 and 1 day ago  rsi( 7 ) <= 40 and latest close > latest open ))"} 
]
