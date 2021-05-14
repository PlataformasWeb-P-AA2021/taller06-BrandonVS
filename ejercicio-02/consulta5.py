from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_,or_

from generar_base import Taller

engine = create_engine('sqlite:///basetaller.db')

Session = sessionmaker(bind=engine)
session = Session()

# Presentar todos los países que tengan en su cadena de nombre de país "uador" o en su cadena de capital "ito".
consulta5 = session.query(Taller).filter(or_(Taller.nombrePais.like('%uador%'), Taller.capital.like('%ito%'))).all()

print(consulta5)