import regex
import lxml.etree as et 

from vdom.svg import tspan

posix = regex.compile('[^\p{posix_punct}]')
uni = regex.compile('[^\p{p}]')
                     
def get_punct(article):
    return regex.sub(uni,'', str(article))

def get_body(article):
    tags = ["/",
            "article",
            "body"]
    return article.get_element_xpath(tags)[0]

def body_punct(article):
    return get_punct(et.tostring(get_body(article), encoding='unicode'))
       
color_map = {"?!.": "red",
             "\"'()[]{}“”": "green",
             "—-,;:/\\&%*$@–": "blue"}

def color_wrap(char):
    color = "black"
    for key, val in color_map.items():
        if char in key:
            color = val
            
    return tspan(char, fill= f'{color}')

# def style_punct(text):
#     return [color_wrap(c) for c in text]

def style_punct(article):
    return [color_wrap(c) for c in body_punct(article)]
    
