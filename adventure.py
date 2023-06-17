name=input("Type Your Name: ")
print("Welcome",name,"To This Adventure")
answer=input("You Are On Dirt Road,It Has Come To An And You Can Go Left Or Right.Which Way Would Like To Go?").lower()
if answer=="left":
    answer=input("Yoc Can Come To River,You Can Walk Arround It Or Swim Across? Type Walk To Arround And Swim If You Want To Swim Across: ")
    if answer=="swim":
        print("You swam across the river and were Eaten by an Alligator")
    elif answer=="walk":
        print("You Walked Miles, Ran Out Of The Water And Lost The Game.")
    else:
        print("Not valid option.you lose")
elif answer=="right":
    answer=input("You Came Across a Bridge,It Looks Wobbly,Do You Want To Cross It Or Head Back(Cross/Back)? ")
    if answer=="back":
     print("You go back and lose")
    elif answer=="cross":
     answer=input("You Cross The Bridge And Met a Stranger.Do You Want To Talk To Him(Yes/ No) ")
     if answer=="yes":
        print("You Talk The Stranger And They Gift You The Tressure.You Won!!!!")
     elif answer=="no":
        print("You Ignore The Stranger And They Get Offened And You Lose")
     else:
        print("Invalid Option You Losed")
    else:
       print("Invalid Option You Losed")
else:
    print("Invalid Option You Lose!!!")
print("Thank You For Trying ",name)    