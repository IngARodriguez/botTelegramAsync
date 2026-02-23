"""
Configuración centralizada del bot.
Las variables sensibles se cargan desde variables de entorno.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# ── TOKEN ──────────────────────────────────────────────────────────────────────
BOT_TOKEN: str = os.environ["BOT_TOKEN"]

# ── CONFIGURACIÓN GENERAL ──────────────────────────────────────────────────────
# ID de un chat/grupo de administradores (opcional)
ADMIN_CHAT_ID: int | None = (
    int(os.environ["ADMIN_CHAT_ID"]) if os.environ.get("ADMIN_CHAT_ID") else None
)

# Nivel de log: DEBUG | INFO | WARNING | ERROR
LOG_LEVEL: str = os.environ.get("LOG_LEVEL", "INFO").upper()
