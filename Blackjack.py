import random as random


def add(x,y):
    y.append(x)
    

def count(li):
    total = 0
    for i in li:
        total += i
    return total


def random_number(x):
    number = random.randint(1,x)
    return number


def main():
    player_1 = []
    dealer = []
    add(random_number(11),player_1)
    add(random_number(11),dealer)

    if player_1[0] == 11:
        add(random_number(10),player_1)
    else:
        add(random_number(11),player_1)
    
    if dealer[0] == 11:
        add(random_number(10),dealer)
    else:
        add(random_number(11),dealer)


  

    print("PLAYER CARDS: " + str(player_1))
    print("DEALER CARDS: " + str(dealer))
    
    turn = False
    if count(player_1) == 21:
        print("Player 1 automatically wins")
        
    if count(dealer) ==21:
        print("Dealer automatically wins")


    if turn == False:
        while count(player_1) < 21:
            answer = input("Want to hit or stay? [Hit, Stay] ")
            if not (answer== "Stay" or  answer == "Hit"):
                print("This response isnt valid, try again")
            elif(answer == "Hit"):
                random = random_number(11)
                if(random == 11 and (count(player_1) + random == 22)):
                    add(1,player_1)
                else:
                    add(random_number(11),player_1)
                print("PLAYER CARDS: " + str(player_1))
                print("DEALER CARDS: " + str(dealer))
            elif(answer == "Stay"):
                    print("PLAYER CARDS: " + str(player_1))
                    print("DEALER CARDS: " + str(dealer))
                    turn = True
                    break
            if count(player_1) > 21:
                print("You have automatically lost")
                break
            elif count(player_1) == 21:
                print("You have automatically won")
                break



#Another if statement to let the user pick what value he wants if numbers are 11 or 1.

    

#Dealer if 1 or 11 is chosen, do subtraction to see if 11 is over 21, if it is, make the value of the card 1.

    if turn == True:
        while count(dealer) < 21:
            if count(dealer) < count(player_1):
                random = random_number(11)
                if(random == 11 and (count(player_1) + random == 22)):
                    add(1,dealer)
                else:
                    add(random_number(11),dealer)
                
                print("DEALER CARDS: " + str(dealer))
            else:
                if count(dealer) > 21 and count(player_1) <=21:
                    print("Player wins")
                    break
                if count(dealer) == 21 and count(player_1) > 21:
                    print("Dealer won")
                    break
                if count(dealer) == count(player_1) and count(dealer) > 18:
                    print("Draw")
                    break
                #Certain case if both numbers are the same at the beginning and user chooses to stay
                if count(dealer) == count(player_1) and count(dealer) < 18:
                    add(random_number(11),dealer)

                if count(dealer) <= 21 and count(player_1) > count(dealer):
                    print("Player wins")
                    break
                if count(dealer) <= 21 and count(player_1) < count(dealer):
                    print("Dealer wins")
                    break

                if count(dealer) >21:
                    print(dealer)
                    print("Player wins")
                    break

   
main()


        

    


    
    









    
