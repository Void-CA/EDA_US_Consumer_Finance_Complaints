# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /notebooks

# Copiar el archivo de requerimientos y el script principal
COPY requirements.txt requirements.txt

# Instalar las dependencias
RUN pip install -r requirements.txt

# Copiar el resto del código y archivos necesarios al contenedor
COPY . .

# Exponer el puerto 8888 para Jupyter Notebook
EXPOSE 8888

# Definir el comando para ejecutar Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
