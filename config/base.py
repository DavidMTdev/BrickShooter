from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# create an engine
Engine = create_engine('mysql+pymysql://root:@localhost/brickShooter', echo=True)

# create a configured "Session" class
Session = sessionmaker(bind=Engine)

session = Session()

# create a configured "Base" class
Base = declarative_base()
