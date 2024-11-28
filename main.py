import os
import re
from util import generate_n_digits
from xml.dom import minidom
import xml.etree.ElementTree as ET
from classes.person import Person
from classes.healthcare import HealthRecord
from classes.report import Report
from converter.converter import process_xml_labels, process_brat_labels

OUTPUT_DIR = "output/"
OUTPUT_DIR_TXT = "output/txt/"
OUTPUT_DIR_XML = "output/xml/"
OUTPUT_DIR_BRAT = "output/brat/"

def create_output_directories():
    """
    Create the output directories if they don't exist.
    """
    try:
        os.makedirs(OUTPUT_DIR)
        os.makedirs(OUTPUT_DIR_TXT)
        os.makedirs(OUTPUT_DIR_XML)
        os.makedirs(OUTPUT_DIR_BRAT)
    except FileExistsError:
        pass

def generate_person_txt():
    """
    Generate a file with random person data and save it in the output directory.
    """
    person_created = Person()
    health_record = HealthRecord(person_created.identification.birthdate)
    report = Report(person_created.identification.birthdate, health_record.assistance.assistance_date)

    numberfile = generate_n_digits(9)
    namefile = f'{OUTPUT_DIR_TXT}{numberfile}.txt'
    
    with open(namefile, "w") as f:
        f.write("Datos del paciente.\n")
        f.write(person_created.person_to_string())
        f.write("\nDatos asistenciales.\n")
        f.write(health_record.health_record_to_string())
        f.write("\nInforme clínico del paciente: ")
        f.write(report.report_to_string())
    
    return numberfile

def generate_person_xml(namefile):
    """
    Generate an XML file from a TXT file with MEDDOCAN entity's notation
    """
    txt_file = f'{OUTPUT_DIR_TXT}{namefile}.txt'
    new_file = f'{OUTPUT_DIR_XML}{namefile}.xml'
    
    with open(txt_file, 'r', encoding='utf-8') as file:
        text = file.read()

    root = ET.Element("MEDDOCAN\n\t")
    text_element = ET.SubElement(root, "TEXT")
    text_element.text = text
    tags = ET.SubElement(root, "TAGS")
    
    process_xml_labels(text, tags)

    rough_string = ET.tostring(root, encoding="utf-8")
    parsed = minidom.parseString(rough_string)
    pretty_xml = parsed.toprettyxml(indent="    ")

    pretty_xml = re.sub(
        r"<TEXT>(.*?)</TEXT>",
        lambda match: f"<TEXT><![CDATA[{match.group(1)}]]></TEXT>",
        pretty_xml,
        flags=re.DOTALL
    )

    with open(new_file, "w", encoding="utf-8") as file:
        file.write(pretty_xml)


def generate_person_brat(namefile):
    txt_file = f'{OUTPUT_DIR_TXT}{namefile}.txt'
    new_file = f'{OUTPUT_DIR_BRAT}{namefile}.ann'
    
    with open(txt_file, 'r', encoding='utf-8') as file:
        text = file.read()
        
    processed_text = process_brat_labels(text)

    with open(new_file, "w", encoding="utf-8") as file:
        file.write(processed_text)

def generate_people(n):
    """
    Generates n files with random people in each one. The files are saved in the output directory.
    """

    for _ in range(n):
        namefile = generate_person_txt()
        generate_person_xml(namefile)
        generate_person_brat(namefile)
        
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
    create_output_directories()
    generate_people(n)
    print("people generated.")