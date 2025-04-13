import numpy as np
import random
import matplotlib.pyplot as plt
import pandas as pd

# Constants
GM2_BUILDUUP_RATE = 0.1  # The rate of GM2 buildup (arbitrary units)

# Mutation effects on enzyme activity (100% = normal activity)
mutation_effects = {
    "normal": 1.0,  # Normal enzyme activity
    "frameshift": 0.2,  # Severe mutation
    "nonsense": 0.5,  # Moderate mutation
    "missense": 0.75  # Mild mutation
}

# Enzyme kinetics function (simplified)
def enzyme_kinetics(enzyme_activity):
    return enzyme_activity * (1 - GM2_BUILDUUP_RATE)

# Stochastic enzyme activity (introduce randomness)
def stochastic_enzyme_activity(enzyme_activity, variability_factor=0.1):
    variability = random.uniform(1 - variability_factor, 1 + variability_factor)
    return enzyme_activity * variability

# Simulation function for Tay-Sachs
def simulate_tay_sachs(enzyme_activity, mutation_type="normal", time_steps=100, therapy_type=None):
    enzyme_activity *= mutation_effects[mutation_type]
    gm2_levels = []

    for t in range(time_steps):
        # Apply therapy if required
        if therapy_type == "ERT":
            enzyme_activity = min(enzyme_activity * 1.5, 1.0)  # Increase enzyme activity by 50%, max 100%

        enzyme_activity = stochastic_enzyme_activity(enzyme_activity)  # Apply stochastic noise
        gm2_buildup = GM2_BUILDUUP_RATE * (1 - enzyme_kinetics(enzyme_activity))  # GM2 buildup rate
        gm2_levels.append(gm2_buildup * t)  # Simulate buildup over time

    return gm2_levels

# Load mutation data from JSON
def load_mutation_data(file_path="data/mutations.json"):
    import json
    with open(file_path) as f:
        data = json.load(f)
    return {mutation['type']: mutation['activity_factor'] for mutation in data['mutations']}

# Load gene data from CSV (for future use or gene correlation analysis)
def load_gene_data(file_path="data/sample_gene_data.csv"):
    return pd.read_csv(file_path)
    
# Plotting function
def plot_gm2_levels(gm2_levels, title="GM2 Buildup Simulation"):
    plt.plot(gm2_levels)
    plt.title(title)
    plt.xlabel("Time Steps")
    plt.ylabel("GM2 Level")

    # Save plot before showing
    plt.savefig("models/output_gm2_plot.png", dpi=300, bbox_inches='tight')
    print("📊 Plot saved to: models/output_gm2_plot.png")

    plt.show()
if __name__ == "__main__":
    gm2_data = simulate_tay_sachs(enzyme_activity=1.0, mutation_type="frameshift", time_steps=100, therapy_type="ERT")
    plot_gm2_levels(gm2_data, title="GM2 Buildup in Tay-Sachs with ERT")

if __name__ == "__main__":
    print("Starting simulation...")
    gm2_data = simulate_tay_sachs(enzyme_activity=1.0, mutation_type="frameshift", time_steps=100, therapy_type="ERT")
    print("Simulation complete. Plotting results...")
    plot_gm2_levels(gm2_data, title="GM2 Buildup in Tay-Sachs with ERT")
    print("Plotting complete.")


