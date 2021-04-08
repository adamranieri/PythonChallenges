import unittest

# write a method that takes in a a phone_number as a string
# raise an InvalidLength if number is too long or too short (should be 10 numbers exactly)
# raise an InvalidCharacter if number contains any letters
# any other chracter should be ignored

class InvalidLength(Exception):
    pass

class InvalidCharacter(Exception):
    pass

def standardizd_phone_number(phone_number):
    pass


########################### TESTS ##############################################################
class TestMethods(unittest.TestCase):

    def test_currency_1(self):
        phone_number = standardizd_phone_number('555-555-5555')
        pass
        
    def test_currency_2(self):
        pass

if __name__ == '__main__':
    unittest.main()