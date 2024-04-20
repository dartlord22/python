print("Welcome to quiz game!")

playing = input("Do you want to play? (Y/N) ")

if playing.lower() != "y":
    quit()

score = 0

answer = input("Who is my favorite person? ")
if answer.lower() == "my mom":
    print('Correct!')
    score += 1
else:
    print("Wrong!")


answer = input("What is my catch phrase? ")
if answer.lower() == "your mom":
    print('Correct!')
    score += 1
else:
    print("Wrong!")

# print the number of questions answered correctly
# score has to be converted to a string so we can add it to the other strings
print("You got " + str(score) + " of 2 questions correct")
