import os
import shutil
import datetime
import pandas

# Obtener la fecha actual
actual_date = datetime.datetime.now()
actual_month_number = actual_date.month
actual_month = actual_date.strftime('%B')  # Nombre del mes en inglés
actual_year = actual_date.year

# Clientes del Excel
excel_data_df = pandas.read_excel("../cuits.xlsx", sheet_name='Personas')
clients_array = excel_data_df.to_dict('records')

# Directorio de origen (Downloads)
source_directory = r'C:\Users\giord\Desktop\Facturas_clientes\Descargas'

# Traducir el nombre del mes a español
month_traduction = {
    'January': 'Enero', 
    'February': 'Febrero', 
    'March': 'Marzo', 
    'April': 'Abril',
    'May': 'Mayo', 
    'June': 'Junio', 
    'July': 'Julio', 
    'August': 'Agosto',
    'September': 'Septiembre', 
    'October': 'Octubre', 
    'November': 'Noviembre', 
    'December': 'Diciembre'
}
spanish_month_traduction = month_traduction.get(actual_month, actual_month)

# Recorrer array y organizar los archivos
for person in clients_array:
    directory = person['Directorio']
    cuit = person['CUIT']
    destination_directory = rf'C:\Users\giord\Desktop\Facturas_clientes\Facturas_clientes\{directory}\{actual_year}\{actual_month_number}_{spanish_month_traduction}_{actual_year}'

    # Crea el directorio de destino si no existe
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # Busca y mueve los archivos que comienzan con el CUIT
    files_moved = False
    for filename in os.listdir(source_directory):
        file_path = os.path.join(source_directory, filename)

        if os.path.isfile(file_path) and filename.startswith(str(cuit)):
            destination_path = os.path.join(destination_directory, filename)
            shutil.move(file_path, destination_path)
            print(f'Archivo {filename} movido a {destination_directory}')
            files_moved = True

    if not files_moved:
        print(f'No se encontraron archivos para el CUIT {cuit}, cliente: {directory}')