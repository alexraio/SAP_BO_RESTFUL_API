# This function will log messages with a specified log level and append them to the specified file.
# +You can customize the log level, log format, and output file as needed.

# Example usage:
# log_and_write_output('output.log', 'This is an info message.')
# log_and_write_output('output.log', 'This is a warning message.', log_level=logging.WARNING)
# log_and_write_output('output.log', 'This is an error message.', log_level=logging.ERROR)

import logging

def log_and_write_output(log_file, message, log_level=logging.INFO):
    # Set up the logger
    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)

    # Set up file handler to write logs to a file
    file_handler = logging.FileHandler(log_file, mode='a')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Check if the logger already has handlers, if not, add the file handler
    if not logger.hasHandlers():
        logger.addHandler(file_handler)

    # Log the message
    if log_level == logging.DEBUG:
        logger.debug(message)
    elif log_level == logging.INFO:
        logger.info(message)
    elif log_level == logging.WARNING:
        logger.warning(message)
    elif log_level == logging.ERROR:
        logger.error(message)
    elif log_level == logging.CRITICAL:
        logger.critical(message)

    # Close the file handler to release resources
    file_handler.close()


