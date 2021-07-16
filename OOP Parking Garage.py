# Your Code will go here
from IPython.display import clear_output

# CHRISTIAN STARTS DRIVING, ZACH NAVIGATING

class parkingGarage():

    def __init__(self, tickets, parkingSpace, currentTicket, ticketsPaid):
        self.tickets = tickets
        self.parkingSpace = parkingSpace
        self.currentTicket = currentTicket
        self.ticketsPaid = ticketsPaid

    def takeTicket(self):
        if self.tickets:
            takenTicket = self.tickets.pop(0)
            takenSpace = self.parkingSpace.pop(0)
            self.currentTicket[takenTicket] = takenTicket
            self.currentTicket[takenSpace] = takenSpace
            self.ticketsPaid[takenTicket] = False
            print(f"Your ticket number is {takenTicket}.")
        else:
            print("Sorry, the garage is full.  Please wait for others to leave.")
        
    def payForParking(self):
        if len(self.tickets) == 10:
            print("We have all of our tickets already, there's nothing to pay for!")
        else:
            ticketNumber = input("What is your ticket number? ")
            if self.ticketsPaid[ticketNumber] == False:
                payment = input('Please type any key to pay.')
                if payment:
                    self.ticketsPaid[ticketNumber] = True
                    print('Your ticket has been paid, you have 15 mins to leave.')
                else:
                    print('You have not paid for your ticket yet.')

    def leaveParking(self):
        if len(self.tickets) == 10:
            print("We have all of our tickets already.  Nobody is parked here!")
        else:
            ticketNumber = input("What is your ticket number? ") 
            if self.ticketsPaid[ticketNumber] == True:
                print('Thank you, have a nice day!')
            else:
                while True:
                    payment = input('You need to pay for your ticket, Please type any key to pay.')
                    if payment:
                        self.ticketsPaid[ticketNumber] = True
                        print('Thank you for your payment, have a nice day!')
                        break
            returnTicket = self.currentTicket.pop(ticketNumber)
            self.tickets.append(returnTicket)
            self.parkingSpace.append(returnTicket)
    
    def garageStatus(self):
        print(f"Parking Spaces Available: {self.parkingSpace}")
        print(f"Parking Tickets Available: {self.tickets}")

# ZACH STARTS DRIVING, CHRISTIAN NAVIGATING
        
    

num_tickets = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
num_parking_spots = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
garage = parkingGarage(num_tickets, num_parking_spots, {}, {})


def garageRun():
    # driver arrives at garage
    print("Welcome to the parking garage.")
    while True:
        driver_choice = input("What would you like to do? park / pay / leave ")
        clear_output()
        if driver_choice == "park":
            garage.takeTicket()
            garage.garageStatus()
        elif driver_choice == "pay":
            garage.payForParking()
        elif driver_choice == "leave":
            garage.leaveParking()
            garage.garageStatus()
        else:
            print("Sorry, that input doesn't work.  Please try again.")

print(garageRun())