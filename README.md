# Synthetic-Patient-Generation 🇪🇸
This repository contains a Python script (`main.py`) that generates synthetic information for Spanish residents, including names, surnames, birthdates, addresses, emails, phone numbers, and more. The generated information is saved in text files (.txt), i2b2 notation (.xml), and brat notation (.ann) within the output directory.

## Files
- `classes`: A directory that contains classes used for generating synthetic information.
- `constants`: A directory that contains the tags and labels used for i2b2 and brat notation.
- `converter`: A directory that contains the functions for converting the generated information to i2b2 and brat notation.
- `data`: A directory that contains data used for generating synthetic information.
- `generator`: A directory that contains the functions for generating different parts of the synthetic information.
- `output\txt`: A directory where the generated information is saved in text files.
- `output\xml`: A directory where the generated information is saved in i2b2 notation.
- `output\brat`: A directory where the generated information is saved in brat notation.
- `.gitignore`: The gitignore file.
- `LICENSE`: The license file.
- `main.py`: The main script that generates synthetic information.
- `README.md`: The readme file.
- `utils`: A file that contains utility functions.


## Usage

To run the script and generate synthetic information, follow these steps:

1. Open a terminal in the repository directory.
2. Run the script with the following command: `python3 main.py`.
3. Enter the number of persons you want to generate.
4. Enjoy :D

## Example Output
A generated clinical history in txt format may have the following format:
    
```plaintext
Datos del paciente.
Nombre: Ramón González Martín
DNI: 93891158Y
Fecha de nacimiento: 01/09/1965
Género: M
Domicilio: Calle del Pez 40
Ciudad: Pamplona, Toledo, Castilla-La Mancha
Código postal: 45720
Email: ramon_martin@imibic.org
Teléfono fijo: +34 925 27 41 11
Teléfono móvil: +34 625 86 55 26
NHC: 0549983
Condición de riesgo: Médico

Datos asistenciales.
Médico: Dr. Manuel Palacios Bernal. NC 696908605. Investigador Principal en Parkinson. Instituto de Investigación Biomédica en Red de Enfermedades Neurodegenerativas (CIBERNED). Avenida Monforte de Lemos 3-5. 28029. Madrid. España.
Fecha de ingreso: 09/07/1991
Episodio: 36069011
Centro de salud: Centro de Salud Carabanchel
Matrícula del coche: 5142RAR
Modelo: BMW 3 Series
VIN: VSRPMN2WU6C579790

Informe clínico del paciente:
Paciente de ascendencia africana del norte de 25 años de edad, acompañado de su prima. 
```
Not all the labels are shown in every generated clinical history. Some labels are randomly selected for each generated clinical history to make the information more diverse. The same clinical history in i2b2 format may have the following format:

```xml
<?xml version="1.0" ?>
<MEDDOCAN>
    <TEXT><![CDATA[Datos del paciente.
Nombre: Ramón González Martín
DNI: 93891158Y
Fecha de nacimiento: 01/09/1965
Género: M
Domicilio: Calle del Pez 40
Ciudad: Pamplona, Toledo, Castilla-La Mancha
Código postal: 45720
Email: ramon_martin@imibic.org
Teléfono fijo: +34 925 27 41 11
Teléfono móvil: +34 625 86 55 26
NHC: 0549983
Condición de riesgo: Médico

Datos asistenciales.
Médico: Dr. Manuel Palacios Bernal. NC 696908605. Investigador Principal en Parkinson. Instituto de Investigación Biomédica en Red de Enfermedades Neurodegenerativas (CIBERNED). Avenida Monforte de Lemos 3-5. 28029. Madrid. España.
Fecha de ingreso: 09/07/1991
Episodio: 36069011
Centro de salud: Centro de Salud Carabanchel
Matrícula del coche: 5142RAR
Modelo: BMW 3 Series
VIN: VSRPMN2WU6C579790

Informe clínico del paciente:
Paciente de ascendencia africana del norte de 25 años de edad, acompañado de su prima. ]]></TEXT>
    <TAGS>
        <NAME id="T1" start="28" end="33" text="Ramón" TYPE="NOMBRE_SUJETO_ASISTENCIA" comment=""/>
        <NAME id="T2" start="34" end="49" text="González Martín" TYPE="NOMBRE_SUJETO_ASISTENCIA" comment=""/>
        <ID id="T3" start="55" end="64" text="93891158Y" TYPE="ID_SUJETO_ASISTENCIA" comment=""/>
        <DATE id="T4" start="86" end="96" text="01/09/1965" TYPE="FECHAS" comment=""/>
        <OTHER id="T5" start="105" end="106" text="M" TYPE="SEXO_SUJETO_ASISTENCIA" comment=""/>
        <LOCATION id="T6" start="118" end="134" text="Calle del Pez 40" TYPE="CALLE" comment=""/>
        <LOCATION id="T7" start="143" end="151" text="Pamplona" TYPE="TERRITORIO" comment=""/>
        <LOCATION id="T8" start="153" end="159" text="Toledo" TYPE="TERRITORIO" comment=""/>
        <LOCATION id="T9" start="161" end="179" text="Castilla-La Mancha" TYPE="TERRITORIO" comment=""/>
        <LOCATION id="T10" start="195" end="200" text="45720" TYPE="TERRITORIO" comment=""/>
        <CONTACT id="T11" start="208" end="231" text="ramon_martin@imibic.org" TYPE="CORREO_ELECTRONICO" comment=""/>
        <CONTACT id="T12" start="247" end="263" text="+34 925 27 41 11" TYPE="NUMERO_TELEFONO" comment=""/>
        <CONTACT id="T13" start="280" end="296" text="+34 625 86 55 26" TYPE="NUMERO_TELEFONO" comment=""/>
        <ID id="T14" start="302" end="309" text="0549983" TYPE="ID_SUJETO_ASISTENCIA" comment=""/>
        <PROFESSION id="T15" start="331" end="337" text="Médico" TYPE="PROFESION" comment=""/>
        <NAME id="T16" start="372" end="394" text="Manuel Palacios Bernal" TYPE="NOMBRE_PERSONAL_SANITARIO" comment=""/>
        <ID id="T17" start="399" end="408" text="696908605" TYPE="ID_TITULACION_PERSONAL_SANITARIO" comment=""/>
        <ID id="T18" start="410" end="445" text="Investigador Principal en Parkinson" TYPE="ID_EMPLEO_PERSONAL_SANITARIO" comment=""/>
        <LOCATION id="T19" start="447" end="536" text="Instituto de Investigación Biomédica en Red de Enfermedades Neurodegenerativas (CIBERNED)" TYPE="INSTITUCION" comment=""/>
        <LOCATION id="T20" start="538" end="567" text="Avenida Monforte de Lemos 3-5" TYPE="CALLE" comment=""/>
        <LOCATION id="T21" start="569" end="574" text="28029" TYPE="TERRITORIO" comment=""/>
        <LOCATION id="T22" start="576" end="582" text="Madrid" TYPE="TERRITORIO" comment=""/>
        <LOCATION id="T23" start="584" end="590" text="España" TYPE="PAIS" comment=""/>
        <DATE id="T24" start="610" end="620" text="09/07/1991" TYPE="FECHAS" comment=""/>
        <ID id="T25" start="631" end="639" text="36069011" TYPE="ID_CONTACTO_ASISTENCIAL" comment=""/>
        <LOCATION id="T26" start="657" end="684" text="Centro de Salud Carabanchel" TYPE="CENTRO_SALUD" comment=""/>
        <ID id="T27" start="706" end="713" text="5142RAR" TYPE="IDENTIF_VEHICULOS_NRSERIE_PLACAS" comment=""/>
        <ID id="T28" start="740" end="757" text="VSRPMN2WU6C579790" TYPE="IDENTIF_VEHICULOS_NRSERIE_PLACAS" comment=""/>
        <OTHER id="T29" start="801" end="831" text="ascendencia africana del norte" TYPE="OTROS_SUJETO_ASISTENCIA" comment=""/>
        <AGE id="T30" start="835" end="842" text="25 años" TYPE="EDAD_SUJETO_ASISTENCIA" comment=""/>
        <OTHER id="T31" start="869" end="874" text="prima" TYPE="FAMILIARES_SUJETO_ASISTENCIA" comment=""/>
    </TAGS>
</MEDDOCAN>
```
Finally, the same clinical history in brat format may have the following format:

```ann
T1	NOMBRE_SUJETO_ASISTENCIA 28 33	Ramón
T2	NOMBRE_SUJETO_ASISTENCIA 34 49	González Martín
T3	ID_SUJETO_ASISTENCIA 55 64	93891158Y
T4	FECHAS 86 96	01/09/1965
T5	SEXO_SUJETO_ASISTENCIA 105 106	M
T6	CALLE 118 134	Calle del Pez 40
T7	TERRITORIO 143 151	Pamplona
T8	TERRITORIO 153 159	Toledo
T9	TERRITORIO 161 179	Castilla-La Mancha
T10 TERRITORIO 195 200	45720
T11 CORREO_ELECTRONICO 208 231	ramon_martin@imibic.org
T12 NUMERO_TELEFONO 247 263	+34 925 27 41 11
T13 NUMERO_TELEFONO 280 296	+34 625 86 55 26
T14 ID_SUJETO_ASISTENCIA 302 309	0549983
T15 PROFESION 331 337	Médico
T16 NOMBRE_PERSONAL_SANITARIO 372 394	Manuel Palacios Bernal
T17 ID_TITULACION_PERSONAL_SANITARIO 399 408	696908605
T18 ID_EMPLEO_PERSONAL_SANITARIO 410 445	Investigador Principal en Parkinson
T19 INSTITUCION 447 536	Instituto de Investigación Biomédica en Red de Enfermedades Neurodegenerativas (CIBERNED)
T20 CALLE 538 567	Avenida Monforte de Lemos 3-5
T21 TERRITORIO 569 574	28029
T22 TERRITORIO 576 582	Madrid
T23 PAIS 584 590	España
T24 FECHAS 610 620	09/07/1991
T25 ID_CONTACTO_ASISTENCIAL 631 639	36069011
T26 CENTRO_SALUD 657 684	Centro de Salud Carabanchel
T27 IDENTIF_VEHICULOS_NRSERIE_PLACAS 706 713	5142RAR
T28 IDENTIF_VEHICULOS_NRSERIE_PLACAS 740 757	VSRPMN2WU6C579790
T29 OTROS_SUJETO_ASISTENCIA 801 831	ascendencia africana del norte
T30 EDAD_SUJETO_ASISTENCIA 835 842	25 años
T31 FAMILIARES_SUJETO_ASISTENCIA 869 874	prima

```

## Contributions
Contributions are welcome. If you want to contribute, please open an issue or send a pull request.

## License
This project is licensed under the MIT License.
