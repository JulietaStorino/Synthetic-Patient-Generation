import random
import string
from data.contacts import mail_domains, conectors, phone_prefixes
from utils.contacts import remove_special_characters

def generate_email(name, surname1, surname2):
    '''
    Generates a random email based on the name and surnames of a person
    '''
    use_name = random.choice([True, True, False])
    use_surname1 = random.choice([True, True, False])
    use_surname2 = random.choice([True, True, False])

    email_parts = []

    # Case of random email
    if not use_name and not use_surname1 and not use_surname2:
        email_parts.append(''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(5, 15))))
    
    # Case of using name, surname1 or/and surname2
    else:
        if use_name:
            email_parts.append(name.lower())
        if use_surname1:
            if use_name:
                email_parts.append(random.choice(conectors))
            email_parts.append(surname1.lower())
        if use_surname2:
            if use_name or use_surname1:
                email_parts.append(random.choice(conectors))
            email_parts.append(surname2.lower())

    # Case of adding a random number (33% of probability)
    if random.choice([True, False, False]):
        email_parts.append(str(random.randint(0, 2025)))

    email = ''.join(email_parts) + f"@{random.choice(mail_domains)}"
    email = remove_special_characters(email)
    
    return email

def generate_phone_number(province_number):
    '''
    Generates a random phone number based on the province number
    '''
    prefix = phone_prefixes[province_number]

    if len(prefix) == 1:
        return f"{prefix}{random.randint(0, 9):01} {random.randint(00, 99):02} {random.randint(00, 99):02} {random.randint(00, 99):02}"

    return f"{prefix} {random.randint(00, 99):02} {random.randint(00, 99):02} {random.randint(00, 99):02}"


def generate_phone_numbers(province_number):
    '''
    Generates a random landline and mobile phone number based on the province number
    '''
    mobile_phone = f"+34 6{generate_phone_number(province_number)}"
    landline_phone = f"+34 9{generate_phone_number(province_number)}"

    return landline_phone, mobile_phone

def generate_contacts(name, surname1, surname2, province_number):
    '''
    Returns a string with the email, landline and mobile phone of a person
    '''
    email = generate_email(name, surname1, surname2)
    landline_phone, mobile_phone = generate_phone_numbers(province_number)

    return f"Email: {email}\nTeléfono fijo: {landline_phone}\nTeléfono móvil: {mobile_phone}\n"
