# 💾 Organizador y generador de Facturas C .PDF para clientes


Este proyecto contiene **dos scripts de Python**. Por un lado, el más importante permite automatizar el orden de los archivos de Facturas C de indeterminada cantidad de personas. Por otro lado, el scripts para generar facturas C permite realizar pruebas sobre el script anterior, ya que es necesario contar con archivos con la misma estructura que las facturas C descargadas de la aplicación web de __ARCA/AFIP__.

## 🛠️ ¿Para quién puede ser útil?

Ideal para:
- **Contadores** o estudios contables que manejan documentación de varios clientes.
- **Empresas** que generan y archivan facturas por cliente de forma periódica.
- Cualquier persona que quiera **automatizar el orden de sus facturas** electrónicas o similares.
---
## 📂 1. Organizador de facturas C

Este script:

- Lee el archivo `cuits.xlsx`, que contiene una tabla con CUIT, nombre, apellido y nombre del directorio que se creará para cada cliente.
- Recorre una carpeta de descargas (donde están los PDFs generados).
- Mueve cada PDF a una carpeta con la siguiente estructura:  
  `Facturas_clientes/<NombreCliente>/<AÑO>/<MES_NUM_MES_NOMBRE_AÑO>/`

Por ejemplo:  
`Facturas_clientes/Perez_Juan/2025/04_Abril_2025/20123456783_011_0000_1_00000001.pdf`

---

## 📄 2. `generador_pdfs.py`

Este script:
- Lee un archivo `cuits.xlsx` con datos de clientes (CUIT, nombre, directorio, etc.).
- Genera 3 archivos PDF para cada cliente con el nombre:  
  `CUIT_011_0000_1_XXXXXXXX.pdf`  
  (como si fuera el formato de una Factura C).
- Guarda los archivos en una carpeta específica (configurable en el script).

---

## ▶️ Requisitos

Instalá las dependencias con pip:

```bash
pip install fpdf pandas openpyxl
```

---

## 🚀 Cómo usar

1. **Colocá tu Excel `cuits.xlsx`** en el directorio raíz del proyecto.
2. Modificá las rutas (`ruta_destino`, `source_directory`, etc.) si es necesario.
3. Ejecutá el primer script para generar PDFs:

```bash
python PDF_generator.py
```

4. Luego corré el segundo para organizarlos:

```bash
python Clients-Electronic-Invoices-Sorter.py
```

---

## 📌 Notas

- El nombre del cliente y su carpeta se toma desde la columna `Directorio` del Excel.
- Ambos scripts están diseñados para Windows, pero pueden adaptarse fácilmente a otros sistemas operativos modificando las rutas.

