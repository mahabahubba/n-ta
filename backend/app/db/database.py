# The create_engine function is a primary way to crate an engine instance which
# Acts as a central source of connectivity to a specific data base
from sqlalchemy import create_engine

# Session maker is another standardied tool that allows you to have the same configuration parameters
# Declarative base connects the Object orientated structure with the relational database.
from sqlalchemy.orm import sessionmaker, declarative_base

# Make a declaration of the db url we are going to connect with.
DATABASE_URL = "sqlite:///./n_ta.db"

# connect args allows for the connection with the database. You can also customize the way you 
# connect to the database..
# the check same thread allows for the database to handle multi threading
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}


# SessionLocal creates a session factory called SessionLocal
# Sessionmaker is a function that create a configured factory for Session's
# objects, essentially a blueprint for making a new session
# Autocommit false means changes arent automatically committed after each operation
# Thus you must recall session.commit to save them permanently to the database
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

# Creates a base class for defining the database using Python class.
Base = declarative_base()