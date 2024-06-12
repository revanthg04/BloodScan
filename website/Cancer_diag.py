import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
import re, joblib
from lime import lime_tabular

# Load the dataset
data = pd.read_csv('Cancer_Diagnosis.csv')  # Replace 'Cancer_diag.csv' with your actual dataset file path

# Extract numeric values from 'Age_at_diagnosis' and convert to numeric
data['Age_at_diagnosis'] = data['Age_at_diagnosis'].apply(lambda x: int(re.search(r'\d+', x).group()))

# Encode categorical variables
label_encoder = LabelEncoder()
data['Gender'] = label_encoder.fit_transform(data['Gender'])
data['Grade'] = label_encoder.fit_transform(data['Grade'])

# Convert remaining categorical columns to one-hot encoding
data = pd.get_dummies(data, columns=['IDH1', 'TP53', 'ATRX', 'PTEN', 'EGFR', 'CIC', 'MUC16', 'PIK3CA', 'NF1', 'PIK3R1', 'FUBP1', 'RB1', 'NOTCH1', 'BCOR', 'CSMD3', 'SMARCA4', 'GRIN2A', 'IDH2', 'FAT4', 'PDGFRA'])
# Split the dataset into features (X) and target variable (y)
X = data.drop('Grade', axis=1)  # Features
y = data['Grade']  # Target variable
print(X.columns)
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest classifier and train the model
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=22)
rf_classifier.fit(X_train, y_train)
#print("Columns in X_train:", X_train.columns)
joblib.dump(rf_classifier, 'x.pkl')