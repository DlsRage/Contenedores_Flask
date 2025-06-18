# Contenedores_Flask

Este proyecto utiliza **Flask** para crear una aplicación web sencilla, ideal para aprender a manejar contenedores y desplegar aplicaciones Python de manera eficiente. Además, el proyecto emplea **Docker** y **Docker Compose** para contenerizar y orquestar la aplicación, facilitando su despliegue y portabilidad entre distintos entornos.

También utiliza un archivo **HTML** ubicado en la carpeta `templates`, que es renderizado por Flask para mostrar la interfaz web de la aplicación cuando se accede localmente.

## ¿Cómo funciona el proyecto?

- **Contenedores_Flask** es una aplicación web construida con [Flask](https://flask.palletsprojects.com/).
- Permite gestionar rutas, vistas y lógica de backend en Python de forma simple y rápida.
- Utiliza una plantilla HTML dentro de la carpeta `templates` para la interfaz web, permitiendo a los usuarios interactuar con la aplicación desde el navegador.
- El proyecto está preparado para ejecutarse dentro de un contenedor Docker y puede ser orquestado mediante Docker Compose, mostrando las mejores prácticas de contenerización en aplicaciones Python.
- El objetivo principal es demostrar cómo se puede contenerizar una aplicación Python/Flask y orquestarla (por ejemplo, con Docker y Docker Compose), facilitando su despliegue en diferentes entornos.
- El proyecto se puede ejecutar localmente o en cualquier plataforma que soporte contenedores.

## Requisitos

- Python 3.8 o superior
- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Instalación y ejecución local

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/DlsRage/Contenedores_Flask.git
   cd Contenedores_Flask
   ```

2. **Instala las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecuta la aplicación:**

   ```bash
   python app.py
   ```

4. **Accede a la app:**
   
   Abre tu navegador y ve a `http://127.0.0.1:5000/`. Se cargará la página HTML ubicada en la carpeta `templates` del proyecto.

## Ejecución con Docker Compose

1. **Inicia los servicios definidos en `docker-compose.yml`:**

   ```bash
   docker compose up --build
   ```

2. **Abre tu navegador en:** `http://localhost:5000/`  
   La interfaz web será mostrada gracias al archivo HTML en la carpeta `templates`.

## ¿Por qué Docker y Docker Compose?

- Docker permite encapsular todas las dependencias y configuraciones necesarias para ejecutar la aplicación en un contenedor aislado.
- Docker Compose facilita la orquestación y el manejo de múltiples servicios (por ejemplo, la aplicación Flask junto a una base de datos).
- Facilita el despliegue y la reproducción del entorno en distintos sistemas, evitando problemas de "funciona en mi máquina".
- Puedes usar la misma configuración en desarrollo, pruebas y producción.

---

## Estructura del proyecto

```
Contenedores_Flask/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
├── templates/
│   └── [archivo(s) HTML]
└── [otros archivos y carpetas]
```

- **app.py**: Código principal de la aplicación Flask.
- **requirements.txt**: Lista de dependencias Python.
- **Dockerfile**: Archivo de configuración para crear la imagen de Docker.
- **docker-compose.yml**: Archivo de orquestación de servicios para Docker Compose.
- **templates/**: Carpeta que contiene los archivos HTML renderizados por la app.
- **README.md**: Documentación del proyecto.

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar el proyecto, abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la licencia MIT.

---

**Autor:** [DlsRage](https://github.com/DlsRage)
