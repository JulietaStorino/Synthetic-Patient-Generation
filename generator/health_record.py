import random
from data.health_record import risk_diseases, high_risk_professions

def generate_risk_condition():
    """
    Generates risk conditions randomly from a list of common diseases and health conditions.
    """
    risk_conditions_list = []
    high_risk_profession = ''
    have_risk_profession = False

    if random.choice([True, False]):
        number_conditions = random.choice([1, 1, 2, 2, 3])

        have_risk_profession = random.choice([True, False, False])

        if have_risk_profession:
            high_risk_profession = random.choice(high_risk_professions)
            number_conditions -= 1

        while number_conditions > 0:
            risk_conditions_list.append(random.choice(risk_diseases))
            number_conditions -= 1
    
    return have_risk_profession, high_risk_profession, risk_conditions_list

def generate_nhc():
    '''
    Generates a random NHC (Número de Historia Clínica - Health Record Number)
    '''
    return f"{random.randint(0, 9999999):07d}"

def generate_health_record():
    """
    Generates a health record with the following fields:
    - NHS number
    - Risk conditions (if any)
    """
    nhc = generate_nhc()
    have_risk_profession, high_risk_profession, risk_conditions_list = generate_risk_condition()

    return nhc, have_risk_profession, high_risk_profession, risk_conditions_list