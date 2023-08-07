import pandas as pd
data = pd.read_csv(r"C:\Users\Surface\Downloads\1. Weather Data.csv")
print(data.to_string())
data.head(5)
print(data.loc[[0,1,2,3,4]])
print(data.shape)
#used to count the number of rows*columns in the dataset#
print(data.head())
#used to print the first five rows in the dataset#
print(data.index)
#used to show the range of data number of rows counted from which index value with what differene between each index and the next value#
print(data.columns)
#used to show all the column titles included in the data set#
print(data.dtypes)
#used to show the data types held by each column#
print(data['Weather'].unique())
#used to show all the unique values in a certain column eg 'Weather' column in this case#
print(data.nunique())
#show the number of unique values in each column#
print(data.count())
#shows the number of none null values in each column.Can apply to a single column or to a whole dataframe#
print(data['Weather'].value_counts())
#shows all the unique values in a column with their count ie how many of each there are.#
print(data.info)
#provides basic information about the dataframe#
print(data['Wind Speed_km/h'].unique())
#shows the unique values in the wind speed column, note that you have to write the column name exactly as written in the dataset table#
print(data[data.Weather == 'Clear'])
print(data.groupby('Weather').get_group('Clear'))
#the two above are both ways to show the rows in which the weather value is "clear" only
print(data[data['Wind Speed_km/h'] == 4])
#shows all rows for which the wind speed value is 4
print(data.isnull().sum())
#shows the number of null values in each column in the data set
print(data.notnull().sum())
#shows the number of not null values in each column in the data set
print(data.rename(columns={'Weather':'Weather Condition'}, inplace=True))
#changes the title of column from weather to weather condition
print(data.Visibility_km.mean())
#calculates the mean visibility
print(data.Press_kPa.std())
#calculates the standard deviation of pressure
print(data['Rel Hum_%'].var())
#calculates the variance of relative humidity
print(data['Weather Condition'].value_counts())
#shows all the unique values in a column with their count ie how many of each there are
print(data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)])
#shows all rows with wind speed above 24 and visibility equal to 25
print(data.groupby('Weather Condition').mean())
#shows the mean of data against the weather condition column
print(data.groupby('Weather Condition').max())
print(data.groupby('Weather Condition').min())
print(data[data['Weather Condition']=='Fog'])
#finds all the instances where the weather is fog
print(data[(data['Weather Condition']=='Clear')|(data['Visibility_km']>40)])
#finds the rows where weather is clear OR the visibility is above 40
print(data[(data['Weather Condition']=='Clear') & (data['Rel Hum_%']>50) |(data['Visibility_km']>40)])
#rows where weather is clear AND humidity is above 50 OR visibility is above 40



