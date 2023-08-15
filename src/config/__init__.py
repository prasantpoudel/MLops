import pymongo
import json
import os
import sys
from dataclasses import dataclass

TARGET_COLUMN='class'

@dataclass
class EnviromentalVariable(object):
    mongodb_url:str="mongodb+srv://prasant:1234@cluster0.z1rv7ep.mongodb.net/"

env_var=EnviromentalVariable()
mongo_client=pymongo.MongoClient(env_var.mongodb_url)