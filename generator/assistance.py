import string
from datetime import datetime, timedelta
from random import randint, choice, choices
from data.assistance import hospitals, health_centers, car_models
from util import generate_n_digits, boolean_with_probability

def generate_assistance_date(birthdate):
    '''
    Generates a random assistance date.
    '''
    start_date = datetime.strptime(birthdate, "%d/%m/%Y")
    end_date = datetime(2025, 12, 31)    

    delta_days = (end_date - start_date).days
    random_days = randint(0, delta_days)

    assistance_date = start_date + timedelta(days=random_days)

    if assistance_date > datetime.now():
        assistance_date = datetime.now()

    return assistance_date.strftime("%d/%m/%Y")

def generate_car_registration():
    '''
    Generates a random car registration
    '''
    return f"{generate_n_digits(4)}{''.join(choices(string.ascii_uppercase, k=3))}"

def generate_car_model():
    '''
    Generates a random car model
    '''
    return choice(car_models)

def generate_vin():
    '''
    Generates a random VIN
    '''
    wmi = "VS" + choice(string.ascii_uppercase)

    # Generate the VDS (Vehicle Descriptor Section) - 6 characters
    # These are random characters for vehicle information (model, type, engine, etc.)
    vds = ''.join(choices(string.ascii_uppercase + string.digits, k=6))

    # Generate the VIS (Vehicle Identifier Section) - 8 characters
    # Character 10 is the year of the model (random year code, e.g., 'K' for 2019)
    year_code = choice("ABCDEFGHJKLMNPRSTVWXY1234567890")  # Corresponding year codes
    plant_code = choice(string.ascii_uppercase)  # Random character for the plant code
    serial_number = ''.join(choices(string.digits, k=6))  # Last 6 digits for the serial number

    # Combine all parts into a complete VIN
    vin = wmi + vds + year_code + plant_code + serial_number
    
    return vin

def generate_episode():
    '''
    Generates a random episode. There is a 70% chance that the patient has an episode.
    '''
    return generate_n_digits(8) if boolean_with_probability(.7) else None

def generate_assistance(birthdate):
    '''
    Generates a random assistance with the following fields:
    - Assistance date
    - Episode
    - Hospital or health center
    - Car registration, VIN and model (if the patient has a car)
    '''

    # Generate the assistance date and episode
    assistance_date = generate_assistance_date(birthdate)
    episode = generate_episode()
    
    # Determine if the patient is going to a hospital or a health center and generate the corresponding institution
    is_hospital = boolean_with_probability(.5)
    hospital = choice(hospitals) if is_hospital else None
    health_center = choice(health_centers) if not is_hospital else None
    
    # Determine if the patient has a car and generate the car registration and VIN if so
    have_car = boolean_with_probability(.4)
    registration = generate_car_registration() if have_car else None
    vin = generate_vin() if have_car else None
    model = generate_car_model() if have_car else None

    return assistance_date, episode, hospital, health_center, registration, vin, model