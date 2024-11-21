import random
import os
from generator.identification import generate_identification
from generator.address import generate_address
from generator.health_record import generate_health_record
from generator.contacts import generate_contacts

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
        name, surname1, surname2, identification = generate_identification()
        province_number, address = generate_address()
        contacts = generate_contacts(name, surname1, surname2, province_number)
        health_record = generate_health_record()
        id = random.randint(0, 999999)
        with open(f"{output_dir}{id}.txt", "w") as f:
            f.write(identification)
            f.write(address)
            f.write(contacts)
            f.write(health_record)

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