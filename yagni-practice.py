# You aren't gonna need it (YAGNI)

# Always implement things when you actually need them, never when you just foresee that you might need them.

# The rationale behind YAGNI is simple: every line of code we write comes with a cost.

# Example: Payment processing

# Over-engineered


def process_payment(self, amount, payment_method):
    if payment_method == "credit_card":
        pass
    elif payment_method == "debit_card":
        pass
    elif payment_method == "upi":
        pass
    elif payment_method == "wallet":
        pass
    elif payment_method == "cash":
        pass


# YAGNI-aligned


def process_payment(self, amount, payment_method):
    if payment_method == "cash":
        pass


# Benefits of YAGNI

# 1. Simplified codebase
# 2. Faster development


# When YAGNI might be inappropriate

# 1. Well known Requirements
# 2. Performance critical areas -> Sometimes, a less-than-optimal but more general solution
# is necessary initially to ensure performance targets are met.
