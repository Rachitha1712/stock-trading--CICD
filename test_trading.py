from trading import trading_decision

def test_buy():
    assert trading_decision(80) == "BUY"

def test_hold():
    assert trading_decision(150) == "HOLD"

def test_sell():
    assert trading_decision(250) == "SELL"