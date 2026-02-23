"""
Punto de entrada principal del bot Telegram asíncrono.
Incluye un servidor HTTP mínimo para el health check de Render (plan free).

Uso:
    python bot.py

Variables de entorno requeridas:
    BOT_TOKEN  – Token obtenido de @BotFather
"""

import logging
import os
import sys
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

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


# ── Health check HTTP (necesario para Render plan free) ────────────────────────
class HealthHandler(BaseHTTPRequestHandler):
    """Servidor HTTP mínimo que responde al health check de Render."""

    def do_GET(self):  # noqa: N802
        if self.path == "/health":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):  # noqa: A002
        # Silencia los logs del servidor HTTP para no saturar la consola
        pass


def run_health_server() -> None:
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), HealthHandler)
    logger.info("Health check HTTP escuchando en puerto %d", port)
    server.serve_forever()


# ── Post-init ──────────────────────────────────────────────────────────────────
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


# ── Main ───────────────────────────────────────────────────────────────────────
def main() -> None:
    """Construye la aplicación y arranca el polling."""
    logger.info("Iniciando bot…")

    # Arranca el servidor de health check en un hilo en segundo plano
    health_thread = threading.Thread(target=run_health_server, daemon=True)
    health_thread.start()

    app = (
        Application.builder()
        .token(config.BOT_TOKEN)
        .post_init(post_init)
        .build()
    )

    # ── Registro de handlers ───────────────────────────────────────────────────
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("ping", ping))
    app.add_handler(CommandHandler("echo", echo))

    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text)
    )
    app.add_handler(MessageHandler(filters.COMMAND, unknown_command))

    # ── Inicio del polling ─────────────────────────────────────────────────────
    logger.info("Bot en ejecución. Presiona Ctrl+C para detener.")
    app.run_polling(allowed_updates=["message", "callback_query"])


if __name__ == "__main__":
    main()
