from fbprophet import Prophet
from datetime import datetime
from datetime import timedelta
import pandas as pd

data = pd.DataFrame(index=range(0, 31), columns=['Date', 'Number'])
for i in range(30, -1, -1):
    data["Date"][i] = (
        datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d')
    if i % 2 == 0:
        data["Number"][i] = 1
    else:
        data["Number"][i] = 0

data['Date'] = pd.to_datetime(data.Date, format='%Y-%m-%d')
data.index = data['Date']

# preparing data
data.rename(columns={'Number': 'y', 'Date': 'ds'}, inplace=True)

print(data)

# train and validation
train = data

# fit the model
model = Prophet()
model.fit(train)

# predictions
close_prices = model.make_future_dataframe(periods=1)
forecast = model.predict(close_prices)
print(forecast.values)
