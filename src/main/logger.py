import logging.config

import yaml

def configure_logging() -> logging.Logger:
    with open('logging.yml', 'r') as f:
        log_cfg = yaml.safe_load(f.read())
        logging.config.dictConfig(log_cfg)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    logger.info('Python Architecture Started')
    return logger

logger = configure_logging()