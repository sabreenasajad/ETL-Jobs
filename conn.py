from sqlalchemy import create_engine

# Replace the connection string with your SQL Server details
conn_str = "mssql+pyodbc://DESKTOP-L3Q8CQG\SQLEXPRESS/practice?driver=SQL+Server"
#conn_str="mssql+pyodbc://username:password@server/database?driver=ODBC+Driver+17+for+SQL+Server"

SqlConn = create_engine(conn_str)

