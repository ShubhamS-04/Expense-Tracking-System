import logging



def setup_logger(name, log_file = 'server.log', level = logging.DEBUG):
    #Creating the custom logger:
    logger = logging.getLogger(name)

    #Configuring the logger:
    logger.setLevel(level)
    file_handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


#To actively monitor the server log using cmd or bash : tail -f server.log