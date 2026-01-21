import os
import datetime
import zipfile

def crear_nombre_backup():
    """Genera un nombre para el archivo de backup basado en la fecha y hora actual"""
    fecha_hora = datetime.datetime.now().strftime("%d%m%y_%H%M%S")
    return f"backup_{fecha_hora}.zip"

def crear_backup(carpeta_origen, carpeta_destino):
    """
    Crear un archivo ZIP con el contenido de la carpeta origen
    
    Args:
        carpeta_origen: Ruta de la carpeta a respaldar
        carpeta_destino: Ruta de la carpeta donde se guardará el archivo de backup

    Returns:
        str: Ruta completa dela rchivo de backup creado
    """
    # Verificar que las carpetas existen
    if not os.path.exists(carpeta_origen):
        print(f"Error: la carpeta de origen '{carpeta_origen}' no existe")
        return None
    
    if not os.path.exists(carpeta_destino):
        print(f"Creando carpeta de destino  '{carpeta_destino}' ...")
        os.makedirs(carpeta_destino)

    # Crear nombre del archivo de backup
    nombre_backup = crear_nombre_backup()
    ruta_backup = os.path.join(carpeta_destino, nombre_backup)

    #Crear archivo zip
    print(f"Creando backup en '{ruta_backup}'...")

    with zipfile.ZipFile(ruta_backup, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        # Recorrer todos los archivos y carpeta en la carpeta origen
        for carpeta_actual, subcarpeta, archivos in os.walk(carpeta_origen):
            for archivo in archivos:
                ruta_archivo = os.path.join(carpeta_actual, archivo)
                ruta_relativa = os.path.relpath(ruta_archivo, os.path.dirname(carpeta_origen))
                zip_file.write(ruta_archivo, ruta_relativa)
                print(f"Añadiendo: {ruta_relativa}")

    print(f"Backup completado: {ruta_backup}")
    return ruta_backup

def main():
    """Funcion principal del programa"""
    print("--- BACKUP AUTOMATICO ---")

    #Configuracion de carpetas (puedes modificar estas rutas segun tus necesidades)
    carpeta_origen = input("Ingresa la ruta de la carpeta a respaldar: ")
    carpeta_destino = input("Ingresa la ruta donde guardar el backup (deja en blanco para usar './backups'): ")

    if not carpeta_destino:
        carpeta_destino = "./backups"

    # Crear backup
    ruta_backup = crear_backup(carpeta_origen, carpeta_destino)

    if ruta_backup:
        print(f"\nTamaño del backup: {os.path.getsize(ruta_backup) / (1024*1024):.2f} MB")
        print("\n¡Backup completa con exito!")

if __name__ == "__main__":
    main()