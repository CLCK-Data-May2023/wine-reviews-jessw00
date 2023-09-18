import pandas as pd

# read input csv file
input_file = 'data/winemag-data-130k-v2.csv.zip'
df = pd.read_csv(input_file, compression='zip')

# group data by country, calculate count and average points
summary_df = df.groupby('country').agg({'country': 'count', 'points': 'mean'})

# rename columns
summary_df = summary_df.rename(columns={'country': 'count', 'points': 'average_points'})

# round average_points column to 1 decimal point
summary_df['average_points'] = summary_df['average_points'].round(1)

# reset index to have 'country' as a column
summary_df.reset_index(inplace=True)

# creat output CSV file
output_file = 'data/reviews-per-country.csv'
summary_df.to_csv(output_file, index=False)