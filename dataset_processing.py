import pandas as pd

def process_data(data, name, y_column):
    data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')
    data['Date'] = data['Date'].dt.year + (data['Date'].dt.month - 1)/12 + (data['Date'].dt.day - 1)/365
    data = data.set_index('Date')

    x_values = data.index.values.reshape(-1, 1)
    x_values = x_values - x_values[0]
    y_values = data[y_column].values.reshape(-1, 1)
   

    x_train = x_values[:int(len(x_values)*3/4)]
    y_train = y_values[:int(len(y_values)*3/4)]
    x_test = x_values[int(len(x_values)*3/4):]
    y_test = y_values[int(len(y_values)*3/4):]
    

    pd.DataFrame(x_train).to_csv('resources/' + name + '/x_training.csv', header=False, index=False)
    pd.DataFrame(y_train).to_csv('resources/' + name + '/y_training.csv', header=False, index=False)
    pd.DataFrame(x_test).to_csv('resources/' + name + '/x_test.csv', header=False, index=False)
    pd.DataFrame(y_test).to_csv('resources/' + name + '/y_test.csv', header=False, index=False)

# S&P500 yearly close price

process_data(pd.read_csv('resources/spy.csv'), 'spy', 'Close')

# Annual Inflation

process_data(pd.read_csv('resources/inflation-clean.csv'), 'inflation', 'Inflation')

# Nasdaq-100 yearly close price

process_data(pd.read_csv('resources/nasdaq.csv'), 'nasdaq', 'Close')

# 538 Biden approval rating

process_data(pd.read_csv('resources/biden.csv'), 'biden', 'Approval Rating')