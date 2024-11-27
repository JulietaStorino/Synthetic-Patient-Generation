import xml.etree.ElementTree as ET
from constant.label import *
from constant.tag import *

# Define the tag patterns
tag_patterns = [
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

# Define the tag elements
id_tag = [ID_SUJETO_ASISTENCIA, ID_TITULACION_PERSONAL_SANITARIO, ID_ASEGURAMIENTO, ID_CONTACTO_ASISTENCIAL, IDENTIF_VEHICULOS_NRSERIE_PLACAS, ID_EMPLEO_PERSONAL_SANITARIO]
name_tag = [NOMBRE_SUJETO_ASISTENCIA, NOMBRE_PERSONAL_SANITARIO]
location_tag = [CALLE, TERRITORIO, PAIS, INSTITUCION, HOSPITAL, CENTRO_DE_SALUD]
contact_tag = [CORREO_ELECTRONICO, NUMERO_TELEFONO, NUMERO_FAX]
other_tag = [SEXO_SUJETO_ASISTENCIA, FAMILIARES_SUJETO_ASISTENCIA, OTROS_SUJETO_ASISTENCIA]
age_tag = [EDAD_SUJETO_ASISTENCIA]
date_tag = [FECHAS]
profession_tag = [PROFESION]

def match_tag(tag_type, tags):
    """
    Returns the correct tag element based on the tag type.
    """
    if tag_type in name_tag:
        return ET.SubElement(tags, NAME)
    elif tag_type in id_tag:
        return ET.SubElement(tags, ID)
    elif tag_type in location_tag:
        return ET.SubElement(tags, LOCATION)
    elif tag_type in date_tag:
        return ET.SubElement(tags, DATE)
    elif tag_type in other_tag:
        return ET.SubElement(tags, OTHER)
    elif tag_type in age_tag:
        return ET.SubElement(tags, AGE)
    elif tag_type in contact_tag:
        return ET.SubElement(tags, CONTACT)
    elif tag_type in profession_tag:
        return ET.SubElement(tags, PROFESSION)
    
    return ET.SubElement(tags, TAG)
