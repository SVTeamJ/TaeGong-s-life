from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import socket

import os


SQLALCHEMY_DATABASE_URL = "mysql+pymysql://taegong:taegong@172.17.0.1:3306/taegong"

try:
    hostname = socket.gethostname()
    # Get the IP address
    ip_address = socket.gethostbyname(hostname)
    if ip_address == "127.0.0.1":
        print("Running on localhost.")
        SQLALCHEMY_DATABASE_URL = "mysql+pymysql://taegong:taegong@localhost:3306/taegong"
    else:
        print("the docker container ip is:",ip_address)
except:
    print("Could not determine if running on localhost or in a Docker container.")




engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    # connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()
