# a = int(input('Enetr fisrt num :'))
# b = int(input('Enetr second num :'))
# avg = (a + b)/2
# print('The avg value of a & b is: ',avg)

# a = 'good morning'
# b = 'harry'
# print(a + b)

# name = 'pragati is'
# # print(name[1: :2])
# print(name.capitalize())
# print(name.replace('is','magar'))

# story = 'this is me.\n is\tshe'
# print(story)

# name = input('')
# print('good afternoon ',name)


# letter = '''Dear <|NAME|>,
# You are selected!
# Date : <|DATE|>
# '''
# name = input('Enter your Name \n')
# date = input('Enter date \n')
# letter = letter.replace('<|NAME|>',name)
# letter = letter.replace('<|DATE|>',date)
# print(letter)


# letter = ''' Dear <|NAME|>
# You are selected!
# Date = <|DATE|>
# '''
# name = input('Enter name \n')
# date = input('Ener date\n')
# letter = letter.replace('<|NAME|>',name)
# letter = letter.replace('<|DATE|>',date)
# print(letter)

#find double space in string
# st = 'my name is'
# lst = st.find('  ')
# print(lst)

# lst = [1, 2, 6, 4, 8]
# lst[2] = 5
# a = lst.sort()
# print(a)

# l1 = [1,8,7,2,21,15]
# l1.reverse()
# l1.append(65)
# l1.insert(1,544)
# l1.remove(21)
# print(l1)


#--------------------------Tuples-----------------------------------------------------
# t = (1,2,3,4,5,2,'item')
# print(t.index('item'))
# t1 = (1,)
# print(type(t1))
# print(t[1])


# f1 = input('Enetr Fruit Name 1 ')
# f2 = input('Enetr Fruit Name 2 ')
# f3 = input('Enetr Fruit Name 3 ')
# f4 = input('Enetr Fruit Name 4 ')
# f5 = input('Enetr Fruit Name 5 ')
# f6 = input('Enetr Fruit Name 6 ')
# f7 = input('Enetr Fruit Name 7 ')
# mylst = [f1,f2,f3,f4,f5,f6]
# print(mylst)

# f1 = int(input('Enetr marks of std Name 1 '))
# f2 = int(input('Enetr marks of std Name 2 '))
# f3 = int(input('Enetr marks of std Name 3 '))
# f4 = int(input('Enetr marks of std Name 4 '))
# f5 = int(input('Enetr marks of std Name 5 '))
# f6 = int(input('Enetr marks of std Name 6 '))

# mylst = [f1,f2,f3,f4,f5,f6]
# mylst.sort()
# print(mylst)

# a = [1,5,6,5]
# print(sum(a))


# mydict = {'key1':25,'key2':'get'}
# mydict['key3'] = [1,2,3]
# print(list(mydict.keys()))
# print(mydict.values())
# print(type(mydict.items()))
# mydict['key4'] = {'k1':25,'k2':23}
# print(mydict)
# add_dict = {'same':'game','key2':25}
# mydict.update(add_dict)
# print(mydict)
# print(mydict.get('key3'))
# print(mydict['key3'])


# s = {1,5,4,6,1}
# print(type(s))
# print(len(s))
# s.remove(4)
# print(s.clear())


# b = set()
# print(type(b))
# b.add(4)
# b.add(25)
# b.add(6)
# b.add((1,2,3))
# print(b)

# s = [1,1,2,3,4,5,6]
# print(list(set(s)))
# s = list(set(s))
# print(s)

# lst1 = {1,5,3,5}
# lst2 = {8,9}
# lst1.update(lst2)
# print(lst1)
# an','dabba':'tifin','vastu':'item'}
# print('your opetions are ',mydict.keys())
# a = input('Enter an hindi word \n')
# print('The meaning of
# mydict = {'pankha':'f this hindi word is ',mydict.get(a))


# favlan = {}
# a = input('Enter your fav language pragii \n')
# b = input('Enter your fav language sona \n')
# c = input('Enter your fav language mona \n')
# d = input('Enter your fav language naina \n')

# favlan['pragii'] = a
# favlan['sona'] = b
# favlan['mona'] = c
# favlan['naina'] = d
# print(favlan)

# a = 22
# if (a>9):
#     print('Greater')

# else:
#     print('Lesser')

# print('Done')    

# age = int(input('Enter your age : '))
# if age>= 18:
#     print('Yes')

# else:
#     print('Not match')    


# a = [45,36,18]
# print(452 in a)

# num1= int(input('Enter an num1 : '))
# num2= int(input('Enter an num2 : '))
# num3= int(input('Enter an num3 : '))
# num4= int(input('Enter an num4 : '))

# if (num1>num4):
#     f1 = num1
# else:
#     f1 = num4

# if (num2>num3):
#     f2 = num2
# else:
#     f2 = num3

# if (f1>f2):
#     print(str(f1) + 'is greatest')
# else:
#     print(str(f2) + 'is greatest')

# text = input('Enter a text')

# if ('make a money' in text):
#     spam = True

# elif ('buy now'in text):
#     spam = True

# else:
#     spam = False

# if(spam):
#     print('This is a spam')
# else:
#     print('This is not spam')


# text = input('Enter a name \n')
# if (len(text)<10):
#     print('less than')
# else:
#     print(text)
# 
# names = ['pragati','shreya','man']
# name = input('Enetr name to check \n')
# if name in names:
#     print('Name is present in list')
# else:
#     print('not in list')        

# i = 0
# while i<10:
#     print('Yes')
#     i+=1

# print('Done')    
# fruits = ['banana','mango','papaya','grapes']
# i = 0
# while i<len(fruits):
#     print(fruits[i])
#     i+=1

# for items in fruits:
#     print(items)

# for i in range(10):
#     print(i)
#     if i==5 :
#         break

# for i in range(10):
#     if i==4:
#         continue
#     print(i)


# num = int(input('Enet an num :'))
# for i in range(1,11):
#     print(str(num) + 'x' + str(i) + '=' + str(i*num))
    #    print(f"{num}x{i}={i*num}")

# l1 = ['prag','same','sachin']
# for name in l1:
#     if name.startswith('s'):
#         print('hello', name)


# num = int(input('Enet an num :'))
# factorial  = 1
# for i in range(1, num+1):
#     factorial = factorial * i
# print(f'The factorial of num is {factorial}')    


# for i in range(4):
#     print('*' * i)


# def greet(name):
#     print('good day ',name)

# greet('pragati') 
# 
# 

# def factorial(num):
#     fact = 1
#     for i in range(1,num+1):
#         fact = fact*i   
#     return fact 

# print(factorial(5))   
# 
# 
# def factorial(num):
#     if num==0 or num==1 :
#         return 1
#     else:
#         return num * factorial(num-1)

# print(factorial(5))
# 

# def maximun(n1,n2,n3):
#     if (n1>n2):
#         if (n1>n3):
#             return n1
#         else:
#             return n3
#     else:
#         if (n2>n3):
#            return n2  
#         else:
#             return n3

# print(maximun(8,34,5))                         
#     print(max(n1,n2,n3))

# maximun(189,1234,5)   
# def farh(cel):
#        return (cel *(9/5)) + 32 

# print(farh(25))



# def sum_of(num):
#     return num + sum(num-1)

# print(sum_of(4))


# n = 3
# for i in range(n):
#     print('*' * (n-i))

# def rem_replace(string,word):
#     newstr = string.replace(word,'-')
#     return newstr.strip()
    

# this = '   is me no    '
# print(rem_replace(this,'is'))




