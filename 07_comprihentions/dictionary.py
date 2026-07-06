tea_prices_inr = {
    "masala chai":40,
    "lemon tea":50,
    "elichi_chai":80
}

tea_price_usd = {tea:price/100 for tea,price in tea_prices_inr.items()}

print(tea_price_usd)