import random
import data.assistance
import data.identification

def generate_gender():
    '''
    Generates a random gender
    '''
    gender = random.choice(["M", "F"]) # M: Male, F: Female

    if (gender == "M"):
        return gender, random.choice(data.identification.male_gender)
    return gender, random.choice(data.identification.female_gender)

def generate_name(gender):
    '''
    Generates a random name based on the gender
    '''
    name = random.choice(data.identification.female_names) if (gender == "F") else random.choice(data.identification.male_names)
    surname1 = random.choice(data.identification.surnames)
    surname2 = random.choice(data.identification.surnames)
    return name, surname1, surname2

def generate_dni():
    '''
    Generates a random DNI where the number is random and the letter is calculated
    '''
    number_dni = random.randint(10000000, 99999999)
    letter_dni = data.identification.dni_letters[number_dni % 23]
    return f"{number_dni}{letter_dni}"

def generate_birthdate():
    '''
    Generates a random birthdate
    '''
    return f"{random.randint(1, 31):02}/{random.randint(1, 12):02}/{random.randint(1950, 2000)}"

def generate_medical_registration_number():
    '''
    Generates a random medical registration number
    '''
    return f'{random.choice(data.identification.medical_signs)} {random.randint(100000000, 999999999):09}'

def generate_institution():
    '''
    Generates a random institution from the list of institutions
    '''
    return random.choice(data.assistance.medical_institutions)

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
    '''

    gender = generate_gender()
    name, surname1, surname2 = generate_name(gender)
    medical_registration_number = generate_medical_registration_number()
    institution = generate_institution()

    return name, surname1, surname2, gender, medical_registration_number, institution