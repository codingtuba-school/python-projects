from random import randint as random

# order declartion
order=[
    0,0,0,0,3
]

# define what each display will look like

# [
#   int <number of new lines>,
#   string <what to display for line>
# ]

displays=[
    [0,"0"],
    [0,">1"],
    [1,"2"],
    [1,">3"],
]

# generate 4 random moves for the user
for i in range(4):
    # generate random move
    order[i]=random(0,2)

print(order)
print("----------------")

def display(i):
    # display the signifier for the input
    for line in range(displays[i][0]):
        print()
    print(displays[i][1])

# loop through the moves
for i in order:
    # display the move
    display(i)
    # wait for move input
    input("----------------")