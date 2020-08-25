import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
for driver in pyodbc.drivers():
    print(driver)



server = 'ANKAN-PC\SPARTA' 
database = 'Happy' 
# username = 'ANKAN-PC\Ankan' 
# password = 'Ankan@2020' 

#define conection string
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};\
                       SERVER='+server+';\
                       DATABASE='+database+';\
                       Trusted_connection=yes;')
#create the connection cursor                       
cursor = cnxn.cursor()


#Insert  the rows from table
# cursor.execute("Insert into dbo.EMP values ('Danny', 'D', 'Male', 20000)") #EMP table's ID cloumn has IDENTITY keyword, which restricts explicit insertion of values in ID
# cursor.execute("Insert into dbo.EMP (FirstName,LastName,Gender,Salary) values ('Shane', 'Diesel', 'Male', 100000),('Jhonny', 'Sins', 'Male', 87000)")

#sql = "INSERT INTO dbo.EMP (FirstName,LastName,Gender,Salary) VALUES (?,?,?,?)"
#val = ('John', "Snow", "Male", 50000)
#
#cursor.execute(sql, val)

sql = "INSERT INTO dbo.EMP (FirstName,LastName,Gender,Salary) VALUES (?,?,NULL,NULL)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

cursor.executemany(sql, val) #in this way we can insert a tuple, list containg mutiple rows in a table





#commit
cnxn.commit()


#print("1 record inserted, ID:", cursor.lastrowid)

#select all the rows from table
cursor.execute('Select * from dbo.Emp')

# loop through the result
for row in cursor:
    print(row)

cnxn.close() # its not necessary, but standard practice to close the connection.


