import logging                                              #ten kod daje wynik przy wpisaniu python testlog.py w terminalu, ale tez w pliku app.log

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')

# log do pliku
file_handler = logging.FileHandler('app.log')
file_handler.setFormatter(formatter)

# log do konsoli
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.info("Działa i tu i tu")