fruits = ["apple", "orange", "banana", "mango"]
nums = [[0,1,1,0],[1,1,1,0],[0,0,0,0]]

file = open("generalizedRooms.txt","w")

for fruit in range(0, len(fruits) - 1):
    file.write("\"")
    file.write(fruits[fruit])
    file.write("\"")
    file.write(",")
file.write("\"")
file.write(fruits[len(fruits)-1])
file.write("\"")
file.write("\n")

for x in range(0, len(nums)):
    for y in range(0, len(nums[x]) - 1):
        z = str(nums[x][y]) + ","
        file.write(z)
    file.write(str(nums[x][y+1]))
    file.write("\n")

file.close()
