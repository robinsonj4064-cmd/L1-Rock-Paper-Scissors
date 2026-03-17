#functions go here

def yes_no(question):
    """Checks user response to a question is yes / no (y/n), return 'yes' or 'no'"""

    while True:

        response = input(question).lower()

        #check the user say yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


def instructions():
    print(''''
   
**** Instructions ****

To begin, choose the number of rounds (or play infinite mode).

Then play against the computer. You need to pick R (rock), P (paper) or S (scissors).

The rules are as followed:
Paper beats rock
Rock beats scissors
Scissors beats paper

Good luck!! :p
    ''')



#Main routine
def string_checker(question, valid_ans=('yes', 'no')):

 error = f"Please enter a valid option from the following list: {valid_ans}"

 while True:

    """Checks users enter either the first letter of the
    full word based on a series of valid answers"""


    # Get user response and make sure it's lowercase
    user_response = input(question).lower()

    for item in valid_ans:
        # check if the user response is a word in the list
        if item == user_response:
            return item

         # check if the user response is the same as
         # the first letter of an item in the list
        elif user_response == item[0]:
            return item

    # print error if user does not enter something that is valid
    print(error)
    print()


print()
print("💎📃✂️ Rock / Paper / Scissors Game")
print()



# ask the user if they want instructions (check they said yes / no)
# them if requested
want_instructions = string_checker("Do you want to see the instructions? ")

# Display the instructions if the user want to see them...
if want_instructions == "yes":
    instructions()

print("Program continues")
