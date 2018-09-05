import math

from uuid import uuid4

from vdom.svg import *
from vdom.core import create_component

from sympy import symbols, sin, cos, pi, Point, Line, Point2D
from sympy.simplify import simplify

class ArchemedianSpiral:
    a, b, θ, ϕ = symbols('a,b,θ, ϕ')
    y1 = (a+b*θ)*sin(θ)
    x1 = (a+b*θ)*cos(θ)
    y2 = (a+b*ϕ)*sin(ϕ)
    x2 = (a+b*ϕ)*cos(ϕ)

    g = (b*sin(θ) + (a + b*θ)*cos(θ))/(b*cos(θ) - (a+b*θ)*sin(θ))
    h = (b*sin(ϕ) + (a + b*ϕ)*cos(ϕ))/(b*cos(ϕ) - (a+b*ϕ)*sin(ϕ))

    p1 = Point(x1,y1)
    p2 = Point(x2,y2)
    l1 = Line(p1, slope=g)
    l2 = Line(p2, slope=h)
    #self.int_point = self.l1.intersection(self.l2)[0]
    # hard code this so that it takes less time to create the class
    int_point = Point2D(
        (a**3*sin(θ) - a**3*sin(ϕ) + a**2*b*θ*sin(θ) - 2*a**2*b*θ*sin(ϕ) + 2*a**2*b*ϕ*sin(θ) 
         - a**2*b*ϕ*sin(ϕ) - a**2*b*cos(θ) + a**2*b*cos(ϕ) - a*b**2*θ**2*sin(ϕ) + 2*a*b**2*θ*ϕ*sin(θ) 
         - 2*a*b**2*θ*ϕ*sin(ϕ) + 2*a*b**2*θ*cos(ϕ) + a*b**2*ϕ**2*sin(θ) - 2*a*b**2*ϕ*cos(θ) - b**3*θ**2*ϕ*sin(ϕ) 
         + b**3*θ**2*cos(ϕ) + b**3*θ*ϕ**2*sin(θ) - b**3*ϕ**2*cos(θ))
        /(a**2*sin(θ - ϕ) + a*b*θ*sin(θ - ϕ) + a*b*ϕ*sin(θ - ϕ) + b**2*θ*ϕ*sin(θ - ϕ) + b**2*θ*cos(θ - ϕ) - 
          b**2*ϕ*cos(θ - ϕ) + b**2*sin(θ - ϕ)), 
        (((a + b*θ)
          *(b*cos(θ) - (a + b*θ)*sin(θ))
          *(a**2*sin(θ - ϕ) + a*b*θ*sin(θ - ϕ) + a*b*ϕ*sin(θ - ϕ) + b**2*θ*ϕ*sin(θ - ϕ) + b**2*θ*cos(θ - ϕ) - b**2*ϕ*cos(θ - ϕ) + b**2*sin(θ - ϕ))
          *sin(θ)) 
         - ((b*sin(θ) + (a + b*θ)*cos(θ))
            *(-(b*sin(θ) + (a + b*θ)*cos(θ))
              *(b*cos(ϕ) - (a + b*ϕ)*sin(ϕ))
              *((a + b*θ)*cos(θ) - (a + b*ϕ)*cos(ϕ)) 
              + ((b*cos(θ) - (a + b*θ)*sin(θ))
                *(b*cos(ϕ) - (a + b*ϕ)*sin(ϕ))
                *((a + b*θ)*sin(θ) - (a + b*ϕ)*sin(ϕ)))
              + ((a + b*θ)*cos(θ) - (a + b*ϕ)*cos(ϕ))
              *(a**2*sin(θ - ϕ) 
                + a*b*θ*sin(θ - ϕ) 
                + a*b*ϕ*sin(θ - ϕ) 
                + b**2*θ*ϕ*sin(θ - ϕ) 
                + b**2*θ*cos(θ - ϕ) 
                - b**2*ϕ*cos(θ - ϕ) 
                + b**2*sin(θ - ϕ))
             ))
        )/((b*cos(θ) - (a + b*θ)*sin(θ))
           *(a**2*sin(θ - ϕ) 
             + a*b*θ*sin(θ - ϕ) 
             + a*b*ϕ*sin(θ - ϕ) 
             + b**2*θ*ϕ*sin(θ - ϕ) 
             + b**2*θ*cos(θ - ϕ) 
             - b**2*ϕ*cos(θ - ϕ) 
             + b**2*sin(θ - ϕ))
          )
    )
    
    def __init__(self, a=0, b=1, num_cycles=3, angle=45, font_size=1, gen_quads=True):
        self.a = a
        self.b = b
        self.num_cycles = num_cycles
        self.angle = angle
        self.font_size = font_size
        self._quads = None
        if gen_quads:
            self.quads
        
    @property
    def center(self):
        return float(self.b*(self.num_cycles*pi*2)+14*self.font_size) + max(self.initial_point)
    
    @property
    def initial_point(self):
        """ Because quadratic curves are assuming that they are absolute we need to provide the starting point.
        """
        return list(map(float, self.p1.subs({"a":self.a, 
                                             "b":self.b, 
                                             "θ":0
                                            }).args))
    
    @property
    def quads(self):
        if self._quads is None: 
            self._quads = list(self.get_quad_control_points())
        return self._quads
    
    @property
    def curve_string(self):
        starting_point = map(lambda x: str(self.center + x), self.initial_point)
        starting_string = f'M{",".join(starting_point)}'        
        return f"{starting_string} {self.quad_string}"


    def quad_to_string(self, quad):
        ctrl_pt = ",".join(map(str, (q+self.center for q in quad[0])))
        final_pt = ",".join(map(str, (q+self.center for q in quad[1])))
        return f"Q{ctrl_pt} {final_pt}"
        
    @property
    def quad_string(self):       
        for quad in self.quads:
            return " ".join(self.quad_to_string(quad) for quad in self.quads)
            
        
    def get_intersection_points(self, num_cycles, angle_change, θ0=0):
        """
        num_cycles: 
            how many times does the spiral go around (this will be rounded up to give a complete segment)
        angle_change:
            how large is the change in angle for each quadratic segment
        """
        num_degs = num_cycles*360
        num_angles = math.floor(num_degs/angle_change)
        

        δθ = (pi/180)*angle_change
        for x in range(num_angles):
            loc_θ = θ0 + x*δθ
            yield {"int_point": self.int_point.subs({"a":self.a, 
                                                     "b":self.b, 
                                                     "θ":loc_θ, 
                                                     "ϕ":(loc_θ+δθ)}),
                   "loc_θ": loc_θ,
                   "δθ": δθ
                  }

    def get_quad_control_points(self, θ0=0):
        
        for x in self.get_intersection_points(self.num_cycles, self.angle, θ0=θ0):
            yield (tuple(map(float, x['int_point'].args)), 
                   tuple(map(float, self.p2.subs({"a":self.a, 
                                                  "b":self.b, 
                                                  "θ":x['loc_θ'], 
                                                  "ϕ":(x['loc_θ']+x['δθ'])
                                                 }).args))
                  )
        
    def _repr_mimebundle_(self, include=None, exclude=None, **kwargs):
        el = svgStyledSpiral("",spiral=self, stroke="red")
        return {'text/html': el.to_html(),
                **el._repr_mimebundle_(include=include, exclude=exclude)
                }

link = create_component('link')

def svgAnimateSpiral(content = None, spiral=None, stroke="", **kwargs):
    """
    font_size: float 
        default is 1; interpreted as em (so 1 is notebook default)
    """

    if content is None:
        content = "The quick brown fox jumps over the lazy dog. "*10
    if spiral is None:
        #   a # how far out to start
        #   b # number of units between cycles
        #   num_cycles # minimum number of cycles to be covered
        #   angle # number of degrees each quadratic curve will approximate

        spiral = ArchemedianSpiral(a=kwargs["a"], 
                                   b=kwargs["b"], 
                                   num_cycles=kwargs['num_cycles'], 
                                   angle=kwargs['angle'],
                                   font_size=kwargs['font_size'])
    delay = kwargs.get("delay") or 0
    center = spiral.center
    font_size = spiral.font_size
    start_anim = animate(
                         attributeName="startOffset", 
                         dur=f"{spiral.num_cycles*1}s", 
                         repeatCount="indefinite",
                         begin=f"{delay}s",
                         **{"from": "0%",
                            "to": "100%"}
                     ) if kwargs.get("start_anim") else ""
    
    rotate_anim =   animateTransform(**{"attributeName":"transform",
                                        "attributeType":"XML",
                                        "type":"rotate",
                                        "from":f"360 {center} {center}",
                                        "to":f"0 {center} {center}",
                                        "dur":"1s",
                                        "repeatCount":"indefinite",
                                        }
                    ) if kwargs.get("rotate_anim") else ""
    starting_point = map(lambda x: str(center + x), spiral.initial_point)

    myid = f"{uuid4()}"
    side = spiral.center*2 + 1.5*font_size*14
    return svg(
        link(rel="stylesheet", href="https://use.typekit.net/hhc2wzo.css"),
        path(id=f"{myid}",
             fill="none", 
             stroke=stroke,
             d=spiral.curve_string
            ),
        text(
            textPath(start_anim,
                     *content,
                     **{"xlink:href":f"#{myid}"}
                    ),
            rotate_anim,
            style={"fontSize": f"{font_size}em",
                   "fontFamily": f"{kwargs.get('font_fam') or 'Minion Pro'}, 'Monospace' ",
                  }
        ),
        
        width=f"{side}",
        height=f"{side}"
    )
    
def svgStyledSpiral(content = None, spiral=None, stroke="", **kwargs):
    """
    font_size: float 
        default is 1; interpreted as em (so 1 is notebook default)
    """

    if content is None:
        content = "The quick brown fox jumps over the lazy dog. "*10
    if spiral is None:
        #   a # how far out to start
        #   b # number of units between cycles
        #   num_cycles # minimum number of cycles to be covered
        #   angle # number of degrees each quadratic curve will approximate

        spiral = ArchemedianSpiral(a=kwargs["a"], b=kwargs["b"], 
                                   num_cycles=kwargs['num_cycles'], 
                                   angle=kwargs['angle'],
                                   font_size=kwargs['font_size'])
                     

    starting_point = map(lambda x: str(center + x), spiral.initial_point)
    font_size = spiral.font_size
    myid = f"{uuid4()}"
    side = spiral.center*2 + 1.5*font_size*14
    return svg(
        path(id=f"{myid}",
             fill="none", 
             stroke=stroke,
             d=spiral.curve_string
            ),
        text(
            textPath(content,
                     **{"xlink:href":f"#{myid}"}),
            style={"fontSize": f"{font_size}em",
                   "fontFamily": f"{kwargs.get('font_fam') or 'Minion Pro'}, 'Monospace' ",
                   "rotate": f"{kwargs.get('rotate')}" or '0', 
                  }
        ),
        width=f"{side}",
        height=f"{side}"
    )
