from random import randint, choice
from data.assistance import hospitals

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

def generate_assistance():
    '''
    Generates a random assistance with the following fields:
    - Assistance date
    - Hospital
    '''
    assistance_date = generate_assistance_date()
    hospital = generate_assistance_hospital()

    return assistance_date, hospital