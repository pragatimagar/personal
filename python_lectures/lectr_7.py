#-----------------Function---------------------------

# def say():
#     print('welcome')
# say()    

# def add_value(a,b):
#     print(a+b)
#     return(a+b)
# x = 5
# y= 6
# c = add_value(x,y)
# print(c)    

# def new_fuct(name):
#     return('hello',name)
# d = new_fuct("pragii1")
# print(d)    


# def sqr_num(a):
#     print(a**2)
#     return('square is no is',a)
# d = sqr_num(5)
# print(d)       

# def pri_no(num):
#     for n in range(2,num):
#         if not num%n==0:
#             print('This is not prime ')
#             break
#     else:
#             print('this is prime')  
# pri_no(7)            

#--------------------map------------------
# def square(num):
#     return num**2

# list1 = [1,5,6,8]

# new_list = list(map(square,list1))
# print(new_list)


# def add(num):
    # return num+2

# lst = [1,2,5,7]
# new = list(map(add,lst))

# print(new)



# names = ['save','saw','same','no']

# def even_odds(name):
#     if ((len(name))%2==0):
#         return 'even'
#     else:
#         return name[0]
# a = list(map(even_odds,names))
# print(a)            




#-----------filter-------------

# def even_odd(num):
#     return num%2==0
# l1 = [1,2,3,4,5,6,8]
# a = list(filter(even_odd,l1))
# print(a) 

def even_odd(num):
    return num%2!=0
l1 = [1,2,3,4,5,6,8]
a = list(filter(even_odd,l1))
print(a)















