import random
from util import boolean_with_probability
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
