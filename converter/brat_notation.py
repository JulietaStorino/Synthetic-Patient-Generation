from constant.label import *
from converter.util import *

def proccess_label(label_type, value, start, end, label_id):
    """
    Create a text line with the corresponding label attributes.
    """
    text = ''

    if label_id < 10:
        text += f"T{label_id}\t"
    else:
        text += f"T{label_id} "

    text += f"{label_type} {start} {end}\t{value}\n"

    return label_id + 1, text

def process_name_subject_assistance(label_type, full_name, start_pos, label_id):
    """
    Split the full name into name and surnames and create the corresponding label lines.
    """
    name, surnames = split_full_name(full_name)
    first_start, first_end, last_start, last_end = calculate_positions(name, surnames, start_pos)

    id, text = proccess_label(label_type, name, first_start, first_end, label_id)
    id, proccessed_text = proccess_label(label_type, surnames, last_start, last_end, id)
    text += proccessed_text

    return id, text

def process_name_healthcare_personnel(match, label_id):
    """
    Create the label lines for the healthcare roles.
    """

    text = ''
    id = label_id
    labels = [
        (NOMBRE_PERSONAL_SANITARIO, 1),
        (ID_TITULACION_PERSONAL_SANITARIO, 2),
        (ID_EMPLEO_PERSONAL_SANITARIO, 3),
        (INSTITUCION, 4),
        (CALLE, 5),
        (TERRITORIO, 6),
        (TERRITORIO, 7),
        (PAIS, 8)
    ]

    for label, group in labels:
        id, processed_text = proccess_label(label, match.group(group).strip(), match.start(group), match.end(group), id)
        text += processed_text

    return id, text

def process_city(full_localitation, start_pos, label_id):
    """
    Split the full localitation into parts and create the corresponding proccessed text.
    """
    parts = full_localitation.split(", ")
    current_start = start_pos
    text = ''
    id = label_id

    for part in parts:
        current_end = current_start + len(part)
        id, proccessed_text = proccess_label(TERRITORIO, part, current_start, current_end, id)
        text += proccessed_text
        current_start = current_end + 2

    return id, text

def process_patient_report(match, label_id):
    """
    Split the patient report into parts and create the corresponding proccessed text.
    """
    id_sujeto_asistencia = match.group(1).strip() if match.group(1) else ""
    edad_sujeto_asistencia = match.group(2).strip() if match.group(2) else ""
    familiares_sujeto_asistencia = match.group(4).strip() if match.group(4) else ""

    text = ''
    id = label_id
    labels = [
        (OTROS_SUJETO_ASISTENCIA, id_sujeto_asistencia, 1),
        (EDAD_SUJETO_ASISTENCIA, edad_sujeto_asistencia, 2),
        (FAMILIARES_SUJETO_ASISTENCIA, familiares_sujeto_asistencia, 4)
    ]

    for label, value, group in labels:
        if value:
            id, processed_text = proccess_label(label, value, match.start(group), match.end(group), id)
            text += processed_text

    return id, text

