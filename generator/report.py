from random import choice, choices, randint
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

    v_report = f"\n Direccion IP (en red interna): {dir_ip}"
    domain = smtp_domains[randint(0, len(smtp_domains)-1)]
    v_report += f"\nDireccion MAC del dispositivo: {mac_addresses[randint(0, 999)]}"
    v_report += f"\nURL de acceso a expediente: http://{domain}/{urls[randint(0, len(urls)-1)]}"
    v_report += f"\nPuerto de acceso al sistema clinico: {dir_ip}:{all_ports[randint(0, 65536)]}"
    v_report += f"\nServidor SMTP (para envio de informacion): smtp.{domain}"
    return v_report

def generate_biometricid_report():
    """
    Generates a report that includes biometric data
    """
    b_report = f"\nHuella dactilar: {biometric_identifiers[randint(0,4999)]}"
    b_report += f"\nEscaneo retiniano: {biometric_identifiers[randint(0,4999)]}"
    b_report += f"\nReconocimiento facial: {biometric_identifiers[randint(0,4999)]}"
    b_report += f"\nFirma biometrica: {biometric_identifiers[randint(0,4999)]}"
    b_report += f"\nEscaneo del iris: {biometric_identifiers[randint(0,4999)]}"
    return b_report