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
Nombre: Belén Hurtado Romemo
DNI: 55912858L
Fecha de nacimiento: 06/02/1947
Género: Mujer
Domicilio: Calle de Valverde 80
Ciudad: Bormujos, La Coruña, Galicia
Código postal: 15177
Email: belen-hurtado@aol.com
Teléfono fijo: +34 981 79 35 10
Teléfono móvil: +34 681 75 77 60
FAX: +34 981 92 32 45
NHC: 6946614
NASS: 753866020233
Condición de riesgo: Microbiólogo

Datos asistenciales.
Médico: Dr. Christian Santana Mora. NC 377307419. Especialista en Enfermedades Infecciosas. Instituto de Investigación Biomédica en Red de Enfermedades Infecciosas (CIBERINFEC). Avenida Monforte de Lemos 3-5. 28029. Madrid. España.
Fecha de ingreso: 26/09/2003
Episodio: 76187527
Hospital: Complejo Hospitalario La Mancha Centro
Matrícula del coche: 2459EQY
Modelo: Mazda CX-5
VIN: VSS4PJC8CYJ596603

Informe clínico del paciente: Paciente de ascendencia norteamericana de 56 años de edad, acompañado de su hijo, se presenta a la consulta con los siguientes síntomas...
```
Not all the labels are shown in every generated clinical history. Some labels are randomly selected for each generated clinical history to make the information more diverse. The same clinical history in i2b2 format may have the following format:

```xml
<?xml version="1.0" ?>
<MEDDOCAN>
    <TEXT><![CDATA[Datos del paciente.
Nombre: Belén Hurtado Romemo
DNI: 55912858L
Fecha de nacimiento: 06/02/1947
Género: Mujer
Domicilio: Calle de Valverde 80
Ciudad: Bormujos, La Coruña, Galicia
Código postal: 15177
Email: belen-hurtado@aol.com
Teléfono fijo: +34 981 79 35 10
Teléfono móvil: +34 681 75 77 60
FAX: +34 981 92 32 45
NHC: 6946614
NASS: 753866020233
Condición de riesgo: Microbiólogo

Datos asistenciales.
Médico: Dr. Christian Santana Mora. NC 377307419. Especialista en Enfermedades Infecciosas. Instituto de Investigación Biomédica en Red de Enfermedades Infecciosas (CIBERINFEC). Avenida Monforte de Lemos 3-5. 28029. Madrid. España.
Fecha de ingreso: 26/09/2003
Episodio: 76187527
Hospital: Complejo Hospitalario La Mancha Centro
Matrícula del coche: 2459EQY
Modelo: Mazda CX-5
VIN: VSS4PJC8CYJ596603

Informe clínico del paciente: Paciente de ascendencia norteamericana de 56 años de edad, acompañado de su hijo, se presenta a la consulta con los siguientes síntomas...]]></TEXT>
    <TAGS>
        <NAME id="T1" start="28" end="33" text="Belén" TYPE="NOMBRE_SUJETO_ASISTENCIA" comment=""/>
        <NAME id="T2" start="34" end="48" text="Hurtado Romemo" TYPE="NOMBRE_SUJETO_ASISTENCIA" comment=""/>
        <ID id="T3" start="54" end="63" text="55912858L" TYPE="ID_SUJETO_ASISTENCIA" comment=""/>
        <DATE id="T4" start="85" end="95" text="06/02/1947" TYPE="FECHAS" comment=""/>
        <OTHER id="T5" start="104" end="109" text="Mujer" TYPE="SEXO_SUJETO_ASISTENCIA" comment=""/>
        <LOCATION id="T6" start="121" end="141" text="Calle de Valverde 80" TYPE="CALLE" comment=""/>
        <LOCATION id="T7" start="150" end="158" text="Bormujos" TYPE="TERRITORIO" comment=""/>
        <LOCATION id="T8" start="160" end="169" text="La Coruña" TYPE="TERRITORIO" comment=""/>
        <LOCATION id="T9" start="171" end="178" text="Galicia" TYPE="TERRITORIO" comment=""/>
        <LOCATION id="T10" start="194" end="199" text="15177" TYPE="TERRITORIO" comment=""/>
        <CONTACT id="T11" start="207" end="228" text="belen-hurtado@aol.com" TYPE="CORREO_ELECTRONICO" comment=""/>
        <CONTACT id="T12" start="244" end="260" text="+34 981 79 35 10" TYPE="NUMERO_TELEFONO" comment=""/>
        <CONTACT id="T13" start="277" end="293" text="+34 681 75 77 60" TYPE="NUMERO_TELEFONO" comment=""/>
        <CONTACT id="T14" start="309" end="325" text="+34 981 92 32 45" TYPE="NUMERO_FAX" comment=""/>
        <ID id="T15" start="299" end="306" text="6946614" TYPE="ID_SUJETO_ASISTENCIA" comment=""/>
        <ID id="T16" start="313" end="325" text="753866020233" TYPE="ID_ASEGURAMIENTO" comment=""/>
        <PROFESSION id="T17" start="347" end="354" text="Microbiólogo" TYPE="PROFESION" comment=""/>
        <NAME id="T18" start="389" end="411" text="Christian Santana Mora" TYPE="NOMBRE_PERSONAL_SANITARIO" comment=""/>
        <ID id="T19" start="416" end="425" text="377307419" TYPE="ID_TITULACION_PERSONAL_SANITARIO" comment=""/>
        <ID id="T20" start="427" end="467" text="Especialista en Enfermedades Infecciosas" TYPE="ID_EMPLEO_PERSONAL_SANITARIO" comment=""/>
        <LOCATION id="T21" start="469" end="553" text="Instituto de Investigación Biomédica en Red de Enfermedades Infecciosas (CIBERINFEC)" TYPE="INSTITUCION" comment=""/>
        <LOCATION id="T22" start="555" end="584" text="Avenida Monforte de Lemos 3-5" TYPE="CALLE" comment=""/>
        <LOCATION id="T23" start="586" end="591" text="28029" TYPE="TERRITORIO" comment=""/>
        <LOCATION id="T24" start="593" end="599" text="Madrid" TYPE="TERRITORIO" comment=""/>
        <LOCATION id="T25" start="601" end="607" text="España" TYPE="PAIS" comment=""/>
        <DATE id="T26" start="627" end="637" text="26/09/2003" TYPE="FECHAS" comment=""/>
        <ID id="T27" start="648" end="656" text="76187527" TYPE="ID_CONTACTO_ASISTENCIAL" comment=""/>
        <LOCATION id="T28" start="667" end="705" text="Complejo Hospitalario La Mancha Centro" TYPE="HOSPITAL" comment=""/>
        <ID id="T29" start="727" end="734" text="2459EQY" TYPE="IDENTIF_VEHICULOS_NRSERIE_PLACAS" comment=""/>
        <ID id="T30" start="759" end="776" text="VSS4PJC8CYJ596603" TYPE="IDENTIF_VEHICULOS_NRSERIE_PLACAS" comment=""/>
        <OTHER id="T31" start="820" end="846" text="ascendencia norteamericana" TYPE="OTROS_SUJETO_ASISTENCIA" comment=""/>
        <AGE id="T32" start="850" end="857" text="56 años" TYPE="EDAD_SUJETO_ASISTENCIA" comment=""/>
        <OTHER id="T33" start="884" end="888" text="hijo" TYPE="FAMILIARES_SUJETO_ASISTENCIA" comment=""/>
    </TAGS>
</MEDDOCAN>
```
Finally, the same clinical history in brat format may have the following format:

```ann
T1	NOMBRE_SUJETO_ASISTENCIA 28 33	Belén
T2	NOMBRE_SUJETO_ASISTENCIA 34 48	Hurtado Romemo
T3	ID_SUJETO_ASISTENCIA 54 63	55912858L
T4	FECHAS 85 95	06/02/1947
T5  SEXO_SUJETO_ASISTENCIA 104 109	Mujer
T6	CALLE 121 141	Calle de Valverde 80
T7	TERRITORIO 150 158	Bormujos
T8	TERRITORIO 160 169	La Coruña
T9	TERRITORIO 171 178	Galicia
T10 TERRITORIO 194 199	15177
T11	CORREO_ELECTRONICO 207 228 belen-hurtado@aol.com
T12	NUMERO_TELEFONO 244 260 +34 981 79 35 10
T13	NUMERO_TELEFONO 277 293 +34 681 75 77 60
T14	NUMERO_FAX 309 325 +34 981 92 32 45
T15	ID_SUJETO_ASISTENCIA 299 306 6946614
T16	ID_ASEGURAMIENTO 313 325 753866020233
T17	PROFESION 347 354 Microbiólogo
T18	NOMBRE_PERSONAL_SANITARIO 389 411 Christian Santana Mora
T19	ID_TITULACION_PERSONAL_SANITARIO 416 425 377307419
T20	ID_EMPLEO_PERSONAL_SANITARIO 427 467 Especialista en Enfermedades Infecciosas
T21	INSTITUCION 469 553 Instituto de Investigación Biomédica en Red de Enfermedades Infecciosas (CIBERINFEC)
T22	CALLE 555 584 Avenida Monforte de Lemos 3-5
T23	TERRITORIO 586 591 28029
T24	TERRITORIO 593 599 Madrid
T25	PAIS 601 607 España
T26	FECHAS 627 637 26/09/2003
T27	ID_CONTACTO_ASISTENCIAL 648 656 76187527
T28	HOSPITAL 667 705 Complejo Hospitalario La Mancha Centro
T29	IDENTIF_VEHICULOS_NRSERIE_PLACAS 727 734 2459EQY
T30	IDENTIF_VEHICULOS_NRSERIE_PLACAS 759 776 VSS4PJC8CYJ596603
T31	OTROS_SUJETO_ASISTENCIA 820 846 ascendencia norteamericana
T32	EDAD_SUJETO_ASISTENCIA 850 857 56 años
T33	FAMILIARES_SUJETO_ASISTENCIA 884 888 hijo
```

## Contributions
Contributions are welcome. If you want to contribute, please open an issue or send a pull request.

## License
This project is licensed under the MIT License.
