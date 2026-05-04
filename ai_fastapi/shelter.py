import json
import math

with open("../data/shelters.json") as f:
    shelters = json.load(f)


def dist(a,b,c,d):
    return math.sqrt((a-c)**2 + (b-d)**2)


def get_shelter(lat, lon):

    if lat is None or lon is None:
        return {"error": "No location"}

    best = None
    best_d = 99999

    for s in shelters:
        d = dist(lat, lon, s["lat"], s["lon"])
        if d < best_d:
            best_d = d
            best = s

    return {
        "shelter": best["name"],
        "distance": round(best_d, 2)
    }