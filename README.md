# Pandas-Data-Frame-into-a-SQL-Table-
Import your data frame into a SQL Table

## Installing the Right Python Libraries

```
pip install pandas
pip install sqlalchemy
pip install psycopg2
pip install pyodbc
```
You likely only need pyodbc if trying to import into a Microsoft SQL Server database.

## Code Walkthrough

These are the components of the libraries being imported in order to run this code. "requests" allows you to make a call to the Mozenda API and bring in that data. "xml.etree.cElementTree" is necessary in order to convert the xml file into a dataframe. "pandas" allows the user to manipulate and create a dataframe.

```
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
```
For more information and more potential databases to export to visit the [sqlalchemy documentation](https://docs.sqlalchemy.org/en/13/core/engines.html) or for more information on the pandas to_sql function visit (this documentation)[https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html].
