import time
#Variables
gift_card = int(input("How much is your gift card worth?"))
dlc_content = 35

#Inputs
print("Your giftcard is worth: ${}".format(gift_card))
time.sleep(2)
print("Additional content Price: $35")
time.sleep(2)
dlc_number = int(input("How many DLCs would you like to purchase?"))
TotalBalance = gift_card - dlc_content * dlc_number

print("Your total balance is...")
print("${}".format(TotalBalance))
if TotalBalance < 0:
    print("Insufficent Funds.")
if TotalBalance > 0:
    print("Transaction complete.")
                               
                            
                              
