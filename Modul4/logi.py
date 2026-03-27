import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")

def print_maturity(age):
    if age >= 18:
        logging.info("You are an adult")
    else:
        logging.info("You are a kiddo!")

if __name__ == "__main__":
    logging.debug("The program was called with this parameters %s" % sys.argv[1:])
    logging.debug("First parameter is %s" % sys.argv[1])
    age = int(sys.argv[1])
    print_maturity(age)
"""print(f"The program was called with this parameters {sys.argv[1:]}")""" #wersja z f-stringiem, czyli nowym stylem formatowania tekstu, ale w tym przypadku nie jest on potrzebny, bo nie ma tu zadnych dodatkowych operacji na tekście, tylko zwykłe wstawienie wartości do tekstu, więc stary styl jest tu równie dobry, a nawet lepszy, bo jest bardziej czytelny i mniej skomplikowany.   