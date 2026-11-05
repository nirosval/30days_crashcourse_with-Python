"""" 
hard_coded
"""
print('plongplong_coder')
answer = input("data_type_answer: ")
if answer == "string":
    print("Correct! The data type is string.")
    if answer != "string":
        print("Incorrect. Please try again.")
print(input("data_type_answer: "))


"""
Fix_by_AI
"""
print('Plongplong_coder')

# This loop will run forever until a correct answer hits the 'break' statement
while True:
    answer = input("data_type_answer: ")
    
    if answer == "string":
        print("Correct! The data type is string.")
        break  # Exits the loop and ends the program immediately
    else:
        print("Incorrect. Please try again.")

