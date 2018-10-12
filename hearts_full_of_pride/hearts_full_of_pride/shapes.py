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
        
    
class Clip:
    
    def __init__(self, *shapes, clipid="clipid", **kwargs):
        self.clipid = clipid
        self.shapes = shapes
        self.kwargs = kwargs
    
    def clipper(self):
        return clipPath(*self.shapes, 
                        **{"id":self.clipid}, **self.kwargs)
    
    def clip(self, *targets, **kwargs):
        return group(*targets, style={"clip-path":f"url(#{self.clipid})"})
    
    def show_clip(self, *targets, edge=False, clip=True, style = None, **kwargs):
        if style is not None:
            style = {}

        outline = self.shapes if edge else [""]
        to_display = [self.clip(*targets, **kwargs)] if clip else targets
        
        return svg(*to_display,
                   *outline,
                   viewBox="-25 -25 50 50")


class ParametricSVG:
    def __init__(self, t, expr_x, expr_y):
        self.t = t
        self.u = symbols('u')
        assert t in expr_x.atoms()
        assert t in expr_y.atoms()
        self.expr_x = expr_x
        self.expr_y = expr_y
        line_1 = self.line(self.t)
        line_2 = self.line(self.u)

    def point(self, var):
        x = self.expr_x.subs(var)
        y = self.expr_y.subs(var)
        return Point()

        
        
    def line(self, var):
        x = self.expr_x.subs(var)
        y = self.expr_y.subs(var)
        return (x, y)

        
