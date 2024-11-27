from random import choice, choices
from data.report import MESH_population_groups, MESH_population_weights, companions_0_to_15, companions_16_to_59, companions_60_to_100
from util.util import boolean_with_probability

def generate_MESH_population_group():
    '''
    Generates a random MESH population group from a list of common characteristics.
    '''
    return choices(MESH_population_groups, weights=MESH_population_weights, k=1)[0]

def generate_patient_companion(years_old):
    '''
    Generates a random relative of a patient from a list of common relatives. It may return None with a 40% probability
    '''
    if years_old <= 15:
        return choice(companions_0_to_15)
    elif years_old <= 59:
        return choice(companions_16_to_59) if boolean_with_probability(.6) else None
    return choice(companions_60_to_100) if boolean_with_probability(.6) else None

def generate_report(years_old):
    """
    Generates a report that may include a MESH population group and a relative of a patient
    """
    mesh_group = generate_MESH_population_group()
    companion = generate_patient_companion(years_old)
    return mesh_group, companion