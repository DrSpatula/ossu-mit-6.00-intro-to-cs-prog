balance = float(
    raw_input("Enter the outstanding balance on your credit card: "))
interest_rate = float(
    raw_input("Enter the annual credit card interest rate as a decimal: "))
monthly_payment_rate = float(
    raw_input("Enter the minimum monthly payment rate as a decimal: "))


total_paid = 0.0

for i in range(1, 13):
    minimum_payment = round(balance * monthly_payment_rate, 2)
    interest_paid = round((interest_rate / 12.0) * balance, 2)
    principal_paid = round(minimum_payment - interest_paid, 2)
    remaining_balance = round(balance - principal_paid, 2)

    print "Month: {0}".format(i)
    print "Minimum monthly payment: ${0:.2f}".format(minimum_payment)
    print "Principle paid: ${0:.2f}".format(principal_paid)
    print "Remaining balance: ${0:.2f}\n".format(remaining_balance)

    balance = remaining_balance
    total_paid += minimum_payment

print "RESULT"
print "Total amount paid: ${0:.2f}".format(total_paid)
print "Remaining balance: ${0:.2f}".format(balance)
