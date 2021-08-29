#--------------------while loop-------------------
# x = 1
# while x<5 :
#     print('value is ',x)
#     x+=1 
#     if (x==2):
#         print('this is exactly value of',x)
#         break

# x = 1
# while x<=10 :
#     print('enter the value ',x)
#     x+=2
#     if (x==3):
#         print('done')
#         break

# x = 1        
# while x<=10 :
#     print('enter value is ',x)
#     x+=2
#     if (x==3):
#         continue
#         print('same value')
#     else:
        
#         print('continue list')


#-------------range---------

# lst1 = list(range(21))
# lst1 = list(range(1,21,3))
# print(lst1)


    #--------------enumerate------
    
# print(list(enumerate('sammy')))     #list exm 

# a = dict(enumerate('sammy'))
# # print(a)
# print(a.keys())


# for i,j in enumerate('sammy'):
#     print('The index is {} and value is {}'.format(i,j))


#------------zip------------------

# list1 = [25,36,45,99,14]
# list1 = [25,36,45,99,14,96]
# list2 = ['get',26,'same','none']
# print(list(zip(list1,list2)))


# list1 = [25,36,45,]
# list2 = {'a':20,'b':'same'}

# print(list(zip(list1,list2)))


#--------------in-----------------------

# ages = [26,'same',96,26,'get','apple']

# if 'apple' in ages:
#     print('data found')


#------------min,max------------------------

# list1 = [96,15,26,74,15,29,364]
# # print(min(list1))
# print(max(list1))


# check_list = [26,93,18,96]
# new_check_list = [16,82,56,16]

# print(min(check_list),max(new_check_list))
# # print(max(new_check_list))


#--------------list comprehension-------------------

# list = [a for a in range(51) if a%3==0]
# print(list)

# list2 = [25,96,411]
# list3 = [a/2 for a in list2]
# print(list3)


# ages = [36,25,13,47,56,14,23]
# list1 = [a for a in ages if a<25 ]
# print(list1)






