import random
from unittest import result


# Check that users have entered a valid
# option based on a list

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

# Display Instructions
def instructions():
    print(''''

**** Instructions ****

To begin, choose the number of rounds (or play infinite mode).

Then play against the computer. You need to pick R (rock), P (paper) or S (scissors).

The rules are as followed:
Paper beats rock
Rock beats scissors
Scissors beats paper

Good luck!! :p (you will need it...)
    ''')

def int_check(question):
    """Checks users enter on integer more than / equal to 13"""

    while True:
        error = "Please enter an integer that is 1 or more."

        response = input(question)

        # check for infinite mode
        if response == "":
            return ""

        try:
            response =int(response)

            #check that the number is more than / equal to 13
            if response < 1:
                print(error)

            else:
                return response

        except ValueError:
            print(error)

# compares user / computer choice and returns
# results (win / lose / tie)
def rps_compare(user, comp) :

    # If the user and the computer choice is the same, it's a tie
    if user == comp:
        round_result = "tie"

    # There are three ways to win
    elif user == "paper" and comp == "rock":
        round_result = "win"
    elif user == "scissors" and comp == "paper":
        round_result = "win"
    elif user == "rock" and comp == "scissors":
        round_result = "win"

    # if it's not a win / tie, then it's a loss
    else:
        round_result = "lose"

    return round_result


# Main routine starts here

# Intialise game variables
mode = "regular"
rounds_played = 0
rounds_tied = 0
rounds_lost = 0

rps_list = ["rock", "paper", "scissors", "xxx"]
game_history = []

print("💎📃✂️ Rock / Paper / Scissors Game 💎📃✂️")
print()

# ask the user if they want instructions (check they said yes / no)
# them if requested
want_instructions = string_checker("Do you want to see the instructions? ")

# Display the instructions if the user want to see them...
if want_instructions == "yes":
    instructions()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds heading
    if mode == "infinite":
        rounds_heading = f"\n♾️♾️♾️ Round {rounds_played + 1} (Infinite Mode) ♾️♾️♾️"
    else:
        rounds_heading = f"\n💿💿💿 Round {rounds_played + 1 } of {num_rounds} 💿💿💿"

    print(rounds_heading)
    print()

    comp_choice = random.choice(rps_list[:-1])
    print("Computer choice", comp_choice)


    user_choice = string_checker("Choose: ", rps_list)
    print("you chose", user_choice)

    if user_choice == "xxx":
        break



    result = rps_compare(user_choice, comp_choice)

    if result == "tie":
       rounds_tied += 1
       feedback = "👔👔 It's a tie!! 👔👔"
    elif result == "lose":
       rounds_lost += 1
       feedback = "😭😭 You Lost! 😭😭"
    else:
       feedback = "❤️❤️ You Won!!!! ❤️❤️"

    round_feedback = f"{user_choice} vs {comp_choice}, {feedback}"
    history_item = f"Round: {rounds_played} - {round_feedback}"

    print(round_feedback)
    game_history.append(history_item)
    rounds_played += 1
    # if user are in infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1


# Game loop ends here

if rounds_played > 0:
    # Calculate Statistics
    rounds_won = rounds_played - rounds_tied - rounds_lost
    percent_won = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100
    percent_tied = 100 - percent_won - percent_lost

    # Output Game Statistics
    print("📊📊📊 Game Statistics 📊📊📊")
    print(f"❤️ Won: {percent_won:.2f} \t"
          f"😭 Lost: {percent_lost:.2f} \t"
          f"👔 Tied: {percent_tied:.2f}")

    # initialise list to hold game history
    game_history = []

    # Game history / Statistics area
    see_history = string_checker("\nDo you want to see your game history? ")
    if see_history == "yes":
        print("Game History")

    for item in game_history:
        print(item)

    print()
    print("Thanks for playing.")

else:
    print("🐔🐔🐔 You chickened out, Coward! 🐔🐔🐔")


