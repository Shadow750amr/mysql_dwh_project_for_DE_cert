This another piece of the Data Engineer Professional Certificate final project by IBM in which I built a MYSQL database to simulate a staging DWH to further export this data into a production enviroment in postgres. 

In this case, this part of the module required to designed a incremental approach to import only the most newest rows based on some id.


You will notice that there was not so much of configuration needed (eg. constructing docker container, configuring the table types or setting the cache) because the module didnt required to do so. Also, there are some improvement areas due to the lack of modularization, redudant code and some hardcoding that didnt affect the final product but troubleshooting.

Anyways, the automation process did required a little bit of effort.

Thanks!!!!