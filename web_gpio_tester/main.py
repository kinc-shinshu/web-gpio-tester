from os import path
from flask import *
from gpio_controller import GpioController


build_path = path.abspath('./views/build/')
static_path = path.abspath('./views/build/static/')
app = Flask(__name__, static_folder=static_path, template_folder=build_path)


controller = GpioController()


@app.route('/')
def render_index():
    name = "hello, world"
    return render_template('index.html', title=name)


@app.route('/gpio/<int:pin_number>/out', methods=["POST"])
def gpio_out(pin_number):
    params = request.json
    controller.cleanup_pin(pin_number)
    controller.setup_pin_output_mode(pin_number)
    controller.set_output(pin_number, int(params["value"]))
    return jsonify(params)


if __name__ == "__main__":
    app.run()
