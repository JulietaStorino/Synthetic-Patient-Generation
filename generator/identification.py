from random import choice, randint
import data.assistance
import data.identification
from utils.utils import generate_n_digits

def generate_gender():
    '''
    Generates a random gender
    '''
    gender = choice(["M", "F"]) # M: Male, F: Female

    if gender == "M":
        return gender, choice(data.identification.male_gender)
    return gender, choice(data.identification.female_gender)

def generate_name(gender):
    '''
    Generates a random name based on the gender
    '''
    name = choice(data.identification.female_names) if (gender == "F") else choice(data.identification.male_names)
    surname1 = choice(data.identification.surnames)
    surname2 = choice(data.identification.surnames)
    return name, surname1, surname2

def generate_dni():
    '''
    Generates a random DNI where the number is random and the letter is calculated
    '''
    number_dni = randint(10000000, 99999999)
    letter_dni = data.identification.dni_letters[number_dni % 23]
    return f"{number_dni}{letter_dni}"

def generate_birthdate():
    '''
    Generates a random birthdate
    '''
    return f"{randint(1, 31):02}/{randint(1, 12):02}/{randint(1950, 2000)}"

def generate_medical_registration_number():
    '''
    Generates a random medical registration number
    '''
    return f'{choice(data.identification.medical_signs)} {generate_n_digits(9)}'

def generate_institution(gender):
    '''
    Generates a random institution from the list of institutions and returns it with its id
    '''
    id = randint(0, len(data.assistance.medical_institutions) - 1)
    institution = data.assistance.medical_institutions[id]
    healthcare_role_id = id * 3 + randint(0, 2)
    healthcare_role = data.assistance.healthcare_roles[healthcare_role_id]
    if gender == "F":
        healthcare_role = healthcare_role.replace("logo", "loga")
        healthcare_role = healthcare_role.replace("Investigador", "Investigadora")
        healthcare_role = healthcare_role.replace("Clínico", "Clínica")
    return healthcare_role, institution

def generate_identification_person():
    '''
    Return the gender and a string with the following fields:
    - Name, surname1 and surname2
    - DNI
    - Birthdate
    - Gender
    '''
    gender, gender_mention = generate_gender()
    name, surname1, surname2 = generate_name(gender)
    dni = generate_dni()
    birthdate = generate_birthdate()

    return name, surname1, surname2, dni, birthdate, gender, gender_mention

def generate_identification_doctor():
    '''
    Return the gender and a string with the following fields:
    - Name, surname1 and surname2
    - Gender
    - Medical registration number
    - Healthcare role
    - Institution
    '''

    gender, _ = generate_gender()
    name, surname1, surname2 = generate_name(gender)
    medical_registration_number = generate_medical_registration_number()
    healthcare_role, institution = generate_institution(gender)

    return name, surname1, surname2, gender, medical_registration_number, healthcare_role, institution