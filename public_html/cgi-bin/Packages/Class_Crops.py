
import cgitb
import cgi
import cx_Oracle
cgitb.enable(format="text")
import folium


with open("../../oracle",'r') as pwf:
 pw = pwf.read().strip()

''' This file inherits a couple of function that are rendering the
crops and classes table. The classes table must also take FieldStorage
into account and calls in case of data another function to generate
a new c '''

def rendercropstable():
    #render crops table
    # use variable for sorttable function
    var_crops = str("cropstable")
    #connect to the data base
    conn = cx_Oracle.connect(dsn="geoslearn",user="student",password=pw)
    c = conn.cursor()
    c.execute("SELECT Crop, Initcap(name), Start_of_season, end_of_season  FROM GISTEACH.CROPS")
    #create the table and call necessary Javascriptfunctions
    tablecrops = f'<table class="table" id="cropstable"><tr class = "headerrow">'
    tablecrops += f'<th onclick="sortTable({var_crops}, 0)" >Crop ID</th>'
    tablecrops += f'<th onclick="sortTable({var_crops},1)">Name</th>'
    tablecrops += f'<th onclick="sortTable({var_crops},2)">Sowing Starts</th>'
    tablecrops += f'<th onclick="sortTable({var_crops}, 3)">Harvest Ends</th></tr>'
    #loop over database to fill the table with the data from the database
    for row in c:
        tablecrops += f'<tr onclick = "changecolourfieldcrops({str(row[0])})"'
        tablecrops += f'class = "fieldrow" id="Cropsrow{str(row[0])}">'
        tablecrops += f'<td>{str(row[0])}</td><td>{str(row[1])}</td>'
        tablecrops += f'<td>{str(row[2].strftime("%d.%m - (%B)"))}</td><td>'
        tablecrops += f'{str(row[3].strftime("%d.%m - (%B)"))}</td></tr>'
    tablecrops += '</table>' # close the table

    return tablecrops


def sqlperiods(period):
    periodlist = []
     #this for loop is converting the number so the farmers to prevent sql injection
    for i in period:
        if i == "1":
            periodlist.append("BRONZE")
        elif i == "2":
            periodlist.append("IRON_AGE")
        elif i == "3":
            periodlist.append("Mesolithic")
        elif i == "4":
            periodlist.append("RECENT")

    periodstring = ''
    counter = 0
     # transform the list to a string to insert it in the sql statement
    for i in periodlist:
        if counter == 0:
            periodstring += "where (Period = '"+i+"'"
            #periodstring += "where (Period LIKE '%"+i+"%'"
        elif counter > 0:
            periodstring += " or Period = '"+i+"'"
        counter += 1

    conn = cx_Oracle.connect(dsn="geoslearn",user="student",password=pw)
    c = conn.cursor()
    c.execute("SELECT Type, initcap(Name), Initcap(Period), Initcap(Use) FROM GISTEACH.CLASS " +periodstring+")")

    return c

def renderartefacttable():
    #render the table for artefacts
    #use a variable for the sorttable function

    var_arts =str("artefacttable")
    #connect to teh database
    conn = cx_Oracle.connect(dsn="geoslearn",user="student",password=pw)
    c = conn.cursor()
    c.execute("SELECT Type, initcap(Name), Initcap(Period), Initcap(Use) FROM GISTEACH.CLASS")

    form = cgi.FieldStorage()
    if form.getlist("period"):
        period = form.getlist("period")

        c = sqlperiods(period)
    #use specific sql query to transform the data, like having only the first letter uppercase etc
    #create the table with specific java script functions that will be called
    tableartefact = '<table class="table2" id="artefacttable"><tr class = "headerrow">'
    tableartefact += f'<th onclick="sortTable({var_arts}, 0)" >Class ID</th>'
    tableartefact += f'<th onclick="sortTable({var_arts},1)">Name</th>'
    tableartefact += f'<th onclick="sortTable({var_arts}, 2)">Period</th>'
    tableartefact += f'<th onclick="sortTable({var_arts},3)">Usage</th></tr>'
    #loop over the database to fill the table with data
    for row in c:
        tableartefact += f'<tr onclick = "changecolourfindartefact({str(row[0])})"'
        tableartefact += f'class = "findrow" id="Classrow{str(row[0])}">'
        tableartefact += f'<td>{str(row[0])}</td><td>{str(row[1]).replace("_"," ")}</td>'
        tableartefact += f'<td>{str(row[2]).replace("_"," ")}</td><td>'
        tableartefact += f'{str(row[3])}</td></tr>'
    tableartefact += '</table>'

    return tableartefact
