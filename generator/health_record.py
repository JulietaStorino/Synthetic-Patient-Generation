import random
from data.health_record import risk_diseases, high_risk_professions

def generate_risk_condition():
    """
    Generates risk conditions randomly from a list of common diseases and health conditions.
    """
    risk_conditions_list = []

    if random.choice([True, False]):
        number_conditions = random.choice([1, 1, 2, 2, 3])

        if random.choice([True, False]):
            risk_conditions_list.append(random.choice(high_risk_professions))
            number_conditions -= 1

        while number_conditions > 0:
            risk_conditions_list.append(random.choice(risk_diseases))
            number_conditions -= 1
    
    return risk_conditions_list

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
    risk_conditions = generate_risk_condition()

    if not risk_conditions:
        return f"NHS: {nhc}\n"
    
    return f"NHS: {nhc}\nRisk conditions: {', '.join(risk_conditions)}\n"