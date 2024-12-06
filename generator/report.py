from random import choice, choices, randint, random
from data.report import MESH_population_groups, MESH_population_weights, companions_0_to_15, companions_16_to_59, companions_60_to_100, biometric_identifiers, ip_list, mac_addresses, all_ports, smtp_domains, urls
from util import boolean_with_probability

def generate_MESH_population_group():
    '''
    Generates a random MESH population group from a list of common characteristics.
    '''
    return choices(MESH_population_groups, weights=MESH_population_weights, k=1)[0]

def generate_patient_companion(years_old):
    '''
    Generates a random relative of a patient from a list of common relatives. It may return None with a 40% probability
    '''
    if years_old <= 15:
        return choice(companions_0_to_15)
    elif years_old <= 59:
        return choice(companions_16_to_59) if boolean_with_probability(.6) else None
    return choice(companions_60_to_100) if boolean_with_probability(.6) else None

def generate_report(years_old):
    """
    Generates a report that may include a MESH population group and a relative of a patient
    """
    mesh_group = generate_MESH_population_group()
    companion = generate_patient_companion(years_old)
    return mesh_group, companion

def generate_virtualinfo_report():
    """
    Generates a report that includes virtual data
    """
    dir_ip = ip_list[randint(0,999)]
    domain = smtp_domains[randint(0, len(smtp_domains)-1)]
    v_report = ""
    if random() < 0.1:
        v_report += f"Se registro una consulta virtual desde la Direccion IP (en red interna): {dir_ip}"
        v_report += f"con Direccion MAC del dispositivo: {mac_addresses[randint(0, 999)]}"
    if random() < 0.1:
        v_report += f"Se realizo un expediente, con  URL de acceso a expediente http://{domain}/{urls[randint(0, len(urls)-1)]}"
    if random() < 0.1:
        v_report += f"Se le dio al usuario un puerto {dir_ip}:{all_ports[randint(0, 65536)]} para ingreso al sistema clinico"
    if random() < 0.1:
        v_report += f"El Servidor SMTP (para envio de informacion) en el que este usuario se comunica es smtp.{domain}"
    return v_report

def generate_biometricid_report():
    """
    Generates a report that includes biometric data
    """
    b_report = ""
    if random() < 0.1:
        b_report += f"Se registro una sesion de Huella dactilar, el codigo obtenido fue para revisarla fue {biometric_identifiers[randint(0,4999)]}."
    if random() < 0.1:
        b_report += f"Se registro una sesion de Escaneo retiniano, el codigo obtenido fue para revisarla fue {biometric_identifiers[randint(0,4999)]}."
    if random() < 0.1:
        b_report += f"Se registro una sesion de Reconocimiento facial, el codigo obtenido fue para revisarla fue {biometric_identifiers[randint(0,4999)]}."
    if random() < 0.1:
        b_report += f"Se registro una sesion de Firma biometrica, el codigo obtenido fue para revisarla fue {biometric_identifiers[randint(0,4999)]}."
    if random() < 0.1:
        b_report += f"Se registro una sesion de Escaneo del iris, el codigo obtenido fue para revisarla fue {biometric_identifiers[randint(0,4999)]}."
    return b_report