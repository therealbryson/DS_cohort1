word='Welcome To Data Science'
s_to_upper=lambda s: s.upper()
print(s_to_upper(word))

s_split=lambda string:string.split(' ')
print(s_split(word))


print(sum_num(4,5,6))

check_format=lambda num:f'(num:e)' if isinstance(num,int)else f'(num: .2f)'

print(check_format(100000))
print(check_format(1234.569))


list_i=[1,2,4,5,6,7,8,9,10,11]
filter_element= list(filter)