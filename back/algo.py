import pandas as pd
import numpy as np

from a_star import *
from models import SessionLocal
from main import get_db, Edge


def process_edges(current, ice_shape):
    ice_now = current.iloc[:, 1]

    ice_now = np.resize(ice_now.to_numpy(), ice_shape)

    all_points = np.moveaxis(np.mgrid[:ice_shape[0],:ice_shape[1]], 0, -1).reshape(-1, 2).tolist()
    thr = 0

    weights = {tuple(loc): ice_now[loc[0], loc[1]] for loc in all_points if ice_now[loc[0], loc[1]] > thr}
    walls = [tuple(loc) for loc in all_points if ice_now[loc[0], loc[1]] <= thr]

    diagram = GridWithWeights(*ice_shape)
    diagram.walls = walls
    diagram.weights = weights

    graph = pd.read_csv('data/graph.csv')
    
    # graph['start_ind'] = graph.apply(lambda row: )
    # graph['points'] = graph.apply(lambda row: a_star_search(diagram, start, goal))
    print(graph.head())

    graph.to_csv('data/graph.csv', index=False)

    # start, goal = (132, 39), (184, 44)
    # came_from, cost_so_far = a_star_search(diagram, start, goal)

    # path = reconstruct_path(came_from, start=start, goal=goal)