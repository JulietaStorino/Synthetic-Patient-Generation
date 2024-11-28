from generator.identification import generate_identification_person
from generator.address import generate_address
from generator.contact import generate_contacts
from generator.health_record import generate_health_record
from classes.util import *
class Identification():
    def __init__(self):
        self.name, self.first_surname, self.second_surname, self.dni, self.birthdate, self.gender, self.gender_mention = generate_identification_person()
    
    def identification_to_string(self):
        dirty_name, dirty_first_surname, dirty_second_surname = dirty_names(self.name, self.first_surname, self.second_surname)
        return f"Nombre: {dirty_name} {dirty_first_surname} {dirty_second_surname}\nDNI: {self.dni}\nFecha de nacimiento: {self.birthdate}\nGénero: {self.gender_mention}\n"

class Address():
    def __init__(self):
        self.province_number, self.city, self.province, self.community, self.street, self.number, self.apt_floor, self.apt_door, self.postal_code = generate_address()

    def address_to_string(self):
        apt = f', {self.apt_floor}{self.apt_door}' if self.apt_door is not None else "" 
        return f"Domicilio: {self.street} {self.number}{apt}\nCiudad: {self.city}, {self.province}, {self.community}\nCódigo postal: {self.postal_code}\n"

class Contacts():
    def __init__(self, name, first_surname, second_surname, province_number):
        self.email, self.landline_phone, self.mobile_phone, self.fax = generate_contacts(name, first_surname, second_surname, province_number)

    def contacts_to_string(self):
        if self.fax is not None:
            return f"Email: {self.email}\nTeléfono fijo: {self.landline_phone}\nFAX: {self.fax}\n"
        return f"Email: {self.email}\nTeléfono fijo: {self.landline_phone}\nTeléfono móvil: {self.mobile_phone}\n"
    
class HealthRecord():
    def __init__(self):
        self.nhc, self.high_risk_profession, self.nass = generate_health_record()

    def health_record_to_string(self):
        health_record = f"NHC: {self.nhc}\n"
        if self.nass is not None:
            health_record += f"NASS: {self.nass}\n"
        if self.high_risk_profession is not None:
            health_record += f"Condición de riesgo: {self.high_risk_profession}\n"
        return health_record

class Person():
    def __init__(self):
        self.identification = Identification()
        self.address = Address()
        self.contacts = Contacts(self.identification.name, self.identification.first_surname, self.identification.second_surname, self.address.province_number)
        self.health_record = HealthRecord()

    def person_to_string(self):
        return self.identification.identification_to_string() + self.address.address_to_string() + self.contacts.contacts_to_string() + self.health_record.health_record_to_string()

    