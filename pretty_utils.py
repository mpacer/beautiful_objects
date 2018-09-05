import io
import matplotlib.pyplot as plt
plt.ioff()

from vdom import div, style, h1

def flag(tag_name, klass):
    return """@keyframes trans {{
            to {{
                background-position: 200% center;
                }}
            }}
        {tag_name}.{klass} {{
             text-align: center;
             background: linear-gradient(to right, lightblue 20%, pink 35%, white 60%, pink 75%, lightblue 100%);
             background-size: 200% auto;
             color: #000;
             animation: trans 1s linear infinite;
             -webkit-background-clip: text;
             -webkit-text-fill-color: transparent;
         }}""".format(tag_name=tag_name, klass=klass)
    
def trans(text):
    return div(
        style(flag("h1", "rainbow")),
        h1(text, 
           style={"fontSize":"80px"},
           **{"class":"rainbow"}),
        style = {"justify-content": "center",
                 "align-items": "center",
                 "background": "#333", 
                 "text-align": "center",
                 "width": "30%",
                 "margin": "0 auto"
                }
        
    )
    
def mpl_image(text, format='png'):
    plt.ioff()
    fig, ax = plt.subplots();
    ax.text(0.5, 0.5, text, transform=ax.transAxes, fontsize=40)
    ax.set_axis_off()
    with io.BytesIO() as f:
        fig.savefig(f,format=format)
        plt.close(fig)
        f.seek(0)
        return f.read()
