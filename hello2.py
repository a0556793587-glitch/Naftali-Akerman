import logging
logging.basicConfig(level=logging.INFO,format="%(asctime)s %(levelname)s %(message)s",filename='logging.log')


list = [12,23,34,45,56,67,"naftali","yoni",67]
total = 0
for item in list:
    try:
        total += item
    except:
        logging.exception("must be numbers")
print(total)

