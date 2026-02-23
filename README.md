# botTelegramAsync 🤖

Bot de Telegram **asíncrono** construido con [python-telegram-bot v21](https://python-telegram-bot.org/), listo para desplegar desde GitHub Actions.

---

## 📁 Estructura del proyecto

```
botTelegramAsync/
├── bot.py                   # Punto de entrada principal
├── config.py                # Carga de variables de entorno
├── requirements.txt         # Dependencias Python
├── .env.example             # Plantilla de variables de entorno
├── .gitignore
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

## 🚀 Despliegue con GitHub Actions

El workflow `.github/workflows/deploy.yml` se ejecuta automáticamente al hacer **push a `main`** y realiza:

1. **Lint** – Verifica que todos los archivos Python compilan.
2. **Smoke test** – Arranca el bot 10 segundos para detectar errores de inicio.
3. **Deploy SSH** *(opcional, descomenta en el workflow)* – Conecta a tu servidor por SSH y reinicia el bot.

### Configurar el Secret `BOT_TOKEN` en GitHub

1. Ve a tu repositorio → **Settings** → **Secrets and variables** → **Actions**
2. Haz clic en **New repository secret**
3. Nombre: `BOT_TOKEN` → Valor: tu token de @BotFather
4. *(Opcional)* Agrega `SSH_HOST`, `SSH_USER`, `SSH_PRIVATE_KEY` si usas deploy SSH.

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
