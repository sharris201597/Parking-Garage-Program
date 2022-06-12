# lucky_parking = Levels()

class Parking_Garage: #just storing information we can use 

    def __init__(self):
        self.name = None
        self.tickets = [1,2,3,4,5,6,7,8,9,10]
        self.parkingSpaces = len(self.tickets)
        self.currentTicket = {} 

    def Help(self):
        print("""
                - To pay for parking follow the Pay prompt
                - If you haven't already, take a ticket with the Ticket prompt before parking
                - If you have a Ticket: You may only Leave after paying your ticket
                    with the Leave prompt
                """)






      

# *******MAIN RUN PROGRAM*********

class Zones(Parking_Garage):

    def __init__(self):
        super().__init__()
        self.floors = []
        self.numberfloor = []
        self.totalspaces = 40

    def checkAvailable(self):
        if self.totalspaces:
            print(f"""
            
            These Zones are Being Occupied:
            
            """)
            if self.floors:
                for zone in self.floors:
                    if zone.parkingSpaces:
                        print(f"""
                        {zone.name}
                        """)
            else:
                print("""
                All Are Available!\n""")
            self.enterZone()

        else:
            print("There are no more parking spaces available! Come back another time!")
            return
    
    def enterZone(self):
        proceed_park = input("Would you like to enter a lot? (y/n) ").lower().strip()
        if proceed_park == 'y':
            print("""
            Zone 1 | Zone 2 | Zone 3| Zone 4""")
            print()
            zone_choice = input("Which Zone would you like to choose? (Please choose starting from Zone 1 up!) ").lower().strip()
            if zone_choice == "zone 1":
                if "1" not in self.numberfloor:
                    Zone_1 = Parking_Garage()
                    Zone_1.name = "Zone 1"
                    self.floors.append(Zone_1)
                    self.numberfloor.append("1")
                    self.run2()
                else:
                    print("Zone 1 FULL")
                    self.enterZone()
            elif zone_choice == "zone 2":
                if "2" not in self.numberfloor:
                    Zone_2 = Parking_Garage()
                    Zone_2.name = "Zone 2"
                    self.floors.append(Zone_2)
                    self.numberfloor.append("2")
                    self.run2()
                else:
                    print("Zone 2 FULL")
                    self.enterZone()
            elif zone_choice == "zone 3":
                if "3" not in self.numberfloor:
                    Zone_3 = Parking_Garage()
                    Zone_3.name = "Zone 3"
                    self.floors.append(Zone_3)
                    self.numberfloor.append("3")
                    self.run2()
                else:
                    print("Zone 3 FULL")
                    self.enterZone()
            elif zone_choice == "zone 4":
                if "4" not in self.numberfloor:
                    Zone_4 = Parking_Garage()
                    Zone_4.name = "Zone 4"
                    self.floors.append(Zone_4)
                    self.numberfloor.append("4")
                    self.run2()
                else:
                    print("Zone 4 FULL")
            else:
                print("invalid response")
                
        else:
            pay = input("Would you like to pay for an existing parking? (y/n)").lower().strip()
            if pay == 'y':
                self.payForParking()
            else:   
                print("Thank you!")
                return
    
      #takeTicket
    def take_ticket(self):
        zone =  int(input("You are in Zone: (1,2,3,4)"))

        if self.floors[zone - 1].tickets:
            self.floors[zone - 1].currentTicket[self.floors[zone - 1].tickets.pop(0)] = ""
            self.parkingSpaces -= 1
            print(f"""
            Tickets Available: {self.floors[zone - 1].tickets}""")
            print(f"""
            Current Customers: {self.floors[zone - 1].currentTicket}""")
            print("\nThank you. You are alloted 2 hours")
        else:
            print("Parking Spaces FULL")
            print("Choose a new Zone!")
            self.run()
    
    def payForParking(self):
        ticket_num = int(input("You are about to pay for parking! What is your ticket number? "))

        zone = int(input("Which Zone are you in? (1,2,3,4) "))
        print(self.floors[zone - 1].currentTicket)

        while ticket_num not in self.floors[zone - 1].currentTicket:
            print("INVALID TICKET")
            ticket_num = int(input("What is your ticket number? ('0' to quit | '911' for assistance"))
            if ticket_num == 0:
                return
            elif ticket_num == 911:
                self.Help()
                    
        if ticket_num in self.floors[zone - 1].currentTicket:
            if self.floors[zone - 1].currentTicket[ticket_num]:
                print("you already payed for your ticket!")
            else:
                self.floors[zone - 1].currentTicket[ticket_num] = 'paid'
                print(self.floors[zone - 1].currentTicket)
                print("Your status has been changed to PAID! You may now safely exit")
        else:
            print("INVALID TICKET")
    
    #leaveGarage  
    def leaveGarage(self):
        ticket_num = int(input("""
        Leaving already? We need to make sure you are set! 

        What is your ticket number? """))

        zone = int(input("What zone are you in? (1,2,3,4) "))
        
        if ticket_num in self.floors[zone - 1].currentTicket:
            if self.floors[zone - 1].currentTicket[ticket_num]:
                del self.floors[zone - 1].currentTicket[ticket_num]
                self.floors[zone - 1].tickets.append(ticket_num)
                self.parkingSpaces += 1
                print("Thank you! Please leave a brief survey!")
                return
            else:
                print("You have not paid. Please pay before leaving")
        else:
            print("INVALID TICKET")
    
    def run(self):
        print("""
        Welcome To LazyBoy! Home of Parking!
        
        
           - please drive up to proceed - """)
        self.checkAvailable()
    
    def run2(self):
      while True:
        response = input("""
                     Please press valid key:
                       [T] Take Ticket
                       [P] Pay For Ticket
                       [L] Leave 
                       [E] Enter new Zone
                       """).lower().strip()
        new_customer = input("\nAre you a new customer? (y/n) ").lower().strip()
        if new_customer == 'y':
            if response == 't':
                self.take_ticket()
            elif response == 'p':
                print("\nYou haven't taken a ticket yet! Please take a ticket first.")
            elif response == 'l':
                print("\nGoodbye, hope you choose us next time!")
                return
            elif response == 'e':
                self.enterZone()
            else:
                print("\nPlease enter valid input: [P], [T], [L] ")
        else: #not a new customer options
            if response == 't':
                print("\nYou already have a ticket! If you are ready to leave please pay")
            elif response == 'p':
                self.payForParking()
            elif response == 'l':
                self.leaveGarage()
            elif response == 'e':
                self.enterZone()
            else:
                print("\nPlease enter valid input: [P], [T], [L] ")

    

lucky = Zones()
lucky.run()

        
