"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This module provides helper functions to calculate preparation,
baking, and total elapsed time for lasagna.
"""

# Constants
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes).
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time in minutes.

    :param number_of_layers: int - number of lasagna layers.
    :return: int - total preparation time (in minutes).
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed cooking time.

    :param number_of_layers: int - number of lasagna layers.
    :param elapsed_bake_time: int - time already spent baking.
    :return: int - total elapsed time (in minutes).
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
