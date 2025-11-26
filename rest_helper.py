import os
import logging
import datetime
import subprocess

# Define a logging function to log messages to a file
def setup_logging(log_dir="logs", log_name="Std_logName"):
    """Sets up the logging configuration to an external log file."""
    # Create the log directory if it doesn't exist
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = os.path.join(log_dir, f"{log_name}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Script started")


# Function to execute command
def execute_cmd(thecmd):
    """
    Runs a script and captures stdout, stderr, and the return code.

    Args:
        thecmd: The command to execute.

    Returns:
        A dictionary containing the stdout, stderr, and return code.  Returns None if the command is not found.
    """

    try:
        process = subprocess.run(thecmd, capture_output=True, text=True, check=False)
        return {
            "stdout": process.stdout,
            "stderr": process.stderr,
            "returncode": process.returncode
        }
    except FileNotFoundError:
        logging.error("Error: Command not found. Ensure it's installed and in your PATH.")
        return None