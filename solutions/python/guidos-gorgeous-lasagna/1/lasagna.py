"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""



EXPECTED_BAKE_TIME = 40

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.
    
    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
    Returns:
        int: The total time needed for preparing.

    This function takes an integer representing the number of lasagna 
    layers. It calculates the total preparation minutes
    needed for cooking (preparing). """
    time = 2 * number_of_layers
    return time
    
    

def bake_time_remaining(time):
    """Calculate the remaining time.
    
    Parameters:
        elapsed_bake_time (int): Time the lasagna has been baking in the oven.
    Returns:
        int: The total time needed for preparing.

    This function takes an integer representing the elapsed time. 
    It calculates the total remaining
    minutes needed for cooking (preparing). """
    time_left = EXPECTED_BAKE_TIME - time
    return time_left

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.
    
    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): Time the lasagna has been baking in the oven.
    
    Returns:
        int: The total time elapsed (in minutes) preparing and baking.

    This function takes two integers representing the number of lasagna 
    layers and the time already spent baking the lasagna. It calculates 
    the total elapsed minutes spent cooking (preparing + baking).
    
    """
    time = (number_of_layers * 2) + elapsed_bake_time
    return time
    



