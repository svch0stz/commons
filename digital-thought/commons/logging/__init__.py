import logging
import logging.config
import os
from datetime import datetime

import yaml
from colorlog import ColoredFormatter

logging_configuration_file = './config/loggingConfig.yaml'
DEFAULT_FORMATTER = '%(log_color)s%(asctime)s - %(levelname)-8s - %(processName)s.%(process)d - %(threadName)s.%(thread)d - %(module)s.%(funcName)s.%(lineno)-3d - %(message)s%(reset)s'
DEFAULT_ELASTIC_FORMATTER = 'ELASTIC: %(log_color)s%(asctime)s - %(levelname)-8s - %(processName)s.%(process)d - %(threadName)s.%(thread)d - %(module)s.%(funcName)s.%(lineno)-3d - %(message)s%(reset)s'


def init(app_name, elastic_server=None, elastic_port=None, elastic_api_key=None, elastic=False, index_prefix=None):
    with open(logging_configuration_file, 'r') as logging_config_file:
        logging_config = yaml.safe_load(logging_config_file)
        log_folder = './logs/{}'.format(datetime.now().strftime("%Y%m%d_%H%M%S"))
        if not os.path.exists('./logs'):
            os.mkdir('./logs')
        if not os.path.exists(log_folder):
            os.mkdir(log_folder)

        formatter = ColoredFormatter(DEFAULT_FORMATTER)

        console_stream = logging.StreamHandler()
        console_stream.setLevel(logging.DEBUG)
        console_stream.setFormatter(formatter)
        console_stream.name = 'console_ALL'

        if not elastic:

            logging_config['handlers']['logfile_ALL']['filename'] = '{}/info-{}'.format(log_folder, app_name)
            logging_config['handlers']['logfile_ERR']['filename'] = '{}/error-{}'.format(log_folder, app_name)
            logging_config['handlers']['logfile_ELASTIC']['filename'] = '{}/elastic-{}'.format(log_folder, app_name)
            logging.config.dictConfig(logging_config)
            logging.getLogger().addHandler(console_stream)
            logging.getLogger("defaultLogger").addHandler(console_stream)
        else:
            if elastic_server is not None:
                logging_config['handlers']['logfile_ALL']['server'] = elastic_server
            if elastic_port is not None:
                logging_config['handlers']['logfile_ALL']['port'] = elastic_port
            if elastic_api_key is not None:
                logging_config['handlers']['logfile_ALL']['api_key'] = elastic_api_key
            if index_prefix is not None:
                logging_config['handlers']['logfile_ALL']['prefix'] = index_prefix

            formatter = ColoredFormatter(DEFAULT_ELASTIC_FORMATTER)

            stream = logging.StreamHandler()
            stream.setLevel(logging.DEBUG)
            stream.setFormatter(formatter)
            stream.name = 'console_ELASTIC'

            logging.config.dictConfig(logging_config)
            logging.getLogger('elastic').addHandler(stream)

        logging.getLogger('console').addHandler(console_stream)
        logging.getLogger('console').debug('Logging configuration read from: {}'.format(logging_configuration_file))
