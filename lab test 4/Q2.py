import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

# Step 1: Generate dataset (AI-simulated)
data = {
    'name': ['pavan', 'Diya', 'manoj', 'Neha', 'Aditya'],
    'department': ['CSE', 'ECE', 'IT', 'CSE', 'ME'],
    'marks': [85, np.nan, 75, 90, np.nan],
    'attendance': [92, 70, np.nan, 88, 60],
    'gender': ['Male', 'Female', 'Male', 'Female', 'Male']
}

df = pd.DataFrame(data)
print("Original Dataset:\n", df, "\n")

# Step 2: Fill missing values with column mean (modern syntax)
df.fillna({
    'marks': df['marks'].mean(),
    'attendance': df['attendance'].mean()
}, inplace=True)

# Step 3: One-hot encode categorical columns (auto-detect version)
try:
    encoder = OneHotEncoder(drop='first', sparse_output=False)  # For sklearn >=1.4
except TypeError:
    encoder = OneHotEncoder(drop='first', sparse=False)         # For sklearn <1.4

encoded_features = encoder.fit_transform(df[['department', 'gender']])
encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(['department', 'gender']))

# Step 4: Combine encoded features with original DataFrame
df_encoded = pd.concat([df.drop(['department', 'gender'], axis=1), encoded_df], axis=1)

# Step 5: Save cleaned dataset
df_encoded.to_csv('processed_students.csv', index=False)

print("Processed Dataset:\n", df_encoded)
print("\n✅ File 'processed_students.csv' has been saved successfully.")
