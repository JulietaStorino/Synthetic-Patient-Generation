import xml.etree.ElementTree as ET
from constant.label import *
from constant.tag import *
from converter.util import *

id_tag = [ID_SUJETO_ASISTENCIA, ID_TITULACION_PERSONAL_SANITARIO, ID_ASEGURAMIENTO, ID_CONTACTO_ASISTENCIAL, IDENTIF_VEHICULOS_NRSERIE_PLACAS, ID_EMPLEO_PERSONAL_SANITARIO]
name_tag = [NOMBRE_SUJETO_ASISTENCIA, NOMBRE_PERSONAL_SANITARIO]
location_tag = [CALLE, TERRITORIO, PAIS, INSTITUCION, HOSPITAL, CENTRO_DE_SALUD]
contact_tag = [CORREO_ELECTRONICO, NUMERO_TELEFONO, NUMERO_FAX]
other_tag = [SEXO_SUJETO_ASISTENCIA, FAMILIARES_SUJETO_ASISTENCIA, OTROS_SUJETO_ASISTENCIA]
age_tag = [EDAD_SUJETO_ASISTENCIA]
date_tag = [FECHAS]
profession_tag = [PROFESION]

def create_tag(label_type, value, start, end, tags, label_id):
    """
    Create a tag element with the corresponding attributes.
    """
    tag = match_tag(label_type, tags)
    tag.set("id", f"T{label_id}")
    tag.set("start", str(start))
    tag.set("end", str(end))
    tag.set("text", value)
    tag.set("TYPE", label_type)
    tag.set("comment", "")
    return label_id + 1

def match_tag(label_type, tags):
    """
    Returns the correct tag element based on the label type.
    """
    if label_type in name_tag:
        return ET.SubElement(tags, NAME)
    elif label_type in id_tag:
        return ET.SubElement(tags, ID)
    elif label_type in location_tag:
        return ET.SubElement(tags, LOCATION)
    elif label_type in date_tag:
        return ET.SubElement(tags, DATE)
    elif label_type in other_tag:
        return ET.SubElement(tags, OTHER)
    elif label_type in age_tag:
        return ET.SubElement(tags, AGE)
    elif label_type in contact_tag:
        return ET.SubElement(tags, CONTACT)
    elif label_type in profession_tag:
        return ET.SubElement(tags, PROFESSION)
    
    return ET.SubElement(tags, TAG)

def process_name_subject_assistance(label_type, full_name, start_pos, tags, label_id):
    """
    Split the full name into name and surnames, and create the corresponding tags.
    """
    name, surnames = split_full_name(full_name)
    first_start, first_end, last_start, last_end = calculate_positions(name, surnames, start_pos)

    label_id = create_tag(label_type, name, first_start, first_end, tags, label_id)
    label_id = create_tag(label_type, surnames, last_start, last_end, tags, label_id)

    return label_id

def process_name_healthcare_personnel(match, tags, label_id):
    """
    Create the tags for the healthcare roles.
    """
    label_id = create_tag(NOMBRE_PERSONAL_SANITARIO, match.group(1).strip(), match.start(1), match.end(1), tags, label_id)
    label_id = create_tag(ID_TITULACION_PERSONAL_SANITARIO, match.group(2).strip(), match.start(2), match.end(2), tags, label_id)
    label_id = create_tag(ID_EMPLEO_PERSONAL_SANITARIO, match.group(3).strip(), match.start(3), match.end(3), tags, label_id)
    label_id = create_tag(INSTITUCION, match.group(4).strip(), match.start(4), match.end(4), tags, label_id)
    label_id = create_tag(CALLE, match.group(5).strip(), match.start(5), match.end(5), tags, label_id)
    label_id = create_tag(TERRITORIO, match.group(6).strip(), match.start(6), match.end(6), tags, label_id)
    label_id = create_tag(TERRITORIO, match.group(7).strip(), match.start(7), match.end(7), tags, label_id)
    label_id = create_tag(PAIS, match.group(8).strip(), match.start(8), match.end(8), tags, label_id)

    return label_id

def process_city_label(full_localitation, start_pos, tags, label_id):
    """
    Split the full localitation into parts and create the corresponding tags.
    """
    parts = full_localitation.split(", ")
    current_start = start_pos

    for part in parts:
        current_end = current_start + len(part)
        label_id = create_tag(TERRITORIO, part, current_start, current_end, tags, label_id)
        current_start = current_end + 2

def process_patient_report(match, tags, label_id):
    """
    Split the patient report into parts and create the corresponding tags.
    """
    id_sujeto_asistencia = match.group(1).strip() if match.group(1) else ""
    edad_sujeto_asistencia = match.group(2).strip() if match.group(2) else ""
    familiares_sujeto_asistencia = match.group(4).strip() if match.group(4) else ""

    if id_sujeto_asistencia:
        label_id = create_tag(OTROS_SUJETO_ASISTENCIA, id_sujeto_asistencia, match.start(1), match.end(1), tags, label_id)
    if edad_sujeto_asistencia:
        label_id = create_tag(EDAD_SUJETO_ASISTENCIA, edad_sujeto_asistencia, match.start(2), match.end(2), tags, label_id)
    if familiares_sujeto_asistencia:
        label_id = create_tag(FAMILIARES_SUJETO_ASISTENCIA, familiares_sujeto_asistencia, match.start(4), match.end(4), tags, label_id)

    return label_id

