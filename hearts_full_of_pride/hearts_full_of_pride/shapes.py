import json 

def store_data(fname, quad_points, initial_point):
    data = {"quad_points": quad_points,
     "initial_point": initial_point
    }
    with open(fname, "w") as fp:
        json.dump(data, fp)

def load_data(fname):
    with open(fname, "r") as fp:
        return json.load(fp)
        
