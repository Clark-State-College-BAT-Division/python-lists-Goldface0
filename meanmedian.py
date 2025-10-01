#prompt the user to enter 5 numbers. Store them in a list.
#Display the list as entered, small to large, and large to small
#Calculate and display the mean and median
#This is a guided practice. You can follow the video or your instructor will go
#over this in class

# I know it's not necessary for this example,
# but I'm declaring nums this way to practice
# good habits
nums = []
total = 0

for _ in range(5):
    nums.append(int(input("Please enter a number: ")))
for i in range(5):
    total += nums[i]

print(nums)

nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

mean = (total/len(nums))
print(f"The mean is: {mean}" )

median = nums[2]
print(f"The median is: {median}")