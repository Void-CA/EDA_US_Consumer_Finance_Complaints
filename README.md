# Proyecto de Ciencia de Datos con Kaggle

## Descripción
Este proyecto realiza un Análisis Exploratorio de Datos (EDA) en un dataset descargado de Kaggle. El objetivo es explorar y limpiar los datos, y presentar los hallazgos de manera clara y concisa.

## Tecnologías Utilizadas
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Docker
- Git

## Estructura del Proyecto
- `data/`: Contiene el dataset.
- `notebooks/`: Contiene los notebooks de Jupyter con el EDA y análisis.
- `scripts/`: Contiene los scripts de Python.
- `reports/`: Contiene las visualizaciones y resultados generados.
- `docs/`: Contiene la documentación del proyecto.
- `README.md`: Descripción general del proyecto.
- `requirements.txt`: Dependencias del proyecto.
- `Dockerfile`: Definición de la imagen Docker.
- `docker-compose.yml`: Orquestación de contenedores Docker.

## Cómo Ejecutar
1. Clonar el repositorio.
2. Construir la imagen de Docker y ejecutar el contenedor:
   ```bash
   docker-compose build
   docker-compose up
