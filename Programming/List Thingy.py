import time

things = ["Milk", "Eggs", "Bread", "Chocolate", "Vegetables", "Snacks", "Butter", "Marmite", "Jam", "Ice Cream"]

for i in range(10):
print(*things, sep = "\n")

def space():
    print(" ")
time.sleep(2)
space()
print("This is your current list.")

Delete_choices = ["Yes","y","Y","YES", "yes", "Yea", "yea"]
space()
Delete_choice = input("Would you like to remove anything from your list? ")

if Delete_choice in Delete_choices:
    Delete_Element = input("Which item would you like to remove from your list? ")
    if Delete_Element in things:
        things.remove(Delete_Element)
    

