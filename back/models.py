from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

DATABASE_URL = "sqlite:///./nsr.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class TravelRequest(Base):
    __tablename__ = "travel_requests"
    id = Column(Integer, primary_key=True, index=True)
    starting_point = Column(Integer)
    destination_point = Column(Integer)
    starting_date = Column(DateTime)
    status = Column(Integer)
    route_id = Column(Integer, ForeignKey('routes.id'))
    ship_id = Column(Integer, ForeignKey('ships.id'))

    ship = relationship("Ship")
    route = relationship("Route")

class Route(Base):
    __tablename__ = "routes"
    id = Column(Integer, primary_key=True, index=True)
    start_point = Column(Integer)
    end_point = Column(Integer)
    start_date = Column(DateTime)
    coords = Column(String)

class Icebreaker(Base):
    __tablename__ = "icebreakers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    ship_class = Column(Integer)
    velocity = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)

class Ship(Base):
    __tablename__ = "ships"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    ship_class = Column(Integer)
    velocity = Column(Float)
    latitude = Column(Float)
    longitude = Column(Float)
    current_icebreaker_id = Column(Integer, ForeignKey('icebreakers.id'))
    route_id = Column(Integer, ForeignKey('routes.id'))
    
    current_icebreaker = relationship("Icebreaker")
    route = relationship("Route")

class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    latitude = Column(Float)
    longitude = Column(Float)

class Edge(Base):
    __tablename__ = "edges"
    id = Column(Integer, primary_key=True, index=True)
    pointA = Column(Integer)
    pointB = Column(Integer)
    length = Column(Float)
    rep_id = Column(Integer)
    status = Column(Integer)

Base.metadata.create_all(bind=engine)
