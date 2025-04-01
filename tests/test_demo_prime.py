from demo_prime import is_prime_number

def test_prime_true():
    assert is_prime_number(7) is True

def test_prime_false():
    assert is_prime_number(8) is False

def test_zero_not_prime():
    assert is_prime_number(0) is False

def test_one_not_prime():
    assert is_prime_number(1) is False

def test_negative_not_prime():
    assert is_prime_number(-5) is False
