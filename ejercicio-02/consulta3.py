from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_,or_

from generar_base import Taller

engine = create_engine('sqlite:///basetaller.db')

Session = sessionmaker(bind=engine)
session = Session()

taller = session.query(Taller).all()

# Presentar los lenguajes de cada país.
for i in taller:
    print("Nombre: %s\t\t\tLenguaje:%s" % (i.nombrePais, i.languages))

