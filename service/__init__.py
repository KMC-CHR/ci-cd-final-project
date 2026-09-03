"""
Service Package
"""
from flask import Flask

app = Flask(__name__)

# Fallback logger for local development
try:
    from service.common import log_handlers
    log_handlers.init_logging(app, "gunicorn.error")
except Exception:
    pass

from service import routes  # pylint: disable=wrong-import-position,cyclic-import

app.logger.info(70 * "*")
app.logger.info("  S E R V I C E   R U N N I N G  ".center(70, "*"))
app.logger.info(70 * "*")
