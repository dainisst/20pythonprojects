# collect the necessary inputs: principal, apr, years
# calculate the monthly payment
# show to the user

def main():
  print("this is monthly payment loan calculator")
  print("")

  pricipal = float(input("input the loan amount: "))
  apr = float(input("input the annual interest rate: "))
  years = int(input("input number of years: "))

  monthly_apr = apr / 12 / 100
  number_of_months = years * 12
  monthly_payment = pricipal * monthly_apr / (1 - (1 + monthly_apr) ** (-number_of_months))

  print(f"the monthly payment for the loan is: {round(monthly_payment, 2)}")

main()