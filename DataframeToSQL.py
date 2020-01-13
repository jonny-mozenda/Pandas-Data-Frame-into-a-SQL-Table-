import sqlalchemy
import psycopg2
from sqlalchemy import create_engine

# Example dataframe
# df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),columns=['a', 'b', 'c'])

# PostgreSQL
# databaseAddress = 'postgresql://username:password@localhost/mydatabase'
# MySQL
# databaseAddress = 'mysql://username:password@localhost/mydatabase'
# Microsoft SQL Server
# databaseAddress = 'mssql+pyodbc://username:password@mydsn'

engine = sqlalchemy.create_engine(databaseAddress)

# Example DataFrame. Here you would want to call your own dataframe. Or test with this sample.
# data = [['Alex',10],['Bob',12],['Clarke',13]]
# df = pd.DataFrame(data,columns = ['Name','Age'])

df.to_sql('table_name', engine, if_exists='append')
