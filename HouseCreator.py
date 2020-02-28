from os import system

class room:
    contents = []
    def __init__(self, size, name):
        self.size = size
        self.name = name

    def addToRoom(self, furniture):
        self.contents.append(furniture)
        print(furniture + " has been added to the " + self.name)
    
    def removeFromRoom(self, furniture):
        if(furniture in self.contents):
            self.contents.remove(furniture)
            print(furniture + " has been removed from the " + self.name)
        else:
            print(furniture + " is not in the " + self.name)
    
    def printFurniture(self):
        print("This room contains: ")
        for furniture in self.contents:
            print(furniture)
    
    def printName(self):
        print(self.name)

    
class house:
    rooms = []
    roomNames = []

    def __init__(self, location):
        self.location = location

    def createRoom(self, newRoom: room):
        self.rooms.append(newRoom)
        self.roomNames.append(newRoom.name)
        print(newRoom.name + " has been added to the house")
    
    def destroyRoom(self, oldRoom: room):
        if(oldRoom in self.rooms):
            self.rooms.remove(oldRoom)
            self.roomNames.remove(oldRoom.name)
            print(oldRoom.name + " has been removed from the house")
    
    def printRooms(self):
        print("This house has these rooms: ")
        print()
        for room in self.rooms:
            room.printName()
    
    def getRoom(self, roomName):
        if(roomName in self.roomNames):
            for room in self.rooms:
                if room.name == roomName:
                    return room
        else:
            return None

def roomCreation() -> room:
    size = input("What size is the room? (ex. small, medium, large, extra large) ")
    name = input("What type of room is this? ")
    print("Ok! Ready to make your new room! ")
    result = room(size, name)
    result.contents = []
    return result

def furnitureCreation(roomSelect: room, name):
    roomSelect.contents.append(name)

def mainMenu():
    print()
    print("Enter 1 to add a room.")
    print("Enter 2 to delete a room.")
    print("Enter 3 to add a piece of furniture to a room.")
    print("Enter 4 to remove a piece of furniture from a room.")
    print("Enter 5 to see what rooms are in your house.")
    print("Enter 6 to see what furniture is in a particular room.")
    print("Enter -1 to Quit.")
    print()


def main():
    system('clear')
    print("Hello! Welcome to my simple house building program! Let's start by making a house.")
    location = input("First, please tell me where in the world you would like to make your house: ")
    
    newHome = house(location)

    print("Bingo! We now have a new house in " + location + "! It doesn't have any rooms in it yet, though.")
    print()
    print("Let's fix that! I'll ask you a couple questions and once we're done we'll have a new room for your house.")

    newRoom = roomCreation()
    system('clear')

    print("Now that you've created a new " + newRoom.name + ", let's add it to your house!")
    print()

    newHome.createRoom(newRoom)

    print("Now your new home has its very own " + newRoom.name + "!")
    print()

    firstFurniture = input("Now let's add a piece of furniture to that room shall we? What would you like to add? ")

    furnitureCreation(newRoom, firstFurniture)
    system('clear')

    print("All set! Your " + firstFurniture + " has been added to the " + newRoom.name + "!")

    print()

    print("Now let's give you full reign of the system. Play with it as much as you like!")

    print()

    while(1):
        mainMenu()
        decision = input("Make your decision: ")
        
        if(decision == "1"):
            #Add a room (try to avoid duplicate names)
            system('clear')
            size = input("What size is the room? (ex. small, medium, large, extra large) ")
            name = input("What type of room is this? ")
            while(name in newHome.roomNames):
                name = input("Name already taken, please input another (if adding a second of a particular room, consider using (name)(number)) ")

            newRoom = room(size, name)
            newHome.createRoom(newRoom)

        elif(decision == "2"):
            #Delete a room
            system('clear')
            roomToDeleteName = input("What room would you like to delete? ")
            roomToDelete = newHome.getRoom(roomToDeleteName)
            if(roomToDelete != None):
                newHome.destroyRoom(roomToDelete)
            else:
                print(roomToDeleteName + " is not in the house")
            
        elif(decision == "3"):
            #Add furniture to a room (try to avoid duplicate names)
            system('clear')
            roomName = input("What room would you like to add furniture to? ")
            furnitureName = input("What furniture would you like to add? ")
            currentRoom = newHome.getRoom(roomName)
            if(currentRoom != None):
                while(furnitureName in currentRoom.contents):
                    furnitureName = input("Name already taken, please input another (if adding a second of a particular furniture, consider using (name)(number)) ")
                currentRoom.addToRoom(furnitureName)
            else:
                print(roomName + " is not in the house")
    
        elif(decision == "4"):
            #Remove furniture from a room
            system('clear')
            roomName = input("What room would you like to remove furniture from? ")
            furnitureName = input("What furniture would you like to remove? ")
            currentRoom = newHome.getRoom(roomName)
            if(currentRoom != None):
                currentRoom.removeFromRoom(furnitureName)
            else:
                print(roomName + " is not in the house")
        
        elif(decision == "5"):
            #List rooms in house
            system('clear')
            newHome.printRooms()
    
        elif(decision == "6"):
            #List furniture in a particular room
            system('clear')
            roomName = input("What room would you like to see the furniture in? ")
            currentRoom = newHome.getRoom(roomName)
            if(currentRoom != None):
                currentRoom.printFurniture()
            else:
                print(roomName + " is not in the house")

        elif(decision == "-1"):
            exit(1)

        else:
            system('clear')
            print("Invalid input.")       
  
if __name__== "__main__":
    main()