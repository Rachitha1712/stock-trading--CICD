def trading_decision(price):

    if price < 100:
        return "BUYED"

    elif price <= 200:
        return "HOLD"

    else:
        return "SELL"


if __name__ == "__main__":

    price = int(input("Enter Stock Price: "))

    print(trading_decision(price))