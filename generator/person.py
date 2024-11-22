from generator.identification import generate_identification_person
from generator.address import generate_address
from generator.contacts import generate_contacts
from generator.health_record import generate_health_record

class Identification():
    def __init__(self):
        self.name, self.surname1, self.surname2, self.dni, self.birthdate, self.gender, self.gender_mention = generate_identification_person()
    
    def identification_to_string(self):
        return f"Nombre: {self.name} {self.surname1} {self.surname2}\nDNI: {self.dni}\nFecha de nacimiento: {self.birthdate}\nGénero: {self.gender_mention}\n"

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
        self.nhc, self.have_risk_profession, self.high_risk_profession, self.risk_conditions_list, self.have_nass, self.nass = generate_health_record()

    def health_record_to_string(self):
        conditions_list = self.risk_conditions_list.append(self.high_risk_profession) if self.have_risk_profession else self.risk_conditions_list
        health_record = f"NHC: {self.nhc}\n"
        if self.have_nass:
            health_record += f"NASS: {self.nass}\n"
        if conditions_list:
            health_record += f"Condiciones de riesgo: {', '.join(conditions_list)}\n"
        return health_record

class Person():
    def __init__(self):
        self.identification = Identification()
        self.address = Address()
        self.contacts = Contacts(self.identification.name, self.identification.surname1, self.identification.surname2, self.address.province_number)
        self.health_record = HealthRecord()

    def person_to_string(self):
        return self.identification.identification_to_string() + self.address.address_to_string() + self.contacts.contacts_to_string() + self.health_record.health_record_to_string()

    