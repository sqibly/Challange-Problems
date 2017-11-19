#get input of x
x = int(input("number for width: "))
#get input of y
y = int(input("number for length: "))

#print first line
for i in range(0, x):
    print("+", end="")

print("")

#determine if the second line has = signes
#print out second through second to last
if x>2:
    for i in range(0, y-2):
        print("+", end="")
        for i in range(0, x-2):
            print("=", end="")
        print("+", end="")
        print("")

#print out last line
for i in range(0, x):
    print("+", end="")

print("")
