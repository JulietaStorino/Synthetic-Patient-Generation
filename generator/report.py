from random import choice
from data.report import MESH_population_groups
from utils.utils import boolean_with_probability

def generate_MESH_population_group():
    '''
    Generates a random MESH population group from a list of common characteristics and if the person has it
    '''
    have_mesh_population_group = boolean_with_probability(.6)
    if have_mesh_population_group:
        return choice(MESH_population_groups)
    return None

def generate_report():
    """
    Generates a report that includes a MESH population group (if any)
    """
    report = 'Paciente '

    mesh_group = generate_MESH_population_group()

    if mesh_group:
        report += f"{mesh_group}."
    else:
        report += "sin grupo poblacional MESH."

    return report