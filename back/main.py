from fastapi import FastAPI, Depends, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from sqlalchemy.orm import Session
import uvicorn
import pandas as pd
import numpy as np

from models import *
from create_classes import *
from algo import *

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
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

@app.get("/routes/{id}")
async def get_route_data(id: int):
    return FileResponse(f"data/route_{id}.json")


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

@app.get("/locations/")
def get_all_locations(db: Session = Depends(get_db)):
    locations = db.query(Location).all()
    return locations

@app.get("/edges/")
def get_all_edges(db: Session = Depends(get_db)):
    edges = db.query(Edge).all()
    return edges


@app.post("/ice/")
def upload_file(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        with open('data/ice_excel.xlsx', 'wb') as f:
            f.write(contents)

        ice_data = pd.read_excel('data/ice_excel.xlsx', sheet_name=None, header=None)

        new_data = pd.DataFrame()

        try:
            ice_shape = ice_data['lon'].shape
            lats = ice_data['lat'].to_numpy().flatten()
            lons = ice_data['lon'].to_numpy().flatten()
            del ice_data['lat'], ice_data['lon']
            new_data['COORDINATES'] = np.swapaxes(np.vstack((lons, lats)), 0, 1).tolist()

            for sheet in ice_data.keys():
                ice_day = ice_data[sheet]
                assert ice_day.shape == ice_shape

                new_data[sheet] = ice_data[sheet].to_numpy().flatten().tolist()

        except Exception as e:
            return JSONResponse(content={"error": str(e)}, status_code=500)
        
        current = new_data[['COORDINATES', list(new_data)[-1]]]
        current.columns = ['COORDINATES', 'ICE']

        current.to_json('data/new_data.json', orient='records')

        process_routes(current)

        return JSONResponse(content={"status": "OK"}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
   


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8123)
