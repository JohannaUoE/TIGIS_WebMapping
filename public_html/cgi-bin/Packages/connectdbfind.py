import cgitb
import cgi
import cx_Oracle
cgitb.enable(format="text")
import folium
import Packages


with open("../../oracle",'r') as pwf:
 pw = pwf.read().strip()

 ''' This file connects to the database to send the variables of each
 row to the finds class. Because the amount of the variables changes, if
 the FieldStorage is filled, the functions is also looking for possible
 data in the Storage. The url of the python file sends the data to the python
 file. Because the url could easily be change to eg. "Drop Table" the sent data
 is checked for sql injection. If the data is injected, the file wont work,
 in order to protect the webpage '''

def sendctofind():
    #this file sends the variables to the findss class
    # secondly it returns the variables that will be send later to html
    c=connectdbfind() #connect to another function, that returns c
    tablefinds1 = tablehead()# get the table header of another function
    svgpoint = ''  #create empty string that will be used later
    for row in c:
        #loop over c and append assign the variables
        findid = str(row[0])
        xcoord = str(row[1])
        ycoord = str(row[2])
        type = str(row[3])
        depth = str(row[4])
        notes = str(row[5])
        #send the variables inside the loop to the class
        finds = Packages.findss(findid, xcoord, ycoord, type, depth, notes)
        # to get the row for the tablefinds
        tablefinds1 += finds.renderfindstable()
        #and svg
        svgpoint += finds.renderfind()
    #close the table when the loop has ended
    tablefinds1 += '</table>'
    return c, tablefinds1, svgpoint

def tablehead():
    var_finds = str("tablefinds")
    #generate the headers with the sort table function inside
    tablefinds1 = f'<table id = "tablefinds"><tr class = "headerrow"><th onclick="sortTable({var_finds}, 0)">Artefact ID</th>'
    tablefinds1 += f'<th>X Coordinate</th><th>Y Coordinate</th>'
    tablefinds1 += f'<th onclick="sortTable({var_finds}, 3)">Class ID</th>'
    tablefinds1 += f'<th onclick="sortTable({var_finds}, 4)">Depth in m</th><th onclick="sortTable({var_finds}, 5)">Comments</th></tr>'
    return tablefinds1

def connectdbfind():
    #connecting to the db to retrieve the data
    conn= cx_Oracle.connect(dsn="geoslearn",user="student",password=pw)
    c = conn.cursor()
    c.execute("SELECT Find_Id, Xcoord, Ycoord, type, round(depth,2), Initcap(Field_notes) FROM GISTEACH.FINDS")
    form = cgi.FieldStorage()
    if form.getvalue("depth"): #check for data in fieldstorage
        depth = form.getvalue("depth")
        testdepth = depth.replace('.','')
        if testdepth.isdigit() == True: # this test is for sql injection
            # store it in a list and call the sql depth function to get a new c
            c = sqldepth(depth) #send it to other function
    form2 = cgi.FieldStorage()
    if form2.getlist("period"): #check for data in FieldStorage
        period = form2.getlist("period")

        c = sqlperiod(period)

    form3 = cgi.FieldStorage()
    if form3.getlist("farmerfind"):
        farmerfind = form3.getlist("farmerfind")
        c = sqlfarmerfind(farmerfind) #send it to other function

    return c #variable stores every entry of the database

def sqlfarmerfind(farmerfind):
    farmerslist = []
     #this for loop is converting the number so the farmers to prevent sql injection
    for i in farmerfind:
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
            farmersstring += "(gisteach.fields.owner LIKE '%"+i+"%'"
        elif counter > 0:
            farmersstring += " or GISTEACH.fields.owner LIKE '%"+i+"%'"
        counter += 1

    conn = cx_Oracle.connect(dsn="geoslearn",user="student",password=pw)
    c = conn.cursor()
    sqlfarmerstatement = ("SELECT Find_Id, Xcoord, Ycoord, type,"
    "round(depth,2), Initcap(Field_notes) FROM GISTEACH.FINDS, "
    "GISTEACH.fields where (GISTEACH.FINDS.xcoord between "
    " GISTEACH.FIELDS.LowX and GISTEACH.FIELDS.Hix)"
    "and (GISTEACH.FINDS.ycoord between GISTEACH.FIELDS.Lowy "
    "and GISTEACH.FIELDS.hiy) and "+ farmersstring +")")
    c.execute(sqlfarmerstatement)
    return c


def sqlperiod(period):
    periodlist = []
     #this for loop is converting the number so the farmers to prevent sql injection
    for i in period:
        if i == "1":
            periodlist.append("BRONZE")
        elif i == "2":
            periodlist.append("IRON_AGE")
        elif i == "3":
            periodlist.append("MESOLITHIC")
        elif i == "4":
            periodlist.append("RECENT")

    periodstring = ''
    counter = 0
     # transform the list to a string to insert it in the sql statement
    for i in periodlist:
        if counter == 0:
            periodstring += "(Period = '"+i+"'"
            #periodstring += "where (Period LIKE '%"+i+"%'"
        elif counter > 0:
            periodstring += " or Period = '"+i+"'"
        counter += 1

    conn = cx_Oracle.connect(dsn="geoslearn",user="student",password=pw)
    c = conn.cursor()
    cstring = ("SELECT Find_Id, Xcoord, Ycoord, Type, round(depth,2), Initcap(Field_notes) FROM"
                "GISTEACH.FINDS, GISTEACH.CLASS where (GISTEACH.FINDS.Type = GISTEACH.CLASS.Type) and "+periodstring+")")
    c.execute("SELECT Find_Id, Xcoord, Ycoord, GISTEACH.FINDS.type, round(depth,2), Initcap(Field_notes) FROM GISTEACH.FINDS, GISTEACH.CLASS where (GISTEACH.FINDS.Type = GISTEACH.CLASS.Type) and "+periodstring+")")

    return c


def sqldepth(depth):
    conn = cx_Oracle.connect(dsn="geoslearn",user="student",password=pw)
    c = conn.cursor()
        #sqlfarmerstatement = "SELECT Field_Id, Lowx, lowy, hix, hiy, round(area,2), initcap(owner), crop FROM GISTEACH.FIELDS where Owner = " + farmers
    c.execute("SELECT Find_Id, Xcoord, Ycoord, type, round(depth,2), Initcap(Field_notes) FROM GISTEACH.FINDS where depth >" + depth)
    return c
