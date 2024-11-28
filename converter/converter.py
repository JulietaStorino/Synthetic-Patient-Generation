import re
from constant.label import *
from constant.tag import *
import converter.xml_notation as xml
import converter.brat_notation as brat

# Define the labels patterns
label_patterns = [
    (NOMBRE_SUJETO_ASISTENCIA, r"Nombre: ([^\n]+)"),
    (ID_SUJETO_ASISTENCIA, r"DNI: ([^\n]+)"),
    (FECHAS, r"Fecha de nacimiento: ([^\n]+)"),
    (SEXO_SUJETO_ASISTENCIA, r"Género: ([^\n]+)"),
    (CALLE, r"Domicilio: ([^\n]+)"),
    (TERRITORIO, r"Ciudad: ([^\n]+)"),
    (TERRITORIO, r"Código postal: ([^\n]+)"),
    (CORREO_ELECTRONICO, r"Email: ([^\n]+)"),
    (NUMERO_TELEFONO, r"Teléfono fijo: ([^\n]+)"),
    (NUMERO_TELEFONO, r"Teléfono móvil: ([^\n]+)"),
    (NUMERO_FAX, r"FAX: ([^\n]+)"),
    (ID_SUJETO_ASISTENCIA, r"NHC: ([^\n]+)"),
    (ID_ASEGURAMIENTO, r"NASS: ([^\n]+)"),
    (PROFESION, r"Condición de riesgo: ([^\n]+)"),
    (NOMBRE_PERSONAL_SANITARIO, r"Médico: Dr\.a? ([^\.]+)\. NC (\d+)\. ([^\.]+)\. ([^\.]+)\. ([^\.]+)\. ([^\.]+)\. ([^\.]+)\. ([^\.]+)\."),
    (FECHAS, r"Fecha de ingreso: ([^\n]+)"),
    (ID_CONTACTO_ASISTENCIAL, r"Episodio: ([^\n]+)"),
    (CENTRO_DE_SALUD, r"Centro de salud: ([^\n]+)"),
    (HOSPITAL, r"Hospital: ([^\n]+)"),
    (IDENTIF_VEHICULOS_NRSERIE_PLACAS, r"Matrícula del coche: ([^\n]+)"),
    (IDENTIF_VEHICULOS_NRSERIE_PLACAS, r"VIN: ([^\n]+)"),
    (OTROS_SUJETO_ASISTENCIA, r"Paciente\s*(?:de\s*)?(.*?)\s*de\s*(\d+ años|\d+ meses|un año|un mes)?\s*de edad\s*(, acompañado de su\s*([^,]+),?)?\s*se presenta a la consulta con los siguientes síntomas\.\.\.")
]

def process_xml_match(label_type, match, tags, label_id, pattern):
    start, end = match.span(1)
    value = match.group(1).strip()
    id = label_id

    if label_type == NOMBRE_SUJETO_ASISTENCIA:
        id = xml.process_name_subject_assistance(label_type, match.group(1).strip(), start, tags, label_id)
    elif label_type == NOMBRE_PERSONAL_SANITARIO:
        id = xml.process_name_healthcare_personnel(match, tags, label_id)
    elif label_type == TERRITORIO and "Ciudad" in pattern:
        xml.process_city(value, start, tags, label_id)
    elif label_type == OTROS_SUJETO_ASISTENCIA:
        id = xml.process_patient_report(match, tags, label_id)
    else:
        id = xml.create_tag(label_type, value, start, end, tags, label_id)

    return id

def process_brat_match(label_type, match, label_id, pattern):
    start, end = match.span(1)
    value = match.group(1).strip()

    text = ""
    id = label_id

    if label_type == NOMBRE_SUJETO_ASISTENCIA:
        id, text = brat.process_name_subject_assistance(label_type, match.group(1).strip(), start, label_id)
    elif label_type == NOMBRE_PERSONAL_SANITARIO:
        id, text = brat.process_name_healthcare_personnel(match, label_id)
    elif label_type == TERRITORIO and "Ciudad" in pattern:
        brat.process_city(value, start, label_id)
    elif label_type == OTROS_SUJETO_ASISTENCIA:
        id, text = brat.process_patient_report(match, label_id)
    else:
        id, text = brat.proccess_label(label_type, value, start, end, label_id)

    return id, text

def process_xml_labels(text, tags):
    """
    Process the text with the tag patterns and create the corresponding tags.
    """
    label_id = 1
    for label_type, pattern in label_patterns:
        matches = re.finditer(pattern, text)

        for match in matches:
            label_id = process_xml_match(label_type, match, tags, label_id, pattern)

def process_brat_labels(text):

    label_id = 1
    processed_text = ""

    for label_type, pattern in label_patterns:
        matches = re.finditer(pattern, text)

        for match in matches:
            label_id, processed_match = process_brat_match(label_type, match, label_id, pattern)
            processed_text += processed_match
            

    return processed_text
