import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name="textSummarizer"

list_of_files=[
    ".github/workflows/.gitkeep/",
    f"src/{project_name}/__init__.py",  # contains all the local packages
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/_pipeline/__init__.py"
    f"src/{project_name}/entity/__init__.py"
    f"src/{project_name}/constants/ __init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)    #sep between the making of the file directory  and making of the file name

    if filedir !="":    # if file  dir not empty 
        os.makedirs(filedir,exist_ok="True")
        logging.info(f"creating direc:{filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)== 0): #getsize seems  how many characters in the file
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists ")



