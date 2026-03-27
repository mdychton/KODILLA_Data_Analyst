import sys

def customized_hello(first_name, last_name, gender_prefix='Mr'):                                #tutaj cwiczymy podawanie argumentow do programu, czyli do funkcji customized_hello, w sposob bezposredni, czyli przez argumenty programu, a nie przez input, czyli bezposrednio w momencie wywolania programu, a nie w trakcie jego dzialania - czyli przez wywolanie w terminalu python argumentyProgramu.py John Cleese Mr     
    print("Hello %s %s %s!" % (gender_prefix, first_name, last_name))

if __name__ == "__main__":
    if len(sys.argv) < 4:
        exit(1)
    first_name = sys.argv[1]
    last_name = sys.argv[2]
    gender_prefix = sys.argv[3]
    customized_hello(first_name, last_name, gender_prefix)