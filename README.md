# botTelegramAsync 🤖

Bot de Telegram **asíncrono** construido con [python-telegram-bot v21](https://python-telegram-bot.org/), listo para desplegar en **Render** desde GitHub.

---

## 📁 Estructura del proyecto

```
botTelegramAsync/
├── bot.py                   # Punto de entrada principal
├── config.py                # Carga de variables de entorno
├── requirements.txt         # Dependencias Python
├── .env.example             # Plantilla de variables de entorno
├── .gitignore
├── render.yaml              # Blueprint de Render (deploy automático)
├── handlers/
│   ├── __init__.py
│   ├── general.py           # /start  /help  /ping
│   └── messages.py          # /echo, texto libre, comandos desconocidos
└── .github/
    └── workflows/
        └── deploy.yml       # CI/CD con GitHub Actions
```

---

## ⚙️ Configuración local

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/botTelegramAsync.git
cd botTelegramAsync
```

### 2. Crear entorno virtual e instalar dependencias

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux / macOS
source .venv/bin/activate

pip install -r requirements.txt
```

### 3. Configurar variables de entorno

```bash
cp .env.example .env
# Edita .env y añade tu BOT_TOKEN
```

### 4. Ejecutar el bot

```bash
python bot.py
```

---

## 🔑 Variables de entorno

| Variable        | Requerida | Descripción                         |
|-----------------|-----------|-------------------------------------|
| `BOT_TOKEN`     | ✅         | Token de @BotFather                 |
| `ADMIN_CHAT_ID` | ❌         | Chat ID del administrador (opcional)|
| `LOG_LEVEL`     | ❌         | `DEBUG` / `INFO` (por defecto INFO) |

> ⚠️ **Nunca** subas tu `.env` a GitHub. Está incluido en `.gitignore`.

---

## 🚀 Despliegue en Render

El archivo `render.yaml` configura automáticamente el servicio como un **Worker** (proceso continuo, sin HTTP), ideal para bots Telegram con polling.

### Pasos

1. **Sube el código a GitHub** (si aún no lo has hecho):
   ```bash
   git add .
   git commit -m "feat: bot telegram async"
   git push origin main
   ```

2. Ve a [render.com](https://render.com) → **New → Blueprint**

3. Conecta tu repositorio de GitHub y selecciona la rama `main`.

4. Render detectará el `render.yaml` y creará el servicio automáticamente.

5. En la configuración del servicio, añade la variable de entorno:
   - **Key:** `BOT_TOKEN`
   - **Value:** tu token de @BotFather

6. Haz clic en **Deploy** — ¡listo! 🎉

> 💡 A partir de ahora, cada `push` a `main` desplegará automáticamente una nueva versión.

## ⚙️ CI con GitHub Actions

El workflow `.github/workflows/deploy.yml` hace lint y verificación de sintaxis en cada push/PR. Render gestiona el deploy de forma independiente vía webhook de GitHub.

---

## 📋 Comandos disponibles

| Comando  | Descripción                        |
|----------|------------------------------------|
| `/start` | Mensaje de bienvenida              |
| `/help`  | Muestra la lista de comandos       |
| `/ping`  | Comprueba que el bot responde      |
| `/echo`  | Repite el texto enviado            |

---

## 🛠️ Agregar nuevos comandos

1. Crea (o edita) un archivo en `handlers/`.
2. Define una función `async def mi_comando(update, context)`.
3. Regístrala en `bot.py`:

```python
from handlers.mi_modulo import mi_comando
app.add_handler(CommandHandler("micomando", mi_comando))
```

---

## 📄 Licencia

MIT — libre de usar y modificar.
