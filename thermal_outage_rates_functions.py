import pandas as pd # type: ignore
import os
import numpy as np


# Define the data for the DataFrame
thermal_forced_outage_rates = pd.DataFrame({
    "Temperature (Celsius)": [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35],
    "CC": [0.149, 0.081, 0.048, 0.033, 0.027, 0.025, 0.028, 0.035, 0.035, 0.041, 0.072],
    "CT": [0.199, 0.099, 0.051, 0.031, 0.024, 0.022, 0.024, 0.027, 0.031, 0.039, 0.066],
    "DS": [0.212, 0.170, 0.137, 0.116, 0.106, 0.102, 0.104, 0.136, 0.135, 0.143, 0.175],
    "HD": [0.070, 0.043, 0.032, 0.027, 0.026, 0.026, 0.027, 0.027, 0.025, 0.029, 0.082],
    "NU": [0.019, 0.018, 0.017, 0.018, 0.018, 0.019, 0.021, 0.027, 0.037, 0.066, 0.0124],
    "ST": [0.133, 0.112, 0.099, 0.091, 0.086, 0.083, 0.084, 0.086, 0.094, 0.114, 0.140],
})


def get_outage_rate_by_temperature(temperature, plant_type):
    """
    Get the forced outage rate for a specific temperature and plant type.
    If the temperature is not in the DataFrame, the function will interpolate the value.
    """
    # Check if the temperature is in the DataFrame
    if temperature in thermal_forced_outage_rates["Temperature (Celsius)"].values:
        return thermal_forced_outage_rates[plant_type][thermal_forced_outage_rates["Temperature (Celsius)"] == temperature].values[0]
    else:
        # Interpolate the value
        return np.interp(temperature, thermal_forced_outage_rates["Temperature (Celsius)"], thermal_forced_outage_rates[plant_type])


def get_outage_curve(df_temperature, plant_type):
    """
    Get the forced outage rate for a DataFrame of temperatures and a specific plant type.
    Returns a new DataFrame with the outage rates and timestamps.
    """
    # Convert temperature DataFrame to include timestamps
    df_temperature = convert_to_timestamp(df_temperature)
    
    # Compute outage rates using vectorized operations
    df_temperature["Outage Rate"] = df_temperature["Temperature"].apply(
        lambda temp: get_outage_rate_by_temperature(temp, plant_type)
    )
    
    # Select relevant columns for output
    return df_temperature[["Timestamp", "Outage Rate"]]


def convert_to_timestamp(df):
    """
    Convert the DataFrame to a timestamp. The columns of the dataframe should be 'Year', 'Month', 'Day', 'Hour', 'Minute'.
    The other columns should remain intact and still be in the returned DataFrame.
    
    Parameters:
        df (pd.DataFrame): Input DataFrame with 'Year', 'Month', 'Day', 'Hour', 'Minute' columns.
    
    Returns:
        pd.DataFrame: DataFrame with a new 'Timestamp' column.
    """
    df["Timestamp"] = pd.to_datetime(df[["Year", "Month", "Day", "Hour", "Minute"]])
    
    return df

# p10, p13, p27, p28, p39, p40, p52, p53, p94, p95, p96, p97