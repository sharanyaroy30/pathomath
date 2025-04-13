# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import json

# Function to load mutation data from JSON file
def load_mutation_data(file_path):
    with open(file_path, 'r') as f:
        mutation_data = json.load(f)
    return mutation_data

# Function to load gene data from CSV file
def load_gene_data(file_path):
    return pd.read_csv(file_path)

# Function to simulate Tay-Sachs disease progression
def simulate_tay_sachs(enzyme_activity, mutation_type, time_steps, therapy_type=None):
    gm2_levels = []  # To store GM2 levels over time
    gm2_level = 0  # Initial GM2 level
    
    # Simulate over time steps
    for t in range(time_steps):
        # Simulate GM2 buildup based on enzyme activity and mutation type
        if mutation_type == "normal":
            gm2_level += 0.01 * (1 - enzyme_activity)  # Normal mutation
        elif mutation_type == "frameshift":
            gm2_level += 0.02 * (1 - enzyme_activity)  # Frameshift mutation
        else:
            gm2_level += 0.05 * (1 - enzyme_activity)  # Other mutations
        
        # Apply therapy if specified
        if therapy_type == "ERT":
            gm2_level -= 0.05 * gm2_level  # Enzyme Replacement Therapy
        elif therapy_type == "gene_therapy":
            gm2_level -= 0.1 * gm2_level  # Gene therapy
        
        gm2_levels.append(gm2_level)
    
    return gm2_levels

# Function to plot GM2 levels over time
def plot_gm2_levels(gm2_levels, title="GM2 Levels Over Time"):
    plt.plot(gm2_levels)
    plt.xlabel('Time Steps')
    plt.ylabel('GM2 Levels')
    plt.title(title)
    plt.grid(True)
    plt.show()

# Main function to run the simulation and plot results
def main():
    # Load mutation and gene data
    mutation_data = load_mutation_data(file_path="data/mutations.json")
    print("Mutation Data:", mutation_data)
    
    gene_data = load_gene_data(file_path="data/sample_gene_data.csv")
    print("Gene Data:\n", gene_data.head())  # Print the first few rows of gene data
    
    # Simulate Tay-Sachs with normal mutation and no therapy
    gm2_levels_normal = simulate_tay_sachs(enzyme_activity=0.2, mutation_type="normal", time_steps=100, therapy_type=None)
    plot_gm2_levels(gm2_levels_normal, title="Normal Mutation - No Therapy")
    
    # Simulate Tay-Sachs with frameshift mutation and Enzyme Replacement Therapy (ERT)
    gm2_levels_frameshift_ert = simulate_tay_sachs(enzyme_activity=0.2, mutation_type="frameshift", time_steps=100, therapy_type="ERT")
    plot_gm2_levels(gm2_levels_frameshift_ert, title="Frameshift Mutation - ERT Therapy")
    
    # Simulate Tay-Sachs with frameshift mutation and gene therapy
    gm2_levels_frameshift_gene_therapy = simulate_tay_sachs(enzyme_activity=0.2, mutation_type="frameshift", time_steps=100, therapy_type="gene_therapy")
    plot_gm2_levels(gm2_levels_frameshift_gene_therapy, title="Frameshift Mutation - Gene Therapy")

# Run the simulation
if __name__ == "__main__":
    main()

