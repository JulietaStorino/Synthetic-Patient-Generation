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

def introduce_typo(text):
    """
    Introduce a typographical error in the given text.
    A typo can be an omission, substitution, duplication, or transposition of a character.
    """
    if not text:
        return text

    typo_type = random.choice(["omission", "substitution", "duplication", "transposition"])
    idx = random.randint(0, len(text) - 1)

    if typo_type == "omission": # Omit a character
        return text[:idx] + text[idx + 1:]

    elif typo_type == "substitution": # Replace a character with a random one
        random_char = random.choice("abcdefghijklmnñopqrstuvwxyz")
        return text[:idx] + random_char + text[idx + 1:]

    elif typo_type == "duplication": # Duplicate a character
        return text[:idx] + text[idx] + text[idx] + text[idx + 1:]

    elif typo_type == "transposition" and len(text) > 1: # Swap two consecutive characters
        if idx == len(text) - 1:
            idx -= 1
        return text[:idx] + text[idx + 1] + text[idx] + text[idx + 2:]

def dirty_names(name, first_surname, second_surname):
    """
    Generate typographical errors in the name and surnames. Each name and surname has a 33% chance of having a typo.
    """
    name_with_typo, first_surname_with_typo, second_surname_with_typo = name, first_surname, second_surname

    if boolean_with_probability(0.33):
        name_with_typo = introduce_typo(name)

    if boolean_with_probability(0.33):
        first_surname_with_typo = introduce_typo(first_surname)
    
    if boolean_with_probability(0.33):
        second_surname_with_typo = introduce_typo(second_surname)
    
    return name_with_typo, first_surname_with_typo, second_surname_with_typo
