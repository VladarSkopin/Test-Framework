import logging
from logging import Logger


class CustomLogger:

    @staticmethod
    def get_logger() -> Logger:
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

        '''
        if logger.hasHandlers():
            logger.handlers.clear()
        '''

        logging.basicConfig(filename=r'D:\GitHubProjects\Test-Framework\logs\test_log.log',
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        logger: Logger = logging.getLogger('alex_logger')
        logger.setLevel(logging.INFO)
        return logger
