# - - - - - - - - - Question1:

def sumFunc(num1, num2):
    sum = num1 + num2
    print(sum)
    
sumFunc(3,5)

# - - - - - - - - - Question2:

myList= [2, 4, 34, 6, 11, 15]

for num in myList:
    print(num)

# - - - - - - - - - Question3:

sumList= 0

for num in myList:
    sumList = sumList + num 

print("the sum for my list is: ", sumList)

# - - - - - - - - - Question4:

laggestNum= 0

for num in myList:
    if num > laggestNum:
        laggestNum= num

print("the lagest number is: ",laggestNum)

# - - - - - - - - - Question5:

def listFunc():

    newlist=[]
    lastIndex = int(input("Enter List Index: "))
    i = 0

    for i in range(i, lastIndex+1):
        newlist.append(i)
    print("My new list: ", newlist)

listFunc()

# - - - - - - - - - Question6:

myStr= "Tuwaiq_Academy"

for letter in myStr:
    print(letter)

# - - - - - - - - - Question7:

list = ["Python", "C++", "Java"]

for x in list:
    if x == "C++":
        break
    print(x)
    