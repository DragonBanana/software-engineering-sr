def calculate_loan_plan(principal, rate, months, plan_type):
    """Calculate loan repayment details based on the given plan."""
    if not isinstance(principal, (int, float)) or principal <= 0:
        raise ValueError("Principal must be a positive number")
    if not isinstance(rate, (int, float)) or rate < 0:
        raise ValueError("Rate must be a non-negative number")
    if not isinstance(months, int) or months <= 0:
        raise ValueError("Months must be a positive integer")
    if plan_type not in ["standard", "accelerated", "interest-only"]:
        raise ValueError("Invalid plan type")

    monthly_rate = rate / 100 / 12
    total_repayment = 0
    total_interest = 0
    monthly_payment = 0
    balance = principal

    if plan_type == "standard":
        # Calculate fixed monthly payment using the formula:
        # M = P * r * (1 + r)^n / ((1 + r)^n - 1)
        if monthly_rate == 0:
            monthly_payment = principal / months
        else:
            monthly_payment = (
                principal
                * monthly_rate
                * (1 + monthly_rate) ** months
                / ((1 + monthly_rate) ** months - 1)
            )
        total_repayment = monthly_payment * months
        total_interest = total_repayment - principal

    elif plan_type == "accelerated":
        # Payments increase by 1% each month
        month = 1
        while month <= months:
            monthly_payment = (principal / months) * (1 + 0.01 * month)
            interest = balance * monthly_rate
            total_interest += interest
            balance -= (monthly_payment - interest)
            total_repayment += monthly_payment
            month += 1

    elif plan_type == "interest-only":
        # Pay only the interest each month, principal at the end
        month = 1
        while month < months:
            monthly_payment = principal * monthly_rate
            total_interest += monthly_payment
            total_repayment += monthly_payment
            month += 1
        total_repayment += principal  # Add the principal at the end

    return {
        "monthly_payment": round(monthly_payment, 2),
        "total_repayment": round(total_repayment, 2),
        "total_interest": round(total_interest, 2),
    }

import unittest
# from loan_calculator import calculate_loan_plan

class TestCalculateLoanPlan(unittest.TestCase):
    def test_standard_plan(self):
        result = calculate_loan_plan(10000, 5, 24, "standard")
        self.assertEqual(result["monthly_payment"], 438.71)
        self.assertEqual(result["total_repayment"], 10529.04)
        self.assertEqual(result["total_interest"], 529.04)

    def test_accelerated_plan(self):
        result = calculate_loan_plan(5000, 3, 12, "accelerated")
        self.assertEqual(result["monthly_payment"], 505.83)
        self.assertEqual(result["total_repayment"], 6155.96)
        self.assertEqual(result["total_interest"], 1155.96)

    def test_interest_only_plan(self):
        result = calculate_loan_plan(15000, 4, 36, "interest-only")
        self.assertEqual(result["monthly_payment"], 50.0)
        self.assertEqual(result["total_repayment"], 16800.0)
        self.assertEqual(result["total_interest"], 1800.0)

    def test_invalid_principal(self):
        with self.assertRaises(ValueError):
            calculate_loan_plan(0, 5, 24, "standard")

    def test_invalid_rate(self):
        with self.assertRaises(ValueError):
            calculate_loan_plan(10000, -2, 24, "standard")

    def test_invalid_months(self):
        with self.assertRaises(ValueError):
            calculate_loan_plan(10000, 5, 0, "standard")

    def test_invalid_plan_type(self):
        with self.assertRaises(ValueError):
            calculate_loan_plan(10000, 5, 24, "invalid-plan")

if __name__ == "__main__":
    unittest.main()