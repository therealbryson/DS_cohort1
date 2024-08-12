my_string='Welcome to GoMyCode'
# for i in my_string:
#     print(f'The Current LETTER IS {i}')

# loop in range 
# for num in range(1,20):
#     print(num)

# for index, value in enumerate(my_string):#Enumerate give index and element 
#     print(index,value)

# list1=['Go','My','Code','Data','Nerd']
# for index,ele in enumerate(list1):
#     print(f'the index is {index} and THE element is {ele}')

# LOOP in dictionary
# my_dic={'Name':'Enoch','Super Skill':'Data Science','Cohort':'1'}
# for key, value in my_dic.items():
#     print(key,value)


# for a in range(1,4):
#     for b in range(1,4):
#         for c in range(1,3):
#             print(a,b,c)


# num_l=[1,2,3,4,5,6,7,8,9,10]       
result=[x for x in range(1,10) if x%2==0]
print(result)

# for x in num_l:
#     if x%2==0:
#        print(x)
 
 #LOOP IN ZIP 
l1=['Data Science','Software', 'Webdesign']
l2=['Python','Javascript','Html']

for skill,tools in zip(l1,l2):
    print(f'The skill {skill} uses {tools} tools')


