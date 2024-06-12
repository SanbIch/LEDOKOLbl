from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class TravelRequestCreate(BaseModel):
    starting_point: Optional[int] = Field(default=None)
    destination_point: Optional[int] = Field(default=None)
    starting_date: datetime
    status: Optional[int] = Field(default=None)
    route_id: Optional[int] = Field(default=None)
    ship_id: Optional[int] = Field(default=None)

class RouteCreate(BaseModel):
    start_point: str
    end_point: str
    start_date: datetime
    coords: str

class IcebreakerCreate(BaseModel):
    name: str
    ship_class: int
    velocity: int
    latitude: float
    longitude: float

class ShipCreate(BaseModel):
    name: str
    ship_class: int
    velocity: float
    latitude: float
    longitude: float
    current_icebreaker_id: Optional[int] = Field(default=None)
    route_id: Optional[int] = Field(default=None)

class LocationCreate(BaseModel):
    name: str
    latitude: float
    longitude: float

class EdgeCreate(BaseModel):
    pointA: int
    pointB: int
    length: float
    rep_id: int
    status: int