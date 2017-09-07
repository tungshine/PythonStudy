# __author: TungShine
# __date: 2017/9/1

import logging

# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S',
#                     filename='test.log',
#                     filemode='a')
#
# logging.critical('critical message')
# logging.info('info message')
# logging.debug('debug message')
# logging.warning('warning message')
# logging.error('error message')


# 用于自定义日志
logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('test.log', encoding='utf8')  # 创建一个handler,用于写入日志文件
sh = logging.StreamHandler()  # 再创建一个handler,用于输出到控制台

formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s- %(message)s')
formatter.datefmt = '%Y-%m-%d %H:%M:%S'  # %B是英文的月份%b是英文月份简写 %

fh.setFormatter(formatter)
sh.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(sh)

logger.debug('logger debug message')
logger.error('logger error message')
logger.info('logger info message')
logger.warning('logger warning message')
