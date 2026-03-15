def int_check(question):
    """Checks users enetr on integer more than / equal to 13"""

    while True:
        error = "Please enter an integer that is 1 or more."

        response = input(question)

        # check for infinite mode
        if response == "":
            return "infinite"

        try:
            response =int(response)

            #check that the number is more than / equal to 13
            if response < 1:
                print(error)

            else:
                return response

        except ValueError:
            print(error)


# Automated testing is below in the form (test_case, expected_value)
while True:
    num_rounds = int_check("How many rounds? ")
    print(f"you chose {num_rounds}")