import os
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read all CSV files and calculate the average MOS for each vcoder
results_dir = './results'
vcoders = set()

# Dictionary to store average MOS for each vcoder
average_mos = {}

for root, dirs, files in os.walk(results_dir):
    for file in files:
        if file.endswith('NISQA_results.csv'):
            # print(root)
            vcoder = root.split('\\')[1]  # Extract vcoder name from the file path
            vcoders.add(vcoder)
            
            # Read CSV file
            file_path = os.path.join(root, file)
            df = pd.read_csv(file_path)
            
            # Calculate average MOS for each vcoder
            avg_mos = df['mos_pred'].mean()
            
            # Store in the dictionary
            if vcoder in average_mos:
                average_mos[vcoder].append(avg_mos)
            else:
                average_mos[vcoder] = [avg_mos]

keys = list(average_mos.keys())
values = [value[0] for value in average_mos.values()]

# Plot the data
plt.figure(figsize=(10, 6))
plt.bar(keys, values, color='green')
plt.xlabel('Vcoders')
plt.ylabel('Average Naturalness')
plt.title('Average Naturalness for Different Vcoders')
plt.ylim(4.1, 4.35)  # Set y-axis limits if needed

# Display the plot
plt.show()
