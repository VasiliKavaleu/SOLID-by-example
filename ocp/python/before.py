import sys
import time


class Logger:
    def log(self, message):
        current_time = time.localtime()
        #  чтобы изменить формат вывода времени, необходимо модифицировать класс напрямую,
        #  в случае если он используется в иных местах приложения, может получится что функционал не будет отрабатывать 
        sys.stderr.write(f"{time.strftime('%Y-%b-%d %H:%M:%S', current_time)} --> {message}\n")


logger = Logger()
logger.log('An error has happened!')
