# loggin

import logging

logging.basicConfig(
    filename="info.log",
    level=logging.DEBUG,
    format="%(levelname)s %(asctime)s: %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S"
)


logger = logging.StreamHandler()
logging.getLogger("").addHandler(logger)

logging.debug("Isso é uma msg de debug")
logging.info("Isso é uma msg de info")
logging.warning("Isso é uma msg de debug warning")
logging.error("Isso é uma msg de debug error")
logging.critical("Isso é uma msg de debug critical")

