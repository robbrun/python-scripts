country = input('What country do you live in? ')
tax = 0

if country.lower() == 'canada':
    province = input('What province/state do you live in? ')
    if province.lower() in('alberta','nunavut','yukon'):
        tax = 0.05
    elif province.lower() == 'ontario':
        tax = 0.13
    else:
        tax = 0.15 
else:
    tax = 0.0
print(tax)