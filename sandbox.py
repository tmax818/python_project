
board = []
display_string = ""

for i in range(1, 101):
    board.append(str(i).zfill(2))

print(board)

for i in board:
    if int(i) % 20 == 0:
        display_string += i + '\n' * 2
    else:
        display_string += i + "  "

print(display_string)
