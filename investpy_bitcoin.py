import investpy

data = investpy.get_crypto_historical_data(crypto='bitcoin',
                                           from_date='01/01/2000',
                                           to_date='04/06/2022')


index = data.index

colnames = ['Currency']
data = data.drop([x for x in colnames if x in data.columns], axis=1)

print(data.head())
print(data.dtypes)