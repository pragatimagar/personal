# class Train:
#     def __init__(self,name,fare,seats):
#         self.name = name
#         self.fare = fare
#         self.seats = seats

#     def getStatus(self):
#         print(f"The name of tarin is : {self.name}")
#         print(f"The available seats in train are :{self.seats}")  

#     def bookTicket(self):
#         if (self.seats>0):
#             print(f'Your ticket has been booked !Your seat number is {self.seats}')
#             self.seats = self.seats-1    
#         else:
#             print('Sorry tarin is full')    

#     def fareInfo(self):
#         print(f"the fare value of tarin is Rs.{self.fare}")


# intercity = Train('Intercity express',90,1)
# intercity.getStatus()
# intercity.bookTicket() 
# intercity.bookTicket()
# intercity.getStatus()           