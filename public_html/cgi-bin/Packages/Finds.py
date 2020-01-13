
import cgitb
import cgi
import cx_Oracle
cgitb.enable(format="text")
import folium


with open("../../oracle",'r') as pwf:
 pw = pwf.read().strip()

''' This file contains the the find class. It renders forch each instance
the svg and table '''

class findss():
    #class of the finds
    def __init__(self,findid, xcoord, ycoord, type, depth, notes):
        #assing passed values to variables in the class
        self.findid = findid
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.type = type
        self.depth = depth
        self.notes = notes


    def showartefact(self):
        #this definition creates a string with interesting inputs for hovering over finds
        conn = cx_Oracle.connect(dsn="geoslearn",user="student",password=pw)
        d = conn.cursor()
        d.execute("SELECT Type, Initcap(Name), Initcap(Period), Initcap(Use) FROM GISTEACH.CLASS")
        artefact = []
        artefactstring = ''
        for row in d:
            # &#010 introduces break in the hovertable
            artefactstring += f'&#010Name: {str(row[1])} &#010Period: {str(row[2])} &#010Usage: {str(row[3])}'
            artefact.append(artefactstring)
            artefactstring = '' #clear string again
        return artefact

    def renderfindstable(self):
        # function renders the finds rows with the variabels given for each instance
        tablefinds1 = f'<tr class = "findrow" id=Findrow{self.findid} onclick = "changecolourfind({self.findid})"><a xlink:href="Find0{self.findid}"style="display:block;">'
        tablefinds1 += f'<td>{self.findid}</td><td>{self.xcoord}</td><td>{self.ycoord}</td><td>'
        tablefinds1 += f'{self.type}</td><td>{self.depth}</td><td>{self.notes}</td></a></tr>'
        return tablefinds1

    def renderfind(self):
        # function renders the svg with the variabels given for each instance
        svgPoint = ' '#create empty string
        artefact2 = self.showartefact() # function is called for inserting it to text
        svgPoint += f'<g><circle onclick = "highlightrowfind({self.findid})" id="Find{self.findid}" class="findart{self.type} hoverfind"'
        svgPoint += f'cx="{self.xcoord}" cy="{self.ycoord} '
        svgPoint += f'" r="0.3" fill="black" data-tabindex="0"/><text class ="textno" text-anchor="middle"'

        svgPoint += f'x="{self.xcoord} " y="{self.ycoord}" dy=".35em" font-family="sans-serif"'
        svgPoint += f'font-size="0.4px" fill="white" transform="translate(0,{int(self.ycoord) *2})'
         # indexing the corresponding artefact id of the finds table
        svgPoint += f'scale(1,-1)">{self.findid}</text><title>Class: {self.type} {artefact2[int(self.type)-1]}'
        svgPoint += f'&#010Depth: {self.depth}m &#010Notes: {self.notes}'
        svgPoint += f'</title></g>'
        return svgPoint
