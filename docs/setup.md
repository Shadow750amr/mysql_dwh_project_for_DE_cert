--- Step 1 import the data and objects

mysql -u user_name -p db_name < path_to_file.sql

--- Step 2 

 psql -h host_name -U user_name -d database_name -c "\copy target_table FROM 'file.csv' WITH (FORMAT csv, HEADER true)


 