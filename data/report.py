import random
import string


# List of 1000 IP addresses
ip_list = [f"192.168.{random.randint(0, 255)}.{random.randint(0, 255)}" for _ in range(1000)]

# List of biometric data IDs
biometric_identifiers = [
    "".join(random.choices(string.ascii_uppercase, k=2)) +
    "".join(random.choices(string.digits, k=3)) +
    "".join(random.choices(string.ascii_uppercase, k=3)) +
    "".join(random.choices(string.digits, k=3))
    for _ in range(5000)
]

# Generate a list of all possible ports in string format (0 to 65535)
all_ports = [str(port) for port in range(0, 65536)]

# List of MAC addresses
mac_addresses = [
    ":".join(f"{random.randint(0, 255):02X}" for _ in range(6)) for _ in range(1000)
]

# List of fake emails
smtp_domains = [
    "example-clinica.com", "example-hospital.org", "example-healthcare.net",
    "example-medical.edu", "example-labs.com", "example-pharma.org",
    "example-research.net", "example-biotech.com", "example-radiology.edu",
    "example-therapy.org", "example-nutrition.net", "example-cardiology.com",
    "example-dermatology.org", "example-ophthalmology.net", "example-neurology.com"
]

# List of 100 fake access URLs for expedientes
urls = [
    f"/{random.randint(10000000, 99999999)}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}"
    for _ in range(100)
]

# List of some characteristics of MESH population groups (NEEDS to be distinguish between age groups)
MESH_population_groups = [
    "de tez blanca", "de ascendencia africana del norte", "de ascendencia asiática", "de ascendencia centroasiática", "de ascendencia asiática oriental",
    "de ascendencia asiática del sudeste", "de ascendencia asiática occidental", "de ascendencia caribeña", "de ascendencia indígena americana",
    "de ascendencia europea oriental", "de ascendencia nórdica o escandinava", "de ascendencia del medio oriente", "de ascendencia norteamericana",
    "de ascendencia oceánica", "de ascendencia australiana", "de ascendencia sudamericana", "de descendencia africana", "de ascendencia árabe",
    "de ascendencia indígena centroamericana", "de ascendencia indígena sudamericana", "de ascendencia gitana", "de comunidades vulnerables", "testigo de Jehová",
    "musulman", "judío", "refugiado", "migrante", "transeúnte", "vegetariano", "vegano", "víctima de desastre", "víctima de violencia de género", "discapacitado",
    "terminal", "sobreviviente de violencia", "fumador", "exfumador", "no fumador", "consumidor de alcohol", "usuario de drogas"
]

# Weights for each MESH population group
MESH_population_weights = [
    25, 5, 10, 5, 10, 5, 5, 3, 4, 8, 7, 6, 15, 2, 2, 12, 8, 6, 3, 4, 
    2, 5, 1, 7, 5, 2, 3, 4, 15, 15, 1, 1, 3, 2, 2, 12, 8, 20, 15, 10
]

# List of some possible relatives of a patient according to their age group
companions_0_to_15 = (
    ["madre"] * 5 + ["padre"] * 3 + ["abuela"] * 3 + ["abuelo"] + ["hermana"] * 2 + ["hermano"] + ["tía"] + ["tío"]
)

companions_16_to_59 = (
    ["madre"] * 5 + ["padre"] * 3 + ["abuela"] * 3 + ["hija"] * 5 + ["hijo"] * 5 + ["abuelo"] + ["hermana"] + ["hermano"] + ["tía"] + ["tío"] + ["prima"] + ["primo"] +
    ["sobrina"] + ["sobrino"] + ["nuera"] + ["yerno"] + ["suegra"] + ["suegro"] + ["marido"] + ["esposa"] + ["pareja"] + ["conviviente"] + ["compañero"] + ["amigo"] +
    ["amiga"] + ["vecino"] + ["vecina"] + ["compañero de trabajo"] + ["compañera de trabajo"] + ["compañero de estudio"]
)

companions_60_to_100 = [
    "madre", "padre", "hermana", "hermano", "hija", "hijo", "nuera", "yerno", "marido", "esposa", "pareja", "conviviente",
]