class Parking_Garage():
    """a simple model of a parking garage"""
    
    def __init__(self):
        self.parking_spaces = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','v','W','X','Y','Z']
        self.tickets = 26
        self.takenspot = []
        self.CurrentTicket = {'paid':False}
    
    def PayParking(self):
        popup = True
        while popup:
            payment = input("please enter a payment or 'Q' for quit")
            if payment == 'Q':
                popup = False
            elif payment == '':
                print('Please enter a payment to get a spot or leave the garage')
            else:
                print('congrats you now have a spot for 15 minutes')
                self.tickets = self.tickets - 1
                self.takenspot.append(self.parking_spaces.pop())
                self.CurrentTicket['paid'] = 'True'
                popup = False
    
    def LeaveGarage(self):
        while self.CurrentTicket['paid'] == False:
            display = input('please pay your ticket')
            if display != '' or ' ':
                print('thank you for your payment')
                self.parking_spaces.append(self.takenspot.pop())
                self.tickets += 1
                self.CurrentTicket['paid'] = True
        if self.CurrentTicket['paid'] == True:
            print('thank you have a nice day')
    def show_avaliable_parking(self):
        print(self.parking_spaces)            
    
    def show_taken_parking(self):
        print(self.takenspot)
    
    def is_current_ticket_paid(self):
        if self.CurrentTicket['paid'] == True:
            print('ticket is paid')
        else:
            print('ticket has been paid')
    
park_garg = Parking_Garage()
park_garg.show_avaliable_parking()
park_garg.show_taken_parking()
park_garg.PayParking()
park_garg.LeaveGarage()
park_garg.show_avaliable_parking()
park_garg.LeaveGarage()

            

