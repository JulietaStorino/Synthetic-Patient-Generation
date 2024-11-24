from generator.report import generate_report

class Report():
    def __init__(self):
        self.mesh_group, self.companion = generate_report()

    def report_to_string(self):
        report = 'Paciente'

        if self.mesh_group:
            report += f" {self.mesh_group}"
        
        if self.companion:
            report += f", acompañado de su {self.companion},"
        
        report += " se presenta a la consulta con los siguientes síntomas..."
        
        return report