import random
import string
from data.address import streets, municipalities, postal_code_prefixes, provinces, communities

def generate_province_number():
    """
    Generates a random province number
    """
    return random.randint(0, len(provinces) - 1)

def generate_city(province_number):
    """
    Generates a random city, province and community
    """
    province = provinces[province_number]
    
    if province == "Ceuta" or province == "Melilla":
        city = f"Ciudad autónoma de {province}."
    else:
        city = random.choice(municipalities)
        
    community = communities[province_number]

    return city, province, community

def generate_street():
    """
    Generates a random street and number from the list of streets in Spain
    """
    street = random.choice(streets)
    number = random.randint(1, 100)

    return street, number

def generate_apt():
    """
    Generates a random apartment floor (number) and door (letter)
    """
    is_apt = random.choice([True, False, False])
    apt_floor = random.randint(1, 10)
    apt_door = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'])

    return is_apt, apt_floor, apt_door

def generate_postal_code(index):
    """
    Generates a random postal code based on the province index
    """
    return f"{postal_code_prefixes[index]}{random.randint(0, 999):03}"

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
