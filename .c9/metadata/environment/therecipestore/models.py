{"filter":false,"title":"models.py","tooltip":"/therecipestore/models.py","undoManager":{"mark":66,"position":66,"stack":[[{"start":{"row":37,"column":77},"end":{"row":38,"column":0},"action":"insert","lines":["",""],"id":154},{"start":{"row":38,"column":0},"end":{"row":38,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":38,"column":4},"end":{"row":38,"column":68},"action":"insert","lines":["recipes = db.relationship('Recipe', backref=\"author\", lazy=True)"],"id":155}],[{"start":{"row":38,"column":31},"end":{"row":38,"column":37},"action":"remove","lines":["Recipe"],"id":156},{"start":{"row":38,"column":31},"end":{"row":38,"column":32},"action":"insert","lines":["I"]},{"start":{"row":38,"column":32},"end":{"row":38,"column":33},"action":"insert","lines":["n"]},{"start":{"row":38,"column":33},"end":{"row":38,"column":34},"action":"insert","lines":["g"]},{"start":{"row":38,"column":34},"end":{"row":38,"column":35},"action":"insert","lines":["r"]},{"start":{"row":38,"column":35},"end":{"row":38,"column":36},"action":"insert","lines":["e"]},{"start":{"row":38,"column":36},"end":{"row":38,"column":37},"action":"insert","lines":["d"]},{"start":{"row":38,"column":37},"end":{"row":38,"column":38},"action":"insert","lines":["i"]}],[{"start":{"row":38,"column":38},"end":{"row":38,"column":39},"action":"insert","lines":["e"],"id":157},{"start":{"row":38,"column":39},"end":{"row":38,"column":40},"action":"insert","lines":["n"]},{"start":{"row":38,"column":40},"end":{"row":38,"column":41},"action":"insert","lines":["t"]}],[{"start":{"row":38,"column":53},"end":{"row":38,"column":59},"action":"remove","lines":["author"],"id":158},{"start":{"row":38,"column":53},"end":{"row":38,"column":54},"action":"insert","lines":["r"]},{"start":{"row":38,"column":54},"end":{"row":38,"column":55},"action":"insert","lines":["e"]},{"start":{"row":38,"column":55},"end":{"row":38,"column":56},"action":"insert","lines":["c"]},{"start":{"row":38,"column":56},"end":{"row":38,"column":57},"action":"insert","lines":["i"]},{"start":{"row":38,"column":57},"end":{"row":38,"column":58},"action":"insert","lines":["p"]},{"start":{"row":38,"column":58},"end":{"row":38,"column":59},"action":"insert","lines":["e"]}],[{"start":{"row":38,"column":4},"end":{"row":38,"column":11},"action":"remove","lines":["recipes"],"id":159},{"start":{"row":38,"column":4},"end":{"row":38,"column":5},"action":"insert","lines":["i"]},{"start":{"row":38,"column":5},"end":{"row":38,"column":6},"action":"insert","lines":["n"]},{"start":{"row":38,"column":6},"end":{"row":38,"column":7},"action":"insert","lines":["g"]},{"start":{"row":38,"column":7},"end":{"row":38,"column":8},"action":"insert","lines":["r"]},{"start":{"row":38,"column":8},"end":{"row":38,"column":9},"action":"insert","lines":["e"]},{"start":{"row":38,"column":9},"end":{"row":38,"column":10},"action":"insert","lines":["d"]},{"start":{"row":38,"column":10},"end":{"row":38,"column":11},"action":"insert","lines":["i"]},{"start":{"row":38,"column":11},"end":{"row":38,"column":12},"action":"insert","lines":["e"]},{"start":{"row":38,"column":12},"end":{"row":38,"column":13},"action":"insert","lines":["n"]},{"start":{"row":38,"column":13},"end":{"row":38,"column":14},"action":"insert","lines":["t"]},{"start":{"row":38,"column":14},"end":{"row":38,"column":15},"action":"insert","lines":["s"]}],[{"start":{"row":38,"column":14},"end":{"row":38,"column":15},"action":"remove","lines":["s"],"id":160}],[{"start":{"row":38,"column":75},"end":{"row":39,"column":0},"action":"insert","lines":["",""],"id":161},{"start":{"row":39,"column":0},"end":{"row":39,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":39,"column":4},"end":{"row":39,"column":75},"action":"insert","lines":["ingredient = db.relationship('Ingredient', backref=\"recipe\", lazy=True)"],"id":162}],[{"start":{"row":39,"column":34},"end":{"row":39,"column":44},"action":"remove","lines":["Ingredient"],"id":163},{"start":{"row":39,"column":34},"end":{"row":39,"column":35},"action":"insert","lines":["I"]},{"start":{"row":39,"column":35},"end":{"row":39,"column":36},"action":"insert","lines":["n"]},{"start":{"row":39,"column":36},"end":{"row":39,"column":37},"action":"insert","lines":["s"]},{"start":{"row":39,"column":37},"end":{"row":39,"column":38},"action":"insert","lines":["t"]},{"start":{"row":39,"column":38},"end":{"row":39,"column":39},"action":"insert","lines":["r"]},{"start":{"row":39,"column":39},"end":{"row":39,"column":40},"action":"insert","lines":["u"]},{"start":{"row":39,"column":40},"end":{"row":39,"column":41},"action":"insert","lines":["c"]},{"start":{"row":39,"column":41},"end":{"row":39,"column":42},"action":"insert","lines":["t"]},{"start":{"row":39,"column":42},"end":{"row":39,"column":43},"action":"insert","lines":["i"]},{"start":{"row":39,"column":43},"end":{"row":39,"column":44},"action":"insert","lines":["o"]},{"start":{"row":39,"column":44},"end":{"row":39,"column":45},"action":"insert","lines":["n"]}],[{"start":{"row":39,"column":4},"end":{"row":39,"column":14},"action":"remove","lines":["ingredient"],"id":164},{"start":{"row":39,"column":4},"end":{"row":39,"column":5},"action":"insert","lines":["i"]},{"start":{"row":39,"column":5},"end":{"row":39,"column":6},"action":"insert","lines":["n"]},{"start":{"row":39,"column":6},"end":{"row":39,"column":7},"action":"insert","lines":["s"]},{"start":{"row":39,"column":7},"end":{"row":39,"column":8},"action":"insert","lines":["t"]},{"start":{"row":39,"column":8},"end":{"row":39,"column":9},"action":"insert","lines":["r"]},{"start":{"row":39,"column":9},"end":{"row":39,"column":10},"action":"insert","lines":["u"]},{"start":{"row":39,"column":10},"end":{"row":39,"column":11},"action":"insert","lines":["c"]},{"start":{"row":39,"column":11},"end":{"row":39,"column":12},"action":"insert","lines":["t"]},{"start":{"row":39,"column":12},"end":{"row":39,"column":13},"action":"insert","lines":["i"]},{"start":{"row":39,"column":13},"end":{"row":39,"column":14},"action":"insert","lines":["o"]},{"start":{"row":39,"column":14},"end":{"row":39,"column":15},"action":"insert","lines":["n"]}],[{"start":{"row":42,"column":16},"end":{"row":42,"column":20},"action":"remove","lines":["User"],"id":165},{"start":{"row":42,"column":16},"end":{"row":42,"column":17},"action":"insert","lines":["R"]},{"start":{"row":42,"column":17},"end":{"row":42,"column":18},"action":"insert","lines":["e"]},{"start":{"row":42,"column":18},"end":{"row":42,"column":19},"action":"insert","lines":["c"]},{"start":{"row":42,"column":19},"end":{"row":42,"column":20},"action":"insert","lines":["i"]},{"start":{"row":42,"column":20},"end":{"row":42,"column":21},"action":"insert","lines":["p"]},{"start":{"row":42,"column":21},"end":{"row":42,"column":22},"action":"insert","lines":["e"]}],[{"start":{"row":51,"column":16},"end":{"row":51,"column":20},"action":"remove","lines":["User"],"id":166},{"start":{"row":51,"column":16},"end":{"row":51,"column":17},"action":"insert","lines":["I"]},{"start":{"row":51,"column":17},"end":{"row":51,"column":18},"action":"insert","lines":["n"]},{"start":{"row":51,"column":18},"end":{"row":51,"column":19},"action":"insert","lines":["g"]},{"start":{"row":51,"column":19},"end":{"row":51,"column":20},"action":"insert","lines":["r"]},{"start":{"row":51,"column":20},"end":{"row":51,"column":21},"action":"insert","lines":["e"]},{"start":{"row":51,"column":21},"end":{"row":51,"column":22},"action":"insert","lines":["d"]},{"start":{"row":51,"column":22},"end":{"row":51,"column":23},"action":"insert","lines":["i"]}],[{"start":{"row":51,"column":23},"end":{"row":51,"column":24},"action":"insert","lines":["e"],"id":167},{"start":{"row":51,"column":24},"end":{"row":51,"column":25},"action":"insert","lines":["n"]},{"start":{"row":51,"column":25},"end":{"row":51,"column":26},"action":"insert","lines":["t"]}],[{"start":{"row":60,"column":16},"end":{"row":60,"column":20},"action":"remove","lines":["User"],"id":168},{"start":{"row":60,"column":16},"end":{"row":60,"column":17},"action":"insert","lines":["I"]},{"start":{"row":60,"column":17},"end":{"row":60,"column":18},"action":"insert","lines":["n"]},{"start":{"row":60,"column":18},"end":{"row":60,"column":19},"action":"insert","lines":["s"]},{"start":{"row":60,"column":19},"end":{"row":60,"column":20},"action":"insert","lines":["t"]},{"start":{"row":60,"column":20},"end":{"row":60,"column":21},"action":"insert","lines":["r"]},{"start":{"row":60,"column":21},"end":{"row":60,"column":22},"action":"insert","lines":["u"]},{"start":{"row":60,"column":22},"end":{"row":60,"column":23},"action":"insert","lines":["c"]},{"start":{"row":60,"column":23},"end":{"row":60,"column":24},"action":"insert","lines":["t"]},{"start":{"row":60,"column":24},"end":{"row":60,"column":25},"action":"insert","lines":["i"]},{"start":{"row":60,"column":25},"end":{"row":60,"column":26},"action":"insert","lines":["o"]},{"start":{"row":60,"column":26},"end":{"row":60,"column":27},"action":"insert","lines":["n"]},{"start":{"row":60,"column":27},"end":{"row":60,"column":28},"action":"insert","lines":["s"]}],[{"start":{"row":33,"column":62},"end":{"row":34,"column":0},"action":"insert","lines":["",""],"id":169},{"start":{"row":34,"column":0},"end":{"row":34,"column":4},"action":"insert","lines":["    "]},{"start":{"row":34,"column":4},"end":{"row":35,"column":0},"action":"insert","lines":["",""]},{"start":{"row":35,"column":0},"end":{"row":35,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":35,"column":4},"end":{"row":35,"column":30},"action":"insert","lines":["meal_preference_vegetarian"],"id":170}],[{"start":{"row":35,"column":30},"end":{"row":35,"column":31},"action":"insert","lines":[" "],"id":171},{"start":{"row":35,"column":31},"end":{"row":35,"column":32},"action":"insert","lines":["="]}],[{"start":{"row":35,"column":32},"end":{"row":35,"column":33},"action":"insert","lines":[" "],"id":172},{"start":{"row":35,"column":33},"end":{"row":35,"column":34},"action":"insert","lines":["d"]},{"start":{"row":35,"column":34},"end":{"row":35,"column":35},"action":"insert","lines":["b"]},{"start":{"row":35,"column":35},"end":{"row":35,"column":36},"action":"insert","lines":["."]},{"start":{"row":35,"column":36},"end":{"row":35,"column":37},"action":"insert","lines":["C"]},{"start":{"row":35,"column":37},"end":{"row":35,"column":38},"action":"insert","lines":["o"]}],[{"start":{"row":35,"column":36},"end":{"row":35,"column":38},"action":"remove","lines":["Co"],"id":173},{"start":{"row":35,"column":36},"end":{"row":35,"column":42},"action":"insert","lines":["Column"]}],[{"start":{"row":35,"column":42},"end":{"row":35,"column":44},"action":"insert","lines":["()"],"id":174}],[{"start":{"row":35,"column":43},"end":{"row":35,"column":44},"action":"insert","lines":["d"],"id":175},{"start":{"row":35,"column":44},"end":{"row":35,"column":45},"action":"insert","lines":["b"]},{"start":{"row":35,"column":45},"end":{"row":35,"column":46},"action":"insert","lines":["."]},{"start":{"row":35,"column":46},"end":{"row":35,"column":47},"action":"insert","lines":["B"]}],[{"start":{"row":35,"column":47},"end":{"row":35,"column":48},"action":"insert","lines":["o"],"id":176},{"start":{"row":35,"column":48},"end":{"row":35,"column":49},"action":"insert","lines":["o"]},{"start":{"row":35,"column":49},"end":{"row":35,"column":50},"action":"insert","lines":["l"]},{"start":{"row":35,"column":50},"end":{"row":35,"column":51},"action":"insert","lines":["e"]}],[{"start":{"row":35,"column":51},"end":{"row":35,"column":52},"action":"insert","lines":["a"],"id":177},{"start":{"row":35,"column":52},"end":{"row":35,"column":53},"action":"insert","lines":["n"]},{"start":{"row":35,"column":53},"end":{"row":35,"column":54},"action":"insert","lines":[","]}],[{"start":{"row":35,"column":54},"end":{"row":35,"column":55},"action":"insert","lines":[" "],"id":178}],[{"start":{"row":35,"column":54},"end":{"row":35,"column":55},"action":"remove","lines":[" "],"id":179},{"start":{"row":35,"column":53},"end":{"row":35,"column":54},"action":"remove","lines":[","]}],[{"start":{"row":33,"column":0},"end":{"row":33,"column":62},"action":"remove","lines":["    meal_preference = db.Column(db.String(20), nullable=False)"],"id":180},{"start":{"row":32,"column":56},"end":{"row":33,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":34,"column":54},"end":{"row":35,"column":0},"action":"insert","lines":["",""],"id":181},{"start":{"row":35,"column":0},"end":{"row":35,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":35,"column":4},"end":{"row":35,"column":54},"action":"insert","lines":["meal_preference_vegetarian = db.Column(db.Boolean)"],"id":182}],[{"start":{"row":35,"column":54},"end":{"row":36,"column":0},"action":"insert","lines":["",""],"id":183},{"start":{"row":36,"column":0},"end":{"row":36,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":36,"column":4},"end":{"row":36,"column":54},"action":"insert","lines":["meal_preference_vegetarian = db.Column(db.Boolean)"],"id":184}],[{"start":{"row":36,"column":54},"end":{"row":37,"column":0},"action":"insert","lines":["",""],"id":185},{"start":{"row":37,"column":0},"end":{"row":37,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":37,"column":4},"end":{"row":37,"column":54},"action":"insert","lines":["meal_preference_vegetarian = db.Column(db.Boolean)"],"id":186}],[{"start":{"row":37,"column":54},"end":{"row":38,"column":0},"action":"insert","lines":["",""],"id":187},{"start":{"row":38,"column":0},"end":{"row":38,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":35,"column":20},"end":{"row":35,"column":30},"action":"remove","lines":["vegetarian"],"id":188},{"start":{"row":35,"column":20},"end":{"row":35,"column":21},"action":"insert","lines":["v"]},{"start":{"row":35,"column":21},"end":{"row":35,"column":22},"action":"insert","lines":["e"]},{"start":{"row":35,"column":22},"end":{"row":35,"column":23},"action":"insert","lines":["g"]},{"start":{"row":35,"column":23},"end":{"row":35,"column":24},"action":"insert","lines":["a"]},{"start":{"row":35,"column":24},"end":{"row":35,"column":25},"action":"insert","lines":["n"]}],[{"start":{"row":36,"column":20},"end":{"row":36,"column":30},"action":"remove","lines":["vegetarian"],"id":189},{"start":{"row":36,"column":20},"end":{"row":36,"column":21},"action":"insert","lines":["p"]},{"start":{"row":36,"column":21},"end":{"row":36,"column":22},"action":"insert","lines":["e"]},{"start":{"row":36,"column":22},"end":{"row":36,"column":23},"action":"insert","lines":["s"]},{"start":{"row":36,"column":23},"end":{"row":36,"column":24},"action":"insert","lines":["c"]},{"start":{"row":36,"column":24},"end":{"row":36,"column":25},"action":"insert","lines":["a"]},{"start":{"row":36,"column":25},"end":{"row":36,"column":26},"action":"insert","lines":["t"]},{"start":{"row":36,"column":26},"end":{"row":36,"column":27},"action":"insert","lines":["a"]},{"start":{"row":36,"column":27},"end":{"row":36,"column":28},"action":"insert","lines":["r"]},{"start":{"row":36,"column":28},"end":{"row":36,"column":29},"action":"insert","lines":["i"]},{"start":{"row":36,"column":29},"end":{"row":36,"column":30},"action":"insert","lines":["a"]},{"start":{"row":36,"column":30},"end":{"row":36,"column":31},"action":"insert","lines":["n"]}],[{"start":{"row":37,"column":20},"end":{"row":37,"column":21},"action":"insert","lines":["r"],"id":190},{"start":{"row":37,"column":21},"end":{"row":37,"column":22},"action":"insert","lines":["a"]},{"start":{"row":37,"column":22},"end":{"row":37,"column":23},"action":"insert","lines":["w"]},{"start":{"row":37,"column":23},"end":{"row":37,"column":24},"action":"insert","lines":["_"]}],[{"start":{"row":39,"column":0},"end":{"row":39,"column":60},"action":"remove","lines":["    meal_allergen = db.Column(db.String(20), nullable=False)"],"id":191}],[{"start":{"row":39,"column":0},"end":{"row":40,"column":0},"action":"insert","lines":["",""],"id":192}],[{"start":{"row":40,"column":0},"end":{"row":40,"column":4},"action":"insert","lines":["    "],"id":193}],[{"start":{"row":40,"column":0},"end":{"row":40,"column":4},"action":"remove","lines":["    "],"id":194},{"start":{"row":39,"column":0},"end":{"row":40,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":39,"column":0},"end":{"row":39,"column":4},"action":"insert","lines":["    "],"id":195}],[{"start":{"row":39,"column":4},"end":{"row":40,"column":0},"action":"insert","lines":["",""],"id":196},{"start":{"row":40,"column":0},"end":{"row":40,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":39,"column":4},"end":{"row":39,"column":5},"action":"insert","lines":["m"],"id":197},{"start":{"row":39,"column":5},"end":{"row":39,"column":6},"action":"insert","lines":["e"]},{"start":{"row":39,"column":6},"end":{"row":39,"column":7},"action":"insert","lines":["a"]},{"start":{"row":39,"column":7},"end":{"row":39,"column":8},"action":"insert","lines":["l"]},{"start":{"row":39,"column":8},"end":{"row":39,"column":9},"action":"insert","lines":["_"]}],[{"start":{"row":39,"column":9},"end":{"row":39,"column":10},"action":"insert","lines":["p"],"id":198},{"start":{"row":39,"column":10},"end":{"row":39,"column":11},"action":"insert","lines":["r"]},{"start":{"row":39,"column":11},"end":{"row":39,"column":12},"action":"insert","lines":["e"]},{"start":{"row":39,"column":12},"end":{"row":39,"column":13},"action":"insert","lines":["f"]},{"start":{"row":39,"column":13},"end":{"row":39,"column":14},"action":"insert","lines":["e"]},{"start":{"row":39,"column":14},"end":{"row":39,"column":15},"action":"insert","lines":["r"]},{"start":{"row":39,"column":15},"end":{"row":39,"column":16},"action":"insert","lines":["e"]}],[{"start":{"row":39,"column":15},"end":{"row":39,"column":16},"action":"remove","lines":["e"],"id":199},{"start":{"row":39,"column":14},"end":{"row":39,"column":15},"action":"remove","lines":["r"]},{"start":{"row":39,"column":13},"end":{"row":39,"column":14},"action":"remove","lines":["e"]},{"start":{"row":39,"column":12},"end":{"row":39,"column":13},"action":"remove","lines":["f"]},{"start":{"row":39,"column":11},"end":{"row":39,"column":12},"action":"remove","lines":["e"]},{"start":{"row":39,"column":10},"end":{"row":39,"column":11},"action":"remove","lines":["r"]},{"start":{"row":39,"column":9},"end":{"row":39,"column":10},"action":"remove","lines":["p"]}],[{"start":{"row":39,"column":9},"end":{"row":39,"column":10},"action":"insert","lines":["a"],"id":200},{"start":{"row":39,"column":10},"end":{"row":39,"column":11},"action":"insert","lines":["l"]},{"start":{"row":39,"column":11},"end":{"row":39,"column":12},"action":"insert","lines":["l"]},{"start":{"row":39,"column":12},"end":{"row":39,"column":13},"action":"insert","lines":["e"]},{"start":{"row":39,"column":13},"end":{"row":39,"column":14},"action":"insert","lines":["r"]},{"start":{"row":39,"column":14},"end":{"row":39,"column":15},"action":"insert","lines":["g"]},{"start":{"row":39,"column":15},"end":{"row":39,"column":16},"action":"insert","lines":["e"]},{"start":{"row":39,"column":16},"end":{"row":39,"column":17},"action":"insert","lines":["n"]},{"start":{"row":39,"column":17},"end":{"row":39,"column":18},"action":"insert","lines":["_"]}],[{"start":{"row":39,"column":18},"end":{"row":39,"column":19},"action":"insert","lines":["n"],"id":201},{"start":{"row":39,"column":19},"end":{"row":39,"column":20},"action":"insert","lines":["u"]},{"start":{"row":39,"column":20},"end":{"row":39,"column":21},"action":"insert","lines":["t"]},{"start":{"row":39,"column":21},"end":{"row":39,"column":22},"action":"insert","lines":["_"]},{"start":{"row":39,"column":22},"end":{"row":39,"column":23},"action":"insert","lines":["f"]},{"start":{"row":39,"column":23},"end":{"row":39,"column":24},"action":"insert","lines":["r"]},{"start":{"row":39,"column":24},"end":{"row":39,"column":25},"action":"insert","lines":["e"]},{"start":{"row":39,"column":25},"end":{"row":39,"column":26},"action":"insert","lines":["e"]}],[{"start":{"row":39,"column":26},"end":{"row":39,"column":27},"action":"insert","lines":[" "],"id":202},{"start":{"row":39,"column":27},"end":{"row":39,"column":28},"action":"insert","lines":["="]}],[{"start":{"row":39,"column":28},"end":{"row":39,"column":29},"action":"insert","lines":[" "],"id":203},{"start":{"row":39,"column":29},"end":{"row":39,"column":30},"action":"insert","lines":["d"]},{"start":{"row":39,"column":30},"end":{"row":39,"column":31},"action":"insert","lines":["b"]},{"start":{"row":39,"column":31},"end":{"row":39,"column":32},"action":"insert","lines":["."]}],[{"start":{"row":39,"column":32},"end":{"row":39,"column":33},"action":"insert","lines":["C"],"id":204},{"start":{"row":39,"column":33},"end":{"row":39,"column":34},"action":"insert","lines":["o"]},{"start":{"row":39,"column":34},"end":{"row":39,"column":35},"action":"insert","lines":["l"]},{"start":{"row":39,"column":35},"end":{"row":39,"column":36},"action":"insert","lines":["u"]},{"start":{"row":39,"column":36},"end":{"row":39,"column":37},"action":"insert","lines":["m"]},{"start":{"row":39,"column":37},"end":{"row":39,"column":38},"action":"insert","lines":["n"]}],[{"start":{"row":39,"column":38},"end":{"row":39,"column":40},"action":"insert","lines":["()"],"id":205}],[{"start":{"row":39,"column":39},"end":{"row":39,"column":40},"action":"insert","lines":["d"],"id":206},{"start":{"row":39,"column":40},"end":{"row":39,"column":41},"action":"insert","lines":["b"]},{"start":{"row":39,"column":41},"end":{"row":39,"column":42},"action":"insert","lines":["."]}],[{"start":{"row":39,"column":42},"end":{"row":39,"column":43},"action":"insert","lines":["B"],"id":207}],[{"start":{"row":39,"column":42},"end":{"row":39,"column":43},"action":"remove","lines":["B"],"id":208},{"start":{"row":39,"column":42},"end":{"row":39,"column":49},"action":"insert","lines":["Boolean"]}],[{"start":{"row":39,"column":50},"end":{"row":40,"column":0},"action":"insert","lines":["",""],"id":209},{"start":{"row":40,"column":0},"end":{"row":40,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":40,"column":4},"end":{"row":40,"column":50},"action":"insert","lines":["meal_allergen_nut_free = db.Column(db.Boolean)"],"id":210}],[{"start":{"row":40,"column":50},"end":{"row":41,"column":0},"action":"insert","lines":["",""],"id":211},{"start":{"row":41,"column":0},"end":{"row":41,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":41,"column":4},"end":{"row":41,"column":50},"action":"insert","lines":["meal_allergen_nut_free = db.Column(db.Boolean)"],"id":212}],[{"start":{"row":40,"column":18},"end":{"row":40,"column":21},"action":"remove","lines":["nut"],"id":213},{"start":{"row":40,"column":18},"end":{"row":40,"column":19},"action":"insert","lines":["l"]},{"start":{"row":40,"column":19},"end":{"row":40,"column":20},"action":"insert","lines":["a"]},{"start":{"row":40,"column":20},"end":{"row":40,"column":21},"action":"insert","lines":["c"]},{"start":{"row":40,"column":21},"end":{"row":40,"column":22},"action":"insert","lines":["t"]},{"start":{"row":40,"column":22},"end":{"row":40,"column":23},"action":"insert","lines":["o"]},{"start":{"row":40,"column":23},"end":{"row":40,"column":24},"action":"insert","lines":["e"]}],[{"start":{"row":40,"column":23},"end":{"row":40,"column":24},"action":"insert","lines":["s"],"id":214}],[{"start":{"row":41,"column":18},"end":{"row":41,"column":21},"action":"remove","lines":["nut"],"id":215},{"start":{"row":41,"column":18},"end":{"row":41,"column":19},"action":"insert","lines":["g"]},{"start":{"row":41,"column":19},"end":{"row":41,"column":20},"action":"insert","lines":["l"]},{"start":{"row":41,"column":20},"end":{"row":41,"column":21},"action":"insert","lines":["u"]},{"start":{"row":41,"column":21},"end":{"row":41,"column":22},"action":"insert","lines":["t"]},{"start":{"row":41,"column":22},"end":{"row":41,"column":23},"action":"insert","lines":["e"]},{"start":{"row":41,"column":23},"end":{"row":41,"column":24},"action":"insert","lines":["n"]}],[{"start":{"row":55,"column":45},"end":{"row":55,"column":61},"action":"remove","lines":[", nullable=False"],"id":216}],[{"start":{"row":64,"column":47},"end":{"row":64,"column":63},"action":"remove","lines":[", nullable=False"],"id":217}],[{"start":{"row":64,"column":16},"end":{"row":64,"column":20},"action":"remove","lines":["name"],"id":218},{"start":{"row":64,"column":16},"end":{"row":64,"column":17},"action":"insert","lines":["d"]},{"start":{"row":64,"column":17},"end":{"row":64,"column":18},"action":"insert","lines":["e"]},{"start":{"row":64,"column":18},"end":{"row":64,"column":19},"action":"insert","lines":["s"]},{"start":{"row":64,"column":19},"end":{"row":64,"column":20},"action":"insert","lines":["c"]},{"start":{"row":64,"column":20},"end":{"row":64,"column":21},"action":"insert","lines":["r"]}],[{"start":{"row":64,"column":21},"end":{"row":64,"column":22},"action":"insert","lines":["i"],"id":219},{"start":{"row":64,"column":22},"end":{"row":64,"column":23},"action":"insert","lines":["p"]},{"start":{"row":64,"column":23},"end":{"row":64,"column":24},"action":"insert","lines":["t"]},{"start":{"row":64,"column":24},"end":{"row":64,"column":25},"action":"insert","lines":["i"]},{"start":{"row":64,"column":25},"end":{"row":64,"column":26},"action":"insert","lines":["o"]},{"start":{"row":64,"column":26},"end":{"row":64,"column":27},"action":"insert","lines":["n"]}],[{"start":{"row":64,"column":16},"end":{"row":64,"column":27},"action":"remove","lines":["description"],"id":220},{"start":{"row":64,"column":16},"end":{"row":64,"column":17},"action":"insert","lines":["n"]},{"start":{"row":64,"column":17},"end":{"row":64,"column":18},"action":"insert","lines":["a"]},{"start":{"row":64,"column":18},"end":{"row":64,"column":19},"action":"insert","lines":["m"]},{"start":{"row":64,"column":19},"end":{"row":64,"column":20},"action":"insert","lines":["e"]}]]},"ace":{"folds":[],"scrolltop":600,"scrollleft":0,"selection":{"start":{"row":61,"column":19},"end":{"row":61,"column":19},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":true,"wrapToView":true},"firstLineState":{"row":54,"state":"start","mode":"ace/mode/python"}},"timestamp":1561049446178,"hash":"d4c2666c1fbf7a401e1b7c8e7fd279f467dd05b2"}