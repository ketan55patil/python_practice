import requests
import mysql.connector
from mysql.connector import errorcode
import datetime


file_name = "us-counties.csv"
url = f"https://raw.githubusercontent.com/nytimes/covid-19-data/master/{file_name}"
max_date = "2020-04-28"

# DB
db_host = "127.0.0.1"
db_user = "root"
db_pass = "1234"
db_name = "covid_19"
db_table_name = "nytimes"

try:
    cnx = mysql.connector.connect(user=db_user, password=db_pass,
                                  host=db_host,
                                  database=db_name)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

cursor = cnx.cursor()
query = f"SELECT max(date) as max_date_col from {db_table_name}"

print("Reading max_date from the table")
cursor.execute(query)

for max_date_col in cursor:
    max_date = str(max_date_col[0])

max_date = "2020-04-29"

print(f"max_date is {max_date}")
sql_insert = f"INSERT INTO {db_table_name} (date, county, state, fips, cases, deaths) \
               VALUES (%s, %s, %s, %s, %s, %s)"

# response = requests.get(url, allow_redirects=True)
# if response.status_code == 200:
if True:
    print('Connection to URL was successful!')

    # print('Writing contents to file...')
    # with open(file_name, 'wb') as fw:
    #     fw.write(response.content)

    print('Reading file to get data where date is greater than max_date...')
    with open(file_name, 'r') as fr:
        data = fr.readlines()
        sql_insert_list = []
        for line in data:
            line_data = line.rstrip('\n').split(',')
            date_col = line_data[0]
            if max_date is not None or (date_col > max_date and date_col != 'date'):
                county_col = line_data[1]
                state_col = line_data[2]
                fips_col = line_data[3] if line_data[3] != '' else 0
                cases_col = line_data[4]
                deaths_col = line_data[5]

                row_list = (date_col, county_col, state_col, fips_col,
                            cases_col, deaths_col)

                sql_insert_list.append(row_list)
print('Inserting values into the table...')
cursor.executemany(sql_insert, sql_insert_list)

print('Committing insert...')
cnx.commit()
print('Closing cursor')
cursor.close()
print('Closing DB connection')
cnx.close()
