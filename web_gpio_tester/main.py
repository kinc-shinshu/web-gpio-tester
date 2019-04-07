from os import path 
from flask import *

build_path = path.abspath('./views/build/')
static_path = path.abspath('./views/build/static/')
app = Flask(__name__, static_folder=static_path, template_folder=build_path)

@app.route('/')
def render_index():
    name = "hello, world"
    return render_template(['index.html'], title=name)


if __name__ == "__main__":
    app.run()
    
    
