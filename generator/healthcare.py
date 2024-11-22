from generator.identification import generate_identification_doctor
from generator.assistance import generate_assistance

class Doctor():
    def __init__(self):
        self.name, self.surname1, self.surname2, self.gender, self.medical_registration_number = generate_identification_doctor()

    def doctor_to_string(self):
        if (self.gender == "H"):
            return f"Médico: Dr. {self.name} {self.surname1} {self.surname2} {self.medical_registration_number}\n"
        return f"Médico: Dra. {self.name} {self.surname1} {self.surname2} {self.medical_registration_number}\n"
    
class Assistance():
    def __init__(self):
        self.assistance_date, self.hospital = generate_assistance()

    def assistance_to_string(self):
        return f"Fecha de ingreso: {self.assistance_date}\nHospital: {self.hospital}\n"
    
class HealthRecord():
    def __init__(self):
        self.doctor = Doctor()
        self.assistance = Assistance()

    def health_record_to_string(self):
        return self.doctor.doctor_to_string() + self.assistance.assistance_to_string()
