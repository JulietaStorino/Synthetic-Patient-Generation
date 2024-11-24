# This must be modified using https://regcess.mscbs.es/regcessWeb/inicioBuscarCentrosAction.do
hospitals = [
    "Hospital Universitario Fundació Jiménez Díaz", "Hospital Universitario La Paz", "Hospital Clínic Barcelona",
    "Hospital Universitario 12 de Octubre", "Hospital Universitari Vall d'Hebron", "Hospital Universitari i Politècnic La Fe",
    "Hospital Universitario Ramón y Cajal", "Hospital Universitario Virgen del Rocío", "Hospital Universitario Puerta de Hierro Majadahonda",
    "Hospital Clínic San Carlos", "Hospital Universitario Marqués de Valdecilla", "Hospital Universitario Reina Sofía de Córdoba",
    "Hospital Universitario Virgen Macarena", "Hospital de la Santa Creu i Sant Pau", "Hospital Universitario Central de Asturias",
    "Hospital Clínic Universitario Virgen de la Arrixaca", "Complejo Hospitalario Universitario de A Coruña", "Hospital Clínic Universitario San Cecilio",
    "Hospital Regional Universitario de Málaga", "Hospital Universitario Doctor Peset", "Complejo Asistencial Universitario Salamanca",
    "Hospital Universitario de Crúces", "Hospital Universitario Río Hortega", "Hospital de Manises", "Hospital Universitario Virgen de la Victoria",
    "Hospital Universitario Rey Juan Carlos de Mostoles", "Hospital Universitario de Basurto", "Complejo Hospitalario Universitario de Cartagena",
    "Complejo Hospitalario Torrecárdenas", "Hospital Clínic Universitario de Valencia", "Hospital Universitario de Fuenlabrada",
    "Hospital Universitario Infanta Leonor", "Hospital Universitario Fundación Alcorcón", "Hospital General Universitario Morales Meseguer",
    "Hospital Universitari de Bellvitge", "Hospital Universitario de Gran Canaria Dr. Negrín", "Complejo Asistencial Universitario de León",
    "Hospital Universitario Severo Ochoa", "Hospital General de Villalba", "Complejo Hospitalario Universitario de Lugo",
    "Hospital Universitario de Cabueñes", "Hospital Universitario Príncipe de Asturias", "Hospital General Universitario Reina Sofía",
    "Hospital Virgen de la Luz", "Complejo Hospitalario Universitario de Santiago", "Hospital GaldaKao - Usansolo",
    "Hospital Universitario Nuestra Señora de Candelaria", "Hospital Universitario Puerto Real", "Complejo Hospitalario La Mancha Centro",
    "Hospital Universitario de la Princesa"
]

# This must be modified using https://regcess.mscbs.es/regcessWeb/inicioBuscarCentrosAction.do
health_centers = [
    "Centro de Salud Aluche", "Centro de Salud Alcalá de Henares", "Centro de Salud Aranjuez", "Centro de Salud Arganzuela",
    "Centro de Salud Barajas", "Centro de Salud Carabanchel", "Centro de Salud Centro", "Centro de Salud Chamartín",
    "Centro de Salud Ciudad Lineal", "Centro de Salud Conde de Casal", "Centro de Salud Coslada", "Centro de Salud Delicias",
    "Centro de Salud Fuencarral", "Centro de Salud Getafe", "Centro de Salud Latina", "Centro de Salud Ronda", "Centro de Salud Tetuán",
    "Centro de Salud Moratalaz", "Centro de Salud Parla", "Centro de Salud Puente de Vallecas", "Centro de Salud San Blas",
    "Centro de Salud Vicálvaro", "Centro de Salud Villaverde", "Centro de Salud Alcorcón", "Centro de Salud Arganda del Rey",
    "Centro de Salud Boadilla del Monte", "Centro de Salud Collado Villalba", "Centro de Salud Fuenlabrada",
    "Centro de Salud Leganés", "Centro de Salud Majadahonda", "Centro de Salud Móstoles", "Centro de Salud Pozuelo de Alarcón",
    "Centro de Salud San Sebastián de los Reyes", "Centro de Salud Torrejón de Ardoz", "Centro de Salud Valdemoro",
    "Centro de Salud Alhaurín de la Torre", "Centro de Salud Benalmádena", "Centro de Salud Fuengirola", "Centro de Salud Marbella",
    "Centro de Salud Málaga Este", "Centro de Salud Málaga Norte", "Centro de Salud Málaga Oeste", "Centro de Salud Málaga Sur",
    "Centro de Salud Sevilla Este", "Centro de Salud Sevilla Norte", "Centro de Salud Sevilla Oeste", "Centro de Salud Sevilla Sur"
]

# List of 9 medical institutions
medical_institutions = [
    "Instituto Universitario de Oftalmobiología Aplicada (IOBA). Avenida Ramón y Cajal, 7. 47011. Valladolid. España.",
    "Instituto Maimónides de Investigación Biomédica de Córdoba (IMIBIC). Avenida Menéndez Pidal, s/n. 14004. Córdoba. España.",
    "Instituto de Investigación Sanitaria del Hospital 12 de Octubre (Imas12). Avenida de Córdoba, s/n. 28041. Madrid. España.",
    "Instituto de Investigación Biomédica en Red de Enfermedades Raras (CIBERER). Avenida Monforte de Lemos 3-5. 28029. Madrid. España.",
    "Instituto de Investigación Biomédica en Red de Salud Mental (CIBERSAM). Avenida Monforte de Lemos 3-5. 28029. Madrid. España.",
    "Instituto de Investigación Biomédica en Red de Enfermedades Cardiovasculares (CIBERCV). Avenida Monforte de Lemos 3-5. 28029. Madrid. España.",
    "Instituto de Investigación Biomédica en Red de Enfermedades Hepáticas y Digestivas (CIBERehd). Avenida Monforte de Lemos 3-5. 28029. Madrid. España.",
    "Instituto de Investigación Biomédica en Red de Enfermedades Neurodegenerativas (CIBERNED). Avenida Monforte de Lemos 3-5. 28029. Madrid. España.",
    "Instituto de Investigación Biomédica en Red de Enfermedades Infecciosas (CIBERINFEC). Avenida Monforte de Lemos 3-5. 28029. Madrid. España.",
]

# List of three healthcare roles for each medical institution
healthcare_roles = [
    "Oftalmólogo Especialista en Retina y Vítreo", "Residente de 3° año en Oftalmología", "Investigador Principal en Optometría Clínica",
    "Endocrinólogo Especialista en Diabetes", "Investigador Clínico en Medicina Interna", "Residente de 4° año en Endocrinología",
    "Cardiólogo de Unidad de Cuidados Intensivos", "Neurólogo Investigador en Trastornos Cognitivos", "Residente de 5° año en Urología",
    "Especialista en Genética Médica", "Investigador Clínico en Síndromes Raros", "Residente de 2° año en Pediatría",
    "Psiquiatra Especialista en Trastornos de Ansiedad", "Neuropsicólogo Clínico Investigador", "Residente de 3° año en Psiquiatría",
    "Cardiólogo Especialista en Electrofisiología", "Investigador Clínico en Insuficiencia Cardíaca", "Residente de 4° año en Cardiología",
    "Gastroenterólogo Especialista en Enfermedades Hepáticas", "Investigador Clínico en Enfermedades Digestivas", "Residente de 3° año en Gastroenterología", 
    "Neurólogo Especialista en Alzheimer", "Investigador Principal en Parkinson", "Residente de 5° año en Neurología",
    "Especialista en Enfermedades Infecciosas", "Investigador Clínico en Epidemiología", "Residente de 4° año en Medicina Interna"
]

# List of 20 car models
car_models = [
    "Toyota Corolla", "Honda Civic", "Ford F-150", "Chevrolet Silverado", "Tesla Model 3", "BMW 3 Series", "Mercedes-Benz C-Class", "Audi A4",
    "Volkswagen Golf", "Nissan Altima", "Hyundai Elantra", "Kia Sorento", "Subaru Outback", "Mazda CX-5", "Jeep Wrangler", "Ram 1500",
    "Chrysler Pacifica", "Honda CR-V", "Toyota RAV4", "Ford Mustang"
]