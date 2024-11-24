from generator.identification import generate_identification_doctor
from generator.assistance import generate_assistance

class Doctor():
    def __init__(self):
        self.name, self.surname1, self.surname2, self.gender, self.medical_registration_number, self.healthcare_role, self.institution = generate_identification_doctor()

    def doctor_to_string(self):
        if self.gender == "M":
            return f"Médico: Dr. {self.name} {self.surname1} {self.surname2}. {self.medical_registration_number}. {self.healthcare_role}. {self.institution}\n"
        return f"Médico: Dra. {self.name} {self.surname1} {self.surname2}. {self.medical_registration_number}. {self.healthcare_role}. {self.institution}\n"
    
class Assistance():
    def __init__(self):
        self.assistance_date, self.have_episode, self.episode, self.hospital, self.health_center, self.is_hospital = generate_assistance()

    def assistance_to_string(self):
        assistance = f"Fecha de ingreso: {self.assistance_date}\n"
        if self.have_episode:
            assistance += f"Episodio: {self.episode}\n"
        if self.is_hospital:
            assistance += f"Hospital: {self.hospital}\n"
        else:
            assistance += f"Centro de salud: {self.health_center}\n"
        return assistance
    
class HealthRecord():
    def __init__(self):
        self.doctor = Doctor()
        self.assistance = Assistance()

    def health_record_to_string(self):
        return self.doctor.doctor_to_string() + self.assistance.assistance_to_string()
