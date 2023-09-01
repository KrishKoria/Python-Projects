import pandas as pd
from sklearn.tree import DecisionTreeRegressor

file_path = 'melb_data.csv'
data = pd.read_csv(file_path)
# print(data.describe())
# print(data.columns)
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = data[melbourne_features]
# print(X.head)
print(X.describe())
y = data.Price
melbourne_model = DecisionTreeRegressor(random_state=1)

melbourne_model.fit(X=X, y=y)
print(X.head())
print(f"Predictions are {melbourne_model.predict(X.head())}")