from math_func import f_pi, f_pow, f_sqrt, f_hypot

def test_f_pi_v1():
    pi_real = "3.141592"
    assert str(f_pi())[0:8] == pi_real

def test_f_pi_v2():
    pi_real = 3.141592
    assert abs(f_pi() - pi_real) < 1e-6

def test_f_sqrt_v1():
    a1, sq_a1 = 4, 2
    a2, sq_a2 = 9, 3
    a3, sq_a3 = 2.25, 1.5
    assert abs(f_sqrt(a1) - sq_a1) < 1e-6
    assert abs(f_sqrt(a2) - sq_a2) < 1e-6
    assert abs(f_sqrt(a3) - sq_a3) < 1e-6

def test_f_pow_v1():
    a, b, res = 5, 2, 25
    assert abs(f_pow(a, b) - res) < 1e-6

    a, b, res = 13, 4, 28561
    assert abs(f_pow(a, b) - res) < 1e-6

def test_f_hypot_v1():
    a, b, c = 3, 4, 5
    assert abs(f_hypot(a, b) - c) < 1e-6