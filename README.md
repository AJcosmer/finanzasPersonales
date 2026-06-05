# 💰 FinanzApp — Guía para Replit

## Pasos para publicar en Replit (desde tu celular Android)

### 1. Crea la cuenta y el proyecto
1. Instala **Replit** desde Play Store
2. Regístrate gratis en replit.com
3. Toca **+** → selecciona **Python** → nómbralo `FinanzApp`

### 2. Sube los archivos
En el panel de archivos de Replit, crea esta estructura y sube cada archivo:

```
finanzapp/               ← raíz del proyecto
├── main.py              ← punto de entrada (OBLIGATORIO en raíz)
├── .replit              ← configuración de Replit
├── replit.nix           ← dependencias del sistema
├── backend/
│   ├── app.py
│   └── requirements.txt
└── frontend/
    ├── index.html
    ├── css/
    │   ├── app.css
    │   └── auth.css
    ├── js/
    │   └── api.js
    └── pages/
        ├── dashboard.html
        ├── transacciones.html
        ├── cuentas.html
        ├── presupuestos.html
        └── metas.html
```

### 3. Activa la base de datos PostgreSQL
1. En el panel izquierdo de Replit toca el ícono 🗄️ **Database**
2. Toca **Create a database** → elige **PostgreSQL**
3. Replit agrega automáticamente la variable `DATABASE_URL` al entorno

### 4. Ejecuta
- Toca el botón **▶ Run**
- Replit instala las dependencias automáticamente
- Las tablas se crean solas al primer arranque
- Aparece una URL pública tipo: `https://finanzapp.tuusuario.repl.co`

### 5. Accede desde tu celular
Abre esa URL en Chrome → menú ⋮ → **Agregar a pantalla de inicio**
¡Ya tienes la app instalada como si fuera nativa!

---

## Tecnologías
- **Backend:** Python + Flask + PostgreSQL (psycopg2)
- **Frontend:** HTML5 + CSS3 + JavaScript + Chart.js
- **Auth:** JWT + bcrypt
- **Moneda:** Peso colombiano (COP)
