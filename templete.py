"""
        This will Create all the necessary folder and files
"""

import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%[message]s:')

project_name= "NLP"

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/components/__init__.py",
    f"src/utils/__init__.py",
    f"src/exception/__init__.py",
    f"src/utils/common.py",
    f"src/logging/__init__.py",
    f"src/config/__init__.py",
    f"src/config/configuration.py",
    f"src/pipeline/__init__.py",
    f"src/entity/__init__.py",
    f"src/constants/__init__.py",
    f"data-to-mongo/__init__.py",
    f"data-to-mongo/dump_mongo.py"
    "config/config.yaml",
    "params.yml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename= os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating Directory:{filedir} for the file{filename}")
     
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
        logging.info(f"Creating File:{filepath} for the file{filename}")

    else:
        logging.info(f"{filename} is already exists")

     
         