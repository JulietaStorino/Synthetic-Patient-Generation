from random import choice
from data.report import MESH_population_groups, patient_companions
from utils.utils import boolean_with_probability

def generate_MESH_population_group():
    '''
    Generates a random MESH population group from a list of common characteristics. It may return None with a 40% probability
    '''
    return choice(MESH_population_groups) if boolean_with_probability(.6) else None

def generate_patient_companion():
    '''
    Generates a random relative of a patient from a list of common relatives. It may return None with a 40% probability
    '''
    return choice(patient_companions) if boolean_with_probability(.6) else None

def generate_report():
    """
    Generates a report that may include a MESH population group and a relative of a patient
    """
    mesh_group = generate_MESH_population_group()
    companion = generate_patient_companion()
    return mesh_group, companion