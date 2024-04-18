import logging

def test_print_logs():
    LOGGER=logging.getLogger(__name__)
    LOGGER.error("This is error")
    LOGGER.info("This is info")
    LOGGER.warning("This is warning")
    LOGGER.critical("This is crit")
