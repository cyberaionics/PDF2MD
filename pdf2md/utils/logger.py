import logging


def get_logger(
    name="pdf2md"
):

    logger = logging.getLogger(
        name
    )

    if logger.handlers:
        return logger

    logger.setLevel(
        logging.INFO
    )

    formatter = logging.Formatter(
        "[%(levelname)s] %(message)s"
    )

    handler = logging.StreamHandler()

    handler.setFormatter(
        formatter
    )

    logger.addHandler(
        handler
    )

    return logger