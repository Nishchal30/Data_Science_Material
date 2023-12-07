import logging
logging.basicConfig(filename="testlog1.log", level=logging.INFO, format='%(name)s %(levelname)s %(asctime)s %(message)s')


def division(a, b):
    logging.info("the numbers entered by user are %s and %s", a, b)
  
    try:
        logging.info("we have entered into the function")
        div = a / b
        logging.info("we have completed the division")
        logging.info("the result of programe is %s", div)
        return div
        

    except Exception as e:
        logging.exception(e)
        

print(division(4,0))

