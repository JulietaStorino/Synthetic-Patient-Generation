from random import randint, choice
from data.assistance import hospitals
from utils.utils import generate_n_digits, boolean_with_probability

def generate_assistance_date():
    '''
    Generates a random assistance date
    '''
    return f"{randint(1, 31):02}/{randint(1, 12):02}/{randint(2015, 2025)}"

def generate_assistance_hospital():
    '''
    Generates a random hospital
    '''
    return choice(hospitals)

def generate_episode():
    '''
    Generates a random episode
    '''
    have_episode = boolean_with_probability(.7)
    episode = generate_n_digits(8)
    
    return have_episode, episode

def generate_assistance():
    '''
    Generates a random assistance with the following fields:
    - Assistance date
    - Episode
    - Hospital
    '''
    assistance_date = generate_assistance_date()
    have_episode, episode = generate_episode()
    hospital = generate_assistance_hospital()

    return assistance_date, have_episode, episode, hospital