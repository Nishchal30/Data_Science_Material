import logging

logging.basicConfig(filename="testlog.log", level=logging.DEBUG, format='%(name)s %(levelname)s %(asctime)s %(message)s')
logging.info("this my second log file with timestamp")
