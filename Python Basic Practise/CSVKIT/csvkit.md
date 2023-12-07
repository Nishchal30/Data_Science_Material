**How to install csvkit and start using from command line**

pip install csvkit 

**To look at the basic stats of the each column of the given file**

csvstat filename

**To create a schema for the given csv file**

csvsql -i mysql filename

**To insert data from csv file into the database**

csvsql --db  mysql+mysqlconnector://<user>:<password>@<host>/database_name --db-schema ccd --table "table_name" --insert Fitbit_data.csv

**Refer to this url for exploring more about csvkit *https://csvkit.readthedocs.io/en/0.9.1/tutorial.html***