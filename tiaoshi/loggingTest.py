import logging

logging.basicConfig(filename="logger.log" ,level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


logger.info('This is a log info')

s = '0'
n = int(s)
logger.info('n = %d' % n)
print(10 / n)