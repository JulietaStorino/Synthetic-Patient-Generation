from random import randint, choice, choices
import string
from data.contact import mail_domains, conectors, phone_prefixes
from util import generate_n_digits, boolean_with_probability
from generator.util import remove_special_characters

def generate_email(name, first_surname, second_surname):
    '''
    Generates a random email based on the name and surnames of a person
    '''
    use_name = boolean_with_probability(.6)
    use_first_surname = boolean_with_probability(.6)
    use_second_surname = boolean_with_probability(.6)

    email_parts = []

    # Case of random email
    if not use_name and not use_first_surname and not use_second_surname:
        email_parts.append(''.join(choices(string.ascii_letters + string.digits, k=randint(5, 15))))
    
    # Case of using name, first_surname or/and second_surname
    else:
        if use_name:
            email_parts.append(name.lower())
        if use_first_surname:
            if use_name:
                email_parts.append(choice(conectors))
            email_parts.append(first_surname.lower())
        if use_second_surname:
            if use_name or use_first_surname:
                email_parts.append(choice(conectors))
            email_parts.append(second_surname.lower())

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
    Generates a random landline and mobile phone (or FAX) number based on the province number
    '''
    use_fax = boolean_with_probability(.2) 

    mobile_phone = f"+34 {choice([6,7])}{generate_phone_number(province_number)}" if not use_fax else None
    landline_phone = f"+34 9{generate_phone_number(province_number)}"
    fax = f"+34 9{generate_phone_number(province_number)}" if use_fax else None
    return landline_phone, mobile_phone, fax

def generate_contacts(name, first_surname, second_surname, province_number):
    '''
    Returns a string with the email, landline and mobile phone (or FAX) of a person
    '''
    email = generate_email(name, first_surname, second_surname)
    landline_phone, mobile_phone, fax = generate_phone_numbers(province_number)
    
    return email, landline_phone, mobile_phone, fax