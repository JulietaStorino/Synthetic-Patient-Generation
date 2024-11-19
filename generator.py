import random
import os

# Provinces of Spain and autonomous cities
provinces = [ "Orense", "Pontevedra", "La Coruña", "Lugo",
               "Vizcaya", "Guipúzcoa", "Álava",
               "Huesca", "Zaragoza", "Teruel",
               "Lérida", "Gerona", "Barcelona", "Tarragona",
               "Castellón", "Valencia", "Alicante",
               "Mallorca", "Menorca", "Ibiza", "Formentera", # Balearic Islands
               "León", "Zamora", "Salamanca", "Ávila", "Segovia", "Palencia", "Burgos", "Soria", "Valladolid",
               "Toledo", "Ciudad Real", "Guadalajara", "Cuenca", "Albacete",
               "Cáceres", "Badajoz",
               "Huelva", "Sevilla", "Cádiz", "Málaga", "Córdoba", "Jaén", "Granada", "Almería",
               "Las Palmas", "Santa Cruz de Tenerife"
               "Asturias", "Cantabria", "Navarra", "La Rioja", "Madrid", "Región de Murcia",
               "Ceuta", "Melilla" # Autonomous cities
             ]

# Autonomous communities
communities = (4 * ["Galicia"] + 3 * ["Pais Vasco"] + 3 * ["Aragón"] + 4 * ["Cataluña"] + 3 * ["Comunidad Valenciana"] + 4 * ["Islas Baleares"]
               + 9 * ["Castilla y León"] + 5 * ["Castilla-La Mancha"] + 2 * ["Extremadura"] + 8 * ["Andalucía"] + 2 * ["Canarias"]
               + ["Asturias"] + ["Cantabria"] + ["Navarra"] + ["La Rioja"] + ["Madrid"] + ["Región de Murcia"])

# Telephone prefixes
phone_prefixes = [ "88", "86", "81", "82",
                   "46", "43", "45",
                   "74", "76", "78",
                   "73", "72", "3", "77",
                   "64", "60", "65",
                   "71", "71", "71", "71", # Balearic Islands
                   "87", "80", "23", "20", "21", "79", "47", "75", "83",
                   "25", "26", "49", "69", "67",
                   "27", "24",
                   "59", "54", "56", "51", "57", "53", "58", "50",
                   "28", "22"
                   "84", "42", "48", "41", "1", "68",
                   "56", "51" # Autonomous cities
                ]

# Postal code prefixes
postal_code_prefixes = [ "32", "36", "15", "27",
                         "48", "20", "01",
                         "22", "50", "44",
                         "25", "17", "08", "43",
                         "12", "46", "03",
                         "07", "07", "07", "07", # Balearic Islands
                         "24", "49", "37", "05", "40", "34", "09", "42", "47",
                         "45", "13", "19", "16", "02",
                         "10", "06",
                         "21", "41", "11", "29", "14", "23", "18", "04",
                         "35", "38"
                         "33", "39", "31", "26", "28", "30", "52", "51" # Autonomous cities
                       ]

# 100 municipalities of Spain (random)
municipalities = ["Fuenlabrada", "Salamanca", "Almería", "Torrelodones", "Vigo", "Marbella", "Málaga", "Elche", "Zaragoza", "Melilla"
                  "Huesca", "Logroño", "Toledo", "Burgos", "Segovia", "San Sebastián", "Murcia", "Vitoria", "Pamplona", "Jaén",
                  "Cáceres", "Córdoba", "Lleida", "Ibiza", "Getafe", "Cuenca", "Teruel", "Tarragona", "Albacete", "León",
                  "Girona", "Badajoz", "Cádiz", "Santander", "Santa Cruz de Tenerife", "Las Palmas de Gran Canaria", "Gijón", "Ciudad Real", "Huelva", "Lugo",
                  "Orense", "Palma", "Avilés", "Alcorcón", "Alcobendas", "Majadahonda", "Ponferrada", "Ourense", "Ronda", "Elda",
                  "Reus", "Parla", "Alcalá de Henares", "Castellón de la Plana", "Ferrol", "Alcázar de San Juan", "Alcoy", "Aranda de Duero", "Béjar", "Benidorm",
                  "Bormujos", "Denia", "Dos Hermanas", "Écija", "Eibar", "Ermua", "Estepa", "Gandía", "Guadix", "Hellín",
                  "Jaca", "Jerez de la Frontera", "Langreo", "Linares", "Liria", "Lorca", "Móstoles", "Motril", "Navalcarnero", "Novelda",
                  "Onda", "Ontinyent", "Palencia", "Plasencia", "Puertollano", "San Fernando", "San Pedro del Pinatar", "Socuéllamos", "Talavera de la Reina", "Totana",
                  "Úbeda", "Vilanova i la Geltrú", "Xàtiva", "Xirivella", "Yecla", "Zafra", "Zamora", "San Vicente del Raspeig", "Telde", "Torrejón de Ardoz",
                 ]

# 100 streets of Spain (random)
streets = [
    "Calle Gran Vía", "Calle de Alcalá", "Calle Serrano", "Paseo de la Castellana", "Calle del Prado",
    "Calle de Atocha", "Calle de Fuencarral", "Calle de la Montera", "Calle de Preciados", "Calle Mayor",
    "Calle de Hortaleza", "Calle de Goya", "Calle de Velázquez", "Calle de Claudio Coello", "Calle de Ayala",
    "Calle de O'Donnell", "Calle de Recoletos", "Calle del Barquillo", "Calle de Espoz y Mina", "Calle de las Huertas",
    "Calle de Toledo", "Calle del Doctor Esquerdo", "Calle de Bravo Murillo", "Calle de Santa Engracia", "Calle de Ríos Rosas",
    "Calle de Génova", "Calle de Miguel Ángel", "Calle de Zurbano", "Calle de la Princesa", "Calle de Ferraz",
    "Calle del Marqués de Urquijo", "Calle de Alberto Aguilera", "Calle de San Bernardo", "Calle de Arenal", "Calle de Leganitos",
    "Calle de la Ribera", "Calle del Rollo", "Calle del Espíritu Santo", "Calle del Pez", "Calle de la Luna",
    "Calle de los Embajadores", "Calle de Arganzuela", "Calle de Segovia", "Calle del Nuncio", "Calle del Sacramento",
    "Calle de Bailén", "Calle del Marqués de Cubas", "Calle de la Lechuga", "Calle de las Tres Cruces", "Calle de la Cabeza",
    "Calle de la Alameda", "Calle de las Infantas", "Calle de la Paz", "Calle de Valverde", "Calle de la Reina",
    "Calle del Amparo", "Calle de los Relatores", "Calle de Mesón de Paredes", "Calle de Tribulete", "Calle de Salitre",
    "Calle de Lavapiés", "Calle de Argumosa", "Calle de la Fe", "Calle del Sombrerete", "Calle del Oso",
    "Calle de la Primavera", "Calle del Doctor Piga", "Calle de la Magdalena", "Calle de Jesús y María", "Calle del Olivar",
    "Calle de la Cabeza del Rey Don Pedro", "Calle de las Yeserías", "Calle de Santa Ana", "Calle de la Libertad", "Calle de la Virgen de los Peligros",
    "Calle del Carmen", "Calle de los Jardines", "Calle de las Salesas", "Calle del Gobernador", "Calle de Piamonte",
    "Calle de Villalar", "Calle de Almagro", "Calle de Covarrubias", "Calle de Fortuny", "Calle de Eduardo Dato",
    "Calle de Sagasta", "Calle de Santa Isabel", "Calle del Duque de Alba", "Calle de Áncora", "Calle de Embajadores",
    "Calle de San Millán", "Calle de San Ildefonso", "Calle de Don Ramón de la Cruz", "Calle de Juan Bravo", "Calle de Narváez",
    "Calle de Ibiza", "Calle de Menorca", "Calle de Lope de Rueda", "Calle de Lope de Vega", "Calle de Moratín",
    "Calle de Amor de Dios", "Calle de las Letras", "Calle del León", "Calle del Fúcar", "Calle de Gobernador"
]

# 150 most common female names in Spain
female_names = ["María Carmen", "María", "Carmen", "Ana María", "Laura", "María Pilar", "María Dolores", "Isabel", "María Teresa", "Ana",
                "Josefa", "Marta", "Cristina", "María Ángeles", "Lucía", "María José", "María Isabel", "Francisca", "Antonia", "Paula",
                "Sara", "Dolores", "Elena", "María Luisa", "Raquel", "Rosa María", "Manuela", "María Jesús", "Pilar", "Concepción",
                "Julia", "Mercedes", "Alba", "Beatriz", "Silvia", "Nuria", "Irene", "Patricia", "Rocío", "Andrea",
                "Rosario", "Juana", "Montserrat", "Teresa", "Encarnación", "Mónica", "Alicia", "María Mar", "Marina", "Sandra",
                "Sonia", "Natalia", "Susana", "Ángela", "Sofía", "Yolanda", "Rosa", "Claudia", "Carla", "Margarita",
                "Eva", "María Josefa", "Inmaculada", "María Rosario", "María Mercedes", "Ana Isabel", "Noelia", "Esther", "Verónica", "Daniela",
                "Carolina", "Nerea", "Martina", "Inés", "Miriam", "Eva María", "María Victoria", "Lorena", "María Elena", "Ana Belén",
                "Victoria", "Ángeles", "María Rosa", "María Concepción", "Alejandra", "María Antonia", "Amparo", "Celia", "Lidia", "Fátima",
                "Ainhoa", "Catalina", "Olga", "María Nieves", "Clara", "Adriana", "Anna", "María Cristina", "Valeria", "María Soledad",
                "Consuelo", "Gloria", "Vanessa", "Emma", "Virginia", "Blanca", "Aurora", "Emilia", "Esperanza", "Luisa",
                "María Luz", "Milagros", "Lourdes", "Laia", "María Belén", "Josefina", "Estefanía", "Noa", "Isabel María", "Begoña",
                "Purificación", "Gema", "María Begoña", "Valentina", "Elisa", "Belén", "Aitana", "María Lourdes", "María Asunción", "Tamara",
                "Ariadna", "María Esther", "María Paz", "Carlota", "Araceli", "Rebeca", "Magdalena", "Mireia", "Paloma", "Gemma",
                "Almudena", "Vanessa", "Lara", "María Inmaculada", "Noemí", "Matilde", "Remedios", "Elvira", "Diana"]

# 150 most common male names in Spain
male_names = [ "Antonio", "Manuel", "José", "Francisco", "David", "Juan", "Javier", "Daniel", "José Antonio", "Francisco Javier",
               "José Luis", "Carlos", "Alejandro", "Jesús", "José Manuel", "Miguel", "Miguel Ángel", "Pablo", "Rafael", "Sergio",
               "Ángel", "Pedro", "Fernando", "Jorge", "José María", "Luis", "Alberto", "Álvaro", "Adrián", "Juan Carlos",
               "Diego", "Juan José", "Raúl", "Iván", "Rubén", "Juan Antonio", "Óscar", "Enrique", "Juan Manuel", "Andrés",
               "Ramón", "Mario", "Santiago", "Víctor", "Vicente", "Joaquín", "Eduardo", "Marcos", "Roberto", "Hugo",
               "Jaime", "Francisco José", "Ignacio", "Jordi", "Alfonso", "Ricardo", "Mohamed", "Salvador", "Marc", "Martín",
               "Guillermo", "Gabriel", "Gonzalo", "Emilio", "José Miguel", "Nicolás", "Julio", "Julián", "Tomás", "Lucas",
               "Samuel", "Agustín", "Ismael", "José Ramón", "Cristian", "Joan", "Aitor", "Héctor", "Félix", "Álex",
               "Iker", "Mateo", "Juan Francisco", "José Carlos", "Sebastián", "César", "Rodrigo", "Josep", "Alfredo", "José Ángel",
               "Mariano", "Víctor Manuel", "Domingo", "José Ignacio", "Felipe", "Luis Miguel", "Pau", "José Francisco", "Xavier", "Albert",
               "Juan Luis", "Izan", "Aarón", "Mohammed", "Eric", "Leo", "Antonio José", "Borja", "Lorenzo", "Gregorio",
               "Arturo", "Esteban", "Bruno", "Joel", "Isaac", "Cristóbal", "Darío", "Asier", "Marco", "José Javier",
               "Antonio Jesús", "Juan Miguel", "Francisco Manuel", "Unai", "Jesús María", "Abel", "Ahmed", "Jaume", "Eugenio", "Jonathan",
               "Germán", "Mikel", "Pedro José", "Omar", "Sergi", "José Vicente", "Christian", "Pol", "Moisés", "Adam",
               "Valentín", "Jon", "Gerard", "Iñigo", "Juan Ramón", "Oliver", "Arnau", "Manuel Jesús", "Juan Pedro", "Adolfo"
            ]

# 200 most common surnames in Spain
surname = ["García", "Rodríguez", "González", "Fernández", "López", "Martínez", "Sánchez", "Pérez", "Gómez", "Martín",
           "Jiménez", "Hernández", "Ruiz", "Díaz", "Moreno", "Muñoz", "Álvarez", "Romero", "Gutiérrez", "Alonso",
           "Navarro", "Torres", "Domínguez", "Ramírez", "Ramos", "Vázquez", "Gil", "Serrano", "Morales", "Molina",
           "Suárez", "Blanco", "Castro", "Delgado", "Ortega", "Ortiz", "Marín", "Rubio", "Núñez", "Medina",
           "Castillo", "Sanz", "Cortés", "Iglesias", "Santos", "Garrido", "Guerrero", "Lozano", "Cano", "Cruz",
           "Flores", "Méndez", "Herrera", "Prieto", "Peña", "León", "Márquez", "Cabrera", "Gallego", "Calvo",
           "Vidal", "Reyes", "Campos", "Vega", "Fuentes", "Carrasco", "Aguilar", "Caballero", "Diez", "Nieto",
           "Vargas", "Santana", "Giménez", "Hidalgo", "Montero", "Pascual", "Herrero", "Lorenzo", "Santiago", "Benítez",
           "Durán", "Arias", "Mora", "Ibáñez", "Rojas", "Ferrer", "Carmona", "Vicente", "Soto", "Crespo",
           "Román", "Parra", "Pastor", "Velasco", "Rivera", "Sáez", "Silva", "Bravo", "Moya", "Gallardo",
           "Soler", "Franco", "Rivas", "Esteban", "Mendoza", "Pardo", "Lara", "Merino", "Espinosa", "Ríos",
           "Vera", "Camacho", "Izquierdo", "Sierra", "Arroyo", "Montes", "Casado", "Carrillo", "Redondo", "Luque",
           "Rey", "Galan", "Segura", "Otero", "Heredia", "Bernal", "Contreras", "Marcos", "Soriano", "Robles",
           "Palacios", "Marti", "Valero", "Pereira", "Guerra", "Varela", "Macias", "Miranda", "Vila", "Exposito",
           "Salazar", "Roldan", "Bueno", "Benito", "Mateo", "Guillen", "Acosta", "Andres", "Aguilera", "Villar",
           "Calderon", "Guzman", "Escudero", "Padilla", "Rivero", "Mateos", "Casas", "Beltran", "Bermudez", "Aparicio",    
           "Salas", "Galvez", "Estevez", "Rico", "Avila", "Jurado", "Quintana", "Escobar", "Conde", "Menendez",
           "Hurtado", "Aranda", "Trujillo", "Plaza", "Abad", "Pacheco", "Gracia", "Villanueva", "Blazquez", "Manzano",
           "Santamaria", "Costa", "Rueda", "Roca", "Mesa", "Luna", "Serra", "Cuesta", "Miguel", "Maldonado",
           "Castaño", "Montoya", "Tomas", "Paredes", "Alarcon", "Zamora", "De la Fuente", "Simon", "Del Rio", "Millan",
          ]

dni_letters = "TRWAGMYFPDXBNJZSQVHLCKE"

mail_domains = ["gmail.com", "hotmail.com", "yahoo.com", "outlook.com", "icloud.com"]

def generate_address():
    """
    Generates a random address contemplating the following fields:
    - Street
    - Number
    - City
    - Province
    - Community
    - Postal code (with the province prefix)
    - Landline phone (with the province prefix)
    - Mobile phone (with the province prefix)
    """

    province_number = random.randint(0, len(provinces) - 1)

    street = random.choice(streets)
    number = random.randint(1, 100)
    city = random.choice(municipalities)

    postal_code = f"{postal_code_prefixes[province_number]}{random.randint(0, 999):03}"
    
    province = provinces[province_number]
    community = communities[province_number]
    
    if province == "Ceuta" or province == "Melilla":
        city_province_community = f"{province}, {province}, Ciudad autónoma de {province}."
    else:
        city_province_community = f"{city}, {province}, {community}."
    
    landline_phone = f"9{phone_prefixes[province_number]}{random.randint(0, 999999):06}"
    mobile_phone = f"6{phone_prefixes[province_number]}{random.randint(0, 999999):06}"

    return f"Calle: {street}, {number}\nCiudad: {city_province_community}\nCódigo postal: {postal_code}.\nTeléfono fijo: {landline_phone}\nTelefono móvil: {mobile_phone}"

def generate_person():
    """
    Generates a random person with the following fields:
    - Name
    - Surname
    - Birthdate
    - Email
    """
    gender = random.choice(["M", "F"])

    name = random.choice(female_names) if (gender == "F") else random.choice(male_names)
    surname1 = random.choice(surname)
    surname2 = random.choice(surname)
    
    birthdate = f"{random.randint(1, 31):02}/{random.randint(1, 12):02}/{random.randint(1950, 2000)}"
    
    number_dni = random.randint(10000000, 99999999)
    letter_dni = dni_letters[number_dni % 23]
    dni = f"{number_dni}{letter_dni}"
    mail = f"{name.lower()}.{surname1.lower()}@{random.choice(mail_domains)}"

    return f"Nombre: {name} {surname1} {surname2}\nFecha de nacimiento: {birthdate}\nDNI: {dni}\nEmail: {mail}"

def generate_persons_txt(n):
    """
    Generates n files with random persons in each one. Each person has the following fields:
    - Name
    - Surname
    - Birthdate
    - Email
    - Address
    - Landline phone
    - Mobile phone
    """

    output_dir = "data/"
    try:
        os.mkdir(output_dir)
    except FileExistsError:
        pass

    for _ in range(n):
        id = random.randint(0, 999999)
        with open(f"{output_dir}{id}.txt", "w") as f:
            f.write(generate_person())
            f.write("\n")
            f.write(generate_address())

if __name__ == "__main__":
    print("This is a Python script to generate random persons with their information.")
    print("How many persons do you want to generate?")
    n = int(input())
    if n <= 0:
        print("The number of persons must be greater than 0.")
        exit(1)
    print(f"Generating {n} persons...")
    generate_persons_txt(n)
    print("Persons generated.")