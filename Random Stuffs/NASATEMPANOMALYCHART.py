import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset properly
file_path = r"C:\Users\spies\Downloads\GLB.Ts+dSST.csv"
df = pd.read_csv(file_path, delim_whitespace=True)  # Fix misalignment

# Check the first few rows
print(df.head())

# Convert the "Year" column to an integer
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")

# Select relevant columns (Year & J-D, which is the annual temperature anomaly)
df = df[["Year", "J-D"]].dropna()

# Convert "J-D" column to float
df["J-D"] = pd.to_numeric(df["J-D"], errors="coerce")

# Plot the data
plt.figure(figsize=(10, 5))
plt.plot(df["Year"], df["J-D"], color="red", linewidth=1)

# Add labels and title
plt.xlabel("Year")
plt.ylabel("Global Temperature Anomaly (°C)")
plt.title("Global Temperature Anomalies Over Time")
plt.grid(True)

# Show the plot
plt.show()