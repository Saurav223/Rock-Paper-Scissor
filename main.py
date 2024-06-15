import random
def winner(x,y):
    global scorebot,scorepla
    if(x == 'rock'):
        if(y == 'paper'):
            print("You Won")
            scorepla+=1
        else:
            print("You lose")
            scorebot+=1
        
    elif(x == 'paper'):
        if(y == 'rock'):
            print("You lose")
            scorebot+=1
        else:
            print("You won")
            scorepla+=1
    
    else:
        if(y == 'rock'):
            print("You Won")
            scorepla+=1
        else:
            print("You lose")
            scorebot+=1

    

option = ['rock','paper','scissor']
scorebot = 0
scorepla = 0
draw = 0

print("*****Welcom to Rock Paper Scisor Game*****")
round = int(input("Enter no. round of game you want :"))
for i in range(1,round+1):
    bot = random.choice(option)
    print(f"\n---ROUND {i}---")
    print("Enter your Choice in Number")
    choice = int(input("1.Rock   2.Paper   3.Scissor   "))
    if(bot == option[choice-1]):
        print(f"Both choose {bot}")
        print("This Round is Draw")
        draw += 1
    else:
        print(f"You choice {option[choice-1]}")
        print(f"Bot choice {bot}")
        winner(bot,option[choice-1])
        print('\n')

print(f"\nYour score = {scorepla} \nBot score = {scorebot} \nDraw = {draw}")