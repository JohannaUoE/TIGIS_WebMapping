import cgitb
import cgi
import cx_Oracle
cgitb.enable(format="text")
import folium

#dierct to oracle password
with open("../../oracle",'r') as pwf:
 pw = pwf.read().strip()

''' This file contains the the fields class. It renders forch each instance
the svg and table '''

class fieldss():
     #class for the fields
    def __init__(self, fieldid, lowx, lowy, highx, highy, area, owner, cropid):
        #assing passed values to variables in the class
        self.fieldid = fieldid
        self.lowx = lowx
        self.lowy = lowy
        self.highx = highx
        self.highy = highy
        self.area = area
        self.owner = owner
        self.cropid = cropid


    def showcrops(self):
        # retrieving data of crops to show, when hovering over fields
        conn = cx_Oracle.connect(dsn="geoslearn",user="student",password=pw)
        d = conn.cursor()
        d.execute("SELECT Crop, Initcap(name), Start_of_season, end_of_season  FROM GISTEACH.CROPS")
        crops = [] #create empty list
        cropsstring = '' #create empty string
        for row in d: #loop over the d
            #&#010 introduces a line break in the hover
            cropsstring += f'&#010Crop Name: {str(row[1])}'
            cropsstring += '&#010Sowing Start: '
            cropsstring += str(row[2].strftime("%d.%m")) #format teh date
            cropsstring += '&#010Harvest Start: '
            cropsstring += str(row[3].strftime("%d.%m"))
            crops.append(cropsstring) # append to the list
            cropsstring = '' #clear string again
        return crops


    def render(self):
        #this function renders the fields rectangle
        cropslist = self.showcrops() #call the showcrops function to retrieve
        #the string
        #calcualte width and hight with the variables
        width = int(self.highx) - int(self.lowx)
        height = int(self.highy) - int(self.lowy)
        #build teh svg string
        svgField = f'<g><rect onclick="highlightrowfield({self.fieldid}, '
        svgField += f'{self.cropid})" class="fields{self.cropid} hoverfield"'
        svgField += f'id ="Field{self.fieldid}" x="{self.lowx }'
        svgField += f'" y="{self.lowy} " width="{str(width)}'
        svgField += f'" height="{str(height)}" stroke="black"'
        svgField += 'stroke-width="0.1"/><text class ="textno" text-anchor="middle" x="'
        #find x middle of rectangle
        svgField += str(( int(self.highx)- int(self.lowx) )/2 + int(self.lowx))
        svgField += '" y="'
         #find y middle of rectangle
        svgField += str((int(self.highy)- int(self.lowy))/2 + int(self.lowy))
        svgField += '" dy=".35em" font-family="sans-serif" font-size="0.6px"'
        svgField += 'fill="black"transform=" translate(0,'
         # translate by the height of the rectangle
        svgField += str(int(self.highy)+ int(self.lowy))
        svgField += f')scale(1,-1)">{self.fieldid}</text>'
        svgField += f'<title>Crop ID: {self.cropid} '
        svgField += cropslist[int(self.cropid)-1]
        svgField += f'&#010Farmer: {self.owner}'
        svgField += '&#010Area of Field: '
        area = float(self.area)
        rarea = round(area,2) #round the area (one value is long)
        svgField += f'{str(rarea)}</title></g>'
        return svgField


    def renderfieldstable(self):
        #this function renders the rows of the fields table
        area = float(self.area) #round teh area
        rarea = round(area,2)
        #build the row string
        tablefields = f'<tr onclick = "changecolourfield({self.fieldid}, {self.cropid})"'
        tablefields += f'class = "fieldrow" id="Fieldrow{self.fieldid}"><td>{self.fieldid}</td>'
        tablefields += f'<td>{self.lowx }</td><td>{self.lowy}</td><td>'
        tablefields += f'{self.highx}</td><td>{self.highy}</td>'
        tablefields += f'<td>{str(rarea)}</td><td>{self.owner }</td>'
        tablefields += f'<td>{self.cropid}</td></tr>'
        return tablefields
