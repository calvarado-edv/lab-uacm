from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route('/')
def bienvenida():
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip_origen = request.remote_addr
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Bienvenido a la demostración de CI/CD con Github</title>
    </head>
    <body>
        <h1>Bienvenidos</h1>
        <p>Fecha y hora actual: {fecha_actual}</p>
        <p>Tu dirección IP: {ip_origen}</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
