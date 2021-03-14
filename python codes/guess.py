secret_number=9
gc=0
gl=3
while gc<gl:
    guess=int(input("guess: "))
    if guess==secret_number:
        print("you won!")
        break
    else:
        if gc==2:
            print("sorry you failed")
            break
        print("try again")
    gc+=1