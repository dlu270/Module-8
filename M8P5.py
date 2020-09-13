# Daniel Lu
# 9/12/20

# This function checks whether your character has picked up all the required items and checks for any status debuffs.

inventory = ["pan","paper","idea","rope","groceries"]
debuffs = ["slow"]

task = input("Please select a task (climb, cook, or write): ")

climb = ("climb")
cook = ("cook")
write = ("write")

if task == climb:
    if "slow" in debuffs:
        print("You are too slow to climb the mountain.")
    elif "rope" in inventory and "coat" in inventory and "first aid kit" in inventory:
        print("You successfully climb the mountain!")
    else:
        print("You do not have the required items to climb the mountain.")

elif task == cook:
    if "small" in debuffs:
        print("You are too small to cook a meal.")
    elif "pan" in inventory and "groceries" in inventory:
        print("You cook a delicious meal!")
    else:
        print("You do not have the required items to cook a meal.")
        
elif task == write:
    if "confusion" in debuffs:
        print("You are too confused to write a book.")
    elif "pen" in inventory and "paper" in inventory and "idea" in inventory:
        print("You successfully write a book!")
    else:
        print("You do not have the required items to write a book.")