from sqlalchemy import create_engine

# Replace the connection string with your SQL Server details
conn_str = r"mssql+pyodbc://DESKTOP-L3Q8CQG\SQLEXPRESS/practice?driver=SQL+Server"

SqlConn = create_engine(conn_str)

