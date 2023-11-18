import pandas as pd
data = pd.read_csv('your_dataset.csv')
features = data[['town', 'flat_type', 'storey_range', 'floor_area_sqm', 'flat_model', 'lease_commence_date']]