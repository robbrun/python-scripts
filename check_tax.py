price = input('How much did you pay? ')
price = float(price)
if price >= 1.00:
    tax = .07
#    print('Tax rate is: ' + str(tax))
else:
    tax = 0
print('Tax rate is: ' + str(tax))     
   
total_price = ((price * tax) + price)
print('Total price paid: $' + str(total_price))    