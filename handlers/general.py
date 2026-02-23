"""
Handlers de comandos generales: /start, /help, /ping
"""

import logging
from telegram import Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Responde al comando /start con un mensaje de bienvenida."""
    user = update.effective_user
    await update.message.reply_html(
        f"👋 ¡Hola, {user.mention_html()}!\n\n"
        "Soy tu bot asíncrono. Usa /help para ver los comandos disponibles."
    )
    logger.info("Usuario %s ejecutó /start", user.id)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Muestra la lista de comandos disponibles."""
    text = (
        "📋 <b>Comandos disponibles</b>\n\n"
        "/start – Mensaje de bienvenida\n"
        "/help  – Esta ayuda\n"
        "/ping  – Comprueba que el bot está vivo\n"
        "/echo  – Repite el texto que escribas\n"
    )
    await update.message.reply_html(text)


async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Responde con 'Pong!' para confirmar que el bot funciona."""
    await update.message.reply_text("🏓 Pong!")
