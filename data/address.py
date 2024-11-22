# Provinces of Spain and autonomous cities
provinces = [
  "Orense", "Pontevedra", "La Coruña", "Lugo",
  "Vizcaya", "Guipúzcoa", "Álava",
  "Huesca", "Zaragoza", "Teruel",
  "Lérida", "Gerona", "Barcelona", "Tarragona",
  "Castellón", "Valencia", "Alicante",
  "Mallorca", "Menorca", "Ibiza", "Formentera", # Balearic Islands
  "León", "Zamora", "Salamanca", "Ávila", "Segovia", "Palencia", "Burgos", "Soria", "Valladolid",
  "Toledo", "Ciudad Real", "Guadalajara", "Cuenca", "Albacete",
  "Cáceres", "Badajoz",
  "Huelva", "Sevilla", "Cádiz", "Málaga", "Córdoba", "Jaén", "Granada", "Almería",
  "Las Palmas", "Santa Cruz de Tenerife",
  "Asturias", "Cantabria", "Navarra", "La Rioja", "Madrid", "Región de Murcia",
  "Ceuta", "Melilla" # Autonomous cities
]

# Postal code prefixes in order of appearance in the provinces list
postal_code_prefixes = [
  "32", "36", "15", "27",
  "48", "20", "01",
  "22", "50", "44",
  "25", "17", "08", "43",
  "12", "46", "03",
  "07", "07", "07", "07", # Balearic Islands
  "24", "49", "37", "05", "40", "34", "09", "42", "47",
  "45", "13", "19", "16", "02",
  "10", "06",
  "21", "41", "11", "29", "14", "23", "18", "04",
  "35", "38",
  "33", "39", "31", "26", "28", "30",
  "52", "51" # Autonomous cities
]

# Autonomous communities in order of appearance in the provinces list
communities = (
  4 * ["Galicia"] + 3 * ["Pais Vasco"] + 3 * ["Aragón"] + 4 * ["Cataluña"] + 3 * ["Comunidad Valenciana"] + 4 * ["Islas Baleares"]
  + 9 * ["Castilla y León"] + 5 * ["Castilla-La Mancha"] + 2 * ["Extremadura"] + 8 * ["Andalucía"] + 2 * ["Canarias"]
  + ["Asturias"] + ["Cantabria"] + ["Navarra"] + ["La Rioja"] + ["Madrid"] + ["Región de Murcia"] + 2 * [""])

# 100 municipalities of Spain (random)
municipalities = [
  "Fuenlabrada", "Salamanca", "Almería", "Torrelodones", "Vigo", "Marbella", "Málaga", "Elche", "Zaragoza", "Melilla"
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