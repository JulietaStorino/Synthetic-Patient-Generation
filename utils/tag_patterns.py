import xml.etree.ElementTree as ET

# Define the tag patterns
tag_patterns = [
    ("NOMBRE_SUJETO_ASISTENCIA", r"Nombre: ([^\n]+)"),
    ("ID_SUJETO_ASISTENCIA", r"DNI: ([^\n]+)"),
    ("FECHAS", r"Fecha de nacimiento: ([^\n]+)"),
    ("SEXO_SUJETO_ASISTENCIA", r"Género: ([^\n]+)"),
    ("CALLE", r"Domicilio: ([^\n]+)"),
    ("TERRITORIO", r"Ciudad: ([^\n]+)"),
    ("TERRITORIO", r"Código postal: ([^\n]+)"),
    ("CORREO_ELECTRONICO", r"Email: ([^\n]+)"),
    ("NUMERO_TELEFONO", r"Teléfono fijo: ([^\n]+)"),
    ("NUMERO_TELEFONO", r"Teléfono móvil: ([^\n]+)"),
    ("NUMERO_FAX", r"FAX: ([^\n]+)"),
    ("ID_SUJETO_ASISTENCIA", r"NHC: ([^\n]+)"),
    ("ID_ASEGURAMIENTO", r"NASS: ([^\n]+)"),
    ("PROFESION", r"Condiciones de riesgo: ([^\n]+)"),
    ("NOMBRE_PERSONAL_SANITARIO", r"Médico: Dr\.a? ([^\.]+)\. NC (\d+)\. ([^\.]+)\. ([^\.]+)\. ([^\.]+)\. ([^\.]+)\. ([^\.]+)\. ([^\.]+)\."),
    ("FECHAS", r"Fecha de ingreso: ([^\n]+)"),
    ("ID_CONTACTO_ASISTENCIAL", r"Episodio: ([^\n]+)"),
    ("CENTRO_DE_SALUD", r"Centro de salud: ([^\n]+)"),
    ("HOSPITAL", r"Hospital: ([^\n]+)"),
    ("IDENTIF_VEHICULOS_NRSERIE_PLACAS", r"Matrícula del coche: ([^\n]+)"),
    ("IDENTIF_VEHICULOS_NRSERIE_PLACAS", r"VIN: ([^\n]+)"),
    ("INFORME_CLINICO_PACIENTE", r"Paciente\s*(.*?)?\s*de\s*(\d+ años|\d+ meses|un año|un mes)?\s*de edad\s*(, acompañado de su\s*([^,]+))?,\s*se presenta a la consulta con los siguientes síntomas\.\.\.")
]

def match_tag(tag_type, tags):
    """
    Returns the correct tag element based on the tag type.
    """
    match tag_type:
        case "NOMBRE_PERSONAL_SANITARIO":
            return ET.SubElement(tags, "NAME")
        case "ID_SUJETO_ASISTENCIA" | "ID_TITULACION_PERSONAL_SANITARIO" | "ID_ASEGURAMIENTO" | "ID_CONTACTO_ASISTENCIAL" | "IDENTIF_VEHICULOS_NRSERIE_PLACAS" | "ID_EMPLEO_PERSONAL_SANITARIO":
            return ET.SubElement(tags, "ID")
        case "CALLE" | "TERRITORIO" | "PAIS":
            return ET.SubElement(tags, "LOCATION")
        case "FECHAS":
            return ET.SubElement(tags, "DATE")
        case "SEXO_SUJETO_ASISTENCIA" | "FAMILIARES_SUJETO_ASISTENCIA":
            return ET.SubElement(tags, "OTHER")
        case "EDAD_SUJETO_ASISTENCIA":
            return ET.SubElement(tags, "AGE")
        case "CORREO_ELECTRONICO" | "NUMERO_TELEFONO" | "NUMERO_FAX":
            return ET.SubElement(tags, "CONTACT")
        case "PROFESION":
            return ET.SubElement(tags, "OCCUPATION")
        case "HOSPITAL" | "CENTRO_DE_SALUD" | "INSTITUCION":
            return ET.SubElement(tags, "LOCATION")
        case "EDAD_SUJETO_ASISTENCIA":
            return ET.SubElement(tags, "AGE")
        
    return ET.SubElement(tags, "TAG")
