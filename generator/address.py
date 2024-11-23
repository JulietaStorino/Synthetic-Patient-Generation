from random import randint, choice
from data.address import streets, municipalities, postal_code_prefixes, provinces, communities
from utils.utils import generate_n_digits, boolean_with_probability

def generate_province_number():
    """
    Generates a random province number
    """
    return randint(0, len(provinces) - 1)

def generate_city(province_number):
    """
    Generates a random city, province and community
    """
    province = provinces[province_number]
    
    if province == "Ceuta" or province == "Melilla":
        city = f"Ciudad autónoma de {province}"
    else:
        city = choice(municipalities)
        
    community = communities[province_number]

    return city, province, community

def generate_street():
    """
    Generates a random street and number from the list of streets in Spain
    """
    street = choice(streets)
    number = randint(1, 100)

    return street, number

def generate_apt():
    """
    Generates a random apartment floor (number) and door (letter)
    """
    is_apt = boolean_with_probability(.4)
    apt_floor = randint(1, 10)
    apt_door = choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'])

    return is_apt, apt_floor, apt_door

def generate_postal_code(index):
    """
    Generates a random postal code based on the province index
    """
    return f"{postal_code_prefixes[index]}{generate_n_digits(3)}"

def generate_address():
    """
    Generates a random address contemplating the following fields:
    - Street and number
    - Apartment floor and door (optional)
    - City, province and community
    - Postal code
    """

    province_number = generate_province_number()
    city, province, community = generate_city(province_number)
    street, number = generate_street()
    is_apt, apt_floor, apt_door = generate_apt()
    postal_code = generate_postal_code(province_number)
        
    return province_number, city, province, community, street, number, is_apt, apt_floor, apt_door, postal_code
