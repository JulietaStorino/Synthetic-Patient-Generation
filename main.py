import os
import re
import random
from xml.dom import minidom
import xml.etree.ElementTree as ET
from classes.person import Person
from classes.healthcare import HealthRecord
from classes.report import Report
from util.tag_pattern import tag_patterns
from util.txt_to_xml import process_tag_patterns

def generate_people_txt(n):
    """
    Generates n files with random people in each one. The files are saved in the output directory.
    """
    output_dir = "output/"
    output_dir_txt = "output/txt/"
    
    try:
        os.mkdir(output_dir)
        os.mkdir(output_dir_txt)
    except FileExistsError:
        pass

    for _ in range(n):
        person_created = Person()
        health_record = HealthRecord(person_created.identification.birthdate)
        report = Report(person_created.identification.birthdate, health_record.assistance.assistance_date)

        namefile = f'{output_dir_txt}{random.randint(0, 999999):06}.txt'
        with open(namefile, "w") as f:
            f.write("Datos del paciente.\n")
            f.write(person_created.person_to_string())
            f.write("\n")
            f.write("Datos asistenciales.\n")
            f.write(health_record.health_record_to_string())
            f.write("\n")
            f.write("Informe clínico del paciente: ")
            f.write(report.report_to_string())

def txt_to_xml():
    """
    Converts a txt file to xml file with the given tag patterns.
    """
    output_dir_xml = "output/xml/"
    output_dir_txt = "output/txt/"
    
    try:
        os.makedirs(output_dir_xml, exist_ok=True)
    except FileExistsError:
        pass

    # Iterate over the txt files in the txt directory
    for file in os.listdir(output_dir_txt):
        new_file = output_dir_xml + file.replace(".txt", ".xml")
        with open(output_dir_txt + file, 'r', encoding='utf-8') as file:
            text = file.read()

        root = ET.Element("MEDDOCAN\n\t")
        text_element = ET.SubElement(root, "TEXT")
        text_element.text = text
        tags = ET.SubElement(root, "TAGS")
        process_tag_patterns(tag_patterns, text, tags)

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
    print("Converting txt files to xml files...")
    txt_to_xml()
    print("Files converted.")