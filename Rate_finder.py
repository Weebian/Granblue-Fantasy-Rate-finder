import xml.etree.ElementTree as ET
tree = ET.parse('rates.xml')
root = tree.getroot()

#See if valid name input and get the grid
def gridExist(name):
    for child in root:
        if name.lower() == child.get('name').lower():
            return True, child
    return False, None

#Get the drops
def getDrops(weapon):
    for drop in weapon:
        print("\tRaid: " + drop.get('name') + ': \n\t\tRate: ' + drop.get('rate') + '\n\t\tCost: ' + drop.get('cost'))

#Print the grid
def printGrid(name):
    exist, grid = gridExist(name)
    
    if exist:
        print("\nGrid: " + name.upper())
        for weapon in grid:
            print("- " + weapon.get('name') + ' (Need ' + weapon.get('need') + ')')
            getDrops(weapon)
            print("")
    else:
       print("Invalid name, please try again")

#Main function
def main():
    print("Granblue Fantasy rate finder")
    while 1:
        name = input("Enter grid name\n")
        printGrid(name)

#Check if main file
if __name__ == "__main__":
    main()
