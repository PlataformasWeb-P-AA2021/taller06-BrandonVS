from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_,or_

from generar_base import Taller

engine = create_engine('sqlite:///basetaller.db')

Session = sessionmaker(bind=engine)
session = Session()

# Presentar los países ordenados por la capital, siempre que el país pertenezca a Europa.
consulta4 = session.query(Taller).filter(Taller.contienente=='EU').order_by(Taller.capital).all()

print(consulta4)