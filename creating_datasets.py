import pandas as pd

# S&P500 yearly close price

spy = pd.read_csv('https://query1.finance.yahoo.com/v7/finance/download/%5EGSPC?period1=788918400&period2=1669900913&interval=1mo&events=history&includeAdjustedClose=true')
spy_df = pd.DataFrame(spy['Close'])
spy_df['Date'] = pd.to_datetime(spy['Date'], format='%Y-%m-%d')
spy_df = spy_df.set_index('Date')
spy_df.to_csv('resources/spy.csv')

# Nasdaq-100 yearly close price

nasdaq = pd.read_csv('https://query1.finance.yahoo.com/v7/finance/download/%5ENDX?period1=788918400&period2=1669900913&interval=1mo&events=history&includeAdjustedClose=true')
nasdaq_df = pd.DataFrame(nasdaq['Close'])
nasdaq_df['Date'] = pd.to_datetime(nasdaq['Date'], format='%Y-%m-%d')
nasdaq_df = nasdaq_df.set_index('Date')
nasdaq_df.to_csv('resources/nasdaq.csv')

# Annual Inflation

inflation = pd.read_csv('resources/inflation.csv')
inflation = inflation[['Year', 'Period', '12-Month % Change']]
inflation['Period'] = inflation['Period'].str.replace('M', '')
inflation['Date'] = inflation['Year'].astype(str) + '-' + inflation['Period'].astype(str)
inflation = inflation.drop(['Year', 'Period'], axis=1)
inflation['Date'] = pd.to_datetime(inflation['Date'], format='%Y-%m')
inflation = inflation.set_index('Date')
inflation = inflation.rename(columns={'12-Month % Change': 'Inflation'})
inflation.to_csv('resources/inflation-clean.csv')

# 538 Biden approval rating

biden = pd.read_csv('resources/approval_topline.csv')
biden = biden[biden['subgroup'] == 'All polls']
biden = biden[['modeldate', 'approve_estimate']]
biden['Date'] = pd.to_datetime(biden['modeldate'], format='%m/%d/%Y')
biden = biden.drop(['modeldate'], axis=1)
biden = biden.set_index('Date')
biden = biden.rename(columns={'approve_estimate': 'Approval Rating'})
biden = biden.iloc[::-1]
biden.to_csv('resources/biden.csv')



