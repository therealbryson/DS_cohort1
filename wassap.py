# age = int(input('How old are you?'))
# age_left = 90-age
# print(f'You have {age_left*365} days, {age_left*52} weeks, and {age_left*12} months left.')

#LOGICAL OPERATORS WITH IF STATEMENT
# order_total=150
# member=True

# if order_total>=100 and member==True:
#     print('Discount is applied')
# else:
#     print('Customer not qualify for')

# not logical operator
# is_member=False
# if not is_member:
#     print('The Customer is a member')
# else:
#     print('The Customer is not a member')


#print(not(False))

# number=16
# if not(number>15):
#     print(number)
# else:
#     print(number-3)


# number=5
# if number%2==0:
#     print('numberis even')
# else:
#     print('number is odd')


# number=17
# if number%2==0 and number>10:
#     print('number is divisble by 2 and is greater than 10')
# else:
#     print('number is not divible by 2')




number=6
if number%2==0 and number>10:
    print('number is divisble by 2 and is greater than 10')
elif number%2==0 and number<10:
    print('number is divisible by 2 but less than 10')
else:
    print('Number is odd')