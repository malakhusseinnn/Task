#File: Number scrabble

#purpose: This is a game. in which two players take a number between 1, 9 and the taken number can not be taken again 
#the taken numbers by each player are stored in her/his list 
#if any three numbers of the list of one of the two players are up to 15, this player is the winner
#if the sum of any three numbers does not equal 15 and all the numbers in list have been taken ,the game is a draw.

#Author: Malak Hussein Mohammed

#ID: 20230415


#create list to contain the numbers from 1 to 9 and two empty lists to store the numbers which the players take
numbers = [1,2,3,4,5,6,7,8,9]
player_1 =[]
player_2 =[]
#loop to enable the user to play again or Exit
z = True
while z:
    print("#"*40)
    print("#"*5 ,"Welcome to Number scrabble" , "#"*5)
    print("#"*40)
    print()
    print("In this game, you should take a number from the numbers list \n Add it to your list, until you have three numbers the sum of them equals to 15\n then you win.\n when you start the game, your list is empty.")
    print()
    i = 0
    #loop to take elements from the user 
    print(f"the numbers list is: {numbers}")
    print()
    while i < 5:
        #take element from user as input
        try:
            elem1= int(input("player_1,please Enter a number berween 1:9 :"))
        except:
              print ("please, Enter a valid value")
              continue
        #check if the entered number between 1,9
        while elem1 < 1 or elem1 > 9:
            try:
               elem1= int(input("Not valid,please Enter a number in the range: "))
            except:
                print("please,Enter a valid value")
                continue
        #check if the entered number in the list or not 
        x = True
        while x:
           if elem1 in numbers:
                numbers.remove(elem1)
                print(f"the numbers list now is: {numbers}")
                x = False
           else:
                try:
                    elem1 = int(input("you can not take the same element again, Take another element: "))
                except:
                    print("please, Enter a valid value")
                    continue
        #add the elements to list one
        player_1.append(elem1)
        print(f"player 1, your list is: {player_1}")
        #check if the sum of the first three elements in the list one equals 15 or not 
        if len(player_1) == 3:
            if sum(player_1) == 15:
                print("the winner is player_1,good job")
                break
        #when there are elements more than three elements, check if the sum of any three element (except for first three elemnts) of the list equals 15
        #test all the possible options when there are 4 elements in list one
        if len(player_1) == 4:
            if player_1[0] + player_1[1] + player_1[3] == 15:
                print("the winner is player_1,good job")
                break
            if player_1[0] + player_1[2] +player_1[3] == 15:
                print("the winner is player_1,good job")
                break
            if player_1[1] + player_1[2] +player_1[3] == 15:
                print("the winner is player_1,good job")
                break
        #list one can contain up to 5 elements
        #test all the possible options when there are 5 elements in list one
        if len(player_1) == 5:
            if player_1[0] + player_1[1] + player_1[4]== 15:
                print("the winner is player_1,good job")
                break
            if player_1[0] + player_1[2] + player_1[4] ==15:
                print("the winner is player_1,good job")
                break
            if player_1[0] + player_1[3] + player_1[4] ==15:
                print("the winner is player_1,good job")
                break
            if player_1[1] + player_1[2] + player_1[4] ==15:
                print("the winner is player_1,good job")
                break
            if player_1[1] + player_1[3] + player_1[4] ==15:
                print("the winner is player_1,good job")
                break
            if player_1[2] + player_1[3] +player_1[4] == 15:
                print("the winner is player_1,good job!")
                break
        #when all the elements are taken without winner,the game is a draw
        if len(numbers) == 0:
            print("the game is a draw")
            break
        #take element from user as input
        try:
           elem2= int(input("player_2,please Enter a number berween 1:9 :"))
        except:
             print("please, Enter a valid value")
             continue
        #check if the entered number between 1,9
        while elem2 < 1 or elem2 > 9:
            try:
               elem2= int(input("Not valid,please Enter a number in the range: "))
            except:
                print("please, Enter a valid value")
                continue
        #check if the entered number in the list or not
        y = True
        while y:
           if elem2 in numbers:
               numbers.remove(elem2)
               print(f"the numbers list now is: {numbers}")
               y = False
           else:
               try:
                  elem2 = int(input("you can not take the same element again, Take another element: "))
               except:
                   print("please, Enter a valid value")
                   continue
                   
        #add the elements to list two
        player_2.append(elem2)
        print(f"player 2, your list is: {player_2}")
       #check if the sum of the first three elements in the list two equals 15 or not 
        if len(player_2) == 3:
            if sum(player_2) == 15:
                print("the winner is player_2,excellent work!")
                break
        #when there are elements more than three elements, check if the sum of any three element (except for first three elemnts) of the list equals 15
        #test all the possible options when there are 4 elements in list one
        if len(player_2) == 4:
            if player_2[0] + player_2[1] + player_2[3] == 15:
                print("the winner is player_2,excellent work")
                break
            if player_2[0] + player_2[2] +player_2[3] == 15:
                print("the winner is player_2,excellent work")
                break
            if player_2[1] + player_2[2] + player_2[3] == 15:
                print("the winner is player_2,excellent work")
                break
        #counter
        i += 1
    #enable the user to play again or Exit
    choice = input("A)play again\nB)Exit: ").upper()
   #loop to ensure that user input A or B only
    while choice != "A" and choice != "B":
        choice = input("please,enter a valid choice A or B: ").upper()
    if choice == "A":
        numbers = [1,2,3,4,5,6,7,8,9]
        player_1 = []
        player_2 = []
    else:
        print("#"*5 ,"Thank You for this participation " , "#" *5)
        z = False
print("20230415")
print("20230394")
