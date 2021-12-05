
class Player:

    def __init__(self):
        self.knife = False
        self.security_codes = False
        self.computer_terminal = False
        self.molotov_cocktail = False
        self.armor = False
        self.crowbar = False

    def pickup_item(self, room_name):
        if room_name == "crew_quarters_1":
            if self.knife == False:    
                self.knife = True
            else:
                print("You have already picked up the knife!")
        elif room_name == "crew_quarters_2":
            if self.security_codes == False:    
                self.security_codes = True
            else:
                print("You have already picked up the security codes!")
        elif room_name == "common_area":
            if self.computer_terminal == False and self.security_codes == True:
                print("You access the computer terminal using the security codes.")
                print("A message flashes on the screen:")
                print("AIRLOCK CONTROLS ARE ONLINE")
                self.computer_terminal = True
            else:
                print("You have already used the computer terminal!")
        elif room_name == "dining_area":
            if self.molotov_cocktail == False:    
                self.molotov_cocktail = True
            else:
                print("You have already picked up the molotov cocktail!")
        elif room_name == "storage_area":
            if self.armor == False:
                self.armor = True
            else:
                print("You have already picked up the armor!")
        elif room_name == "engine_room":
            if self.crowbar == False:
                self.crowbar = True
            else:
                print("You have already picked up the crowbar!")
        else:
            print("There are no items in this room.")
        print("\n")
