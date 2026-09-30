import logging
import os


LOG_FOLDER = "logs"
LOG_FILE = os.path.join(LOG_FOLDER, "securedesk.log")


def setup_logger():
    os.makedirs(LOG_FOLDER, exist_ok=True)

    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8"
    )


def log_info(message):
    logging.info(message)


def log_warning(message):
    logging.warning(message)


def log_error(message):
    logging.error(message)