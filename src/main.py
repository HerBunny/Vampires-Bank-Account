import time

years = int(input("How many years, is your vampire investing his income for? "))

def period(y):  
  m = y * 12
  return m

months = period(years)
  
# Period related variables
salary = 10
annual_increase = 3
principle = 0
year = 1

# Bank account related variables
currency = '$'
bankbalance = 0.00
deposit = salary * 0.1
interest = 4.5

print("Year " + str(year))
print(currency + '{:,.2f}'.format(bankbalance))

while months > 0:
  bankbalance = bankbalance + deposit + (bankbalance * (interest/100))/12
  principle = principle + deposit
  months = months - 1
  if months % 12 == 0 and months > 0:
    print()
    year = year + 1
    print("Year " + str(year))
    salary = salary + (salary * (annual_increase/100))
    deposit = salary/10
    print("Salary: $" + str(salary))
       
  print(currency + '{:,.2f}'.format(bankbalance))
  #time.sleep(1/24)

print()  
print("Principle: " + currency + str('{:,.2f}'.format(principle)))
print("Interest earned: " + currency + str('{:,.2f}'.format(bankbalance - principle)))
