trans = {"colors":['lightskyblue', 'lightpink', 'white',  'lightpink', 'lightskyblue'],
         "name":"trans",}

intersex = {"colors":["gold"],
            "name": "intersex",}
intersex['symbol'] = circle(cx="0", cy="2", r="5", fill="transparent", 
                            stroke="purple", **{"stroke-width":"2.5"})

genderqueer = {"colors":['purple', 'white', 'forestgreen'],
               "name": "genderqueer",}

pride = {"colors":['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'brown', 'black'], 
         "name": "pride",}

agender = {"colors":['black', 'lightgrey', 'white', 'chartreuse', 'white', 'lightgrey', 'black']
           "name": "agender",}

ace = {"colors":['black','lightgrey','white', 'purple'], 
       "name": "asexual", }

bi = {"colors":['deeppink', 'deeppink', 'mediumpurple', 'blue','blue'],
      "name": "bi",}

enby = {"colors":['#ffef00', 'white', '#9C59D1', 'black'], 
        "name": "enby",}

genderfluid = {"colors":['#ff75a2', "white","#be18d6", 'black', 'mediumblue'],
               "name": "genderfluid",}

pansexual = {"colors":['deeppink', "gold", "deepskyblue"],
             "name": "pansexual",}

polysexual = {"colors":["#f61cb9", "#07d569", 'dodgerblue'],
              "name": "polysexual",}

aromantic = {"colors":["#3da542", "#a7d379", "white", "lightgrey", "black"],
             "name": "aromantic",}

lipstick = {"colors":["#A60061", "#B95393", "#D260A7", "#EDEDEB", "#E5ABD0", "#C74D52", "#8C1D00"], 
            "name": "lipstick",}



polyamory = {"colors":["blue", "red", "black"]
             "name": "polyamory",}

bear = {"colors": ["#623804", "chocolate", "#fedd63", "moccasin", "white", "dimgray", "black"], 
        "name": "bear",}

lesbian = {"colors":["purple"],
           "name": "lesbian",}

polyamory['symbol'] = text("π", y="4.5", fill="yellow", 
                           **{'text-anchor': "middle", "font-family": "Minion Pro", "font-size":"15"})
bear['symbol'] = path(d="M98.9 24.4c-5.7 0-11.5 1.3-16.3 4.4C61.2 42.6 91.1 48.3 96 51.1c4.7 2.7 22.4 22.9 29.7-8.4 2.2-9.7-12.2-18.3-26.8-18.3m45.4 11.2c-17.7 1.9-.8 43 23.6 44.4 16.5.9 28.9-39.3-23.6-44.4m-94.4 8.9C34.2 44 43.7 73.3 69 83.6c5.1 2.1 14.2-4.7 14.4-16 .1-4.2-7.1-22.2-33.5-23.1m61 17.7c-7.1-.1-14.6 3-22.8 11.5-28.9 30.3 13.8 35.5 10.6 51.9-9.7 48.5-.9 52.5 8.3 55.6 11.7 3.9 33.8-33.4 43.1-40.4 12.4-9.4 77.9-42.2 62.4-58.8-22.3-23.8-27 7.3-57.7-1-14.6-3.9-28.3-18.8-43.9-18.8M54.4 96.5c-2.8-.1-5.5.4-8.1 1.6-11.5 5.2 10.8 36.5 20.9 37.4 12.4 1.1 17.4-8.9 17.6-14.7.3-7.6-15.4-24-30.4-24.3m4 46.7c-4.5.1-8 1.2-9.6 3.3-4.1 6.2 21.6 30.4 28.7 32 6.5 1.5 12.6-13 11.4-18.7-2.2-10.4-19.2-16.7-30.5-16.6",
                      transform = "scale(.08 .08) translate(-120,-80) ") 
lesbian['symbol'] = group(path(d="M500 550L211.325 50h577.35z", fill="black"),
                          path(d="M479.667 132.374a162.687 162.687 0 0 1-108.732-62.373 162.687 162.687 0 0 0 0 198.075 162.687 162.687 0 0 1 108.732-62.373zm40.672 73.329a162.687 162.687 0 0 1 108.732 62.373 162.687 162.687 0 0 0 0-198.075 162.687 162.687 0 0 1-108.732 62.373zm-4.067-91.571a16.269 8.134 0 0 0-32.538 0v347.743a16.269 8.134 0 0 0 32.538 0z", 
                               fill="white"), 
                          transform = "scale(.04, .04) translate(-500 -150)")


flag_defs = [trans, lesbian, bear, agender, ace, bi, pride, enby, genderfluid, pansexual, polysexual, aromantic, lipstick, genderqueer, intersex, polyamory]
