#-------------------------------------------------------

# def lesser_two_nos(a,b):
#     if a%2==0 and b%2==0 :
#         return(min(a,b))
#     else:
#         return(max(a,b))

# new_lst = lesser_two_nos(2,4) 
# new_lst1= lesser_two_nos(2,5)  
# print(new_lst)
# print(new_lst1)          


#------------------------------

# def animal_crackers(names):
#     lst_animal = names.split()
#     if lst_animal[0][0] == lst_animal[1][0]:
#        return('True')
#     else:
#         return('false')

# # abc = animal_crackers('Levelheaded Llama')
# abc1 = animal_crackers('Crazy Kangroo')
# # print(abc)
# print(abc1)

#--------------------------------------------

# def makes_twenty(a,b):
#     if (a+b)==20 or a==20 or b==20 :
#         return('True')
#     else:
#         return('false')  
# num = makes_twenty(5,21)
# print(num) 


#-----------xxxxxxxxxxxxx------------------------

# def old_macdonald(names):

#     return names[:3].capitalize() + names[3:].capitalize()

# finl_op = old_macdonald('macdonald')
# print(finl_op)    



#----------xxxxxxxxxxxxx------------------------

# def master_yoda(text):
#     return " ".join(text.split()[::-1])          #join allows to join strings together in list with any connector

# abc = master_yoda('I am Home')
# print(abc)

#----------xxxxxxxxxxxxxxx-------------------------------------
# def almost_there(n):
#     if ((abs(100-n)<=10) or (abs(200-n)<=10)):
#         return('True')
#     else:
#         return('False')

# otp = almost_there(115)
# print(otp)


#-----------xxxxxxxxxxxxxx-----------------------


# doubt find 33 level2



       

#------------------------------------------------------

# def paper_doll(text):
#     return "".join([chrt*3 for chrt in text])
# otp = paper_doll('Hello')
# print(otp) 


#--------------xxxxxxxxxxxxxxxxxxxxx-------------------------------------

# def blackjack(a,b,c):
#     for a,b,c in range(1,12):     
#     if sum((a,b,c))<=21 :
#         return sum((a,b,c))
#     else:
#         if a==11 or b==11 or c==11 :
#             return sum((a,b,c))-10
#         else:
#             return('BUST')      

# print(blackjack(9,9,11))              


#--------------------------------------------
#summer of 69






#----------------------------------

# import random
# print('GUESS GAME CHALLANGE')
# num = random.randint(1,100)
# print(num)

# guess_list = []
# guess_num = int(input('Guess no :'))
# guess_list.append(guess_num)
# print(guess_list)

# if guess_num<1 or guess_num>100 :
#     print('OUT OF BOUNDS')

# else:
#     if ((num-guess_num)<=10):
#         print('WARM')
#     else:
#         print('COLD') 

#------------------------------------------------------


# def prime_num(num):
#     for i in range(2,num):
#         if num%i==0 :
#             return 'This is not prime number'
#         else:
#             return 'This is prime'    

# print(prime_num(8))

#---------------------------------------------------
#find max number from 3

# def max_num(a,b,c):
#     return max(a,b,c)

# print(max_num(5,14,2))

#-------------------------xxxxxxxxxxx-----------------------------

# lst = [8,2,3,0,7]
# def sum_funt(num):
#     return (sum(num))

# print(sum_funt(lst))
     

# lst = [8, 2, 3, 0, 7]

# def sum(num):
#     total = 0
    
#     for i in lst:
#         total+=i
#     return total

# print(sum(lst))        


# #-----------------------------------------------
# lst1 = [8,2,3,-1,7]
# def multi(lst):
#     result = 1
#     for i in lst1:
#         result*=i
#     return result

# print(multi(lst1))       


#--------------------------------------------------------

# strng = '1234abcd'
# def rev_st(name):
#     return name[::-1]
# print(rev_st(strng))   

#---------------------------------
       
# def fact_num(num):
#     lst = []
#     for i in range(1,num):
#         if num%i==0:
#             lst.append(i)
#     return lst


# print(fact_num(6))    


#------------------------------------------------
# to find factorial

# def fact_num(num):
#     factoial = 1
#     for i in range(1,num+1):
#         factoial*=i
#     return factoial

# print(fact_num(6))        

#-----------------------------------------
# check whether 5 in available in given list
# lst = [1,2,5,6,9,7]
# def num_find(num):
#     if 5 in lst:
#         return 'data find'

# print(num_find(lst))        



#-------------------------------------
# string = 'The quick Brow Fox'
# def name(s):
#     uppers = 0
#     lowers = 0
#     for i in s:
#         if i.isupper():
#             uppers+=1
#         elif i.islower():
#             lowers+=1
#         else:
#             pass
#     print('Count of upper is : ',uppers)
#     print('Count of lower is : ',lowers)

# print(name(string))


#------------------------------------------------------------
# sample_lst = [1,2,3,3,3,5,6,8]
# def unique_lst(lst):
#     return list(set(sample_lst))

# print(unique_lst(sample_lst))  


#------------------------------------------------------
#prime number function

# def prime_num(num):
#     for i in range(2,num):
#         if num%i==0:
#             return'Num is not prime'
#         else:
#             return 'Num is prime'

# print(prime_num(8))        


#----------------------------------------------------------
# lst = [1,2,3,4,5,6,7,8,9]
# def even_num(num):
#     return [i for i in num if i%2==0]


            
# print(even_num(lst))

#--------------------------------------------------------------
# find perect number
# def perfect_num(n):
#     sum = 0
#     for x in range(1, n):
#         if n % x == 0:
#             sum += x
#     if sum ==n :
#         return'perfect number'
#     else:
#         'not perfect '    
# print(perfect_num(7))   


#-----------------------------xxxxxxxxxxxxxxxxxxxx---------------------
#check whether palinfrome word ie madam
# def input_string(name):
#     if name[0:]==name[::-1]:
#         return name

# print(input_string('pragati'))   


# ------------------------------------xxxxxxxxxxxxxxxx-------------------
# st = 'Print only the words that start with s in this statement'
# def find_word(string):
#     for words in st.split():
#         if words[0] == 's':
#          print(words)
         

# find_word(st) 


#------------------------------------------------

# def even_num(num):
#     return list(range(0,11,2))

# print(even_num(11))    
# 
# -------------------------------------------------

#attribute
# def lst_numbr():
#     return [a for a in range(1,51) if a%3 == 0]

# print(lst_numbr())    

#-----------------------------------------------------------------
# st = 'Print only the words that start with s in this statement'
# def find_word(string):
#     lst = []
#     for words in st.split():
#         if words[0] == 's':
#             lst.append(words)
#     return lst

# print(find_word(st)) 

#---------------------------------------------------------------

# st = 'Print every word in this sentence that has an even number of letters'

# def even_words(name):
#     for word in st.split():
#         if ((len(word))%2 == 0):
#            print(word +' has even length')

# print(even_words(st))            

#----------------------------------------------------------

# def fizz(a):
#    
#         if num%3 == 0 and num%5 == 0:
#             return 'Fizzbuzz'
#         elif num%3 == 0:
#             return 'Fizz'
#         elif num%5 == 0:
#             return 'Buzz'
#         else:
#             return num

# print(fizz(100))            


# def fizz(num):
#     for num in range(1,101):
#         if num%3 == 0 and num%5 == 0:
#             print('Fizzbuzz')
#         elif num%3 == 0:
#             print ('Fizz')
#         elif num%5 == 0:
#             print('Buzz')
#         else:
#             print(num) 

# print(fizz(100))

#-----------------------------------------------------------------------

# st = 'Create a list of the first letters of every word in this string'
# def name(string):
#     return [word[0] for word in st.split()]


# print(name(st))    


#--------------------------------------------------------------------------
# def is_prime(num):
#     '''
#     Naive method of checking for primes. 
#     '''
#     for n in range(2,num):
#         if num % n == 0:
#             return num,'is not prime'
            
#     else: # If never mod zero, then prime
#         return num,'is prime!'

# print(is_prime(7))      

#-----------------------------------------------------------------------------
  









        




            



 