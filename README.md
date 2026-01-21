# Sistema de Backup Automático

Un script sencillo en Python para crear copias de seguridad automáticas de tus carpetas importantes en formato ZIP.

## Características

- Creación automática de archivos ZIP comprimidos
- Nombres de archivo con fecha y hora (formato: `backup_DDMMYY_HHMMSS.zip`)
- Preserva la estructura de carpetas original
- Feedback en tiempo real durante el proceso de backup
- Creación automática de la carpeta de destino si no existe
- Muestra el tamaño final del archivo de backup

## Requisitos

- Python 3.x
- Bibliotecas estándar de Python (no requiere instalaciones adicionales)

## Instalación

1. Clona este repositorio o descarga el archivo `back_up.py`:
```bash
git clone https://github.com/MiguelDV84/automatization_back_up.git
```

2. Navega al directorio del proyecto:
```bash
cd automatization_back_up
```

## Uso

### Uso Básico

Ejecuta el script desde la terminal:

```bash
python back_up.py
```

El programa te pedirá:
1. La ruta de la carpeta que deseas respaldar
2. La ruta donde guardar el backup (opcional, por defecto usa `./backups`)

### Ejemplo de Uso

```
--- BACKUP AUTOMATICO ---
Ingresa la ruta de la carpeta a respaldar: /home/usuario/documentos
Ingresa la ruta donde guardar el backup (deja en blanco para usar './backups'): 

Creando backup en './backups/backup_220125_143025.zip'...
Añadiendo: documentos/archivo1.txt
Añadiendo: documentos/subfolder/archivo2.pdf
...
Backup completado: ./backups/backup_220125_143025.zip

Tamaño del backup: 15.42 MB

¡Backup completa con exito!
```

## Estructura del Código

El script está organizado en tres funciones principales:

- `crear_nombre_backup()`: Genera nombres únicos basados en fecha y hora
- `crear_backup(carpeta_origen, carpeta_destino)`: Crea el archivo ZIP con el contenido de la carpeta
- `main()`: Función principal que maneja la interacción con el usuario

## Personalización

Puedes modificar el script para automatizar completamente el proceso estableciendo rutas predeterminadas en la función `main()`:

```python
carpeta_origen = "/ruta/a/tu/carpeta"
carpeta_destino = "/ruta/destino/backups"
```

## Notas Importantes

- El script verifica que la carpeta de origen exista antes de iniciar el backup
- Si la carpeta de destino no existe, se crea automáticamente
- Los archivos se comprimen usando el método ZIP_DEFLATED para ahorrar espacio
- La estructura de carpetas original se mantiene en el archivo ZIP

## Posibles Mejoras Futuras

- Programación automática de backups (usando cron o Task Scheduler)
- Rotación automática de backups antiguos
- Exclusión de ciertos tipos de archivos
- Backup incremental
- Cifrado de archivos de backup
- Envío de notificaciones por email

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios mayores antes de crear un pull request.

## Autor

Creado como herramienta de utilidad para gestión de backups personales.
