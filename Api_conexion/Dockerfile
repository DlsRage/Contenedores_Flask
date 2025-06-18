# Usar la imagen oficial de Python como base
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos requeridos
COPY requerimientosApi.txt requerimientosApi.txt
RUN pip install -r requerimientosApi.txt

# Copiar el resto de la aplicación
COPY . .

# Exponer el puerto en el que Flask se ejecuta
EXPOSE 5000

