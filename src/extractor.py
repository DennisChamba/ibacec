'''
import pdfplumber
import pandas as pd

# Definir la ruta del archivo PDF
pdf_path = 'PRUEBA.pdf'

with pdfplumber.open(pdf_path) as pdf:
    all_tables = []
    
    # Recorre cada página del PDF
    for page in pdf.pages:
        # Extraer tablas de la página
        tables = page.extract_tables()
        
        # Procesar cada tabla y almacenarlas
        for table in tables:
            df = pd.DataFrame(table)
            all_tables.append(df)

# Combinar todas las tablas en un solo DataFrame si lo deseas
if all_tables:
    combined_df = pd.concat(all_tables, ignore_index=True)

# Guardar las tablas extraídas en un archivo CSV
combined_df.to_csv("extracciones/extraccion_tablas.csv", index=False, encoding='utf-8-sig')

print("Extracción completada y guardada en extraccion_tablas.csv")

'''

'''
import pdfplumber
import pandas as pd

# Definir la ruta del archivo PDF
pdf_path = '40099555.pdf'

# Inicializar listas vacías para cada sección
equipos_data = []
mano_obra_data = []
materiales_data = []
transporte_data = []

with pdfplumber.open(pdf_path) as pdf:
    # Recorre cada página del PDF
    for page in pdf.pages:
        # Extraer tablas de la página
        tables = page.extract_tables()

        # Procesar cada tabla
        for table in tables:
            current_section = None
            for row in table:
                # Detectar las secciones según la primera columna
                if row[0] == "EQUIPOS":
                    current_section = "EQUIPOS"
                elif row[0] == "MANO DE OBRA":
                    current_section = "MANO DE OBRA"
                elif row[0] == "MATERIALES":
                    current_section = "MATERIALES"
                elif row[0] == "TRANSPORTE":
                    current_section = "TRANSPORTE"
                
                # Ignorar filas vacías
                if not any(row):
                    continue
                
                # Almacenar las filas en la lista correspondiente según la sección
                if current_section == "EQUIPOS":
                    if len(row[0]) != 0 and row[0] not in (existing_row[0] for existing_row in equipos_data) :
                        equipos_data.append(row)


                elif current_section == "MANO DE OBRA":
                    if len(row[0]) != 0 and row[0] not in (existing_row[0] for existing_row in mano_obra_data) :
                        mano_obra_data.append(row)
                elif current_section == "MATERIALES":
                    if len(row[0]) != 0 and row[0] not in (existing_row[0] for existing_row in materiales_data) :
                        materiales_data.append(row)
                elif current_section == "TRANSPORTE":
                    if len(row[0]) != 0 and row[0] not in (existing_row[0] for existing_row in transporte_data) :
                        transporte_data.append(row)

# Convertir cada lista de datos en un DataFrame
equipos_df = pd.DataFrame(equipos_data)
mano_obra_df = pd.DataFrame(mano_obra_data)
materiales_df = pd.DataFrame(materiales_data)
transporte_df = pd.DataFrame(transporte_data)

# Guardar cada DataFrame en un archivo CSV separado
equipos_df.to_csv("extracciones/equipos.csv", index=False, encoding='utf-8-sig')
mano_obra_df.to_csv("extracciones/mano_obra.csv", index=False, encoding='utf-8-sig')
materiales_df.to_csv("extracciones/materiales.csv", index=False, encoding='utf-8-sig')
transporte_df.to_csv("extracciones/transporte.csv", index=False, encoding='utf-8-sig')

print("Extracción completada y guardada en archivos CSV separados.")

'''
import pdfplumber
import pandas as pd
from tqdm import tqdm  # Importar tqdm para la barra de progreso

# Definir la ruta del archivo PDF
pdf_path = '40099555.pdf'

# Inicializar listas vacías para cada sección
equipos_data = []
mano_obra_data = []
materiales_data = []
transporte_data = []

with pdfplumber.open(pdf_path) as pdf:
    # Recorre cada página del PDF con una barra de progreso
    for page in tqdm(pdf.pages, desc="Procesando páginas", unit="página"):
        # Extraer tablas de la página
        tables = page.extract_tables()

        # Procesar cada tabla
        for table in tqdm(tables, desc="Procesando tablas", unit="tabla", leave=False):
            current_section = None
            for row in table:
                # Detectar las secciones según la primera columna
                if row[0] == "EQUIPOS":
                    current_section = "EQUIPOS"
                elif row[0] == "MANO DE OBRA":
                    current_section = "MANO DE OBRA"
                elif row[0] == "MATERIALES":
                    current_section = "MATERIALES"
                elif row[0] == "TRANSPORTE":
                    current_section = "TRANSPORTE"
                
                # Ignorar filas vacías
                if not any(row):
                    continue
                
                # Almacenar las filas en la lista correspondiente según la sección
                if current_section == "EQUIPOS":
                    if len(row[0]) != 0 and row[0] not in (existing_row[0] for existing_row in equipos_data):
                        equipos_data.append(row)

                elif current_section == "MANO DE OBRA":
                    if len(row[0]) != 0 and row[0] not in (existing_row[0] for existing_row in mano_obra_data):
                        mano_obra_data.append(row)
                elif current_section == "MATERIALES":
                    if len(row[0]) != 0 and row[0] not in (existing_row[0] for existing_row in materiales_data):
                        materiales_data.append(row)
                elif current_section == "TRANSPORTE":
                    if len(row[0]) != 0 and row[0] not in (existing_row[0] for existing_row in transporte_data):
                        transporte_data.append(row)

# Convertir cada lista de datos en un DataFrame
equipos_df = pd.DataFrame(equipos_data)
mano_obra_df = pd.DataFrame(mano_obra_data)
materiales_df = pd.DataFrame(materiales_data)
transporte_df = pd.DataFrame(transporte_data)

# Guardar cada DataFrame en un archivo CSV separado
equipos_df.to_csv("extracciones/equipos.csv", index=False, encoding='utf-8-sig')
mano_obra_df.to_csv("extracciones/mano_obra.csv", index=False, encoding='utf-8-sig')
materiales_df.to_csv("extracciones/materiales.csv", index=False, encoding='utf-8-sig')
transporte_df.to_csv("extracciones/transporte.csv", index=False, encoding='utf-8-sig')

print("Extracción completada y guardada en archivos CSV separados.")
