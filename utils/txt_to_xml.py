import xml.etree.ElementTree as ET

def match_tag(tag_type, tags):
    """
    Returns the correct tag element based on the tag type.
    """
    match tag_type:
        case "NOMBRE_PERSONAL_SANITARIO":
            return ET.SubElement(tags, "NAME")  # Cambiamos "TAG" por "NAME"
        case "ID_SUJETO_ASISTENCIA" | "ID_TITULACION_PERSONAL_SANITARIO" | "ID_ASEGURAMIENTO" | "ID_CONTACTO_ASISTENCIAL" | "IDENTIF_VEHICULOS_NRSERIE_PLACAS":
            return ET.SubElement(tags, "ID")
        case "CALLE" | "TERRITORIO" | "PAIS":
            return ET.SubElement(tags, "LOCATION")
        case "FECHAS":
            return ET.SubElement(tags, "DATE")
        case "SEXO_SUJETO_ASISTENCIA":
            return ET.SubElement(tags, "OTHER")
        case "EDAD_SUJETO_ASISTENCIA":
            return ET.SubElement(tags, "AGE")
        case "CORREO_ELECTRONICO" | "NUMERO_TELEFONO" | "NUMERO_FAX":
            return ET.SubElement(tags, "CONTACT")
        case "PROFESION":
            return ET.SubElement(tags, "OCCUPATION")
        case "HOSPITAL" | "CENTRO_DE_SALUD":
            return ET.SubElement(tags, "LOCATION")
        
    return ET.SubElement(tags, "TAG")

def process_name_tag(tag_type, full_name, start_pos, tags, tag_id):
    """
    Split the full name into name and surnames, and create the corresponding tags.
    """
    parts = full_name.split()
    name = parts[0]
    surnames = " ".join(parts[1:])

    # Calculates the start and end positions for the name and surnames
    first_start = start_pos
    first_end = first_start + len(name)
    last_start = first_end + 1 
    last_end = last_start + len(surnames)

    # Create the tag for the name
    name_tag = ET.SubElement(tags, "NAME")
    name_tag.set("id", f"T{tag_id}")
    name_tag.set("start", str(first_start))
    name_tag.set("end", str(first_end))
    name_tag.set("text", name)
    name_tag.set("TYPE", tag_type)
    name_tag.set("comment", "")

    # Create the tag for the surnames
    surnames_tag = ET.SubElement(tags, "NAME")
    surnames_tag.set("id", f"T{tag_id + 1}")
    surnames_tag.set("start", str(last_start))
    surnames_tag.set("end", str(last_end))
    surnames_tag.set("text", surnames)
    surnames_tag.set("TYPE", tag_type)
    surnames_tag.set("comment", "")

    # Return the next tag id
    return tag_id + 2

def process_city(tag_type, full_localitation, start_pos, tags, tag_id):
    """
    Split the full localitation into parts and create the corresponding tags.
    """
    parts = full_localitation.split(", ")
    current_start = start_pos

    for part in parts:
        current_end = current_start + len(part)
        location_tag = ET.SubElement(tags, "LOCATION")
        location_tag.set("id", f"T{tag_id}")
        location_tag.set("start", str(current_start))
        location_tag.set("end", str(current_end))
        location_tag.set("text", part)
        location_tag.set("TYPE", tag_type)
        location_tag.set("comment", "")
        tag_id += 1
        current_start = current_end + 2