from os import path
from flask import *
from flask_cors import CORS
from gpio_controller import GpioController


build_path = path.abspath('./views/build/')
static_path = path.abspath('./views/build/static/')
app = Flask(__name__, static_folder=static_path, template_folder=build_path)
CORS(app)

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
    return jsonify({"result": "set pin out"})


@app.route('/gpio/<int:pin_number>/in')
def gpio_in(pin_number):
    controller.cleanup_pin(pin_number)
    controller.setup_pin_in_mode(pin_number)
    return jsonify({"result": "set pin in"})


@app.route('/gpio/<int:pin_number>/read', methods=["GET"])
def gpio_read(pin_number):
    gpio_input = controller.read_pin_input(pin_number)
    return jsonify({"gpio_input": str(gpio_input)})


@app.route('/gpio/<int:pin_number>/pwm', methods=["POST"])
def gpio_pwm(pin_number):
    params = request.json
    controller.cleanup_pin(pin_number)
    controller.setup_pin_pwm_mode(pin_number, int(params['frequency']))
    return jsonify({"result": "pwm done "})


@app.route('/gpio/<int:pin_number>/pwm/start', methods=["POST"])
def gpio_pwm_start(pin_number):
    params = request.json
    controller.start_pwm(pin_number, params['duty_ratio'])
    return jsonify({"result": "pwm start"})


@app.route('/gpio/<int:pin_number>/pwm/stop', methods=["GET"])
def gpio_pwm_stop(pin_number):
    controller.stop_pwm(pin_number)
    return jsonify({"result": "pwm stop"})


if __name__ == "__main__":
    app.run(host='8.8.8.8')
