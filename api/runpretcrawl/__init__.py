import logging
import azure.functions as func

import numpy as np
from pyproj import Transformer
import geojson
from shapely.geometry import MultiPoint, LineString
import json




transformer = Transformer.from_crs(4326, 3857)
transformer_back = Transformer.from_crs(3857, 4326)
with open("prets.geojson") as f:
    prets = geojson.load(f)


prets_4326 = prets
prets_4326_list = [tuple(g.geometry.coordinates) for g in prets.features]


def distance(point, points_array):
    return np.sqrt(np.sum((points_array - point) ** 2, 1))


prets_list = list(map(lambda x: transformer.transform(*x), [g.geometry.coordinates for g in prets.features]))
prets = MultiPoint(prets_list)


def run_pret_crawl(start_point, end_point, distance_thresh=2500):
    start_point_4326 = start_point
    end_point_4326 = end_point
    start_point = np.array(transformer.transform(*start_point))
    end_point = np.array(transformer.transform(*end_point))

    logging.info(start_point)
    logging.info(end_point)
    route = LineString((start_point, end_point))
    buffered_route = route.buffer(500)

    filtered_prets = np.array([np.array((geom.xy[0][0], geom.xy[1][0])) for geom in filter(lambda x: buffered_route.contains(x),prets)])

    start_distances = distance(start_point, filtered_prets)
    first_pret = filtered_prets[np.argmin(np.abs(start_distances - distance_thresh))]

    current_pret = first_pret

    pret_crawl = [start_point, current_pret]

    while distance(current_pret, [end_point])[0] >= distance_thresh:
        distance_array = distance(current_pret, filtered_prets)
        next_pret = filtered_prets[np.argmin(np.abs(distance_array - distance_thresh))]
        pret_crawl.append(next_pret)
        current_pret = next_pret

        relevant_indices = np.where(start_distances > distance(current_pret, [start_point])[0])[0]
        filtered_prets = np.take(filtered_prets, relevant_indices, axis=0)
        start_distances = np.take(start_distances, relevant_indices)
        print(f"distance to end point: {distance(current_pret, [end_point])[0]}")

    pret_crawl.append(end_point)

    pc = [start_point_4326]
    for pret in pret_crawl[1:-1]:
        logging.info(np.where(pret == np.array(prets_list)))
        pc.append(prets_4326_list[np.where(pret == np.array(prets_list))[0][0]])
    pc.append(end_point_4326)



    return pc


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    start_point = (float(req.params.get("startPointLng")), float(req.params.get("startPointLat")))
    logging.info(start_point)
    end_point = (float(req.params.get("endPointLng")), float(req.params.get("endPointLat")))
    logging.info(end_point)
    distance_thresh = req.params.get("distanceThreshold")

    print(start_point)
    if distance_thresh:
        pret_crawl = run_pret_crawl(start_point, end_point, distance_thresh)
    else:
        pret_crawl = run_pret_crawl(start_point, end_point)

    logging.info(pret_crawl)



    return func.HttpResponse(json.dumps(pret_crawl))
