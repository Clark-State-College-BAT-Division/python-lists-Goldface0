#Create two seperate lists for player one and player two. 
#Each one should contain 10 random numbers between 1 and 50.
#Do NOT sort the lists.
#Compare the lists in order. Whichever list has the higher number wins.
#Keep track of how many times each list wins.
#Find the highest number in each list and it's index. If the number occers multiple times take the first instsance.
#Find the lowest number in each list and it's index. If the number occers multiple times take the first instsance.
#A tie is not record as a win for either player
#Display the lists
#Report to the user how many times each player won and the information from lines 6 and 7.
#For the example output I am limiting the range to 1 to 9 to keep it more readable.

#Player One = [5,7,2,9,1,1,3,8,6,9]
#Player Two = [3,8,5,5,8,1,4,7,4,7]
#Player one won 5 times
#Player two won 4 times
#Player one's highest number is 9 at index 3
#Player two's highest number is 8 at index 1
#Player one's lowest number is 1 at index 4
#Player two's lowest number is 1 at index 5

import random
p1 = []
p2 = []

# 10 means there will be 10 elements in the array
# each list, p1 and p2, will be filled with 10 randomly
# gennerated numbers 1-50 each
for _ in range(10):
    p1.append(random.randint(1,50))
    p2.append(random.randint(1,50))

print(f"Player One = {p1}\nPlayer Two = {p2}")

p1Wins = 0
p2Wins = 0

# index 0 = the number stored
# index 1 = the index of said number
# index 0 of the low variables must be set to 51 for it to work, 
# as 51 is higher than the program can output on its own
# This probably isn't the best way to do this, but it works!
p1High = [0,0]
p1Low = [51,0]
p2High = [0,0]
p2Low = [51,0]

for i in range(len(p1)):
    if p1[i] > p2[i]:
        p1Wins += 1

    elif p2[i] > p1[i]:
        p2Wins += 1

    # I was told not to use sort,
    # I'm aware this is terrifying code,
    # but it works somehow, so it stays!
    if p1[i] > p1High[0]:
        p1High = [p1[i],i]
    if p2[i] > p2High[0]:
        p2High = [p2[i],i]
    if p1[i] < p1Low[0]:
        p1Low = [p1[i],i]
    if p2[i] < p2Low[0]:
        p2Low = [p2[i],i]
print(f"Player one won {p1Wins} times\nPlayer two won {p2Wins} times")
print(f"Player one's highest number is {p1High[0]} at index {p1High[1]}")
print(f"Player two's highest number is {p2High[0]} at index {p2High[1]}")
print(f"Player one's lowest number is {p1Low[0]} at index {p1Low[1]}")
print(f"Player two's lowest number is {p2Low[0]} at index {p2Low[1]}")