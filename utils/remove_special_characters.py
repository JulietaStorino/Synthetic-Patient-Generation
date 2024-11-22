import unicodedata

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