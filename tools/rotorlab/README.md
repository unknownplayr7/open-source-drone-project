# RotorLab

A small, dependency-free multirotor sizing sandbox for learning the trade-offs between aircraft mass, motor thrust, and battery endurance.

## Run it

Open `index.html` in any modern browser. No install, server, account, or build step required. It works offline.

## What it estimates

- **Maximum thrust-to-weight ratio:** total listed maximum static thrust divided by all-up mass.
- **Ideal hover thrust per motor:** aircraft mass divided by the number of thrust-producing motors.
- **Usable battery energy:** nominal voltage × capacity × the fraction remaining after the selected reserve.
- **Theoretical endurance:** usable amp-hours divided by average total flight current.

The calculator updates locally as you type. Inputs are not sent anywhere.

## Limitations

These are rough first-pass estimates, not flight-performance predictions or a safety certification. Real thrust depends on the exact motor/propeller/voltage combination. Real endurance varies with throttle, voltage sag, wind, temperature, battery condition, and flight profile. Static thrust-to-weight ratio does not establish controllability or structural safety.

Before building or flying, check manufacturer data and all motor, propeller, ESC, battery, and frame ratings; test safely; and follow applicable laws and airspace restrictions. Remove propellers during bench electronics work whenever practical.

## License

MIT. See the parent repository's license.
