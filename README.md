# Thermal Outage Calculation

This repository calculates the thermal outages given a temperature profile for a region. 

## Running the thermal outage rates.

Add your temperature profiles in `thermal_outage/input_temps`.

The data format of the temperature profiles should have the following columns:

- `Year`
- `Month`
- `Day`
- `Hour`
- `Minute`
- `Temperature`

To run the script, use the following command:

```sh
python thermal_outage_run.py --input_dir path/to/input --output_dir path/to/output