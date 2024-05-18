# print("Card:")
term = input()
# print(term)

# print("Definition:")
definition = input()
# print(definition)

answer = input()

right_answer = "Your answer is right!"
wrong_answer = "Your answer is wrong..."

if answer == definition:
    print(right_answer)
elif answer != definition:
    print(wrong_answer)
