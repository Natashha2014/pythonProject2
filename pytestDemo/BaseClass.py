import logging

import pytest

@pytest.mark.usefixtures("setup")
class BaseClass:
    def get_logger(self):
        log = logging.getLogger(__name__)
        filehandler = logging.FileHandler("logs.log")
        log.addHandler(filehandler)
        set_format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(set_format)
        log.setLevel(logging.ERROR)
        log.warning("Warning statement")
        log.debug("Debug statement")
        log.info("Info statement")
        log.info("Second info statement")
        log.debug("Second debug statement")
        log.debug("Debug statement")
        log.info("Info statement")
        log.error("Error statement")
        log.critical("Critical statement")
        return log