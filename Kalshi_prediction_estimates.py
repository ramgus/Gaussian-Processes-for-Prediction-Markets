import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from KalshiClientsBaseV2 import ExchangeClient
import seaborn as sns
from getpass import getpass

#Accessing the Kalshi API
email = "ramgus@mit.edu" 
password = "Gustavin99KS!!"
api_base = 'https://trading-api.kalshi.com/trade-api/v2'
exchange_client = ExchangeClient(exchange_api_base = api_base, email = email, password = password)


def GenerateProbabilityEstimates(event_ticker, delimiter = '-'):
    #Obtaining Market Data for given Event Ticker
    all_markets = exchange_client.get_markets(event_ticker = event_ticker)
    #Calculating Probability of a given range by averaging bid and ask of 'yes' contracts
    probabilities = [ (market['yes_ask'] + market['yes_bid'])/2 for market in all_markets['markets']]
    probabilities = [prob *.01 for prob in probabilities]
    
    subtitles = [market['subtitle'] for market in all_markets['markets']]
    df = pd.DataFrame({'subtitle': subtitles, 'probabilities': probabilities})
    max_prob = max(probabilities)
    max_prob_index = probabilities.index(max_prob)
    max_prob_subtitle = subtitles[max_prob_index]
    if delimiter == '-':
        prediction = delimiter_handling(max_prob_subtitle, delimiter)
    elif delimiter == 'to':
        prediction = delimiter_handling(max_prob_subtitle, delimiter)
    elif delimiter == 'between':
        prediction = delimiter_handling(max_prob_subtitle, delimiter)
        
    # Plotting Bar Chart for Predicted Answer range vs. Probability
    sns.set_theme(style="whitegrid")
    ax = sns.barplot(x="subtitle", y="probabilities", data=df)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    ax.tick_params(axis='x', labelsize=5)
    ax.set_title('Kalshi Prediction Estimates for ' + event_ticker)
    ax.set_ylabel('Probability')
    ax.set_xlabel(event_ticker)
    ax.legend(labels=['The most likely outcome for ' + event_ticker + ' is ' + str(round(prediction, 2)) + ' with a probability of ' + str(round(max_prob, 2))], loc='upper left', fontsize=5)
    print('The most likely outcome for ' + event_ticker + ' is ' + str(round(prediction, 2)) + ' with a probability of ' + str(round(max_prob, 2)))
    plt.tight_layout()
    plt.savefig('Repository/resources/Prediction_estimates_plots/' +event_ticker + '.png')
    plt.show()
    return prediction

# Handling Range string as given by API
def delimiter_handling(subtitle, delimiter):
    if delimiter == '-':
        subtitle = subtitle.split('-')
        subtitle = [float(i) for i in subtitle]
    elif delimiter == 'to':
        subtitle = subtitle.split('to')
        subtitle[0] = subtitle[0].replace('%', '')
        subtitle[1] = subtitle[1].replace('%', '')
        subtitle = [float(i) for i in subtitle]
    elif delimiter == 'between':
        subtitle = subtitle[7:]
        subtitle = subtitle.split('-')
        subtitle[1] = subtitle[1].replace('%', '')
        subtitle = [float(i) for i in subtitle]
    subtitle = (subtitle[0] + subtitle[1])/2
    return subtitle



# S&P500 yearly close price
spy_prediction = GenerateProbabilityEstimates('INXY-22DEC30')

# Annual inflation
inflation_prediction = GenerateProbabilityEstimates('ACPI-22', delimiter = 'between')

# Nasdaq-100 yearly close price
nasdaq_prediction = GenerateProbabilityEstimates('NASDAQ100Y-22DEC30')

# 538 Biden approval rating
biden_prediction = GenerateProbabilityEstimates('538APPROVE-22DEC21', delimiter = 'to')


