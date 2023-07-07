#Random number generator in flask python
#lets import flask first
from flask import Flask, render_template
#lets import render_template() to render html templates
import random
#lets create our first app

app = Flask(__name__)

#lets create our first route
@app.route('/')
#lets create a function for route
def random_gen():
    #lets import random
    rand_value  = random.randint(100,1000) 
    # first value(zero) is min 
    # last value(100) is max value
    #lets pass this random value to html template
    return render_template('index.html', rand_value = rand_value)

#lets run our app
app.run(debug=True, port = 8080)
#final step to create a templates folder and index.html file