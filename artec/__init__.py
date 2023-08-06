import logging

# Root logger
logger = logging.getLogger("Artec")
logger.setLevel(logging.INFO)

# Handlers (sub-loggers)
file_handler = logging.FileHandler("log.txt", delay=True, mode="w")
console_handler = logging.StreamHandler()

# Formatters
file_handler.setFormatter(
    logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
)
console_handler.setFormatter(logging.Formatter("> %(message)s."))

# Levels
file_handler.setLevel(logging.INFO)

# Add the Handlers
logger.addHandler(file_handler)
logger.addHandler(console_handler)
