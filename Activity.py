#Counting Prime Numbers In Student Number
print("enter student nymber:")
snumber= input()
print("0. The student number is: " + str(snumber))
stringsnumber = str(snumber)
listsnumber =[]
p=0
for digit in stringsnumber:
    listsnumber.append(int(digit))
for num in listsnumber:
    if num > 1:   
   # Iterate from 2 to n / 2  
        for i in range(2, num//2):    
       # If num is divisible by any number between  
       # 2 and n / 2, it is not prime  
            if (num % i) == 0: 
                p += 0
                break
    else: 
       p +=1
else: 
   p +=0
print("1. The number of prime numbers in this student number is " + str(p))
#Getting Random Number
import random
q =random.randint(25,50)
print("2. The random number is: " + str(q))
#Number of Strings To Be Generated Is
r = round(q/p)
print("3. The number of strings to be generated is: " + str(r))
#Generate Random Strings
import string
def randomString(stringLength=5):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
print("4. List of Strings:")
print("******************")
listletters = []
for x in range(0,r):
    if((x%2) !=0):
        five = randomString(5)
        print(five)
        listletters.append(five)
    elif((x%2) ==0):
        seven = randomString(7)
        print(seven)
        listletters.append(seven)
print("******************")
#Doing The Sorted List
print("5. Sorted List:")
print("******************")
def vowelCounter(listName):
    string = ''.join(listName)
    count = 0
    vowels = 'aeiouAEIOU'
    for ch in string:
        if ch in vowels:
            count += 1
    return count

for x in range(0,r):
    vowelcount = []
    count = vowelCounter(listletters[x])
    vowelcount.append(count)
    print(str(listletters[x]) + " (Vowels: " + str(vowelcount) +")")
print("******************")