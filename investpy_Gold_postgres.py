import investpy
from sqlalchemy import create_engine
import psycopg2
import sqlalchemy


search_result = investpy.search_quotes(text='Gold Guinea Futures', products=['commodities'],
                                       countries=['India'], n_results=1)

historical_data = search_result.retrieve_historical_data(from_date='01/01/2007', to_date='07/06/2022')

data = historical_data

engine = create_engine("postgresql://postgres:password@localhost:5432/data")

data.to_sql('gold', engine, if_exists='append', index=True, dtype={
                    'Date': sqlalchemy.types.Date(),
                   'Open': sqlalchemy.types.Float(precision=3, asdecimal=True),
                   'High': sqlalchemy.types.Float(precision=3, asdecimal=True),
                   'Low': sqlalchemy.types.Float(precision=3, asdecimal=True),
                   'Close': sqlalchemy.types.Float(precision=3, asdecimal=True),
                    'Volume': sqlalchemy.types.BigInteger(),
                    'Change pct': sqlalchemy.types.Float(precision=3, asdecimal=True)
                    })

print("\nImporting Done successfully!")

conn=psycopg2.connect(
    database="data",
    user="postgres",
    password="password",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()
  
# query to count total number of rows
sql = 'SELECT count(*) from gold;'
data=[]
  
# execute the query
cursor.execute(sql,data)
# cursor.execute(sql)
results = cursor.fetchall()
  

for r in results:
  print(r)
print("Total number of rows in the table:", r)


conn.commit()
  
# Closing the connection
conn.close()