import cgitb
import cgi
import cx_Oracle
cgitb.enable(format="text")
import folium
import Packages


with open("../../oracle",'r') as pwf:
 pw = pwf.read().strip()

 ''' This file connects to the database to send the variables of each
 row to the fields class. Because the amount of the variables changes, if
 the FieldStorage is filled, the functions is also looking for possibile
 data in the Storage. The url of the python file sends the data to the python
 file. Because the url could easily be change to eg. "Drop Table" the sent data
 is checked for sql injection. If the data is injected, the file wont work,
 in order to protect the webpage '''

def sendctofield():
    #this file sends the variables to the fields class
    # secondly it returns the variables that will be send later to html
    c, arearesult =connectdbfield() #connect to another function, that returns c
    tablefields = tablehead() # get the table header of another function
    svgfield = '' #create empty string that will be used later
    for row in c:
        #loop over c and append assign the variables
        fieldid = str(row[0])
        lowx = str(row[1])
        lowy = str(row[2])
        highx = str(row[3])
        highy = str(row[4])
        area = str(row[5])
        owner = str(row[6])
        cropid = str(row[7])
        #send the variables inside the loop to the class
        fields = Packages.fieldss(fieldid, lowx, lowy, highx, highy, area, owner, cropid)
        # to get the row for the tablefields
        tablefields += fields.renderfieldstable()
        #and the svg
        svgfield += fields.render()
    #close the table when the loop has ended
    tablefields += '</table>'
    return tablefields, svgfield, arearesult

def tablehead():
    var_fields = str("fieldstable")
    #generate the headers with the sort table function inside
    tablefields = f'<table id = "fieldstable"><tr class = "headerrow">'
    tablefields += f'<th onclick="sortTable({var_fields}, 0)">Field ID</th>'
    tablefields += f'<th>Low X</th>'
    tablefields += f'<th >Low Y</th>'
    tablefields += f'<th >High X</th>'
    tablefields += f'<th >High Y</th>'
    tablefields += f'<th onclick="sortTable({var_fields}, 5)">Area</th>'
    tablefields += f'<th onclick="sortTable({var_fields}, 6)">Owner of Field</th>'
    tablefields += f'<th onclick="sortTable({var_fields}, 7)" >Crop ID</th></tr>'
    return tablefields

def connectdbfieldmap():
    #connecting to the db to retrieve the data
    #this function ist just for the map.py to gurantee a goof map layout
    conn = cx_Oracle.connect(dsn="geoslearn",user="student",password=pw)
    c = conn.cursor()
    c.execute("SELECT Field_Id, Lowx, lowy, hix, hiy, round(area,2), initcap(owner), crop FROM GISTEACH.FIELDS")
    return c

def connectdbfield():
    #connecting to the db to retrieve the data
    conn = cx_Oracle.connect(dsn="geoslearn",user="student",password=pw)
    c = conn.cursor()
    c.execute("SELECT Field_Id, Lowx, lowy, hix, hiy, round(area,2), initcap(owner), crop FROM GISTEACH.FIELDS")

    #check if something is in fieldstorage and send it to another function
    form = cgi.FieldStorage()
    if form.getlist("farmer"): # check if there is data in the field storage
        farmers = form.getlist("farmer")
         # store it in a list and call the sql farmer function to get a new c
        c = sqlfarmer(farmers)

    arearesult = 0
    form2 = cgi.FieldStorage()
    if form2.getlist("area"): # check if there is data in the field storage
        area = form2.getlist("area")
         # store it in a list and call the sql farmer function to get a new c
        arearesult= sqlarea(area)

    return c, arearesult

def sqlarea(area):
    #this function just retrieves the fieldid and area to sum up
    #the selected fields
    conn = cx_Oracle.connect(dsn="geoslearn",user="student",password=pw)
    c = conn.cursor()
    c.execute("Select Field_ID, area from GISTEACH.Fields")
    testlist = ["0", "1", "2", "3", "4", "5", "6", "7"]
    #check for sql injection if the values are not hacked
    check = all(item in testlist for item in area)
    value = 0
    if check is True:
        index = 0
        arealistint = []
        #loop over the list and append teh values as integers to another list
        for i in area:
            arealistint.append(int(i))
        for row in c:
            #loop over c and add the value to the result, if the
            #corresponds with the list item
            if index in arealistint:
                value += float(row[1])
            index += 1

    return round(value,2) # round because field 4 has many values after the point



def sqlfarmer(farmers):
    #this function is called, when something is in teh fieldstorage of farmers
    farmerslist = []
    #this for loop is converting the number so the farmers to prevent sql injection
    for i in farmers:
        if i == "1":
            farmerslist.append("BROWN")
        elif i == "2":
            farmerslist.append("GREEN")
        elif i == "3":
            farmerslist.append("WHITE")
        elif i == "4":
            farmerslist.append("BLACK")

    farmersstring = ''
    counter = 0
     # transform the list to a string to insert it in the sql statement
    for i in farmerslist:
        if counter == 0:
            farmersstring += "where (owner LIKE '%"+i+"%'"
        elif counter > 0:
            farmersstring += "or owner LIKE '%"+i+"%'"
        counter += 1

    conn = cx_Oracle.connect(dsn="geoslearn",user="student",password=pw)
    c = conn.cursor()
     #sqlfarmerstatement = "SELECT Field_Id, Lowx, lowy, hix, hiy, round(area,2), initcap(owner), crop FROM GISTEACH.FIELDS where Owner = " + farmers
    c.execute("SELECT Field_Id, Lowx, lowy, hix, hiy, round(area,2), initcap(owner), crop FROM GISTEACH.FIELDS "+farmersstring+")")

    return c
