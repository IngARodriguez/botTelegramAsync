"""
Handlers de comandos generales: /start, /help, /ping
"""

import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
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
    """Muestra los comandos disponibles como botones inline."""
    keyboard = [
        [
            InlineKeyboardButton("🏓 Ping",   callback_data="cmd_ping"),
            InlineKeyboardButton("🔁 Echo",   callback_data="cmd_echo"),
        ],
        [
            InlineKeyboardButton("👋 Start",  callback_data="cmd_start"),
            InlineKeyboardButton("❓ Ayuda",  callback_data="cmd_help"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "📋 *Comandos disponibles* — pulsa uno para usarlo:",
        parse_mode="Markdown",
        reply_markup=reply_markup,
    )


async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Responde con 'Pong!' para confirmar que el bot funciona."""
    await update.message.reply_text("🏓 Pong!")
