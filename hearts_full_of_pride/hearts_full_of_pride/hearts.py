import uuid 
import os

from vdom.svg import path

from .shapes import load_data

def setup_data(fname=None):
    if fname is None:
        fname = os.path.join(os.path.dirname(__file__),'heart_quads.json'))
    data = load_data(fname)
    quads = data['quad_points']
    initial_point = data['initial_point']
    return quads, initial_point

# d = f'M{initial_point[0]},{initial_point[1]} {" ".join("Q"+",".join(map(str, (q for q in quad[0])))+" "+",".join(map(str, (q for q in quad[1]))) for quad in quads)} '
def gen_id():
    return f"{uuid4()}".replace("-","")

def gen_heart(myid=None):
    if myid is None:
        myid = gen_id()
    quads, initial_point = setup_data()
    d = f'M{initial_point[0]},{initial_point[1]} {" ".join("Q"+",".join(map(str, (q for q in quad[0])))+" "+",".join(map(str, (q for q in quad[1]))) for quad in quads)} Z'
    my_heart = path(
        id=f"{myid}",
        fill="none", 
        stroke="red",
        d=d,
        transform = "scale(1.25 -1.25)",
        **{"stroke-width": ".5"}
        )
    
    return my_heart
