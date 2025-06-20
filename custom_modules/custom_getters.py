def get_int(prompt="Input: ", min_value=-999999999, max_value=999999999) -> int:
    """
    Returns an integer input by the user.

    Also provides error checking, prompting the user with the same prompt, as specified in the 'prompt' argument, until the user enters a valid integer. The prompt with which to ask user can be specified using the prompt parameter. The user input must be between integers passed in min_value and max_value arguments. If not specified, valies from -1 billion to +1 billion are allowed.

    :param prompt: The prompt using which the user is asked for an input.
    :param min_value: Minimum possible value the user can enter
    :param max_value: Maximum possible value the user can enter
    """
    while True:
        try:
            ip = input(prompt)
            num = int(ip)
            if num < min_value:
                print(f"Input should be greater than {min_value}.")
                continue
            if num > max_value:
                print(f"The number should be lesser than {max_value}.")
                continue
            return num
        
        except ValueError:
            print("Kindly enter an integer")
        except:
            print("Invalid input, cause not known..")



def get_positive_int(prompt="Input: ", max_value=999999999):
    """
    Returns a positive integer as inputted by the user.

    Also provides error checking, prompting the user with the same prompt, as specified in the 'prompt' argument, until the user enters a valid positive integer. The prompt with which to ask user can be specified using the prompt parameter. User can also specify a maximum value, which will is to be allowed to enter. By default, the maximum value is set to 1 Billion.

    :param prompt: The prompt using which the user is asked for an input.
    :param max_value: The maximum possible value the user can enter
    """
    while True:
        try:
            ip = input(prompt)
            num = int(ip)
            if num <= 0:
                print(f"The integer must be positive.")
                continue
            if num > max_value:
                print(f"The number should be lesser than {max_value}.")
                continue
            return num

        except ValueError:
            print("Kindly enter an integer")
        except:
            print("Invalid input, cause not knowm..")



def get_float(prompt="Input: ", min_value=-999999, max_value=-999999):
    """
    Returns a float (decimal number) input by the user.

    Also provides error checking, prompting the user with the same prompt, as specified in the 'prompt' argument, until the user enters a valid float. The prompt with which to ask user can be specified using the prompt parameter. The user input must be between floats passed in min_value and max_value arguments. If not specified, valies from -1 million to +1 million are allowed.

    :param prompt: The prompt using which the user is asked for an input.
    :param min_value: Minimum possible value the user can enter
    :param max_value: Maximum possible value the user can enter
    """
    while True:
        try:
            ip = input(prompt)
            num = float(ip)
            if num < min_value:
                print(f"Input should be greater than {min_value}.")
                continue
            if num > max_value:
                print(f"The number should be lesser than {max_value}.")
                continue
            return num
        
        except ValueError:
            print("Kindly enter an float")
        except:
            print("Invalid input, cause not known..")



def get_positive_float(prompt="Input: ", max_value=999999999):
    """
    Returns a positive float as inputted by the user.

    Also provides error checking, prompting the user with the same prompt, as specified in the 'prompt' argument, until the user enters a valid positive float. The prompt with which to ask user can be specified using the prompt parameter. User can also specify a maximum value, which will is to be allowed to enter. By default, the maximum value is set to 1 billion.

    :param prompt: The prompt using which the user is asked for an input.
    :param max_value: The maximum possible value the user can enter
    """
    while True:
        try:
            ip = input(prompt)
            num = float(ip)
            if num <= 0:
                print(f"The float must be positive.")
                continue
            if num > max_value:
                print(f"The number should be lesser than {max_value}.")
                continue
            return num

        except ValueError:
            print("Kindly enter a float")



def get_choice(*choices, prompt="Input: ", exact_match=False):
    """
    ...
    """
    
    while True:
        if exact_match:
            choice = input(prompt)
        elif not exact_match:
            choice = input(prompt).strip().casefold()
            choices = map(str.casefold, choices)
        
        if choice in choices:
            return choice
        else:
            print(f"Kindly input one of the these: {choices}")