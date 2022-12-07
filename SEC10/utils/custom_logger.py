import logging


class Logger:

    @staticmethod
    def get_logger(loglevel=logging.DEBUG):
        logger_name = 'D:\\VIP_Selenium\\automation.log'
        logger = logging.getLogger()
        logger.setLevel(loglevel)

        fh = logging.FileHandler(logger_name,mode='a',encoding='utf8')
        fh.setLevel(loglevel)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                      datefmt='%Y/%m/%d %I:%M:%S %p')

        fh.setFormatter(formatter)

        logger.addHandler(fh)

        return logger