import unittest

def calculate(first_operand: int, second_operand: int, operator: str) -> int | float:
    match operator:
        case '+':
            result = first_operand + second_operand
        case '-':
            result = first_operand - second_operand
        case '*':
            result = first_operand * second_operand
        case '/':
            if second_operand != 0:
                result = first_operand / second_operand
            else:
                raise ArithmeticError("Division by zero is not possible")
        case _:
            raise ValueError("Unexpected value operator: " + operator)
    return result


def calculate_discount(purchase_amount: float, discount_amount: int) -> float:
    if discount_amount < 0:
        raise ArithmeticError("Discount can't be less then zero")
    elif discount_amount > 100:
        raise ArithmeticError("Discount can't be more then 100")

    return purchase_amount - discount_amount / 100 * purchase_amount


class TestCalculator(unittest.TestCase):
    def test_result(self):
        self.assertEqual(90.0, calculate_discount(purchase_amount=100, discount_amount=10))

    def test_zero_result(self):
        self.assertEqual(0, calculate_discount(purchase_amount=0, discount_amount=10))

    def test_zero_discount(self):
        self.assertEqual(100, calculate_discount(purchase_amount=100, discount_amount=0))

    def test_discount_less_0(self):
        self.assertRaisesRegex(ArithmeticError, "Discount can't be less then zero",
                               calculate_discount, purchase_amount=100, discount_amount=-5)

    def test_discount_more_100(self):
        self.assertRaisesRegex(ArithmeticError, "Discount can't be more then 100",
                               calculate_discount, purchase_amount=100, discount_amount=110)


if __name__ == '__main__':
    unittest.main(verbosity=2)