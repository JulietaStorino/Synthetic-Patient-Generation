def split_full_name(full_name):
    """
    Split the full name into name and surnames.
    """
    parts = full_name.split()
    if len(parts) == 4:
        name = " ".join(parts[:2])
        surnames = " ".join(parts[2:])
    else:
        name = parts[0]
        surnames = " ".join(parts[1:])
    return name, surnames

def calculate_positions(name, surnames, start_pos):
    """
    Calculate the positions for the name and surnames.
    """
    first_start = start_pos
    first_end = first_start + len(name)
    last_start = first_end + 1 
    last_end = last_start + len(surnames)
    return first_start, first_end, last_start, last_end