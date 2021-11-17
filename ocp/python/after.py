import sys
import time


class Logger:
    def __init__(self):
        self.prefix = time.strftime('%Y-%b-%d %H:%M:%S', time.localtime())
        
    def log(self, message):
        sys.stderr.write(f"{self.prefix} --> {message}\n")


class CustomerLogger(Logger):
    # при необходимости изменить формат вывода времени создается кастомный класс и переопределяется необходимое значение
    def __init__(self):
        super().__init__()
        self.prefix = time.strftime('%Y-%b-%d', time.localtime())
 

logger = Logger()
logger.log('An error has happened!')

c_logger = CustomerLogger()
c_logger.log('Custom logged message!')
