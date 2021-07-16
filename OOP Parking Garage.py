from IPython.display import clear_output

class parkingGarage():

    def __init__(self, tickets, parkingSpace, currentTicket):
        self.tickets = tickets
        self.parkingSpace = parkingSpace
        self.currentTicket = currentTicket

    def takeTicket(self):
        if self.tickets:
            takenTicket = self.tickets.pop(0)
            takenSpace = self.parkingSpace.pop(0)
            self.currentTicket['ticket number'] = takenTicket
            self.currentTicket['parking space'] = takenSpace
            self.currentTicket['paid'] = False
        else:
            print("Sorry, the garage is full.  Please wait for others to leave.")
        
    def payForParking(self):
        payment = input('Please type any key to pay.')
        if payment:
            self.currentTicket['paid'] = True
            print('Your ticket has been paid, you have 15 mins to leave.')
        else:
            self.currentTicket['paid'] = False
            print('You have not paid for your ticket yet.')

    def leaveParking(self):
        if self.currentTicket['paid'] == True:
            print('Thank you, have a nice day!')
        else:
            while True:
                payment = input('You need to pay for your ticket, Please type any key to pay.')
                if payment:
                    self.currentTicket['paid'] = True
                    print('Thank you for your payment, have a nice day!')
                    break
        returnTicket = self.currentTicket.pop('ticket number')
        returnSpaces = self.currentTicket.pop('parking space')
        self.tickets.append(returnTicket)
        self.parkingSpace.append(returnSpaces)
    
    def garageStatus(self):
        print(f"Parking Spaces Available: {self.parkingSpace}")
        print(f"Parking Tickets Available: {self.tickets}")


num_tickets = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
num_parking_spots = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
garage = parkingGarage(num_tickets, num_parking_spots, {})


def garageRun():
    # driver arrives at garage
    print("Welcome to the parking garage.")
    while True:
        driver_choice = input("What would you like to do? park / pay / leave ")
        clear_output
        if driver_choice == "park":
            garage.takeTicket()
            garage.garageStatus()
        elif driver_choice == "pay":
            garage.payForParking()
        elif driver_choice == "leave":
            garage.leaveParking()
            garage.garageStatus()
            break
        else:
            print("Sorry, that input doesn't work.  Please try again.")

print(garageRun())