import time

months = 500 * 12
currency = '$'
bankbalance = 0.00
deposit = 1
interest = 4.5
principle = 0
year = 1

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
       
  print(currency + '{:,.2f}'.format(bankbalance))
  time.sleep(1/24)

print()  
print("Principle: " + currency + str('{:,.2f}'.format(principle)))
print("Interest earned: " + currency + str('{:,.2f}'.format(bankbalance - principle)))