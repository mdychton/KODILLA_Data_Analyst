import logging
import sys

"""to jest przyklad wygenerowany prezz ChATa"""

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s | %(levelname)s | %(name)s | %(message)s', filename="logfileChat.log"
)

def print_maturity(age):
    logging.debug("Entered print_maturity with age=%s", age)

    if age < 0:
        logging.error("Invalid age provided: %s", age)
        return

    if age >= 18:
        logging.info("You are an adult")

        if age > 100:
            logging.warning("Unusually high age: %s", age)

    else:
        logging.info("You are a kiddo!")

        if age < 5:
            logging.warning("Very young age: %s", age)


if __name__ == "__main__":
    logging.debug("Program started")
    logging.debug("All parameters: %s", sys.argv[1:])

    if len(sys.argv) < 2:
        logging.critical("No age parameter provided! Program cannot continue.")
        sys.exit(1)

    try:
        age = int(sys.argv[1])
        logging.debug("Parsed age: %s", age)

    except ValueError:
        logging.exception("Failed to convert age to int: %s", sys.argv[1])
        sys.exit(1)

    print_maturity(age)

    logging.debug("Program finished successfully")