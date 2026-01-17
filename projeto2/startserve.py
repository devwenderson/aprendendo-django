import os
from waitress import serve
from core.wsgi import application

HOST = '0.0.0.0'
PORT = 8080

if __name__ == "__main__":
    print(f"Servidor rodando em http://{HOST}:{PORT}")
    serve(application, host=HOST, port=PORT)