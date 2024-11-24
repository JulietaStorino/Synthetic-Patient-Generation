from datetime import datetime
from generator.report import generate_report

class Report():
    def __init__(self, birthdate, date):
        if isinstance(birthdate, str):
            birthdate = datetime.strptime(birthdate, "%d/%m/%Y")
        if isinstance(date, str):
            date = datetime.strptime(date, "%d/%m/%Y")

        self.years = date.year - birthdate.year
        if (date.month, date.day) < (birthdate.month, birthdate.day):
            self.years -= 1

        if self.years < 1:
            self.months = (date.year - birthdate.year) * 12 + (date.month - birthdate.month)
            if date.day < birthdate.day:
                self.months -= 1
        else:
            self.months = None

        self.mesh_group, self.companion = generate_report(self.years)

    def report_to_string(self):
        report = 'Paciente'

        if self.mesh_group:
            report += f" {self.mesh_group}"

        if self.years < 1:
            if self.months == 1:
                report += f" de un mes de edad"
            else:
                report += f" de {self.months} meses de edad"
        else:
            if self.years == 1:
                report += f" de un año de edad"
            else:
                report += f" de {self.years} años de edad"
        
        if self.companion is not None:
            report += f", acompañado de su {self.companion},"
        
        report += " se presenta a la consulta con los siguientes síntomas..."
        
        return report