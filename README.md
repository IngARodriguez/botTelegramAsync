# botTelegramAsync 🤖

Bot de Telegram **asíncrono** construido con [python-telegram-bot v21](https://python-telegram-bot.org/), desplegado en **Render** vía GitHub.

---

## 📁 Estructura del proyecto

```
botTelegramAsync/
├── bot.py                   # Punto de entrada + servidor HTTP health check
├── config.py                # Carga de variables de entorno
├── requirements.txt         # Dependencias Python
├── .python-version          # Fija Python 3.12 (requerido por Render)
├── render.yaml              # Blueprint de Render
├── .env.example             # Plantilla de variables de entorno
├── .gitignore
├── handlers/
│   ├── __init__.py
│   ├── general.py           # /start  /help  /ping
│   └── messages.py          # /echo, texto libre, comandos desconocidos
└── .github/
    └── workflows/
        └── deploy.yml       # CI: lint en cada push/PR
```

---

## ⚙️ Configuración local

```bash
# 1. Clonar
git clone https://github.com/TU_USUARIO/botTelegramAsync.git
cd botTelegramAsync

# 2. Entorno virtual
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # Linux / macOS

pip install -r requirements.txt

# 3. Variables de entorno
cp .env.example .env
# Edita .env y añade tu BOT_TOKEN

# 4. Ejecutar
python bot.py
```

---

## 🔑 Variables de entorno

| Variable        | Requerida | Descripción                          |
|-----------------|-----------|--------------------------------------|
| `BOT_TOKEN`     | ✅        | Token de @BotFather                  |
| `ADMIN_CHAT_ID` | ❌        | Chat ID del administrador (opcional) |
| `LOG_LEVEL`     | ❌        | `DEBUG` / `INFO` (default: `INFO`)   |

> ⚠️ **Nunca** subas tu `.env` a GitHub. Está incluido en `.gitignore`.

---

## 🚀 Despliegue en Render

### Requisitos previos
- Cuenta en [render.com](https://render.com)
- Repositorio subido a GitHub con todos los archivos (incluido `.python-version`)

### Pasos

**1. Sube el código a GitHub:**
```bash
git add .
git commit -m "feat: bot telegram async"
git push origin main
```

**2. Crea el servicio en Render:**
- Ve a [render.com](https://render.com) → **New → Blueprint**
- Conecta tu repositorio de GitHub y selecciona la rama `main`
- Render detecta el `render.yaml` y crea el servicio como **Web Service**

**3. Configura la variable de entorno `BOT_TOKEN`:**
- En tu servicio → **Environment → Edit**
- Agrega:
  - **Key:** `BOT_TOKEN`
  - **Value:** tu token de @BotFather
- Guarda los cambios → Render redespliega automáticamente

**4. Verifica en los logs:**
```
Using Python version 3.12.x
Build successful 🎉
Health check HTTP escuchando en puerto 10000
Bot en ejecución.
```

> 💡 Cada `push` a `main` redespliega el bot automáticamente.

### ⚠️ Notas importantes

| Tema | Detalle |
|------|---------|
| **Python** | Fijado en **3.12** via `.python-version`. Render instala 3.14 por defecto, que rompe `asyncio`. |
| **Tipo de servicio** | Se usa **Web Service** (no Background Worker) porque el plan free no incluye workers. El bot incluye un servidor HTTP mínimo en `/health` para satisfacer el health check de Render. |
| **BOT_TOKEN** | Debe configurarse **manualmente** en el dashboard de Render. El `.env` local nunca se sube a GitHub. |

---

## ⚙️ CI con GitHub Actions

El workflow `.github/workflows/deploy.yml` verifica la sintaxis de todos los archivos Python en cada push/PR. Render gestiona el deploy de forma independiente vía webhook de GitHub.

---

## 📋 Comandos disponibles

| Comando  | Descripción                   |
|----------|-------------------------------|
| `/start` | Mensaje de bienvenida         |
| `/help`  | Muestra la lista de comandos  |
| `/ping`  | Comprueba que el bot responde |
| `/echo`  | Repite el texto enviado       |

---

## 🛠️ Agregar nuevos comandos

1. Crea o edita un archivo en `handlers/`
2. Define `async def mi_comando(update, context)`
3. Regístralo en `bot.py`:

```python
from handlers.mi_modulo import mi_comando
app.add_handler(CommandHandler("micomando", mi_comando))
```

---

## 📄 Licencia

MIT — libre de usar y modificar.
