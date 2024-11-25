import os
import re
import random
from xml.dom import minidom
import xml.etree.ElementTree as ET
from classes.person import Person
from classes.healthcare import HealthRecord
from classes.report import Report
from utils.txt_to_xml import match_tag, process_name_subject_assistance_tag, process_name_healthcare_personnel_tag, process_city_tag, process_patient_report

def generate_people_txt(n):
    """
    Generates n files with random people in each one. The files are saved in the output directory.
    """
    output_dir = "output/"
    
    try:
        os.mkdir(output_dir)
    except FileExistsError:
        pass

    for _ in range(n):
        person_created = Person()
        health_record = HealthRecord(person_created.identification.birthdate)
        report = Report(person_created.identification.birthdate, health_record.assistance.assistance_date)

        namefile = f'{output_dir}{random.randint(0, 999999):06}.txt'
        with open(namefile, "w") as f:
            f.write("Datos del paciente.\n")
            f.write(person_created.person_to_string())
            f.write("\n")
            f.write("Datos asistenciales.\n")
            f.write(health_record.health_record_to_string())
            f.write("\n")
            f.write("Informe clínico del paciente: ")
            f.write(report.report_to_string())

def txt_to_xml(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Creates the root element
    root = ET.Element("MEDDOCAN\n\t")
    
    # Creates the TEXT section
    text_element = ET.SubElement(root, "TEXT")
    text_element.text = text  # Agregamos el texto, lo ajustaremos manualmente más adelante

    # Creates the TAGS section
    tags = ET.SubElement(root, "TAGS")

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

    # Process the tag patterns
    tag_id = 1
    for tag_type, pattern in tag_patterns:
        matches = re.finditer(pattern, text)

        for match in matches:
            start, end = match.span(1)
            value = match.group(1).strip()

            if tag_type == "NOMBRE_SUJETO_ASISTENCIA":
                tag_id = process_name_subject_assistance_tag(tag_type, match.group(1).strip(), start, tags, tag_id)
            elif tag_type == "NOMBRE_PERSONAL_SANITARIO":
                tag_id = process_name_healthcare_personnel_tag(match, tags, tag_id)
            elif tag_type == "TERRITORIO" and "Ciudad" in pattern:
                process_city_tag(value, start, tags, tag_id)
            elif tag_type == "INFORME_CLINICO_PACIENTE":
                tag_id = process_patient_report(match, tags, tag_id)
            else:
                name_tag = match_tag(tag_type, tags)
                name_tag.set("id", f"T{tag_id}")
                name_tag.set("start", str(start))
                name_tag.set("end", str(end))
                name_tag.set("text", value)
                name_tag.set("TYPE", tag_type)
                name_tag.set("comment", "")
                tag_id += 1

    # Saves the XML file
    rough_string = ET.tostring(root, encoding="utf-8")

    # Parse the XML
    parsed = minidom.parseString(rough_string)
    pretty_xml = parsed.toprettyxml(indent="    ")

    # Replace the TEXT section with a CDATA section
    pretty_xml = re.sub(
        r"<TEXT>(.*?)</TEXT>",
        lambda match: f"<TEXT><![CDATA[{text}]]></TEXT>",
        pretty_xml,
        flags=re.DOTALL
    )

    # Save the parsed XML
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(pretty_xml)

if __name__ == "__main__":
    print("This is a Python script to generate random people with their information.")
    print("How many people do you want to generate?")
    
    try:
        n = int(input())
    except KeyboardInterrupt:
        print("\nBye!")
        exit(1)
    except ValueError:
        print("The number of people must be an integer.")
        exit(1)
    if n <= 0:
        print("The number of people must be greater than 0.")
        exit(1)
    print(f"Generating {n} people...")
    generate_people_txt(n)
    print("people generated.")