from generator.identification import generate_identification
from generator.address import generate_address
from generator.contacts import generate_contacts
from generator.health_record import generate_health_record

class Identification():
    def __init__(self):
        self.name, self.surname1, self.surname2, self.dni, self.birthdate, self.gender = generate_identification()
    
    def identification_to_string(self):
        return f"Nombre: {self.name} {self.surname1} {self.surname2}\nDNI: {self.dni}\nFecha de nacimiento: {self.birthdate}\nGénero: {self.gender}\n"

class Address():
    def __init__(self):
        self.province_number, self.city, self.province, self.community, self.street, self.number, self.is_apt, self.apt_floor, self.apt_door, self.postal_code = generate_address()

    def address_to_string(self):
        apt = f', {self.apt_floor} "{self.apt_door}"' if self.is_apt else "" 
        return f"Domicilio: {self.street} {self.number}{apt}\nCiudad: {self.city}, {self.province}, {self.community}\nCódigo postal: {self.postal_code}\n"

class Contacts():
    def __init__(self, name, surname1, surname2, province_number):
        self.email, self.landline_phone, self.mobile_phone, self.fax, self.use_fax = generate_contacts(name, surname1, surname2, province_number)

    def contacts_to_string(self):
        if self.use_fax:
            return f"Email: {self.email}\nTeléfono fijo: {self.landline_phone}\nNúmero de fax: {self.fax}\n"
        return f"Email: {self.email}\nTeléfono fijo: {self.landline_phone}\nTeléfono móvil: {self.mobile_phone}\n"
    
class HealthRecord():
    def __init__(self):
        self.nhc, self.have_risk_profession, self.high_risk_profession, self.risk_conditions_list = generate_health_record()

    def health_record_to_string(self):
        list = self.risk_conditions_list.append(self.high_risk_profession) if self.have_risk_profession else self.risk_conditions_list
        if not list:
            return f"NHS: {self.nhc}\n"
        return f"NHS: {self.nhc}\nRisk conditions: {', '.join(list)}\n"

class Person():
    def __init__(self):
        self.identification = Identification()
        self.address = Address()
        self.contacts = Contacts(self.identification.name, self.identification.surname1, self.identification.surname2, self.address.province_number)
        self.health_record = HealthRecord()

    def person_to_string(self):
        return self.identification.identification_to_string() + self.address.address_to_string() + self.contacts.contacts_to_string() + self.health_record.health_record_to_string()

    