#!/usr/bin/env python3

#importingg necessary packages
import cgitb
import cgi
import cx_Oracle


cgitb.enable(format="text")
from jinja2 import Environment, FileSystemLoader
import folium
import Packages

''' This file is calles when "Make your own table" is chosen
it takes the arguments of the FieldStorage and perfroms a
sql query which will be displayed'''


# protect the password by having it in another folder
with open("../../oracle",'r') as pwf:
 pw = pwf.read().strip()

def print_html():
    #function that calls the classes and the send variables to the html
    env = Environment(loader=FileSystemLoader('.'))
    temp = env.get_template('inditable.html')

    tableindi = renderindividualtable()
    # pass the varibales to html
    print(temp.render(tableindii = tableindi ))

def renderindividualtable():
    #make your own table, by clicking columns on the page
    #this list is just to check the input data for sql injection
    checklist = ["GISTEACH.Finds.Find_ID","GISTEACH.Finds.XCoord",
    "GISTEACH.Finds.YCoord","GISTEACH.Finds.Type","GISTEACH.Class.Name",
    "GISTEACH.Class.Period","GISTEACH.Class.Use","GISTEACH.Finds.Depth",
    "GISTEACH.Finds.Field_Notes","GISTEACH.Fields.Field_ID","GISTEACH.Fields.LowX",
    "GISTEACH.Fields.LowY","GISTEACH.Fields.HiX","GISTEACH.Fields.HiY",
    "GISTEACH.Fields.Area","GISTEACH.Fields.Owner","GISTEACH.Crops.Crop",
    "GISTEACH.Crops.Name","GISTEACH.Crops.Start_of_Season","GISTEACH.Crops.End_of_Season"]

    form = cgi.FieldStorage()
    if form.getlist("sql"): # check if there is data in the field storage
        columns = form.getlist("sql")
        # check the given list from webpage against the checklist
        # this is done to prevent sql injection
        check = all(item in checklist for item in columns)
        if check is True:
            insertstring = ''
            counter = 0
            lenlist = len(columns)
            for i in columns:
                #construct the sql selct statement

                insertstring += str(i)
                counter += 1
                # if there are more columns insert a ","
                if counter < lenlist:
                    insertstring += ", "


            conn = cx_Oracle.connect(dsn="geoslearn",user="student",password=pw)
            c = conn.cursor()
            # sql statement connecting all the tables, doing so gurantees a successfull retrieval
            s = ("SELECT " + insertstring +
            " FROM GISTEACH.CLASS, GISTEACH.FIELDS, GISTEACH.FINDS, GISTEACH.CROPS "
            "where (GISTEACH.FINDS.xcoord between GISTEACH.FIELDS.LowX and GISTEACH.FIELDS.Hix) "
            "and (GISTEACH.FINDS.ycoord between GISTEACH.FIELDS.Lowy and GISTEACH.FIELDS.hiy) "
            "and (GISTEACH.FIELDS.crop = GISTEACH.CROPS.crop) "
            "and (GISTEACH.FINDS.Type = GISTEACH.CLASS.Type)")
            c.execute(s)
            var_indi = str("inditable") # ensuring that the variable insert the the " " with the name
            tableindi= '<table id = "inditable"><tr class = "headerrow">'
            counterindi = 0
            for i in columns:
                header = i.split(".")[-1]
                tableindi += '<th onclick="sortTable('+var_indi+', '+ str(counterindi)+')">' + str(header) +'</th>'
                counterindi += 1
            tableindi += '</tr>'
            for row in c:
                tableindi += '<tr class = "findrow">'
                for i in range(lenlist): # this loop must be done bc unkown amount of columns
                    if str(row[i]).startswith('20'): # test for the date column which starts with the year 20xxx
                        tableindi += '<td>%s</td>' %str(row[i].strftime("%d.%m - (%B)")) # if its date column, transform the date column
                    else:
                        tableindi += '<td>%s</td>' %(str(row[i]))
                tableindi += '</tr>'
            tableindi += '</table>'
            return tableindi




if __name__ == '__main__':
    print_html()
