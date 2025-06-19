def get_int(prompt="Input: ", min=-999999999, max=999999999) -> int:
    """
    Returns an integer input by the user.

    Also provides error checking, prompting the user with the same prompt, as specified in the 'prompt' argument, untill the user enters a valid integer. The prompt with which to ask user can be specified using the prompt parameter. The user input must be between integers passed in min and max arguments. If not specified, valies from -1 billion to +1 billion are allowed.

    :param prompt: The prompt using which the user is asked for an input.
    :param min: Minimum possible value the user can enter
    :param max: Maximum possible value the user can enter
    """
    while True:
        try:
            ip = input(prompt)
            num = int(ip)
            if num < min:
                print(f"Input should be greater than {min}.")
                continue
            if num > max:
                print(f"The number should be lesser than {max}.")
                continue
            return num
        
        except ValueError:
            print("Kindly enter an integer")
        except:
            print("Invalid input, cause not known..")



def get_positive_int(prompt="Input: ", max=999999999):
    """
    Returns a positive integer as inputted by the user.

    Also provides error checking, prompting the user with the same prompt, as specified in the 'prompt' argument, untill the user enters a valid positive integer. The prompt with which to ask user can be specified using the prompt parameter. User can also specify a maximum value, which will is to be allowed to enter. By default, the maximum value is set to 1 Billion.

    :param prompt: The prompt using which the user is asked for an input.
    :param max: The maximum possible value the user can enter
    """
    while True:
        try:
            ip = input(prompt)
            num = int(ip)
            if num <= 0:
                print(f"The integer must be positive.")
                continue
            if num > max:
                print(f"The number should be lesser than {max}.")
                continue
            return num

        except ValueError:
            print("Kindly enter an integer")
        except:
            print("Invalid input, cause not knowm..")



def get_float(prompt="Input: ", min=-999999, max=-999999):
    """
    Returns a float (decimal number) input by the user.

    Also provides error checking, prompting the user with the same prompt, as specified in the 'prompt' argument, untill the user enters a valid float. The prompt with which to ask user can be specified using the prompt parameter. The user input must be between floats passed in min and max arguments. If not specified, valies from -1 million to +1 million are allowed.

    :param prompt: The prompt using which the user is asked for an input.
    :param min: Minimum possible value the user can enter
    :param max: Maximum possible value the user can enter
    """
    while True:
        try:
            ip = input(prompt)
            num = float(ip)
            if num < min:
                print(f"Input should be greater than {min}.")
                continue
            if num > max:
                print(f"The number should be lesser than {max}.")
                continue
            return num
        
        except ValueError:
            print("Kindly enter an float")
        except:
            print("Invalid input, cause not known..")



def get_positive_float(prompt="Input: ", max=999999999):
    """
    Returns a positive float as inputted by the user.

    Also provides error checking, prompting the user with the same prompt, as specified in the 'prompt' argument, untill the user enters a valid positive float. The prompt with which to ask user can be specified using the prompt parameter. User can also specify a maximum value, which will is to be allowed to enter. By default, the maximum value is set to 1 Million.

    :param prompt: The prompt using which the user is asked for an input.
    :param max: The maximum possible value the user can enter
    """
    while True:
        try:
            ip = input(prompt)
            num = float(ip)
            if num <= 0:
                print(f"The float must be positive.")
                continue
            if num > max:
                print(f"The number should be lesser than {max}.")
                continue
            return num

        except ValueError:
            print("Kindly enter a float")
        except:
            print("Invalid input, cause not knowm..")




def get_choice(*choices, prompt="Input: ", excat_match="False"):
    """
    Watch CS50P week 9 video and then do
    ...
    """
    
    ...