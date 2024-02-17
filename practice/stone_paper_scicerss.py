import random as r
# options=["stone","paper","sciscers"]
# player1=r.choice(options)
# print(player1)
print("\t\tWelcome to the game: ")

def player_():
    player1=input("Enter your choies: ")
    options=["stone","paper","sciscers"]
    player2=r.choice(options)
    print(player1," ",player2)
    scoring(player1,player2)
def scoring(player1,player2):
    score_p1=0
    score_p2=0
    if player1=='S'or player1=='s'and player2=="paper":
        score_p2+=1
    elif player1=='S'or player1=='s'and player2=="sciscers":
        score_p1+=1
    elif player1=='s'or player1=='S'and player2=="stone":
        score_p1+=1
        score_p2+=1
    elif player1=='p'or player1=='P'and player2=="stone":
        score_p2+=1
    elif player1=='p'or player1=='P'and player2=="sciscers":
        score_p2+=1
    elif player1=='p'or player1=='P'and player2=="paper":
        score_p2+=1
        score_p1+=1
    elif player1=='c'or player1=='C'and player2=="stone":
        score_p2+=1
    elif player1=='c'or player1=='C'and player2=="paper":
        score_p1+=1
    elif player1=='c'or player1=='C'and player2=="sciscers":
        score_p2+=1
        score_p1+=1
    else:
        print("Invalid")
    if score_p1>score_p2:
        print("Player 1 is the winner ")
    elif score_p2>score_p1:
        print("player 2 is the winner ")
    else:
        print("The mathch is drow ")
player_()


    
    
