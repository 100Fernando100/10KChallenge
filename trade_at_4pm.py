import json

# Sample static trades data (you can modify this later with dynamic logic)
trades = {
    "alex": {
        "action": "No trade",
        "symbol": "ETH/USDT",
        "price": 2000.48,
        "explanation": "Alex did not trade because the RSI (44.72) was not in overbought or oversold territory."
    },
    "zoe": {
        "action": "No trade",
        "symbol": "BTC/USDT",
        "price": 85013.0,
        "explanation": "Zoe did not trade because the price did not break above the 20-period moving average ($84777.80) with sufficient momentum (-0.17%)."
    },
    "priya": {
        "action": "No trade",
        "symbol": "ADA/USDT",
        "price": 0.703441,
        "explanation": "Priya did not trade because the 24-hour price change (-0.23%) was not significant enough."
    },
    "liam": {
        "action": "No trade",
        "symbol": "BTC/USDT",
        "price": 85157.0,
        "explanation": "Liam did not trade because there was not enough data for the 200-period moving average."
    }
}

# Write the trades data to trades.json
with open('trades.json', 'w') as f:
    json.dump(trades, f, indent=4)

print("trades.json has been updated!")