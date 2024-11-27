from random import choice, randint
from datetime import datetime
import data.assistance
import data.identification
from util.util import generate_n_digits

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
    first_surname = choice(data.identification.surnames)
    second_surname = choice(data.identification.surnames)
    return name, first_surname, second_surname

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
    current_date = datetime.now()
    start_year = current_date.year - 100
    year = randint(start_year, current_date.year)
    month = randint(1, 12)
    
    if month == 2:  # February
        day = randint(1, 29) if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else randint(1, 28)
    elif month in {4, 6, 9, 11}:  # Months with 30 days
        day = randint(1, 30)
    else:  # Months with 31 days
        day = randint(1, 31)

    birthdate = datetime(year, month, day)

    if birthdate > current_date:
        birthdate = current_date

    return birthdate.strftime("%d/%m/%Y")

def generate_medical_registration_number():
    '''
    Generates a random medical registration number
    '''
    return f'NC {generate_n_digits(9)}'

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
    - Name, first_surname and second_surname
    - DNI
    - Birthdate
    - Gender
    '''
    gender, gender_mention = generate_gender()
    name, first_surname, second_surname = generate_name(gender)
    dni = generate_dni()
    birthdate = generate_birthdate()

    return name, first_surname, second_surname, dni, birthdate, gender, gender_mention

def generate_identification_doctor():
    '''
    Return the gender and a string with the following fields:
    - Name, first_surname and second_surname
    - Gender
    - Medical registration number
    - Healthcare role
    - Institution
    '''
    gender, _ = generate_gender()
    name, first_surname, second_surname = generate_name(gender)
    medical_registration_number = generate_medical_registration_number()
    healthcare_role, institution = generate_institution(gender)

    return name, first_surname, second_surname, gender, medical_registration_number, healthcare_role, institution