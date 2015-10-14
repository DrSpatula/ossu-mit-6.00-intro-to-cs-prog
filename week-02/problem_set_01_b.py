initial_balance = float(
    raw_input("Enter the outstanding balance on your credit card: "))
interest_rate = float(
    raw_input("Enter the annual credit card interest rate as a decimal: "))
monthly_interest_rate = interest_rate / 12.0


for payment in range(10, int(initial_balance), 10):
    month = 1
    balance = initial_balance

    while month <= 12 and balance >= 0:
        balance = (balance * (1 + monthly_interest_rate)) - payment
        month += 1

    if balance <= 0:
        print "Results:"
        print "Monthly payment needed to pay off debt", \
            "in one year: ${0:.2f}".format(payment)
        print "Number of months needed: {0:d}".format(month - 1)
        print "Balance: ${0:.2f}".format(balance)
        break
