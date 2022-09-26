
# Question 1: Write a function that takes two numbers and return their sum

def sum(num1,num2):
    return num1+num2
print(sum(1,2))

# Question 2: Prints all the elements in the list using a for loop
def priEle(list):
    for x in list:
        print(x)

mylist=[1,2,3]
priEle(mylist)

# Question 3: Write a Python program to sum all the items in the list
def listSum(list):
    sum=0
    for x in list:
        sum=sum+x
    return sum
        
print(listSum(mylist))
# Question 4: Write a Python program to get the largest number from the list
def largest(list):
    maxi=max(list)
    print(maxi)

largest(mylist)

# Question 5: write a function that take a list and a number then return a new partial list starting from index 0 to index "number"

def add_index(list,num):
    list.append(num)
    print(list)

add_index(mylist,4)
# Question 6: Loop through the letters in the string: "Tuwaiq_Academy
letter="Tuwaiq_Academy"
for x in letter:
    print(x , "\n")

# Question 7: Consider this list = ["Python", "C++", "Java"] Exit the loop when x is equal to "C++"

yourlist=["Python", "C++", "Java"]

for x in yourlist:
    if x=="C++":
        break
    else:
        print(x)