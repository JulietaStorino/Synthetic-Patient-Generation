import unicodedata
import random

def remove_special_characters(text):
    '''
    Removes the special characters from a text 
    '''
    # Normalize the text to decompose the characters
    normalized_text = unicodedata.normalize('NFD', text)
    # Remove the accents and replace 'ñ' by 'n'
    text_without_accents = ''.join(
        c if unicodedata.category(c) != 'Mn' else '' for c in normalized_text
    ).replace("ñ", "n").replace("Ñ", "N")
    
    return text_without_accents.replace(" ", "")

def generate_n_digits(n):
    """
    Return a string with n random digits
    """
    n_times_nine = int("9" * n)
    return f"{random.randint(0, n_times_nine):0{n}d}"

def boolean_with_probability(probability):
    '''
    Returns True or False with a given probability
    '''
    return random.random() < probability