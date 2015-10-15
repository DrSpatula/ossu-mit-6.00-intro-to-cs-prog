initial_balance = float(
    raw_input("Enter the outstanding balance on your credit card: "))
interest_rate = float(
    raw_input("Enter the annual credit card interest rate as a decimal: "))
monthly_interest_rate = interest_rate / 12.0

lower_bound = initial_balance / 12.0
upper_bound = (initial_balance * (1 + monthly_interest_rate)**12) / 12.0


def get_payment():
    return round((lower_bound + upper_bound) / 2.0, 2)


payment = get_payment()
e = 0.15

while payment >= lower_bound and payment <= upper_bound:
    balance = initial_balance

    for month in range(1, 13):
        balance = (balance * (1 + monthly_interest_rate)) - payment
        month += 1

    if abs(0 - balance) <= e:
        print "Results:"
        print "Monthly payment needed to pay off debt", \
            "in one year: ${0:.2f}".format(payment)
        print "Number of months needed: {0:d}".format(month - 1)
        print "Balance: ${0:.2f}".format(balance)
        break
    else:
        if balance > 0:
            lower_bound = payment
        else:
            upper_bound = payment

    payment = get_payment()
