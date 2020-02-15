win=0
loss=0
for x in range(6):
    n=input("win or lose?")
    if n =="W" or n =="w":
        win += 1
    else:
        loss += 1
if win == 5 or win == 6:
    print("Group 1")
if win == 4 or win == 3:
    print("Group 2")
if win == 2 or win == 1:
    print("Group 3")
if win == 0:
    print("Group -1")