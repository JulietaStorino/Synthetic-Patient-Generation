import random

def generate_n_digits(n):
    """
    Return a string with n random digits
    """
    n_times_nine = int("9" * n)
    return f"{random.randint(0, n_times_nine):0{n}d}"

def boolean_with_probability(probability):
    '''
    Returns True or False with a given probability
    '''
    return random.random() < probability