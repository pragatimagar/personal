# x = 1j
# print(type(x))  

# #-------------frozenset-----------------
# lst = [1,2,3,4,5,6]
# #converting list into frozenset
# num = frozenset(lst)
# print(num)

#---------floor devision------------

# a = 9//2
# print(a)

# my_income = 25
# tax_rate = 0.2

# my_tax = my_income*tax_rate
# print(my_tax)

# a = 10
# a = a+10
# print(a)

# print('use \n to print new line')
# print('\n')

# name = 'pragati'
# print(len(name))

# intr = 'My Name'
# # print(intr[0])
# # print(intr[ :5])
# # print(intr[1:])
# # print(intr[-3:1])
# # print(intr[::-1])
# print(intr.split('y'))


# data = int(input('enter a num'))
# # print(data*10)
# print(data*10)

# data = int(input())
# print(data*10)

# data = int(input())
# print(data)

# data = int(input())
# # print(data*10)
# data = input()
# print(data)

# print('My name is ','Pragati')
# print('My name is {}'.format('Pragati'))
# print('I am {1} and my age is {0}'.format('Pragati',25))

#----------------padding & precision of floating point number----------------
#  print('The floating point number : %1.2f' %(13.456))
# print('Floating point numbers: %1.0f' %(13.144))

# print('Floating point number : %2.0f' %(13.456))

# print('Floating point number : %25.2f' %(16.98526) )


# print('Floating point number : %1.0f' %(16.245))

# print('First :%s ,Second :%1.0f,Third:%s '%('pragii',16.1,'yes'))

# print('First={2},second={0} and third={1}'.format('age',26,'same'))

# a = 'this is a string'
# a = a.split()
# print(a)
# a = '/'.join(a)
# print(a)


# print ('{0:8} | {9:1}'.format('Fruits','names'))
# print ('{0:8} | {9:1}'.format('frt1','apple'))
# print ('{0:8} | {9:1}'.format('frt2','mango'))




# print('My name is {}'.format('Pragati'))
# print(f'My name is {'pragati'}')

# name = 'pragati'
# print(f'My name is {name}')


# print('output value is : %1.0f' %(15.666))

# my_list = ['ages',25,'same',0.256]
# # my_list = my_list + ['here']
# # my_list += ['here']

# my_list += ['ram',25]
# print(my_list)

# print(my_list*2)
# print(my_list)
# print(my_list.append('append me!'))
# print(my_list)
# print(my_list.pop(0))
# print(my_list)

# my_list.remove('same')
# print(my_list)
# print(list(my_list.reverse()))

# a = [5,6,7,1,8,9]
# print(list(a.sort())) #-------------doubt------------



# list1 = [4,5,6]
# list2 = [7,8,9]
# list3 = [10,11,12]

# matrix = [list1,list2,list3]
# print(matrix)
# # list2[0]=2
# # print(list2)
# # print(matrix)
# new_list = [row[2]for row in matrix]
# print(new_list)

# lst = ['apple','banana','mango']
# lst.insert(1,'watermelon')
# print(lst)


# new_lst = ['apple','mango','banana','kiwi']
# lst = []
# for x in new_lst:
#     if 'a' in x:
#         lst.append(x)
# print(lst)        


# lst1 = ['Rahul',5]
# lst2 = ['suraj',1]
# lst3 = ['ram',9]
# matrix = [lst1,lst2,lst3]
# print(matrix[1])      

# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
  
# final_output = [[i,j,k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if ((i+j+k)!=n)]
# print(final_output)

# my_dict = {'key1':25,'key2':'get'}
# print(my_dict)

# d = {}
# d['animal']='dog'
# print(d)
# my_dict['key2'] = 1
# print(my_dict)
# print(len(my_dict))
# my_dict['key3'] = ['sweet',13,'get']
# print(my_dict)
# my_dict['key3'][1] = 26
# my_dict['key3'][0].upper()
# print(my_dict)
# my_dict['key2'].upper()
# print(my_dict)
# my_dict['key1'] = my_dict['key1']-10
# print(my_dict)

# dict = {'key' :{'name' :{'same' : 'zero'}}}
# print(dict ['key']['name']['same'])

# t = (1,5,'name',0.25)
# print(len(t))
# print(t[1])
# print(t.index('name'))

# x = set()
# x.add(1)
# x.add(2)
# print(x)

# list1 = [1,1,5,2,4,6,4,5]
# print(list(set(list1)))

# a = 4 * (6 + 5)
# print(a)

# a = 3
# print(a*0.5)

# lst = []
# lst.append(0)
# lst.append(0)
# lst.append(0)

# print(lst)

# if (1==1):
#     print('im in if st')
# else:
#     print('im not')  

# a = []
# if a:
#     print('im in if')
#     if (1==3):
#         print('im true')
# else:
#     print('in am in else')          

# if False:
#     print('im in if')
# else:
#     print('im not')
# 
# person = 'pragati'

# if person == 'sammy':
#     print('its correct')
# elif person == 'shreyas':
#      print('its wrong')
# else:
#     print('non there')

# x = 15

# if x > 10:
#     print('even no')
#     if x > 20:
#         print('odd one')
#     else:
#         print('less than 20')    


#-----------------------heckerrank if else------------------
# n = int(input())

# if n%2!=0 :
#     print('weird')
# else:
#     if n <= 2 <=5:
#         print('not weird')
#     elif n <=6 <=20:
#         print('weird')
#     else:
#         print('not weird')       
# 


# lst1 = [1,2,3,4,5,6,7,8]
# for v in lst1:
#     print(v)
# for num in lst1:
#     if num%2==0:
#         print(num)


# for a in lst1:
#     if a%3==0:
#         print(a)
# for num in lst1:
#      if num%2==0 :
#          print('even no')
#      else:
#          print(num)    

# sum_no = 0.0
# for num in lst1:
#     sum_no = sum_no + num
# print(sum_no)    

# for vari in 'The beautiful':
#     print(vari)

# tup = [(5,6),(2,6),(8,6)]
# print(tup[0][1])
# for v in
# for v1,v2 in tup:
    # print(v1)

# dict = {'k1':25,'k2':'name','k3':59}
# for a,b in dict:
#     print(list(dict.keys()))

# lst1 = [1,2,3,4,5,6]
# for i in lst1:
#     if not(i%2) :
#         print(i)

# lst = 'my name is'
# for i in lst.upper():
#     print(i)

# for i in range(51):
#     if i%2==0 :
#         print(i)


# x = 0
# while x < 10:
#     print('Value is :',x)
#     x = x+2

# x = 1
# while x<8 :
#     print('Value is :',x)
#     x+=1
#     if x == 3 :
#         print('its an odd num')
#         break
#     else:
#         print('looping list')
#         continue



# x = 0
# while x<=8 :
#     x+=1
#     print('value :',x)
#     if x == 4 :
#         print('its even')
#         break
# else:
#     print('list ended')    


# lst1 = list(range(0,51,5))
# print(lst1)


# print(list(enumerate('my name is ')))

# a = dict(enumerate('pragati'))
# print(a.items())


# for i,j in enumerate('paagati'):
    # print('the index is {} and value is {}'.format(i,j))


# lst1 = [5,10,15,63]
# lst2 = ['names','ages',25,'same']  
# lst3 = {'k1':25,'k2':'sweet','k3':33}

# print(list(zip(lst2,lst3)))

# print(list(zip(lst1,lst2)))



# lst = [25,'same','no',264,82]
# if 'same' in lst:
    # print('name find')

# lst = [15,53,96,16,2,735,]
# print(min(lst))
# print(max(lst))



# lst = [15,96,15,63,75]
# b = [a for a in lst if a<=50]
# b = [a/2 for a in lst]
# print(b)


# random_numb = random.randint(0,5)
# print(random_numb)

# random_number =  random.randint(0, 5)
# # print(random_number)
# rand = random.random()
# print(rand)

# lst = ['sam','ram','pragati']
# lst1 = random.choice(lst)
# print(lst)


# import random

# num = random.randint(0,5)
# print(num)
# rand_num = random.random()*52
# print(rand_num)

# lst = ['ram','sham','same']
# new_lst = random.choice(lst)
# print(new_lst)

# random.shuffle(lst)
# print(lst)

# def my_fuc():
#     print('welcome')
# my_fuc()    

# def add_num(a,b):
#     print(a+b)
# x = 3
# y = 2
# add_num(x,y)    


# def add_num(a,b):
#     return(a+b)
# x = 5
# y = 10
# c = add_num(x,y)
# print(c)    

# def square(num,operation):
#     if operation**2 :
#         return('square')
#     else:
#         return(num*0.5)
# final_opt = square(9,square)
# print(final_opt)   

# def pri_num(num):
#     for n in range(2,num):
#         if not num%n==0 :
#             print('no is not prime')
#             break  
#     else:
#         ('no is prime')
# pri_num(7)            



# def pri_no(num):
#     for n in range(2,num):
#         if num%n==0 :
#             print('number is not prime')
#     else:
#         print('number is prime')
# pri_no(7)    

# def prime_no(num):
#     for n in range(2,num):
#         if num%n==0:
#             print('number is not prime')

#     else:
#         print('Number is prime')
# prime_no(7)   

# #-------------why none----------
# def func(x):
#     for a in range(1,x):
#       print(a*x)

# my_lst = func(5)
# print(my_lst)


#------------xxxxx------------------

# a = 'My Name'
# lst = a.split()
# print(lst[0][0])


# def square_num(num):
#     return num**2
# lst = [1,2,3,4]
# print(list(map(square_num,lst))) 
# 
# 
# def all_num(n):
#     return n**3
# lst = [1,3,5,6,7]
# print(list(map(all_num,lst)))     
# 
#   
# lst_name = ['pragati','ram','sham','no']
# def even_odd(name):
#     if ((len(name))%2==0) :
#         return('even')
#     else:
#         return name[0]

# opt = list(map(even_odd,lst_name))
# print(opt)            

#--------------xxxxxxxxx----------------
# list of add nums from list
# lst = [1,2,3,4,5,6]
# def even_odd(num):
#     return num%2!=0
# print(list(filter(even_odd,lst))) 
# 

def paper_doll(text):
    return [chrt*3 for chrt in text]
otp = paper_doll('Hello')
print(otp) 