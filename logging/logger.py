import logging

logger = logging.getLogger(name="logger")
# 全局預設為warining handler setlevel需要大於等於全局的level否則不生效
logger.setLevel(logging.DEBUG)
# handler
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log', 'w', 'UTF-8')
c_handler.setLevel(logging.INFO)
f_handler.setLevel(logging.ERROR)
# formatter
c_formatter = logging.Formatter("(%(levelname)s-%(name)s)-%(message)s")
f_formatter = logging.Formatter(
    "%(asctime)s-(%(levelname)s-%(name)s)--%(message)s")
c_handler.setFormatter(c_formatter)
f_handler.setFormatter(f_formatter)
logger.addHandler(c_handler)
logger.addHandler(f_handler)


def main():
    logger.debug('this is a debug!')
    logger.info('this is a info')
    logger.warning('this is a warning')
    logger.error('this is a error')
    logger.critical('this is a critical')


if __name__ == "__main__":
    main()
