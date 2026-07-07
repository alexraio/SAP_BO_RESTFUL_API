import os
import logging
import datetime
import subprocess
import csv
import json

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

def export_to_csv(data, filename, fieldnames):
    """
    Exports a list of dictionaries to a CSV file.
    """
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        logging.info(f"Successfully exported data to CSV: {filename}")
        return True
    except Exception as e:
        logging.error(f"Failed to export data to CSV {filename}: {e}")
        return False

def export_to_json(data, filename):
    """
    Exports data to a JSON file.
    """
    try:
        with open(filename, mode='w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        logging.info(f"Successfully exported data to JSON: {filename}")
        return True
    except Exception as e:
        logging.error(f"Failed to export data to JSON {filename}: {e}")
        return False
