import inspect
import logging


class loggenreter:
    @staticmethod
    def loggen():
        loggername = inspect.stack() [3][1]
        logger = logging.getLogger(loggername)
        file = logging.FileHandler("C:\\Users\\Jyoti\\PycharmProjects\\pytest_nopcommProject\\Logs\\nopcomm.log")
        format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s")
        file.setFormatter(format)
        logger.addHandler(file)
        logger.setLevel(logging.INFO)
        return logger


# get log--> logging.getLogger()
# logfile --> path and name
# format --> logs format
# setFormatter -- > link file and format
# and handler --> maintenance -- >log file