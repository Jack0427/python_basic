"""
重要性 ->
debug(),info(),warning(),error(),critical()
"""
import logging

# print(logging.BASIC_FORMAT) 找到format格式  python文黨有許多內容
format = "%(asctime)s-(%(levelname)s-%(name)s)%(message)s"
# debug之上 會打印出來 預設 warning filename 預設為a 不刪除加內容
logging.basicConfig(level='DEBUG', filename='test.log',
                    filemode='w', format=format)

logging.debug('this is a debug!')
logging.info('this is a info')
logging.warning('this is a warning')
logging.error('this is a error')
logging.critical('this is a critical')
