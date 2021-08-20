
welcome_message = """
************** Welcome to Tic-Tac-Toe****************

    |   |   
-------------
    |   |   
-------------
    |   |   

**** Game Menu ****
1) player vs player
2) player vs computer
3) exit

"""
while True:
    print(welcome_message)
    selection = input("Make your selection: ")
    if selection == "3":
        break
