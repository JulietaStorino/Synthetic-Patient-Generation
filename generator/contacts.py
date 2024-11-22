from random import randint, choice, choices
import string
from data.contacts import mail_domains, conectors, phone_prefixes
from utils.utils import remove_special_characters, generate_n_digits, boolean_with_probability

def generate_email(name, surname1, surname2):
    '''
    Generates a random email based on the name and surnames of a person
    '''
    use_name = boolean_with_probability(.6)
    use_surname1 = boolean_with_probability(.6)
    use_surname2 = boolean_with_probability(.6)

    email_parts = []

    # Case of random email
    if not use_name and not use_surname1 and not use_surname2:
        email_parts.append(''.join(choices(string.ascii_letters + string.digits, k=randint(5, 15))))
    
    # Case of using name, surname1 or/and surname2
    else:
        if use_name:
            email_parts.append(name.lower())
        if use_surname1:
            if use_name:
                email_parts.append(choice(conectors))
            email_parts.append(surname1.lower())
        if use_surname2:
            if use_name or use_surname1:
                email_parts.append(choice(conectors))
            email_parts.append(surname2.lower())

    # Case of adding a random number (33% of probability)
    if boolean_with_probability(.3):
        email_parts.append(str(randint(0, 2025)))

    email = ''.join(email_parts) + f"@{choice(mail_domains)}"
    email = remove_special_characters(email)
    
    return email

def generate_phone_number(province_number):
    '''
    Generates a random phone number based on the province number
    '''
    prefix = phone_prefixes[province_number]

    if len(prefix) == 1:
        return f"{prefix}{generate_n_digits(1)} {generate_n_digits(2)} {generate_n_digits(2)} {generate_n_digits(2)}"

    return f"{prefix} {generate_n_digits(2)} {generate_n_digits(2)} {generate_n_digits(2)}"


def generate_phone_numbers(province_number):
    '''
    Generates a random landline and mobile phone number based on the province number
    '''
    mobile_phone = f"+34 {choice([6,7])}{generate_phone_number(province_number)}"
    landline_phone = f"+34 9{generate_phone_number(province_number)}"
    fax = f"+34 9{generate_phone_number(province_number)}"
    return landline_phone, mobile_phone, fax

def generate_contacts(name, surname1, surname2, province_number):
    '''
    Returns a string with the email, landline and mobile phone or fax of a person
    '''
    email = generate_email(name, surname1, surname2)
    landline_phone, mobile_phone, fax = generate_phone_numbers(province_number)
    
    use_fax = boolean_with_probability(.2)

    return email, landline_phone, mobile_phone, fax, use_fax