# Synthetic-Patient-Generation 🇪🇸

This repository contains a Python script (`generator.py`) that generates synthetic information for Spanish residents, including names, surnames, birthdates, addresses, emails, and phone numbers. The generated information is saved in text files within the `data/` directory.

## Files

- `generator.py`: Main script that generates the synthetic information.
- `data/`: Directory where the generated text files are stored.
- `README.md`: This repository description file.

## Usage

To run the script and generate synthetic information, follow these steps:

1. Open a terminal in the repository directory.
2. Run the script with the following command:

```sh
python [generator.py](http://_vscodecontentref_/0)
```
3. Enter the number of persons you want to generate when prompted.
4. The generated files will be saved in the data/ directory.

## Example Output
A generated file may have the following format:
    
```plaintext
Nombre: Pablo Flores Lozano
Fecha de nacimiento: 20/05/1972
DNI: 21536039N
Email: pablo.flores@hotmail.com
Calle: Calle de la Alameda, 67
Ciudad: Móstoles, Zaragoza, Aragón.
Código postal: 50583.
Teléfono fijo: 976242701
Telefono móvil: 676750436
```

## Dependencies
The script uses the following Python libraries:
- random: To generate random data.
- os: To handle the file system.

## Contributions
Contributions are welcome. If you want to contribute, please open an issue or send a pull request.

## License
This project is licensed under the MIT License.
