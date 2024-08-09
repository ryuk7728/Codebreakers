from flask import Flask, jsonify, request
import numpy as np
import random

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_parameters():
    k = 8
    api_input = request.args.get('type')

    # Engine Parameters
    mu_oilpressure = 45
    sigma_oilpressure = 20
    eng_oilpressure = np.random.normal(mu_oilpressure, sigma_oilpressure)
    if eng_oilpressure < 0:
        eng_oilpressure = 10 + random.uniform(0, 5)
    if random.randint(1, k) == 1:
        eng_oilpressure = 65 + random.uniform(0, 5)

    mu_enginespeed = 900
    sigma_enginespeed = 450
    eng_speed = np.random.normal(mu_enginespeed, sigma_enginespeed)
    if eng_speed < 0:
        eng_speed = 600 + random.uniform(0, 5)
    if random.randint(1, k) == 1:
        eng_speed = 1800 + random.uniform(10, 100)

    mu_enginetemp = 52
    sigma_enginetemp = 26
    eng_temp = np.random.normal(mu_enginetemp, sigma_enginetemp)
    if eng_temp < 0:
        eng_temp = 30 + random.uniform(0, 5)
    if random.randint(1, k) == 1:
        eng_temp = 105 + random.uniform(1, 10)

    # Drive Parameters
    mu_brakecontrol = 5
    sigma_brakecontrol = 2.5
    brake_control = np.random.normal(mu_brakecontrol, sigma_brakecontrol)
    if brake_control < 0:
        brake_control = 2 + random.uniform(0, 1)
    if random.randint(1, k) == 1:
        brake_control = 1 - random.uniform(0, 1)

    mu_transpressure = 325
    sigma_transpressure = 62
    trans_pressure = np.random.normal(mu_transpressure, sigma_transpressure)
    if trans_pressure < 0:
        trans_pressure = 200 + random.uniform(0, 10)
    if random.randint(1, k) == 1:
        trans_pressure = 200 + random.uniform(10, 30)

    mu_pedalsens = 2.5
    sigma_pedalsens = 1.25
    pedal_sens = np.random.normal(mu_pedalsens, sigma_pedalsens)
    if pedal_sens < 0:
        pedal_sens = 1 + random.uniform(0, 0.5)
    if random.randint(1, k) == 1:
        pedal_sens = 4.7 + random.uniform(0.1, 3)

    # Fuel Parameters
    mu_waterfuel = 900
    sigma_waterfuel = 450
    water_fuel = np.random.normal(mu_waterfuel, sigma_waterfuel)
    if water_fuel < 0:
        water_fuel = 500 + random.uniform(0, 20)
    if random.randint(1, k) == 1:
        water_fuel = 1800 + random.uniform(10, 100)

    mu_fuellevel = 7.5
    sigma_fuellevel = 4
    fuel_level = np.random.normal(mu_fuellevel, sigma_fuellevel)
    if fuel_level < 0:
        fuel_level = 3 + random.uniform(0, 1)
    if random.randint(1, k) == 1:
        fuel_level = 1 - random.uniform(0.2, 1)

    mu_fuelpressure = 50
    sigma_fuelpressure = 7.5
    fuel_pressure = np.random.normal(mu_fuelpressure, sigma_fuelpressure)
    if fuel_pressure < 0:
        fuel_pressure = 40 + random.uniform(0, 2)
    if random.randint(1, k) == 1:
        fuel_pressure = 65 + random.uniform(0, 10)

    mu_fueltemp = 200
    sigma_fueltemp = 100
    fuel_temp = np.random.normal(mu_fueltemp, sigma_fueltemp)
    if fuel_temp < 0:
        fuel_temp = 120 + random.uniform(0, 10)
    if random.randint(1, k) == 1:
        fuel_temp = 400 + random.uniform(1, 30)

    # Miscellaneous Parameters
    mu_sysvolt = 13.5
    sigma_sysvolt = 0.75
    sys_volt = np.random.normal(mu_sysvolt, sigma_sysvolt)
    if sys_volt < 0:
        sys_volt = 10 + random.uniform(0, 1)
    if random.randint(1, k) == 1:
        sys_volt = 12 - random.uniform(0.1, 5)

    mu_exhausttemp = 182
    sigma_exhausttemp = 90
    exhaust_temp = np.random.normal(mu_exhausttemp, sigma_exhausttemp)
    if exhaust_temp < 0:
        exhaust_temp = 100 + random.uniform(0, 10)
    if random.randint(1, k) == 1:
        exhaust_temp = 365 + random.uniform(1, 30)

    mu_hydpump = 62
    sigma_hydpump = 31
    hyd_pump = np.random.normal(mu_hydpump, sigma_hydpump)
    if hyd_pump < 0:
        hyd_pump = 30 + random.uniform(0, 10)
    if random.randint(1, k) == 1:
        hyd_pump = 125 + random.uniform(1, 20)

    mu_airpressure = 10
    sigma_airpressure = 5
    air_pressure = np.random.normal(mu_airpressure, sigma_airpressure)
    if air_pressure < 0:
        air_pressure = 5 + random.uniform(0, 2)
    if random.randint(1, k) == 1:
        air_pressure = 20 - random.uniform(1, 5)

    if api_input == "engine":
        return jsonify({
            "eng_temp": eng_temp,
            "eng_oilpressure": eng_oilpressure,
            "eng_speed": eng_speed
        })

    if api_input == "drive":
        return jsonify({
            "trans_pressure": trans_pressure,
            "brake_control": brake_control,
            "pedal_sens": pedal_sens
        })

    if api_input == "fuel":
        return jsonify({
            "water_fuel": water_fuel,
            "fuel_temp": fuel_temp,
            "fuel_level": fuel_level,
            "fuel_pressure": fuel_pressure
        })

    if api_input == "misc":
        return jsonify({
            "exhaust_temp": exhaust_temp,
            "air_pressure": air_pressure,
            "sys_volt": sys_volt,
            "hyd_pump": hyd_pump
        })

    return jsonify({"error": "Invalid input"}), 400


if __name__ == '__main__':
    app.run(debug=True)
