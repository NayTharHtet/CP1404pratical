from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/f/<celsius_str>')
def convert_temperature(celsius_str):
    try:
        celsius = float(celsius_str)
        fahrenheit = celsius_to_fahrenheit(celsius)
        return f"The temperature {celsius}°C is equal to {fahrenheit}°F."
    except ValueError:
        return "Invalid input. Please enter a valid Celsius temperature."


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit



if __name__ == '__main__':
    app.run()
