def hanoi(n , start , end):
    if n == 1:
        pm(start, end)
    else:
        other  = 6 - (start + end)
        hanoi(n - 1, start , other)
        pm(start , end)
        hanoi(n - 1, other , end)

def pm(start , end):
    global total_moves
    total_moves += 1
    print (start , "->" , end)


total_moves = 0
hanoi(3,  1 , 3)
print("Total moves:", total_moves)