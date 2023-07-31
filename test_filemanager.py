from bank import str2float, add_cash, buy_obj

def test_str2float():
    a, r_a = "5.15", 5.15
    assert str2float(a) == r_a

def test_add_cash():
    a, b, r_a = 5.15, 10.85, 16
    assert add_cash(a, b) == r_a