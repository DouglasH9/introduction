num1 = 42
num2 = 2.3
boolean = True
string = 'Hello World'
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
# array^

person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
# object^

fruit = ('blueberry', 'strawberry', 'banana')
# variable declarations^

print(type(fruit))
print(pizza_toppings[1])
# log statements^

pizza_toppings.append('Mushrooms')
# add value^

print(person['name'])
# log statement

person['name'] = 'George'
person['eye_color'] = 'blue'
# change value^

print(fruit[2])
# log statement

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
# conditional statement

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
# conditional statement

for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
# for loops^
x = 0
# variable declaration
while(x < 5):
    print(x)
    x += 1
# while loop

pizza_toppings.pop()
pizza_toppings.pop(1)
# change value^

print(person)
person.pop('eye_color')
print(person)
# log statement

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
    # conditional statement and for loop

def print_hello_ten_times():
    for num in range(10):
        print('Hello')
        # function with for loop

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')
        # function with for loop

print_hello_x_times(4)
# log statement

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')
        # function with for loop and log statement

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)
# log statement


"""
Bonus section
"""
function acronym(str) {
    // your code here
    var acr = ""
    //iterate through string
    for(var i = 0; i < str.length; i++){
        //character after space is part of the acronym
        if(str[i] == " " && str[i+1] !== " " && str[i+1] !== undefined){
            acr += str[i+1]
        }
        if(i == 0 && str[i] !== " "){
            acr += str[i]
        }
    }
    //first character would be apart of the acronym. 
    return acr.toLocaleUpperCase()
}
//acronym("there's no free lunch - gotta pay yer way")
console.log(acronym(" there's no free lunch - gotta pay yer way "));



// Implement reverseString(str) that takes in a String, and then returns a string of the same length, but with the characters reversed.

// Example: "creature" ---> "erutaerc"

// ** Don't use the built-in reverse() method!

function reverseString(str) {
    // your code here
    var newstr = ""
    for(var i = str.length-1; i >= 0; i--){
        newstr += str[i]
    }
    return newstr
}

console.log(reverseString("creature")); // "erutaerc"

Message #🏫cohort-kaysee-nick-robert
# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)