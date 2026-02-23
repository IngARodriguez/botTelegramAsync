"""
Handlers para los botones inline del menú /help.
Cada callback_data corresponde a un botón definido en general.py.
"""

import logging
from telegram import Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Responde a los botones inline del menú /help."""
    query = update.callback_query
    await query.answer()  # Quita el "reloj" del botón en Telegram

    responses = {
        "cmd_ping":  "🏓 Pong!",
        "cmd_echo":  "🔁 Usa el comando así:\n/echo Hola mundo",
        "cmd_start": (
            "👋 Soy tu bot asíncrono construido con python-telegram-bot v21.\n"
            "Usa /help para ver todos los comandos."
        ),
        "cmd_help":  (
            "📋 *Comandos disponibles:*\n"
            "/start – Bienvenida\n"
            "/help  – Este menú\n"
            "/ping  – Comprueba que el bot está vivo\n"
            "/echo  – Repite el texto enviado"
        ),
    }

    text = responses.get(query.data, "❓ Botón desconocido.")
    await query.message.reply_text(text, parse_mode="Markdown")
    logger.debug("Botón '%s' pulsado por usuario %s", query.data, query.from_user.id)
