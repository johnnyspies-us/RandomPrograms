import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r"C:\Users\spies\Downloads\GLB.Ts+dSST.csv"
df = pd.read_csv(file_path, skiprows=1)

# Check the first few rows
print(df.head())

# Check the column names
print(df.columns)


# Convert "Year" to numeric (just in case)
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")

# Convert "J-D" (annual temperature anomaly) to numeric
df["J-D"] = pd.to_numeric(df["J-D"], errors="coerce")

# Drop any rows with missing values
df = df.dropna(subset=["J-D"])

# Plot the data
plt.figure(figsize=(10, 5))
plt.plot(df["Year"], df["J-D"], marker="o", linestyle="-", color="red", linewidth=1)

# Add labels and title
plt.xlabel("Year")
plt.ylabel("Global Temperature Anomaly (°C)")
plt.title("Global Temperature Anomalies Over Time")
plt.grid(True)

# Show the plot
plt.show()