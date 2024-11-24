from random import choice
from data.health_record import risk_diseases, high_risk_professions
from utils.utils import boolean_with_probability, generate_n_digits
def generate_risk_condition():
    """
    Generates risk conditions randomly from a list of common diseases and health conditions.
    """
    risk_conditions_list = []
    high_risk_profession = None
    have_risk_profession = False

    if boolean_with_probability(.5):
        number_conditions = choice([1, 1, 2, 2, 3])

        have_risk_profession = boolean_with_probability(.5)

        if have_risk_profession:
            high_risk_profession = choice(high_risk_professions)
            number_conditions -= 1

        while number_conditions > 0:
            risk_disease = choice(risk_diseases)
            if risk_disease not in risk_conditions_list:
                risk_conditions_list.append(risk_disease)
            number_conditions -= 1
    
    return high_risk_profession, risk_conditions_list

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
    high_risk_profession, risk_conditions_list = generate_risk_condition()

    return nhc, high_risk_profession, risk_conditions_list, nass