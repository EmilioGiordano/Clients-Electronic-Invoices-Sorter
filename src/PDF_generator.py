from fpdf import FPDF
import os
import pandas

# Definir la ruta donde se guardarán los PDFs
ruta_destino = r'C:\Users\giord\Desktop\Facturas_clientes\Descargas'

# Asegurarse de que la ruta existe
if not os.path.exists(ruta_destino):
    os.makedirs(ruta_destino)

# Clientes del Excel
excel_data_df = pandas.read_excel("../cuits.xlsx", sheet_name='Personas')
clients_array = excel_data_df.to_dict('records')

# Lista de CUITs proporcionada
cuits = [
    "20123456789", 
    "20334455661", 
    "23665544335",
    "23987654321", 
    "24554433229",
    "27456789123",
    "27778899003",
    "30112233445", 
    "30223344557",
    "33998877667"
]

# Función para generar un archivo PDF con el nombre específico
def generar_pdf(cuit, numero):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Archivo generado para CUIT: {cuit}", ln=True, align="C")
    # Usar la ruta definida para guardar el archivo
    nombre_archivo = f"{cuit}_011_0000_1_{numero:08d}.pdf"
    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    pdf.output(ruta_completa)
    print(f"PDF generado: {ruta_completa}")

# Generar 3 archivos PDF por cada CUIT
# for cuit in cuits:
#     for i in range(1, 4):  # Genera 3 archivos por CUIT
#         generar_pdf(cuit, i)

for person in clients_array:
    cuit = person['CUIT']
    for i in range(1, 4):
        generar_pdf(cuit,i)

print("Archivos PDF generados exitosamente en la ruta:", ruta_destino)