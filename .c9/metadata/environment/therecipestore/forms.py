{"changed":true,"filter":false,"title":"forms.py","tooltip":"/therecipestore/forms.py","value":"from flask_wtf import FlaskForm\nfrom flask_wtf.file import FileField, FileAllowed\nfrom wtforms import StringField, TextAreaField, PasswordField, SubmitField, BooleanField, FileField, RadioField, SelectField\nfrom wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError\nfrom flask_login import current_user\nfrom therecipestore.models import User, Recipe, Ingredient, Instruction\n\n\n\nclass Signup(FlaskForm):\n    firstname = StringField('Firstname', validators=[DataRequired()])\n    lastname = StringField('Lastname', validators=[DataRequired()])\n    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])\n    email = StringField('Email', validators=[DataRequired(), Email()])\n    password = PasswordField('Password', validators=[DataRequired()])\n    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])\n    submit = SubmitField('Sign Up')\n    \n    \"\"\"Check whether the username has been used before, if it has return an error to tell the user they must choose a different username\"\"\"\n    def validate_username(self, username):\n        user = User.query.filter_by(username=username.data).first()\n        if user:\n            raise ValidationError('An account with that username already exists, please try another.')\n\n    \"\"\"Check whether the email has been used before, if it has return an error to ask the user whether they already have an account\"\"\"\n    def validate_email(self, email):\n        user = User.query.filter_by(email=email.data).first()\n        if user:\n            raise ValidationError('That email is already taken by a member. Do you already have an account?')\n\n\n    \nclass Login(FlaskForm):\n    email = StringField('Email', validators=[DataRequired(), Email()])\n    password = PasswordField('Password', validators=[DataRequired()])\n    remember = BooleanField('Remember Me')\n    submit = SubmitField('Log In')\n\n\n\nclass UpdatePersonalHome(FlaskForm):\n    firstname = StringField('Firstname', validators=[DataRequired()])\n    lastname = StringField('Lastname', validators=[DataRequired()])\n    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])\n    email = StringField('Email', validators=[DataRequired(), Email()])\n    submit = SubmitField('Update Details')\n    \n    \"\"\"Ensure that the username has not been taken by another user previously, unless it is the current, logged in user\"\"\"\n    def validate_username(self, username):\n        if username.data != current_user.username:\n            user = User.query.filter_by(username=username.data).first()\n            if user:\n                raise ValidationError('An account with that username already exists, please try another.')\n                \n    \"\"\"Ensure that the email has not been taken by another user previously, unless it is the current, logged in user\"\"\"\n    def validate_email(self, email):\n        if email.data != current_user.email:\n            user = User.query.filter_by(email=email.data).first()\n            if user:\n                raise ValidationError('That email is already taken by a member. Do you already have an account?')\n                \n                \n\nclass CreateRecipe(FlaskForm):\n    recipe_name = StringField('Recipe Name', validators=[DataRequired(), Length(min=2, max=40)])\n    recipe_description = TextAreaField('Recipe Description', validators=[DataRequired()])\n    recipe_difficulty = SelectField('Difficulty Level', choices=[('value_''Easy'),('Medium'),('Difficult')], validators=[DataRequired()])\n    recipe_prep_time = StringField('Preparation Time', validators=[DataRequired()])\n    recipe_cook_time = StringField('Cooking Time', validators=[DataRequired()])\n    meal_type = RadioField('Meal Type', choices=[('value_one','Light Bites'),('value_two','Snacks'),('value_three','Main Meals'),('value_four','Desserts')], validators=[DataRequired()])\n    \n    meal_preference_vegetarian = BooleanField('Vegetarian')\n    meal_preference_vegan = BooleanField('Vegan')\n    meal_preference_pescatarian = BooleanField('Pescatarian')\n    meal_preference_raw_vegetarian = BooleanField('Raw Vegetarian')\n    \n    meal_allergen_nut_free = BooleanField('Nut Free')\n    meal_allergen_lactose_free = BooleanField('Lactose Free')\n    meal_allergen_gluten_free = BooleanField('Gluten Free')\n\n    ingredient_name = StringField('Recipe Ingredient', validators=[DataRequired()])\n    instruction_name = TextAreaField('Recipe Instruction', validators=[DataRequired()])\n    submit = SubmitField('Create Recipe')\n    \n\n#The following is for the like button on the recipe pages. This will add one to the recipe score when pressed.\nclass RateRecipe(FlaskForm):\n    submit = SubmitField('Like')","undoManager":{"mark":92,"position":100,"stack":[[{"start":{"row":74,"column":57},"end":{"row":74,"column":58},"action":"insert","lines":["a"],"id":347},{"start":{"row":74,"column":58},"end":{"row":74,"column":59},"action":"insert","lines":["n"]}],[{"start":{"row":75,"column":51},"end":{"row":75,"column":61},"action":"remove","lines":["Vegetarian"],"id":348},{"start":{"row":75,"column":51},"end":{"row":75,"column":52},"action":"insert","lines":["R"]},{"start":{"row":75,"column":52},"end":{"row":75,"column":53},"action":"insert","lines":["a"]},{"start":{"row":75,"column":53},"end":{"row":75,"column":54},"action":"insert","lines":["w"]}],[{"start":{"row":75,"column":54},"end":{"row":75,"column":55},"action":"insert","lines":[" "],"id":349},{"start":{"row":75,"column":55},"end":{"row":75,"column":56},"action":"insert","lines":["V"]},{"start":{"row":75,"column":56},"end":{"row":75,"column":57},"action":"insert","lines":["e"]},{"start":{"row":75,"column":57},"end":{"row":75,"column":58},"action":"insert","lines":["g"]},{"start":{"row":75,"column":58},"end":{"row":75,"column":59},"action":"insert","lines":["e"]},{"start":{"row":75,"column":59},"end":{"row":75,"column":60},"action":"insert","lines":["t"]},{"start":{"row":75,"column":60},"end":{"row":75,"column":61},"action":"insert","lines":["a"]},{"start":{"row":75,"column":61},"end":{"row":75,"column":62},"action":"insert","lines":["r"]},{"start":{"row":75,"column":62},"end":{"row":75,"column":63},"action":"insert","lines":["i"]},{"start":{"row":75,"column":63},"end":{"row":75,"column":64},"action":"insert","lines":["a"]},{"start":{"row":75,"column":64},"end":{"row":75,"column":65},"action":"insert","lines":["n"]}],[{"start":{"row":70,"column":156},"end":{"row":71,"column":0},"action":"insert","lines":["",""],"id":350},{"start":{"row":71,"column":0},"end":{"row":71,"column":4},"action":"insert","lines":["    "]},{"start":{"row":71,"column":4},"end":{"row":72,"column":0},"action":"insert","lines":["",""]},{"start":{"row":72,"column":0},"end":{"row":72,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":72,"column":0},"end":{"row":72,"column":4},"action":"remove","lines":["    "],"id":351},{"start":{"row":71,"column":4},"end":{"row":72,"column":0},"action":"remove","lines":["",""]},{"start":{"row":71,"column":0},"end":{"row":71,"column":4},"action":"remove","lines":["    "]},{"start":{"row":70,"column":156},"end":{"row":71,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":75,"column":67},"end":{"row":76,"column":0},"action":"insert","lines":["",""],"id":352},{"start":{"row":76,"column":0},"end":{"row":76,"column":4},"action":"insert","lines":["    "]},{"start":{"row":76,"column":4},"end":{"row":77,"column":0},"action":"insert","lines":["",""]},{"start":{"row":77,"column":0},"end":{"row":77,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":77,"column":4},"end":{"row":80,"column":67},"action":"insert","lines":["meal_preference_vegetarian = BooleanField('Vegetarian')","    meal_preference_vegan = BooleanField('Vegan')","    meal_preference_pescatarian = BooleanField('Pescatarian')","    meal_preference_raw_vegetarian = BooleanField('Raw Vegetarian')"],"id":353}],[{"start":{"row":77,"column":9},"end":{"row":77,"column":30},"action":"remove","lines":["preference_vegetarian"],"id":354},{"start":{"row":77,"column":9},"end":{"row":77,"column":10},"action":"insert","lines":["a"]},{"start":{"row":77,"column":10},"end":{"row":77,"column":11},"action":"insert","lines":["l"]},{"start":{"row":77,"column":11},"end":{"row":77,"column":12},"action":"insert","lines":["l"]},{"start":{"row":77,"column":12},"end":{"row":77,"column":13},"action":"insert","lines":["e"]},{"start":{"row":77,"column":13},"end":{"row":77,"column":14},"action":"insert","lines":["r"]},{"start":{"row":77,"column":14},"end":{"row":77,"column":15},"action":"insert","lines":["g"]},{"start":{"row":77,"column":15},"end":{"row":77,"column":16},"action":"insert","lines":["e"]},{"start":{"row":77,"column":16},"end":{"row":77,"column":17},"action":"insert","lines":["n"]}],[{"start":{"row":78,"column":4},"end":{"row":78,"column":25},"action":"remove","lines":["meal_preference_vegan"],"id":355},{"start":{"row":78,"column":4},"end":{"row":78,"column":17},"action":"insert","lines":["meal_allergen"]}],[{"start":{"row":79,"column":4},"end":{"row":79,"column":31},"action":"remove","lines":["meal_preference_pescatarian"],"id":356},{"start":{"row":79,"column":4},"end":{"row":79,"column":17},"action":"insert","lines":["meal_allergen"]}],[{"start":{"row":80,"column":4},"end":{"row":80,"column":34},"action":"remove","lines":["meal_preference_raw_vegetarian"],"id":357},{"start":{"row":80,"column":4},"end":{"row":80,"column":17},"action":"insert","lines":["meal_allergen"]}],[{"start":{"row":77,"column":17},"end":{"row":77,"column":18},"action":"insert","lines":["_"],"id":358},{"start":{"row":77,"column":18},"end":{"row":77,"column":19},"action":"insert","lines":["n"]},{"start":{"row":77,"column":19},"end":{"row":77,"column":20},"action":"insert","lines":["u"]},{"start":{"row":77,"column":20},"end":{"row":77,"column":21},"action":"insert","lines":["t"]}],[{"start":{"row":77,"column":21},"end":{"row":77,"column":22},"action":"insert","lines":["_"],"id":359},{"start":{"row":77,"column":22},"end":{"row":77,"column":23},"action":"insert","lines":["f"]},{"start":{"row":77,"column":23},"end":{"row":77,"column":24},"action":"insert","lines":["r"]},{"start":{"row":77,"column":24},"end":{"row":77,"column":25},"action":"insert","lines":["e"]},{"start":{"row":77,"column":25},"end":{"row":77,"column":26},"action":"insert","lines":["e"]}],[{"start":{"row":77,"column":43},"end":{"row":77,"column":53},"action":"remove","lines":["Vegetarian"],"id":360},{"start":{"row":77,"column":43},"end":{"row":77,"column":44},"action":"insert","lines":["N"]},{"start":{"row":77,"column":44},"end":{"row":77,"column":45},"action":"insert","lines":["u"]},{"start":{"row":77,"column":45},"end":{"row":77,"column":46},"action":"insert","lines":["t"]}],[{"start":{"row":77,"column":46},"end":{"row":77,"column":47},"action":"insert","lines":[" "],"id":361},{"start":{"row":77,"column":47},"end":{"row":77,"column":48},"action":"insert","lines":["F"]},{"start":{"row":77,"column":48},"end":{"row":77,"column":49},"action":"insert","lines":["r"]},{"start":{"row":77,"column":49},"end":{"row":77,"column":50},"action":"insert","lines":["e"]},{"start":{"row":77,"column":50},"end":{"row":77,"column":51},"action":"insert","lines":["e"]}],[{"start":{"row":78,"column":17},"end":{"row":78,"column":18},"action":"insert","lines":["_"],"id":362},{"start":{"row":78,"column":18},"end":{"row":78,"column":19},"action":"insert","lines":["l"]},{"start":{"row":78,"column":19},"end":{"row":78,"column":20},"action":"insert","lines":["a"]},{"start":{"row":78,"column":20},"end":{"row":78,"column":21},"action":"insert","lines":["c"]},{"start":{"row":78,"column":21},"end":{"row":78,"column":22},"action":"insert","lines":["t"]},{"start":{"row":78,"column":22},"end":{"row":78,"column":23},"action":"insert","lines":["o"]},{"start":{"row":78,"column":23},"end":{"row":78,"column":24},"action":"insert","lines":["s"]},{"start":{"row":78,"column":24},"end":{"row":78,"column":25},"action":"insert","lines":["e"]},{"start":{"row":78,"column":25},"end":{"row":78,"column":26},"action":"insert","lines":["_"]}],[{"start":{"row":78,"column":26},"end":{"row":78,"column":27},"action":"insert","lines":["f"],"id":363},{"start":{"row":78,"column":27},"end":{"row":78,"column":28},"action":"insert","lines":["r"]},{"start":{"row":78,"column":28},"end":{"row":78,"column":29},"action":"insert","lines":["e"]},{"start":{"row":78,"column":29},"end":{"row":78,"column":30},"action":"insert","lines":["e"]}],[{"start":{"row":78,"column":47},"end":{"row":78,"column":52},"action":"remove","lines":["Vegan"],"id":364},{"start":{"row":78,"column":47},"end":{"row":78,"column":48},"action":"insert","lines":["L"]},{"start":{"row":78,"column":48},"end":{"row":78,"column":49},"action":"insert","lines":["a"]},{"start":{"row":78,"column":49},"end":{"row":78,"column":50},"action":"insert","lines":["c"]},{"start":{"row":78,"column":50},"end":{"row":78,"column":51},"action":"insert","lines":["t"]},{"start":{"row":78,"column":51},"end":{"row":78,"column":52},"action":"insert","lines":["o"]},{"start":{"row":78,"column":52},"end":{"row":78,"column":53},"action":"insert","lines":["s"]},{"start":{"row":78,"column":53},"end":{"row":78,"column":54},"action":"insert","lines":["e"]}],[{"start":{"row":78,"column":54},"end":{"row":78,"column":55},"action":"insert","lines":[" "],"id":365},{"start":{"row":78,"column":55},"end":{"row":78,"column":56},"action":"insert","lines":["F"]},{"start":{"row":78,"column":56},"end":{"row":78,"column":57},"action":"insert","lines":["r"]},{"start":{"row":78,"column":57},"end":{"row":78,"column":58},"action":"insert","lines":["e"]},{"start":{"row":78,"column":58},"end":{"row":78,"column":59},"action":"insert","lines":["e"]}],[{"start":{"row":79,"column":17},"end":{"row":79,"column":18},"action":"insert","lines":["_"],"id":366},{"start":{"row":79,"column":18},"end":{"row":79,"column":19},"action":"insert","lines":["g"]},{"start":{"row":79,"column":19},"end":{"row":79,"column":20},"action":"insert","lines":["l"]},{"start":{"row":79,"column":20},"end":{"row":79,"column":21},"action":"insert","lines":["u"]},{"start":{"row":79,"column":21},"end":{"row":79,"column":22},"action":"insert","lines":["t"]},{"start":{"row":79,"column":22},"end":{"row":79,"column":23},"action":"insert","lines":["e"]},{"start":{"row":79,"column":23},"end":{"row":79,"column":24},"action":"insert","lines":["n"]},{"start":{"row":79,"column":24},"end":{"row":79,"column":25},"action":"insert","lines":["_"]},{"start":{"row":79,"column":25},"end":{"row":79,"column":26},"action":"insert","lines":["f"]},{"start":{"row":79,"column":26},"end":{"row":79,"column":27},"action":"insert","lines":["r"]}],[{"start":{"row":79,"column":27},"end":{"row":79,"column":28},"action":"insert","lines":["e"],"id":367},{"start":{"row":79,"column":28},"end":{"row":79,"column":29},"action":"insert","lines":["e"]}],[{"start":{"row":79,"column":46},"end":{"row":79,"column":57},"action":"remove","lines":["Pescatarian"],"id":368},{"start":{"row":79,"column":46},"end":{"row":79,"column":47},"action":"insert","lines":["G"]},{"start":{"row":79,"column":47},"end":{"row":79,"column":48},"action":"insert","lines":["l"]},{"start":{"row":79,"column":48},"end":{"row":79,"column":49},"action":"insert","lines":["u"]},{"start":{"row":79,"column":49},"end":{"row":79,"column":50},"action":"insert","lines":["t"]},{"start":{"row":79,"column":50},"end":{"row":79,"column":51},"action":"insert","lines":["e"]},{"start":{"row":79,"column":51},"end":{"row":79,"column":52},"action":"insert","lines":["n"]}],[{"start":{"row":79,"column":52},"end":{"row":79,"column":53},"action":"insert","lines":[" "],"id":369},{"start":{"row":79,"column":53},"end":{"row":79,"column":54},"action":"insert","lines":["F"]},{"start":{"row":79,"column":54},"end":{"row":79,"column":55},"action":"insert","lines":["r"]},{"start":{"row":79,"column":55},"end":{"row":79,"column":56},"action":"insert","lines":["e"]},{"start":{"row":79,"column":56},"end":{"row":79,"column":57},"action":"insert","lines":["e"]}],[{"start":{"row":80,"column":0},"end":{"row":80,"column":50},"action":"remove","lines":["    meal_allergen = BooleanField('Raw Vegetarian')"],"id":370},{"start":{"row":79,"column":59},"end":{"row":80,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":80,"column":0},"end":{"row":81,"column":140},"action":"remove","lines":["    ","    meal_allergen = BooleanField('Meal Type', choices=[('value_one','Nut Free'),('value_two','Lactose Free'),('value_three','Gluten Free')])"],"id":371}],[{"start":{"row":88,"column":26},"end":{"row":88,"column":38},"action":"remove","lines":["Score Recipe"],"id":372},{"start":{"row":88,"column":26},"end":{"row":88,"column":27},"action":"insert","lines":["L"]},{"start":{"row":88,"column":27},"end":{"row":88,"column":28},"action":"insert","lines":["i"]},{"start":{"row":88,"column":28},"end":{"row":88,"column":29},"action":"insert","lines":["k"]},{"start":{"row":88,"column":29},"end":{"row":88,"column":30},"action":"insert","lines":["e"]}],[{"start":{"row":64,"column":0},"end":{"row":64,"column":91},"action":"remove","lines":["    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])"],"id":373},{"start":{"row":63,"column":30},"end":{"row":64,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":80,"column":4},"end":{"row":80,"column":11},"action":"remove","lines":["recipe_"],"id":374}],[{"start":{"row":81,"column":4},"end":{"row":81,"column":11},"action":"remove","lines":["recipe_"],"id":375}],[{"start":{"row":80,"column":14},"end":{"row":80,"column":15},"action":"insert","lines":["_"],"id":376},{"start":{"row":80,"column":15},"end":{"row":80,"column":16},"action":"insert","lines":["n"]},{"start":{"row":80,"column":16},"end":{"row":80,"column":17},"action":"insert","lines":["a"]},{"start":{"row":80,"column":17},"end":{"row":80,"column":18},"action":"insert","lines":["e"]},{"start":{"row":80,"column":18},"end":{"row":80,"column":19},"action":"insert","lines":["m"]}],[{"start":{"row":80,"column":18},"end":{"row":80,"column":19},"action":"remove","lines":["m"],"id":377},{"start":{"row":80,"column":17},"end":{"row":80,"column":18},"action":"remove","lines":["e"]}],[{"start":{"row":80,"column":17},"end":{"row":80,"column":18},"action":"insert","lines":["m"],"id":378},{"start":{"row":80,"column":18},"end":{"row":80,"column":19},"action":"insert","lines":["e"]}],[{"start":{"row":81,"column":15},"end":{"row":81,"column":16},"action":"insert","lines":["_"],"id":379},{"start":{"row":81,"column":16},"end":{"row":81,"column":17},"action":"insert","lines":["n"]},{"start":{"row":81,"column":17},"end":{"row":81,"column":18},"action":"insert","lines":["a"]},{"start":{"row":81,"column":18},"end":{"row":81,"column":19},"action":"insert","lines":["m"]},{"start":{"row":81,"column":19},"end":{"row":81,"column":20},"action":"insert","lines":["e"]}],[{"start":{"row":80,"column":53},"end":{"row":80,"column":81},"action":"insert","lines":[", validators=[DataRequired()"],"id":380}],[{"start":{"row":80,"column":81},"end":{"row":80,"column":82},"action":"insert","lines":["]"],"id":381}],[{"start":{"row":81,"column":56},"end":{"row":81,"column":84},"action":"insert","lines":[", validators=[DataRequired()"],"id":382}],[{"start":{"row":81,"column":84},"end":{"row":81,"column":85},"action":"insert","lines":["]"],"id":383}],[{"start":{"row":81,"column":45},"end":{"row":81,"column":55},"action":"remove","lines":["Ingredient"],"id":384},{"start":{"row":81,"column":45},"end":{"row":81,"column":46},"action":"insert","lines":["I"]},{"start":{"row":81,"column":46},"end":{"row":81,"column":47},"action":"insert","lines":["n"]},{"start":{"row":81,"column":47},"end":{"row":81,"column":48},"action":"insert","lines":["s"]},{"start":{"row":81,"column":48},"end":{"row":81,"column":49},"action":"insert","lines":["t"]},{"start":{"row":81,"column":49},"end":{"row":81,"column":50},"action":"insert","lines":["r"]},{"start":{"row":81,"column":50},"end":{"row":81,"column":51},"action":"insert","lines":["u"]},{"start":{"row":81,"column":51},"end":{"row":81,"column":52},"action":"insert","lines":["c"]},{"start":{"row":81,"column":52},"end":{"row":81,"column":53},"action":"insert","lines":["t"]},{"start":{"row":81,"column":53},"end":{"row":81,"column":54},"action":"insert","lines":["i"]},{"start":{"row":81,"column":54},"end":{"row":81,"column":55},"action":"insert","lines":["o"]},{"start":{"row":81,"column":55},"end":{"row":81,"column":56},"action":"insert","lines":["n"]}],[{"start":{"row":69,"column":155},"end":{"row":69,"column":156},"action":"insert","lines":[","],"id":385}],[{"start":{"row":69,"column":156},"end":{"row":69,"column":157},"action":"insert","lines":[" "],"id":386}],[{"start":{"row":69,"column":157},"end":{"row":69,"column":185},"action":"insert","lines":[", validators=[DataRequired()"],"id":387}],[{"start":{"row":69,"column":158},"end":{"row":69,"column":159},"action":"remove","lines":[" "],"id":388},{"start":{"row":69,"column":157},"end":{"row":69,"column":158},"action":"remove","lines":[","]}],[{"start":{"row":69,"column":183},"end":{"row":69,"column":184},"action":"insert","lines":["]"],"id":389}],[{"start":{"row":35,"column":0},"end":{"row":35,"column":42},"action":"remove","lines":["    remember = BooleanField('Remember Me')"],"id":390},{"start":{"row":34,"column":69},"end":{"row":35,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":68,"column":50},"end":{"row":68,"column":62},"action":"remove","lines":["'value_one',"],"id":391}],[{"start":{"row":68,"column":66},"end":{"row":68,"column":78},"action":"remove","lines":["'value_two',"],"id":392}],[{"start":{"row":68,"column":77},"end":{"row":68,"column":91},"action":"remove","lines":["'value_three',"],"id":393}],[{"start":{"row":68,"column":92},"end":{"row":68,"column":105},"action":"remove","lines":["'value_four',"],"id":394}],[{"start":{"row":65,"column":66},"end":{"row":65,"column":78},"action":"remove","lines":["'value_one',"],"id":395}],[{"start":{"row":65,"column":75},"end":{"row":65,"column":87},"action":"remove","lines":["'value_two',"],"id":396}],[{"start":{"row":65,"column":86},"end":{"row":65,"column":100},"action":"remove","lines":["'value_three',"],"id":397}],[{"start":{"row":65,"column":66},"end":{"row":65,"column":67},"action":"insert","lines":["V"],"id":398},{"start":{"row":65,"column":67},"end":{"row":65,"column":68},"action":"insert","lines":["a"]},{"start":{"row":65,"column":68},"end":{"row":65,"column":69},"action":"insert","lines":["l"]},{"start":{"row":65,"column":69},"end":{"row":65,"column":70},"action":"insert","lines":["u"]},{"start":{"row":65,"column":70},"end":{"row":65,"column":71},"action":"insert","lines":["e"]}],[{"start":{"row":65,"column":70},"end":{"row":65,"column":71},"action":"remove","lines":["e"],"id":399},{"start":{"row":65,"column":69},"end":{"row":65,"column":70},"action":"remove","lines":["u"]},{"start":{"row":65,"column":68},"end":{"row":65,"column":69},"action":"remove","lines":["l"]},{"start":{"row":65,"column":67},"end":{"row":65,"column":68},"action":"remove","lines":["a"]},{"start":{"row":65,"column":66},"end":{"row":65,"column":67},"action":"remove","lines":["V"]}],[{"start":{"row":65,"column":66},"end":{"row":65,"column":67},"action":"insert","lines":["V"],"id":400},{"start":{"row":65,"column":67},"end":{"row":65,"column":68},"action":"insert","lines":["a"]},{"start":{"row":65,"column":68},"end":{"row":65,"column":69},"action":"insert","lines":["l"]},{"start":{"row":65,"column":69},"end":{"row":65,"column":70},"action":"insert","lines":["u"]},{"start":{"row":65,"column":70},"end":{"row":65,"column":71},"action":"insert","lines":["e"]}],[{"start":{"row":65,"column":71},"end":{"row":65,"column":72},"action":"insert","lines":["_"],"id":401}],[{"start":{"row":65,"column":71},"end":{"row":65,"column":72},"action":"remove","lines":["_"],"id":402},{"start":{"row":65,"column":70},"end":{"row":65,"column":71},"action":"remove","lines":["e"]},{"start":{"row":65,"column":69},"end":{"row":65,"column":70},"action":"remove","lines":["u"]},{"start":{"row":65,"column":68},"end":{"row":65,"column":69},"action":"remove","lines":["l"]},{"start":{"row":65,"column":67},"end":{"row":65,"column":68},"action":"remove","lines":["a"]},{"start":{"row":65,"column":66},"end":{"row":65,"column":67},"action":"remove","lines":["V"]}],[{"start":{"row":65,"column":66},"end":{"row":65,"column":68},"action":"insert","lines":["''"],"id":403}],[{"start":{"row":65,"column":67},"end":{"row":65,"column":68},"action":"insert","lines":["v"],"id":404},{"start":{"row":65,"column":68},"end":{"row":65,"column":69},"action":"insert","lines":["a"]},{"start":{"row":65,"column":69},"end":{"row":65,"column":70},"action":"insert","lines":["l"]},{"start":{"row":65,"column":70},"end":{"row":65,"column":71},"action":"insert","lines":["u"]},{"start":{"row":65,"column":71},"end":{"row":65,"column":72},"action":"insert","lines":["e"]}],[{"start":{"row":65,"column":72},"end":{"row":65,"column":73},"action":"insert","lines":["_"],"id":405},{"start":{"row":65,"column":73},"end":{"row":65,"column":74},"action":"insert","lines":["o"]},{"start":{"row":65,"column":74},"end":{"row":65,"column":75},"action":"insert","lines":["n"]},{"start":{"row":65,"column":75},"end":{"row":65,"column":76},"action":"insert","lines":["e"]}],[{"start":{"row":65,"column":77},"end":{"row":65,"column":78},"action":"insert","lines":[","],"id":406}],[{"start":{"row":65,"column":87},"end":{"row":65,"column":98},"action":"insert","lines":["'value_one'"],"id":407}],[{"start":{"row":65,"column":98},"end":{"row":65,"column":99},"action":"insert","lines":[","],"id":408}],[{"start":{"row":65,"column":110},"end":{"row":65,"column":121},"action":"insert","lines":["'value_one'"],"id":409}],[{"start":{"row":65,"column":121},"end":{"row":65,"column":122},"action":"insert","lines":[","],"id":410}],[{"start":{"row":65,"column":94},"end":{"row":65,"column":97},"action":"remove","lines":["one"],"id":411},{"start":{"row":65,"column":94},"end":{"row":65,"column":95},"action":"insert","lines":["t"]},{"start":{"row":65,"column":95},"end":{"row":65,"column":96},"action":"insert","lines":["w"]},{"start":{"row":65,"column":96},"end":{"row":65,"column":97},"action":"insert","lines":["o"]}],[{"start":{"row":65,"column":117},"end":{"row":65,"column":120},"action":"remove","lines":["one"],"id":412},{"start":{"row":65,"column":117},"end":{"row":65,"column":118},"action":"insert","lines":["t"]},{"start":{"row":65,"column":118},"end":{"row":65,"column":119},"action":"insert","lines":["h"]},{"start":{"row":65,"column":119},"end":{"row":65,"column":120},"action":"insert","lines":["r"]},{"start":{"row":65,"column":120},"end":{"row":65,"column":121},"action":"insert","lines":["e"]},{"start":{"row":65,"column":121},"end":{"row":65,"column":122},"action":"insert","lines":["e"]}],[{"start":{"row":68,"column":50},"end":{"row":68,"column":61},"action":"insert","lines":["'value_one'"],"id":413}],[{"start":{"row":68,"column":61},"end":{"row":68,"column":62},"action":"insert","lines":[","],"id":414}],[{"start":{"row":68,"column":78},"end":{"row":68,"column":89},"action":"insert","lines":["'value_one'"],"id":415}],[{"start":{"row":68,"column":89},"end":{"row":68,"column":90},"action":"insert","lines":[","],"id":416}],[{"start":{"row":68,"column":85},"end":{"row":68,"column":88},"action":"remove","lines":["one"],"id":417},{"start":{"row":68,"column":85},"end":{"row":68,"column":86},"action":"insert","lines":["t"]},{"start":{"row":68,"column":86},"end":{"row":68,"column":87},"action":"insert","lines":["w"]},{"start":{"row":68,"column":87},"end":{"row":68,"column":88},"action":"insert","lines":["o"]}],[{"start":{"row":68,"column":101},"end":{"row":68,"column":112},"action":"insert","lines":["'value_one'"],"id":418}],[{"start":{"row":68,"column":112},"end":{"row":68,"column":113},"action":"insert","lines":[","],"id":419}],[{"start":{"row":68,"column":108},"end":{"row":68,"column":111},"action":"remove","lines":["one"],"id":420},{"start":{"row":68,"column":108},"end":{"row":68,"column":109},"action":"insert","lines":["t"]},{"start":{"row":68,"column":109},"end":{"row":68,"column":110},"action":"insert","lines":["w"]},{"start":{"row":68,"column":110},"end":{"row":68,"column":111},"action":"insert","lines":["o"]}],[{"start":{"row":68,"column":108},"end":{"row":68,"column":111},"action":"remove","lines":["two"],"id":421},{"start":{"row":68,"column":108},"end":{"row":68,"column":109},"action":"insert","lines":["t"]},{"start":{"row":68,"column":109},"end":{"row":68,"column":110},"action":"insert","lines":["h"]},{"start":{"row":68,"column":110},"end":{"row":68,"column":111},"action":"insert","lines":["r"]},{"start":{"row":68,"column":111},"end":{"row":68,"column":112},"action":"insert","lines":["r"]}],[{"start":{"row":68,"column":111},"end":{"row":68,"column":112},"action":"remove","lines":["r"],"id":422}],[{"start":{"row":68,"column":111},"end":{"row":68,"column":112},"action":"insert","lines":["e"],"id":423},{"start":{"row":68,"column":112},"end":{"row":68,"column":113},"action":"insert","lines":["e"]}],[{"start":{"row":68,"column":130},"end":{"row":68,"column":141},"action":"insert","lines":["'value_one'"],"id":424}],[{"start":{"row":68,"column":141},"end":{"row":68,"column":142},"action":"insert","lines":[","],"id":425}],[{"start":{"row":68,"column":137},"end":{"row":68,"column":140},"action":"remove","lines":["one"],"id":426},{"start":{"row":68,"column":137},"end":{"row":68,"column":138},"action":"insert","lines":["f"]},{"start":{"row":68,"column":138},"end":{"row":68,"column":139},"action":"insert","lines":["o"]},{"start":{"row":68,"column":139},"end":{"row":68,"column":140},"action":"insert","lines":["u"]},{"start":{"row":68,"column":140},"end":{"row":68,"column":141},"action":"insert","lines":["e"]},{"start":{"row":68,"column":141},"end":{"row":68,"column":142},"action":"insert","lines":["r"]}],[{"start":{"row":68,"column":141},"end":{"row":68,"column":142},"action":"remove","lines":["r"],"id":427},{"start":{"row":68,"column":140},"end":{"row":68,"column":141},"action":"remove","lines":["e"]}],[{"start":{"row":68,"column":140},"end":{"row":68,"column":141},"action":"insert","lines":["r"],"id":428}],[{"start":{"row":34,"column":69},"end":{"row":35,"column":0},"action":"insert","lines":["",""],"id":429},{"start":{"row":35,"column":0},"end":{"row":35,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":35,"column":4},"end":{"row":35,"column":42},"action":"insert","lines":["remember = BooleanField('Remember Me')"],"id":430}],[{"start":{"row":66,"column":66},"end":{"row":66,"column":78},"action":"remove","lines":["'value_one',"],"id":431}],[{"start":{"row":66,"column":75},"end":{"row":66,"column":87},"action":"remove","lines":["'value_two',"],"id":432}],[{"start":{"row":66,"column":86},"end":{"row":66,"column":100},"action":"remove","lines":["'value_three',"],"id":433}],[{"start":{"row":66,"column":65},"end":{"row":66,"column":66},"action":"remove","lines":["("],"id":434}],[{"start":{"row":66,"column":71},"end":{"row":66,"column":72},"action":"remove","lines":[")"],"id":435}],[{"start":{"row":66,"column":72},"end":{"row":66,"column":73},"action":"remove","lines":["("],"id":436}],[{"start":{"row":66,"column":80},"end":{"row":66,"column":81},"action":"remove","lines":[")"],"id":437}],[{"start":{"row":66,"column":81},"end":{"row":66,"column":82},"action":"remove","lines":["("],"id":438}],[{"start":{"row":66,"column":92},"end":{"row":66,"column":93},"action":"remove","lines":[")"],"id":439}],[{"start":{"row":66,"column":65},"end":{"row":66,"column":66},"action":"insert","lines":["("],"id":440}],[{"start":{"row":66,"column":72},"end":{"row":66,"column":73},"action":"insert","lines":[")"],"id":441}],[{"start":{"row":66,"column":74},"end":{"row":66,"column":75},"action":"insert","lines":["("],"id":442}],[{"start":{"row":66,"column":83},"end":{"row":66,"column":84},"action":"insert","lines":[")"],"id":443}],[{"start":{"row":66,"column":85},"end":{"row":66,"column":86},"action":"insert","lines":["("],"id":444}],[{"start":{"row":66,"column":97},"end":{"row":66,"column":98},"action":"insert","lines":[")"],"id":445}],[{"start":{"row":66,"column":66},"end":{"row":66,"column":68},"action":"insert","lines":["''"],"id":446}],[{"start":{"row":66,"column":67},"end":{"row":66,"column":68},"action":"insert","lines":["v"],"id":447},{"start":{"row":66,"column":68},"end":{"row":66,"column":69},"action":"insert","lines":["a"]},{"start":{"row":66,"column":69},"end":{"row":66,"column":70},"action":"insert","lines":["l"]},{"start":{"row":66,"column":70},"end":{"row":66,"column":71},"action":"insert","lines":["u"]},{"start":{"row":66,"column":71},"end":{"row":66,"column":72},"action":"insert","lines":["e"]},{"start":{"row":66,"column":72},"end":{"row":66,"column":73},"action":"insert","lines":["_"]}]]},"ace":{"folds":[],"scrolltop":675,"scrollleft":0,"selection":{"start":{"row":66,"column":73},"end":{"row":66,"column":73},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":true,"wrapToView":true},"firstLineState":{"row":43,"state":"start","mode":"ace/mode/python"}},"timestamp":1562664630528}