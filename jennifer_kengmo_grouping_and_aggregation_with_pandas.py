# -*- coding: utf-8 -*-
"""Jennifer_Kengmo_Grouping_and_Aggregation_with_Pandas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/Kengmo75/Kengmo75/blob/main/Jennifer_Kengmo_Grouping_and_Aggregation_with_Pandas.ipynb

## Setup

This CSV data contains a snapshot of NYC Airbnb listings as of October 2023. Source: [Inside Airbnb](http://insideairbnb.com/get-the-data).

Run the code below to get started.
"""

# Import libraries
import pandas as pd

# Load data
listings = pd.read_csv("http://data.insideairbnb.com/united-states/ny/new-york-city/2023-10-01/visualisations/listings.csv")
listings.head()

"""## Refresher 0"""

listings['neighbourhood_group'].value_counts()

"""## Code Exercise 0

Answer the following questions:

1. What is the percentage of listings per room type?
2. What is the overall mean and median nightly price?
"""

listings['room_type'].value_counts(normalize=True)

"""## Refresher 1"""

listings['price'].agg(['mean', 'median'])

"""## Code Exercise 1

Answer the following questions:

1. What are the mean and median nightly price by room type?
2. Create a new column called `short_term` that is `True` if the minimum nights is under 30 days and `False` otherwise. What is the average price for short-term vs. long-term listings?
"""

listings.groupby('room_type')['price'].agg(['mean', 'median'])

"""## Refresher 2"""

listings['short_term'] = listings['minimum_nights']< 30
listings.groupby('short_term')['price'].mean()

"""## Code Exercise 2

1.   Compute the average nightly price and number of listings by room type and short vs. long term.
2.   Is short term always more expensive than long term?
"""

listings.pivot_table(values='price', index = 'short_term', columns = 'room_type', aggfunc = ['mean', 'count'])

"""## Conclusions

Based on all of the analysis we did about room types and short vs. long-term, what would you tell someone who wanted to book an Airbnb in NYC? Assuming they want to find good prices and more listings to choose from. Write a couple sentences.

Opt for long-term stays: Analysis indicates that long-term room stays in NYC are generally more cost-effective compared to short-term options.

Better value for money: Long-term bookings offer better value, allowing for savings and potentially more affordable accommodation choices.

Increased listing variety: Choosing a long-term stay increases the likelihood of finding a suitable place, given the broader range of listings available for extended durations.

Aligns with budget considerations: Long-term stays provide a budget-friendly option, enabling individuals to maximize their budget while enjoying an extended stay in New York City.
"""