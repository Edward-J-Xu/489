import os
import pandas as pd
import matplotlib.pyplot as plt

results_dir = './results'
vcoders = set()

average_mos = {}

for root, dirs, files in os.walk(results_dir):
    for file in files:
        if file.endswith('NISQA_results.csv'):
            # print(root)
            vcoder = root.split('\\')[1]
            vcoders.add(vcoder)
            
            file_path = os.path.join(root, file)
            df = pd.read_csv(file_path)
            
            avg_mos = df['mos_pred'].mean()
            
            if vcoder in average_mos:
                average_mos[vcoder].append(avg_mos)
            else:
                average_mos[vcoder] = [avg_mos]

keys = list(average_mos.keys())
values = [value[0] for value in average_mos.values()]

plt.figure(figsize=(10, 6))
plt.bar(keys, values, color='green')
plt.xlabel('Vcoders')
plt.ylabel('Average Naturalness')
plt.title('Average Naturalness for Different Vcoders')
plt.ylim(4.1, 4.35)

plt.show()
