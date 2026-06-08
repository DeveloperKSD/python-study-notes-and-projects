import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(101)

base_times = pd.date_range(start="2026-06-08 00:00:00", periods=50, freq='h')

raw_data = {
    'Timestamp': base_times,
    'Power_Output_Raw': np.random.choice(['50', '65', '120kW', 'ERROR', '85', 'NaN', '95'], size=50),
    'Temperature_Sensor': np.random.normal(loc=40.0, scale=5.0, size=50)
}

raw_data['Temperature_Sensor'][12] = 250.0
raw_data['Temperature_Sensor'][35] = -99.0

df_iot = pd.DataFrame(raw_data)
print("--- Raw Flawed IoT Ingestion Pipeline ---")
print(df_iot.iloc[[10, 12, 14, 35]])

df_iot['Power_Output_Numeric'] = pd.to_numeric(df_iot['Power_Output_Raw'], errors='coerce')
df_iot['Power_Output_Numeric'] = df_iot['Power_Output_Numeric'].ffill()

mean_temp = df_iot['Temperature_Sensor'].mean()
std_temp = df_iot['Temperature_Sensor'].std()

cutoff = std_temp * 3
lower_bound = mean_temp - cutoff
upper_bound = mean_temp + cutoff

df_iot['Temperature_Cleaned'] = np.clip(df_iot['Temperature_Sensor'], lower_bound, upper_bound)

df_iot.set_index('Timestamp', inplace=True)
df_iot['Temp_Rolling_Avg'] = df_iot['Temperature_Cleaned'].rolling(window=6, min_periods=1, center=True).mean()

print("\n--- Processed Edge-Case DataFrame Summary ---")
print(df_iot[['Power_Output_Numeric', 'Temperature_Cleaned', 'Temp_Rolling_Avg']].head(10))

plt.figure(figsize=(12, 6))

plt.plot(df_iot.index, df_iot['Temperature_Sensor'], label='Raw Unclean Temperature (With Spikes)', color='red', linestyle='--', alpha=0.5)
plt.plot(df_iot.index, df_iot['Temperature_Cleaned'], label='Cleaned Temperature (Clipped Bounds)', color='blue', linewidth=1.5)
plt.plot(df_iot.index, df_iot['Temp_Rolling_Avg'], label='6-Hour Smoothed Trend Line', color='green', linewidth=2.5)

plt.title("Industrial IoT Sensory Remediation Pipeline", fontsize=14, fontweight='bold')
plt.xlabel("Timeline Execution Track")
plt.ylabel("Core Temperature Scale")
plt.legend(loc="upper right")
plt.grid(True, which='both', linestyle=':', alpha=0.5)

plt.tight_layout()
plt.show()