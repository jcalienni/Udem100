import logging

# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG,filename='convert.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

# logging.debug("Esto es un debug")
# logging.warning("esto es un warning")
# logging.info("esto es info")
# logging.error("Aca hay un error")
# logging.critical("Ojo que esta critico")

def convert_number(number,base):
    logging.info("I am entering to the convert number function")
    logging.debug("Number: " + str(number))
    logging.debug('Base: ' + str(base))
    try:
        if base == 2:
            return bin(number)
        if base == 8:
            return oct(number)
        if base == 16:
            return hex(number)
        logging.error('This is an incorrect base, we will add it in the future')
        return("incorrect base selected")
    except:
        logging.critical('Cant perform operation')
        return('CRITICAL ERROR')

print(convert_number(2000,2))
print(convert_number(1500,8))
print(convert_number(250,16))
print(convert_number(120,65))
print(convert_number('Pepe',2))