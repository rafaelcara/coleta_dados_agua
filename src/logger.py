###############################
# LEMBRETE
# ARQUIVO CRIADO POR IA
# NECESSÁRIO ESTUDAR O CÓDIGO
###############################

import logging
from logging.handlers import RotatingFileHandler
import os

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Configuração básica
logger = logging.getLogger("app_logger")
logger.setLevel(logging.DEBUG)  # Níveis: DEBUG, INFO, WARNING, ERROR, CRITICAL

# Formato das mensagens
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Log para arquivo com rotação
file_handler = RotatingFileHandler(
    os.path.join(LOG_DIR, "app.log"), 
    maxBytes=5*1024*1024, 
    backupCount=3,
    encoding="utf-8"
)
file_handler.setFormatter(formatter)

# Log no console
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# Adiciona os handlers
logger.addHandler(file_handler)
logger.addHandler(console_handler)
