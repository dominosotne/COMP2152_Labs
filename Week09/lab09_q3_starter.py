# ============================================================
#  WEEK 09 LAB — Q3: UNIT TESTING
#  COMP2152 — Alikhan Zhilkibayev
# ============================================================

import unittest


# --- Functions to test (provided) ---
# Error handling example from Week 06 is inside is_valid_ip().

def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit: c * 9/5 + 32"""
    return c * 9 / 5 + 32


def is_valid_ip(address):
    """Return True if address is a valid IPv4 string (4 octets, 0-255)."""
    try:
        parts = address.split(".")
        if len(parts) != 4:
            return False
        for p in parts:
            if int(p) < 0 or int(p) > 255:
                return False
        return True
    except (ValueError, AttributeError):
        return False


def fizzbuzz(n):
    """Return 'FizzBuzz', 'Fizz', 'Buzz', or str(n)."""
    if n % 15 == 0: return "FizzBuzz"
    if n % 3 == 0:  return "Fizz"
    if n % 5 == 0:  return "Buzz"
    return str(n)


# TODO: Complete TestCelsius
#   test_freezing  → celsius_to_fahrenheit(0)   == 32.0
#   test_boiling   → celsius_to_fahrenheit(100) == 212.0
#   test_negative  → celsius_to_fahrenheit(-40) == -40.0
class TestCelsius(unittest.TestCase):
    pass


# TODO: Complete TestValidIP
#   test_valid         → is_valid_ip("192.168.1.1") is True
#   test_invalid_octet → is_valid_ip("256.1.1.1")   is False
#   test_too_few_parts → is_valid_ip("1.2.3")       is False
#   test_empty         → is_valid_ip("")            is False
class TestValidIP(unittest.TestCase):
    pass


# TODO: Complete TestFizzBuzz
#   test_fizz     → fizzbuzz(3)  == "Fizz"
#   test_buzz     → fizzbuzz(5)  == "Buzz"
#   test_fizzbuzz → fizzbuzz(15) == "FizzBuzz"
#   test_number   → fizzbuzz(7)  == "7"
class TestFizzBuzz(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()