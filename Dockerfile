FROM python:3.9-slim-buster
WORKDIR /app
COPY app.py .
# Instala las dependencias (en este caso, Flask)
RUN pip install Flask
# Expone el puerto en el que la aplicación Flask escuchará (por defecto es el 5000)
EXPOSE 5000
# Define el comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]
