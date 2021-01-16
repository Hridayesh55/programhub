num=20
guesses=1
print("guess the number\ntotal number of attempt=5")
while(guesses<=5):
    a=int(input("enter your number ~ "))
    if a==num:
        print("congratulation you guess the right number\nnumber of gusses left 4")
        break
    elif a<num:
        print("your guessed number is to low")
    elif a>num:
        print("your guessed number is to high")
    print(5-guesses,"number of gusses left")
    guesses=guesses+1
if guesses>5:
    print("game over")


   
            
