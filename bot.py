"""
Punto de entrada principal del bot Telegram asíncrono.

Uso:
    python bot.py

Variables de entorno requeridas:
    BOT_TOKEN  – Token obtenido de @BotFather
"""

import logging
import sys

from telegram import BotCommand
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

import config
from handlers.general import help_command, ping, start
from handlers.messages import echo, handle_text, unknown_command

# ── Logging ────────────────────────────────────────────────────────────────────
logging.basicConfig(
    format="%(asctime)s | %(levelname)-8s | %(name)s – %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=getattr(logging, config.LOG_LEVEL, logging.INFO),
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)


async def post_init(application: Application) -> None:
    """Configura los comandos visibles en el menú de Telegram."""
    commands = [
        BotCommand("start", "Mensaje de bienvenida"),
        BotCommand("help", "Muestra esta ayuda"),
        BotCommand("ping", "Comprueba que el bot está vivo"),
        BotCommand("echo", "Repite el texto enviado"),
    ]
    await application.bot.set_my_commands(commands)
    logger.info("Comandos del bot registrados correctamente.")


def main() -> None:
    """Construye la aplicación y arranca el polling."""
    logger.info("Iniciando bot…")

    app = (
        Application.builder()
        .token(config.BOT_TOKEN)
        .post_init(post_init)
        .build()
    )

    # ── Registro de handlers ───────────────────────────────────────────────────
    # Comandos generales
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("ping", ping))
    app.add_handler(CommandHandler("echo", echo))

    # Mensajes de texto libres (sin comando)
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text)
    )

    # Comandos no reconocidos (siempre al final)
    app.add_handler(MessageHandler(filters.COMMAND, unknown_command))

    # ── Inicio del polling ─────────────────────────────────────────────────────
    logger.info("Bot en ejecución. Presiona Ctrl+C para detener.")
    app.run_polling(allowed_updates=["message", "callback_query"])


if __name__ == "__main__":
    main()
