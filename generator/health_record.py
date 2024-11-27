from random import choice
from data.health_record import high_risk_professions
from util.util import boolean_with_probability, generate_n_digits
def generate_risk_condition():
    """
    Generates a risk condition randomly from a list of common professions.
    """
    return choice(high_risk_professions) if boolean_with_probability(.7) else None

def generate_nhc():
    '''
    Generates a random NHC (Número de Historia Clínica - Health Record Number)
    '''
    return generate_n_digits(7)

def generate_nass():
   '''
   Generates a random NASS (Número de Afiliación a la Seguridad Social - Social Security Affiliation Number) and if the person has it
   '''
   return generate_n_digits(12) if boolean_with_probability(.7) else None

def generate_health_record():
    """
    Generates a health record with the following fields:
    - NHC number
    - High risk profession (if any)
    - Risk conditions (if any)
    - NASS number (if any)
    """
    nhc = generate_nhc()
    nass = generate_nass()
    high_risk_profession = generate_risk_condition()

    return nhc, high_risk_profession, nass