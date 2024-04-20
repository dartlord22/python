import random
import time

# setting up the operators, total number of problems in the game, and the min/max operand that can be randomly selected.  With the below code, it will not select any numbers less than 3 or greater than 15 to add, subtract, or mutliply
OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 15
TOTAL_PROBLEMS = 10


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    # the evaluate function will evaluate the answer of our expression for us so we don't need to code anything special to do this such as using if statements
    answer = eval(expr)
    # python treats this as a tuple even though it's not wrapped in parenthesis
    return expr, answer


wrong = 0
input("Press enter to start")
print("--------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):  # here we convert the answer to a string since it's an integer and our guess is a string.  Now we can compare them accurately
            break
        wrong += 1

end_time = time.time()
# rounding to 2 decimal places, otherwise we will get a long string of numbers
total_time = round(end_time - start_time, 2)

print("--------------------")
print("Nice work! You finished in", total_time,
      "seconds with", wrong, "incorrect guesses")
