from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
import uvicorn

from models import *
from create_classes import *

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173"
    "https://ledokolbl.vercel.app/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/ice_data")
async def get_ice_data():
    return FileResponse("data/new_data.json")


@app.get("/graph_data")
async def get_graph_data():
    return FileResponse("data/graph.csv")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/route_requests/add/")
def create_travel_request(
    travel_request: TravelRequestCreate, db: Session = Depends(get_db)
):
    db_travel_request = TravelRequest(
        starting_point=travel_request.starting_point,
        destination_point=travel_request.destination_point,
        starting_date=travel_request.starting_date,
        status=0,
        ship_id=travel_request.ship_id,
    )
    db.add(db_travel_request)
    db.commit()
    db.refresh(db_travel_request)
    return db_travel_request


@app.get("/route_requests/")
def get_all_travel_requests(db: Session = Depends(get_db)):
    travel_requests = db.query(TravelRequest).all()
    return travel_requests


@app.get("/icebreakers/")
def get_all_icebreakers(db: Session = Depends(get_db)):
    icebreakers = db.query(Icebreaker).all()
    return icebreakers


@app.get("/routes/")
def get_all_routes(db: Session = Depends(get_db)):
    routes = db.query(Route).all()
    return routes


@app.get("/ships/")
def get_all_routes(db: Session = Depends(get_db)):
    ships = db.query(Ship).all()
    return ships


@app.get("/routes/{id}")
def get_route_by_id(id: int, db: Session = Depends(get_db)):
    route = db.query(Route).filter(Route.id == id).first()
    if route is None:
        raise HTTPException(status_code=404, detail="Route not found")
    return route


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8123)
