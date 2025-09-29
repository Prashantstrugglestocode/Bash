"""Functions used in preparing a lasagna."""

# The expected total bake time for the lasagna in minutes.
EXPECTED_BAKE_TIME = 40

# The time in minutes to prepare a single layer.
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time in minutes.

    This function takes the actual minutes the lasagna has been in the oven as
    an argument and subtracts it from the EXPECTED_BAKE_TIME.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculate the preparation time in minutes.

    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int - total preparation time in minutes.

    This function takes the number of layers and multiplies it by the
    PREPARATION_TIME per layer.
    """
    return PREPARATION_TIME * number_of_layers


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Calculate the total elapsed time in minutes.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total elapsed time in minutes.

    This function calculates the total time spent so far by adding the
    preparation time to the time the lasagna has already been baking.
    """
    prep_time = preparation_time_in_minutes(number_of_layers)
    return prep_time + elapsed_bake_time