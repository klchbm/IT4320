#fizzbuzz version 1

for number in range (1, 101):
    string = ""
    if number % 3 == 0:
        string = string + "Fizz"
    if number % 5 == 0:
        string = string + "Buzz"
    if number % 3 != 0 and number % 5 != 0:
        string = string + str(number)
    print(string)
