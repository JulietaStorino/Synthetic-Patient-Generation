import random
import os
from classes.person import Person
from classes.healthcare import HealthRecord
from classes.report import Report

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
        health_record = HealthRecord()
        report = Report()

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