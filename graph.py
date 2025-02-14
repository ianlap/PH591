import pandas as pd
import matplotlib.pyplot as plt

# Load and plot multiple CSV files
def plot_multiple_csv(filenames):
    plt.figure(figsize=(10, 6))
    colors = ['g', 'b', 'm']  # Green, Blue, Magenta
    labels = ['CS2Ref_CS1', 'CS5Ref_CS1', 'CS5Ref_CS2']
    
    for i, filename in enumerate(filenames):
        df = pd.read_csv(filename)
        x = df.iloc[:, 0]
        y = df.iloc[:, 2]
        plt.plot(x, y, linestyle='-', color=colors[i % len(colors)], label=labels[i % len(labels)])
    
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Drift Removed Phase Data")
    plt.legend()
    plt.grid(True)
    plt.savefig("residuals.png")
    plt.show()

# Example usage
plot_multiple_csv(["CS2_REF_CS1_In_phase_residuals.csv","CS5Ref_CS1in_phase_residuals.csv","CS5Ref_CS2in_phase_residuals.csv"])