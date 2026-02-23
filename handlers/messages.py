"""
Handlers de mensajes de texto: echo, etc.
"""

import logging
from telegram import Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Repite el mensaje recibido (útil para pruebas)."""
    text = " ".join(context.args) if context.args else None
    if not text:
        await update.message.reply_text("✏️ Uso: /echo <texto>")
        return
    await update.message.reply_text(f"🔁 {text}")
    logger.debug("Echo para usuario %s: %s", update.effective_user.id, text)


async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Informa que el comando no existe."""
    await update.message.reply_text(
        "❓ Comando desconocido. Usa /help para ver los disponibles."
    )


async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Maneja mensajes de texto que no son comandos."""
    # Aquí puedes implementar lógica conversacional o NLP
    await update.message.reply_text(
        "💬 Recibí tu mensaje. Usa /help para ver los comandos disponibles."
    )
