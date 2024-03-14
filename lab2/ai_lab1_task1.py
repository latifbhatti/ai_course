# Develop a flight booking system that allows users to search for flights based on departure and destination cities, departure date,
#  etc. Use lists and tuples to store flight information such as flight number, departure time, and available seats. Implement
#  decision statements and loops to handle user input, display available flights, and manage booking transactions. Utilize functions
#  for different stages of the booking process, such as searching for flights, reserving seats, and generating booking
#  confirmations.

class flight_booking_system:
    def __init__(self):
        self.lst = [(1,'karachi','multan','10/dec/24','8:00 AM','12:00pm',2000,500),(1,'karachi','multan','10/dec/24','8:00 AM','12:00pm',2000,500),(1,'karachi','multan','10/dec/24','8:00 AM','12:00pm',2000,500),(1,'karachi','multan','10/dec/24','8:00 AM','12:00pm',2000,500)] # 1==flight n0 , 1=departure time , 2=arrival time, 3=price , 4=number of seats available
    def search(self,departure,destination,date):
        for i in self.lst:
            if i[1]==departure and  i[2]==destination and i[3]==date:
                print("this seat is available ")
                return 'yes'
            else:
                print("this seat is not avalaible")
                return 'no'
    def reserved_seat(self):
        print('this seat is reserved from your account')
    def generating_booking_confirmation(self,con,departure,destination,date):
        if con=='yes' and self.search(departure,destination,date)=='yes':
            self.reserved_seat()
        else:
            print('explore other  options or try again later')


if  __name__ == "__main__":
    name = str(input("Enter Your Name : "))
    name=flight_booking_system()
    print('------welcome into  the Flight Booking System-------\nchoice no 1 is search the train and avalaible seat \n choice no 2 generate booking system after search the seat')
    choice=int(input("enter your choice from 1 to 2 : "))
    if choice==1:
        dep,desti,dat=str(input("Enter your deparure city : ")),str(input("Enter your destination city")),str(input("Enter the date of journey "))
        name.search(dep,desti,dat)
    elif choice==2:
        dep,desti,dat=str(input("Enter your deparure city")),str(input("Enter your destination city")),str(input("Enter the date of journey "))
        con=input('confirm  booking yes/no? ')
        name.generating_booking_confirmation(con,dep,desti,dat)
    else:
        print("enter correct number or contact us ")
