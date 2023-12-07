import logging
logging.basicConfig(filename="test.log", level=logging.INFO)
logging.info("this is my first code for loging")
logging.warning("this is my warning message")
logging.error("this is the error message")

# There are 5 level of logs inside the python
# 1) DEBUG  - priority no 10
# 2) Info - priority no 20
# 3) Warning - priority no 3
# 4) Error / Exception - priority no 40  (only difference is error logs only error message but exception logs whole exception)
# 5) Critical - priority no 50

logging.shutdown() # shutdown the logging after this