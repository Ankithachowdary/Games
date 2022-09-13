print("Welcome to the quiz")
a = input("are you ready to play the quiz game? (yes/no): ")
score = 0
questions = 3

if a.lower() == "yes":
    a = input("question 1: what is the capital of India: ")
    if a.lower() == "delhi":
        score += 1
        print("correct")
    else:
        print("wrong answer")

    a = input("question 2: who is the first prime minister of India: ")
    if a.lower() == "jawaharlal nehru":
        score += 1
        print("correct")
    else:
        print("wrong answer")

    a = input("question 3: what is the national game of India: ")
    if a.lower() == "hockey":
        score += 1
        print("correct")
    else:
        print("wrong answer")
print("Thank you for playing the quiz game")
print("your score is: ", score)
marks = (score / questions) * 100
print("marks obtained are: ", marks)
print("bye")

