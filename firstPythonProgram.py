#print hello world

print("Hello World!")

#cast 33 value into float, string, int
turnFloat = float(33)
turnString = str(33)
turnInteger = int(33)
print(turnFloat, turnString, turnInteger)

#get type
x = 5
X = 23
y = "John"
z = 33.66
print(type(x))
print(type(y))
print(type(z))
print(x, X)

#assign multiple values / concatination
firstFruit, secondFruit, thirdFruit = "Apple", "Banana", "Orange"
print(firstFruit, secondFruit, thirdFruit)
print("My favorite fruit is " + secondFruit)

#one value to multiple variables
firstColor = secondColor = thirdColor = "Maroon"
print(firstColor)
print(secondColor)
print(thirdColor)

#unpacking
fruits = ["apple", "banana", "cherry"]
aFruit, bFruit, cFruit = fruits
print(aFruit)
print(bFruit)
print(cFruit)

#output variables
descriptionPython = "awesome"
print("Python is " + descriptionPython)
firstString = "Python is "
secondString = "awesome."
outputValue = firstString + secondString
print(outputValue)

#math addition
aPlus = 10
bPlus = 25
cTotal = aPlus + bPlus
print(cTotal)
print(aPlus + bPlus)

#global variables in function
definitionGlobal = "great"
def firstFunction():
    print("I am " + definitionGlobal)

firstFunction()

#same global variables that are declared in a function
sameVariableGlobal = "awesome"
def myfunc():
    sameVariableGlobal = "fantastic"
    print("Python is " + sameVariableGlobal)

myfunc()
print("Python is " + sameVariableGlobal)

#global in function
def secondFunction():
    global variableFunctionGlobal
    variableFunctionGlobal = "Darude - Sandstorm"

secondFunction()
print("Next song to be played is " + variableFunctionGlobal)

#import random
import random
print(random.randrange(1, 100))
print(random.random())

#multiline string
loremIpsum = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(loremIpsum)
print(loremIpsum[18])
#print(loremIpsum[random.randrange(1, 50)]) doesnt work atm just a trial

#for loop in string // get length
for spellValue in "Lorem ipsum":
    print(spellValue)
    #print(len(spellValue))

spellValueLength = "Lorem ipsum"
print(len(spellValueLength))

#check string
textCheck = "The best things in life are free!" 
print("free" in textCheck)

# check string input trial
# searchText = "The best things in life are free!"
# searchValue = input()
# print(searchValue in searchText)

#check if
sampleText = "The best things in life are free!" 
if "things" in sampleText:
    print("Yes, value is present in '" + sampleText + "'")

if "walay" not in sampleText:
    print("Walay not in sampleText")
else:
    print("Wala ka man ngayon sa aking piling")

#slice
text1 = "Wala ka man ngayon sa aking piling"
print(text1[8:19])
print(text1[:19])
print(text1[19:])

#upperCaseLowerCase
sampleQoutation = "Lorem ipsum dolor sit amet, consectetur adipiscing elit,"
def sampleTextToGlobal():
    global lyricsGLobal
    lyricsGLobal = "Wala ka man ngayon sa aking piling, nasasaktan man ang puso't damdamin."
    print(lyricsGLobal)

sampleTextToGlobal()
print(lyricsGLobal.upper())
print(sampleQoutation.upper())
print(sampleQoutation.lower())

#replaceString
print(lyricsGLobal.replace("s", "t"))

#splitString the split() method splits the string into substrings if it finds instances of the separator:
splitText = lyricsGLobal.split("a")
print(splitText)

#trial converting / cant concatinate str and int 
age = 36
ageConvert = str(age)
txt = "My name is John, I am " + ageConvert
print(txt)


#format strings
#can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
#starts with 0 as well
userAge = 20
userIntroduction = "My name is Karen and I am {}"
print(userIntroduction.format(userAge))

itemQuantity = 10
itemNumber = 2053
itemPrice = 16.50
customerOrder = "I want {} pieces of item {} for {} dollars."
print(customerOrder.format(itemQuantity, itemNumber, itemPrice))

customerOrder2 = "I want to pay {2} dollars for {0} pieces of item {1}."
print(customerOrder2.format(itemQuantity, itemNumber, itemPrice))

#center
wanheda = "scared to be lonely"
print(wanheda.center(100))
print(lyricsGLobal.center(150))

#lists index starts with 0
characterList = ["Otis", "Eric", "Maeve", "Adam", "Jackson", "Otis", "Lily"]
print(characterList)
print(len(characterList))
print(characterList[2])

#end Dec 3 2020

#change list
characterList[5] = "Jean"
print(characterList)

#insert list
characterList.insert(4, "Aimee")
print(characterList)

#append list
characterList.append("Rahim")
print(characterList)

#extend list
characterUntouchableList = ["Ruby", "Anwar", "Olivia"]
characterList.extend(characterUntouchableList)
print(characterList)

#you can add tuple in a list using .extend()

#remove list .pop removes the last item if you do not specify the index
#del keyword can also be used
characterList.remove("Otis")
print(characterList)
characterList.pop(1)
print(characterList)
del characterList[0]
print(characterList)

#clear list .clear empties the list but it still remains
characterUntouchableList.clear()
print(characterUntouchableList)

#loop in list
for checkCharacterList in characterList:
    print(checkCharacterList)

#while loop
countLoop = 0
while countLoop < len(characterList):
    print(characterList[countLoop])
    countLoop = countLoop + 1

#list comprehension
# characterListComprehension = [ checkForA for characterList if "a" in checkForA ]
# print(characterListComprehension)

#sort list
characterList.sort(key = str.lower)
print(characterList)

#sort reverse
characterList.sort(reverse = True) #or .reverse
print(characterList)

#copy list
characterListCopied = characterList.copy()
print(characterListCopied)
characterListCopied2 = list(characterList)
print(characterListCopied2)

#join list methods
characterListJoined = characterList + characterUntouchableList
print(characterListJoined)

characterList.extend(characterUntouchableList)
print(characterList)

#tuples
colorTuple = ("red", "yellow", "blue", "red", "green", "violet", "orange")
print(colorTuple)
print(colorTuple)

oneColorTuple = ("purple", )
print(type(oneColorTuple))

#check in tuple
if "green" in colorTuple:
    print("Green is inside the colorTuple")

#tuples can be converted into list and vice versa
convertColorTupleToList = list(colorTuple)
convertColorTupleToList[0] = "maroon"
print(convertColorTupleToList) #print to see convertion
colorTuple = tuple(convertColorTupleToList)
print(colorTuple)

#unpacking tuple / using asterisk creates a list for the rest
fruitsTuple = ("apple", "banana", "cherry", "dragonfruit", "strawberry")
(green, yellow, *red) = fruitsTuple
print(green)
print(yellow)
print(red)

#while loop in tuple
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
#eek

#multiplying tuple
multipliedFruitsTuple = fruitsTuple * 2
print(multipliedFruitsTuple)

#start dec7
#if elif else
value1 = 200
value2 = 33
value3 = 200

if value1 > value2:
    print("value1: " + str(value1) + " is greater than value2: " + str(value2))
else:
    print("value1: " + str(value1) + " is less than value2: " + str(value2))

if value1 > value3:
    print("value1: " + str(value1) + " is greater than value3: " + str(value3))
elif value1 == value3:
    print("value1: " + str(value1) + " has the same value as value3: " + str(value3))
else:
    print("value1: " + str(value1) + " is less than value3: " + str(value3))

if value1 > value2 and value2 < value3:
    print("Both conditions are true")
else:
    print("One condition did not satisfy")

if value1 == value2 or value2 == value3:
    print("Both conditions are true")
else:
    print("At least one condition was not satisfied")

if value3 >= value2:
    pass

#while loop
iWhile = 1
while iWhile < 10:
    print(iWhile)
    iWhile = iWhile + 1

iWhile = 1
while iWhile < 10:
    print(iWhile)
    if iWhile == 3:
        break
    iWhile += 1

iWhile = 0
while iWhile < 10:
    iWhile += 1
    if iWhile == 5:
        continue
    print(iWhile)

#for loop
for sexEd in characterList:
    print(sexEd)

#break for loop
for sexEd2 in characterList:
    print(sexEd2)
    if sexEd2 == "Jackson":
        break

#range for loop
for xRange in range(5): #up to 5
    print(xRange)

for xRange2 in range(1, 5): #starts with 1
    print(xRange2)

for xRange3 in range(1, 40, 3): #count/increment by 3
    print(xRange3)

for xRange4 in range(5):
    print(xRange4)
else:
    print("Finished counting!")

#nested for loop
adjective = ["red", "big", "tasty"]
prutas = ["apple", "banana", "cherry"]

for xAdjective in adjective:
    for xPrutas in prutas:
        print(xAdjective, xPrutas)

#functions
def nameFunction(firstName, lastName):
    print("My full name is " + firstName + " " + lastName)

nameFunction("Karen", "Low")

#functions using *
def childFunction(*child):
    print("My eldest child is " + child[2])

childFunction("Aleksib", "Nitro", "Kekw")

#function keywords
def my_function(child3, child2, child1):
    print("The youngest child is " + child2)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#function default
def myCountry(country = "Norway"):
    print("My country is " + country)

myCountry("Nepal")
myCountry("India")
myCountry()
myCountry("Sweden")

#function list
def listFunction(prutasMo):
    for pruts in prutasMo:
        print(pruts)

prutas = ["apple", "banana", "cherry"]
listFunction(prutas)

#function return
def returnFunction(valueReturn):
    return valueReturn * 10

print(returnFunction(4))
print(returnFunction(3))
print(returnFunction(8))

#lambda syntax -> lambda arguments : expression
xLamb = lambda aLamb: aLamb + 10
print(xLamb(5))

aa = lambda xx, yy : xx * yy
print(aa(6, 10))


def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))

#array
import numpy as np

myArray = np.array([1, 2, 3, 4, 5])
print(myArray)
print(np.__version__)

#class
class myClass:      #this is a class
    classValue = 10

objectP1 = myClass()    #this is an object
print(objectP1.classValue)

#__init__() function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 34)
print(p1.name)
print(p1.age)

#init round 2
class Robot: #this is the class
    def introduce_self(self):
        print("My name is : " + self.name)

r1 = Robot() #this is the object
r1.name = "Tom"
r1.color = "red"
r1.weight = 30

r2 = Robot() #this is the object
r2.name = "Jerry"
r2.color = "blue"
r2.weight = 40

r1.introduce_self()
r2.introduce_self()

#init from youtube
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullInfo(self):
        return '{} {}'.format(self.first, self.last)

emp1 = Employee("correy", "smirth", 50000)
emp2 = Employee("test", "user", 60000)

# print(emp1)
# print(emp2)

print(emp1.first)
print(emp2.first)
print(emp2.fullInfo())










#no look init class function
class Students:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def fullName(self):
        print("student info is " + self.firstName + " " + self.lastName)

s1 = Students("amer", "al barkawi")
s2 = Students("artour", "babaev")

s1.fullName()
s2.fullName()











#inheritance class
class InformationTechnology:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
    def showInformationTechnology(self):
        print("Student name: " + self.lastName + " " + self.firstName)

section1 = InformationTechnology("Hye Jun", "Sa")
section2 = InformationTechnology("Jeong Ha", "An")
section1.showInformationTechnology()
section2.showInformationTechnology()

class Program(InformationTechnology):
    #pass
    def __init__(self, firstName, lastName, graduationYear):
        #InformationTechnology.__init__(self, firstName, lastName)
        super().__init__(firstName, lastName)
        self.graduationYear = graduationYear
    def withYear(self):
        print("Student name: " + self.lastName + " " + self.firstName + " \nGraduation year: " + str(self.graduationYear))

section3 = Program("Hae Na", "Won", 2020)
#section3.showInformationTechnology() works
section3.withYear()
print(section3.graduationYear)












#inheritance class my work no look
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def printDetails(self):
        print("your name is " + self.name + " with email " + self.email)

class Common(User): #inheritance by calling parent class User/ this is the child class
    def __init__(self, name, email, id): #put new parameters for child class
        super().__init__(name, email) #to inherit all from parent
        self.id = id

    def commonDetails(self):
        print("your name is " + self.name + " with email " + self.email + " and id " + str(self.id))

customer = User("amashi", "amashi@company.com") #object for class User
customer2 = Common("seijuro", "seijuro@company.com", 2020001)
customer.printDetails() #called function using customer object
customer2.commonDetails()











#inheritance class my work no look try 2
class Coach:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def employeeDetails(self):
        print("Name: " + self.name + "\nAge: " + str(self.age) + "\nSalary: " + str(self.salary))

class Additional(Coach):
    def __init__(self, name, age, salary, status):
        super().__init__(name, age, salary)
        self.status = status

    def addEmployeeDetails(self):
        print("Name: " + self.name + "\nAge: " + str(self.age) + "\nSalary: " + str(self.salary) +
              "\nStatus: " + self.status)

employee = Coach("John", 26, 26000)
employee2 = Coach("Sarah", 30, 45200)
employee3 = Additional("Joji", 26, 26200, "Regular")
employee4 = Additional("Lina", 22, 20000, "Part Time")
employee.employeeDetails()
employee2.employeeDetails()
employee3.addEmployeeDetails()
employee4.addEmployeeDetails()
employee3.employeeDetails()
employee4.employeeDetails()
employee5 = Additional("Tyler", 34, 29500, "Terminated")
employee5.addEmployeeDetails()
