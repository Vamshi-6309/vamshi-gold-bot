def get_signal(candles):
    if len(candles) < 2:
        return "WAIT"

    previous = candles[-2]
    current = candles[-1]

    if (
        previous["close"] < previous["open"]
        and current["close"] > current["open"]
        and current["close"] > previous["high"]
    ):
        return "BUY"

    if (
        previous["close"] > previous["open"]
        and current["close"] < current["open"]
        and current["close"] < previous["low"]
    ):
        return "SELL"

    return "WAIT"


print("Vamshi Gold Bot Started")
print("Market: XAUUSD")
print("Timeframe: 15 Minutes")
print("Signal logic ready")
