from sqlalchemy import create_engine

engine = create_engine('sqlite:///basetaller.db')

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String


class Taller(Base):
    __tablename__ = "Taller"

    id = Column(Integer, primary_key=True)
    nombrePais = Column(String)
    capital = Column(String)
    contienente = Column(String)
    dial = Column(Integer)
    geonameId = Column(Integer)
    itu = Column(String)
    languages = Column(String)
    isIndependent = Column(String)

    def __repr__(self):
        return "Taller: nombre:%s capital:%s continente:%s dial:%s geonameID:%s itu:%s lennguajes:%s independiente:%s\n" % (
            self.nombrePais,
            self.capital,
            self.contienente,
            self.dial,
            self.geonameId,
            self.itu,
            self.languages,
            self.isIndependent)


Base.metadata.create_all(engine)
