# Synthetic-Patient-Generation 🇪🇸
This repository contains a Python script (`main.py`) that generates synthetic information for Spanish residents, including names, surnames, birthdates, addresses, emails, phone numbers, and more. The generated information is saved in text files and xml notation within the output directory.

## Files
- `main.py`: The main script that generates synthetic information.
- `classes`: A directory that contains classes used for generating synthetic information.
- `constants`: A directory that contains the tags and labels used for xml notation.
- `data`: A directory that contains data used for generating synthetic information.
- `generator`: A directory that contains the functions for generating different parts of the synthetic information.
- `utils`: A directory that contains utility functions.
- `output\txt`: A directory where the generated information is saved in text files.
- `output\xml`: A directory where the generated information is saved in xml notation.
- `.gitignore`: The gitignore file.
- `LICENSE`: The license file.

## Usage

To run the script and generate synthetic information, follow these steps:

1. Open a terminal in the repository directory.
2. Run the script with the following command:
3. Enter the number of persons you want to generate.

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
Not all the labels are shown in every generated clinical history. Some labels are randomly selected for each generated clinical history to make the information more diverse. The same clinical history in xml format may have the following format:

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
        <LOCATION id="T7" start="194" end="199" text="15177" TYPE="TERRITORIO" comment=""/>
        <CONTACT id="T8" start="207" end="228" text="belen-hurtado@aol.com" TYPE="CORREO_ELECTRÓNICO" comment=""/>
        <CONTACT id="T9" start="244" end="260" text="+34 981 79 35 10" TYPE="NÚMERO_TELÉFONO" comment=""/>
        <CONTACT id="T10" start="277" end="293" text="+34 681 75 77 60" TYPE="NÚMERO_TELÉFONO" comment=""/>
        <CONTACT id="T11" start="309" end="325" text="+34 981 92 32 45" TYPE="NÚMERO_FAX" comment=""/>
        <ID id="T11" start="299" end="306" text="6946614" TYPE="ID_SUJETO_ASISTENCIA" comment=""/>
        <ID id="T12" start="313" end="325" text="753866020233" TYPE="ID_ASEGURAMIENTO" comment=""/>
        <PROFESSION id="T13" start="347" end="354" text="Microbiólogo" TYPE="PROFESIÓN" comment=""/>
        <NAME id="T14" start="389" end="411" text="Christian Santana Mora" TYPE="NOMBRE_PERSONAL_SANITARIO" comment=""/>
        <ID id="T15" start="416" end="425" text="377307419" TYPE="ID_TITULACIÓN_PERSONAL_SANITARIO" comment=""/>
        <ID id="T16" start="427" end="467" text="Especialista en Enfermedades Infecciosas" TYPE="ID_EMPLEO_PERSONAL_SANITARIO" comment=""/>
        <LOCATION id="T17" start="469" end="553" text="Instituto de Investigación Biomédica en Red de Enfermedades Infecciosas (CIBERINFEC)" TYPE="INSTITUCIÓN" comment=""/>
        <LOCATION id="T18" start="555" end="584" text="Avenida Monforte de Lemos 3-5" TYPE="CALLE" comment=""/>
        <LOCATION id="T19" start="586" end="591" text="28029" TYPE="TERRITORIO" comment=""/>
        <LOCATION id="T20" start="593" end="599" text="Madrid" TYPE="TERRITORIO" comment=""/>
        <LOCATION id="T21" start="601" end="607" text="España" TYPE="PAÍS" comment=""/>
        <DATE id="T22" start="627" end="637" text="26/09/2003" TYPE="FECHAS" comment=""/>
        <ID id="T23" start="648" end="656" text="76187527" TYPE="ID_CONTACTO_ASISTENCIAL" comment=""/>
        <LOCATION id="T24" start="667" end="705" text="Complejo Hospitalario La Mancha Centro" TYPE="HOSPITAL" comment=""/>
        <ID id="T25" start="727" end="734" text="2459EQY" TYPE="IDENTIF_VEHÍCULOS_NRSERIE_PLACAS" comment=""/>
        <ID id="T26" start="759" end="776" text="VSS4PJC8CYJ596603" TYPE="IDENTIF_VEHÍCULOS_NRSERIE_PLACAS" comment=""/>
        <OTHER id="T27" start="820" end="846" text="ascendencia norteamericana" TYPE="OTROS_SUJETO_ASISTENCIA" comment=""/>
        <AGE id="T28" start="850" end="857" text="56 años" TYPE="EDAD_SUJETO_ASISTENCIA" comment=""/>
        <OTHER id="T29" start="884" end="888" text="hijo" TYPE="FAMILIARES_SUJETO_ASISTENCIA" comment=""/>
    </TAGS>
</MEDDOCAN>
```

## Contributions
Contributions are welcome. If you want to contribute, please open an issue or send a pull request.

## License
This project is licensed under the MIT License.
