    
import os                           # Provides functions for interacting with the operating system (files, directories, paths)
from pathlib import Path            # Offers an object-oriented approach to handling filesystem paths
import logging                      # Used for logging informational messages during execution

# Configure the logging system to display INFO-level messages with timestamps
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s]: %(message)s:'
)

project_name = "datascience"        # Name of the main project/package

# List of files and directories to be created for the project structure
list_of_files = [
    ".gthub/workflows/.gitkeep",                     # Keeps the workflows directory tracked by Git
    f"src/{project_name}/__init__.py",               # Marks the main project directory as a Python package and import from it
    f"src/{project_name}/components/__init__.py",    # Initializes the components subpackage
    f"src/{project_name}/utils/__init__.py",         # Initializes the utils subpackage
    f"src/{project_name}/utils/common.py",           # Common utility/helper functions
    f"src/{project_name}/config/__init__.py",        # Initializes the config subpackage
    f"src/{project_name}/config/configuration.py",   # Handles configuration logic
    f"src/{project_name}/pipeline/__init__.py",      # Initializes the pipeline subpackage
    f"src/{project_name}/entity/__init__.py",        # nitializes the entitIy subpackage
    f"src/{project_name}/entity/config_entity.py",   # Configuration-related data entities
    f"src/{project_name}/constants/__init__.py",     # Initializes constants subpackage
    "config/config.yaml",                            # Application configuration file
    "params.yaml",                                   # Parameters for experiments or pipelines
    "schema.yaml",                                   # Data schema definition
    "main.py",                                       # Main execution script
    "Dockerfile",                                    # Docker configuration for containerization
    "setup.py",                                      # Package setup and installation script
    "research/research.ipynb",                       # Jupyter notebook for research and experiments
    "templates/index.html",                          # HTML template for web applications
    "app.py"                                         # Entry point for application (e.g., Flask app)
]

# Iterate over each file path in the list
for filepath in list_of_files:
    filepath = Path(filepath)                        # Convert string path to Path object
    filedir, filename = os.path.split(filepath)      # Split the directory path and file name

    # Create the directory if it does not already exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)          # Create directories recursively if needed
        logging.info(f"Creating directory {filedir} for the file : {filename}")

    # Create the file if it does not exist or if it exists but is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:                # Open the file in write mode (creates file if missing)
            pass                                     # No content written; file is created as empty
            logging.info(f"Creating empty file: {filepath}")

    # Log a message if the file already exists and is not empty
    else:
        logging.info(f"{filename} is already exists")