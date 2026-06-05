"""
Punto de entrada para Replit.
Instala dependencias, inicializa la DB y arranca Flask.
"""
import subprocess, sys, os

# Instalar dependencias automáticamente
subprocess.check_call([sys.executable, "-m", "pip", "install", "-r",
                       "backend/requirements.txt", "-q"])

# Añadir backend al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "backend"))

# Apuntar Flask a la carpeta frontend como carpeta estática
import flask
app_module = __import__("app")
app_module.app.static_folder = os.path.join(os.path.dirname(__file__), "frontend")
app_module.app.static_url_path = ""

# Inicializar tablas
app_module.init_db()

# Arrancar
port = int(os.getenv("PORT", 5000))
app_module.app.run(host="0.0.0.0", port=port, debug=False)
