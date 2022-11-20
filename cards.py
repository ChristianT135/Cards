'''
import random

diamonds =["AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D","10D", "JD" ,"QD" ,"KD"]

hand =[]
while diamonds:
    
    user_input = input("Press enter to pick a card, or enter Q to quit:")
    if user_input == "Q" or "q":
        break
else :
    user_input = random.choice(diamonds)
    hand.append(user_input)
    diamonds.remove(user_input)
    print("your hand" , hand)
    print("cards remaining: " , diamonds)

    if not diamonds:
        print("there no more cards thank you ")
'''


my_string = "zebra"
print(my_string[0])