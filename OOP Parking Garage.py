class parkingGarage():

    def __init__(self, tickets, parkingSpace, currentTicket)
        self.tickets = tickets
        self.ParkingSpace = parkingSpace
        self.currentTicket = currentTicket


    def takeTicket(self):
        takenTicket = self.tickets.pop(0)
        takenSpace = self.parkingSpace.pop(0)
        self.currentTicket['ticket number'] = takenTicket
        self.currentTicket['parking space'] = takenSpace
        
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
            payment = input('You need to pay for your ticket, Please type any key to pay.')
            if payment:
                self.currentTicket['paid'] = True
                print('Thank you for your payment, have a nice day!')
        returnTicket = self.currentTicket.pop('ticket number')
        returnSpaces = self.currentSpace.pop('parking space')
        
