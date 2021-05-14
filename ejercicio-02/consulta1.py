from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_,or_

from generar_base import Taller

engine = create_engine('sqlite:///basetaller.db')

Session = sessionmaker(bind=engine)
session = Session()

# Presentar todos los países del continente americano
consulta1 = session.query(Taller).filter(Taller.contienente=="SA").order_by(Taller.nombrePais).all()

print(consulta1)