command=""
started=0
while command!=quit:
    command=input("").lower()
    if command == 'start':
        if started==1:
            print("car is already started")
        else:
            started=1
            print("car is started")
    elif command=='stop':
        if  started==1:
            print("car is  stopped")
            started=0
        else:
            print("car is already stopped..")
    elif command=='help':
        print("""
        start-to start the car
        stop- to stop the  car
        quit- to exit""")
    elif command=="quit":
        break
    else:
        print("sorry!, i don't understamd that..")