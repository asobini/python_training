### Random function
import random

random_integer = random.randint(1,12)
print(random_integer)

#Creating random floating point numbers
random_number_0_to_1 = random.random()
print(random_number_0_to_1)

# Random_Floating point number generation with two boarders
random_float = random.uniform(1,10)
print(random_float)


# short code to program heads or tails

random_integer = random.randint(1,2)
if random_integer == 1:
    print("Heads")
else: 
    print("Tails")


# Lists in Python
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia"]
print(states_of_america[1])
print(states_of_america[-1])

# add / append items to list
states_of_america.append("Florida")
print(states_of_america)
## extend list with multiple items
states_of_america.extend(["California", "Virginia", "Kansas", "South Carolina"])
print(states_of_america)
print(len(states_of_america))

## Code challange - Who pays the bill
import random
friends_list = ["Alicia", "Ali", "Sam", "Steve", "Peter"]
print(friends_list[random.randint(0,4)])

# alternative way
print(random.choice(friends_list))


## nested lists
fruits = ["apple", "banana", "kiwi"]
vegtables = ["potatos", "onion", "kale"]
dirty_dozens = [fruits, vegtables]
print(dirty_dozens)
print(dirty_dozens[1][0])


# Rock Paper Scissors Game
import random
print("Welcome to Rock Paper Scissors Game")

my_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
computer_choice = random.randint(0,2)
if my_choice == 0:
    if computer_choice == 1:
        print("you loose")
    elif computer_choice == 2:
        print("you won")
    elif computer_choice == 0:
        print("draw")
    else: 
        print("your input is wrong")

elif my_choice == 1:
    if computer_choice == 0:
        print("you won")
    elif computer_choice ==1:
        print("draw")
    elif computer_choice == 2:
        print("you loose")
    else: 
        print("you entered wrong input")
elif my_choice == 2:
    if computer_choice == 0:
        print("you loose")
    elif computer_choice ==1:
        print("you won")
    elif computer_choice ==2:
        print("draw")
    else:
        print("wrong entry")

else:
    print("your entry is wrong, please check")


## For Looos

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
print(fruits)


# For Loops, Sum and Highest score

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89]
# total summ

total_sum = 0  # Renamed from sum1 to total_sum to avoid conflict with the built-in sum function
for score in student_scores:
    total_sum += score
print(total_sum)  # This prints the sum calculated in the loop
#highest score
hiscore = 0
for score in student_scores:
    if score > hiscore:
        hiscore = score
print(hiscore)

# Python Password Generator with fixed order

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = " "
for letter in range(0, nr_letters):
    password+= random.choice(letters)

for symbol in range(0, nr_symbols):
    password+= random.choice(symbols)

for number in range(0, nr_numbers):
    password+= random.choice(numbers)

print(password)
