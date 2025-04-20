#Write a function that takes two parameters: a prompt message and an error message.
#The function will prompt the user with the passed in prompt to enter an integer
#If the text entered cannot be cast to an int, display the error message.
#The function will continue to prompt the user to enter an integer until a proper integer is entered.
#The most direct way of doing this would be using a try block, which has not been covered yet. You will need to research this.
#Write supporting code to call the function, and then display the number that was entered.

def get_integer(prompt, error_message): 
    while True: 
        user_choice = input(prompt)
        try:
            return int(user_choice)
        except ValueError:
            print("That is not a valid choice, retry!")

number = get_integer("Please enter a number: ", "That is not a valid number, retry!")
print(f"Your entered: {number}")
