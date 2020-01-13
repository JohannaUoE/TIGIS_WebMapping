#!/usr/bin/env python3

#importingg necessary packages
import cgitb
import cgi
import cx_Oracle


cgitb.enable(format="text")
from jinja2 import Environment, FileSystemLoader
import folium
import Packages #own Package having classes outside of the main document

'''This is main python file that collect teh variables from all other files
and sends it to the spcifies html document'''

# protect the password by having it in another folder
with open("../../oracle",'r') as pwf:
    pw = pwf.read().strip()


try:
    def print_html():
        #function that calls the classes and definition
        #and the send variables to the html

        env = Environment(loader=FileSystemLoader('.'))
        temp = env.get_template('main.html')
        #get varibales for finds
        c, tablefindss, svgPonit = Packages.sendctofind()

        #get varibales for fields
        tablefieldss, svgfields1, arearesult = Packages.sendctofield()

        # crops and artefact table
        tablecrops = Packages.rendercropstable()
        tableartefact = Packages.renderartefacttable()

        # map Background
        map = Packages.backgroundmap()
        viewbox, gviewbox, currenthx, currenthy, currentlx, currently = map.findhighestlowestxy()
        gridsvgx, gridsvgy = map.rendersvggrid()
        svgtickx = map.renderxticks()
        svgticky = map.renderyticks()

        # pass the varibales to html
        print(temp.render(svggpoint = svgPonit, svggField = svgfields1, tablefinds = tablefindss, tablefieldsH = tablefieldss,
        tablecropss = tablecrops, tableartefacts = tableartefact, gridsvgxx = gridsvgx, gridsvgyy = gridsvgy,
        svgtickxx = svgtickx, svgtickyy =svgticky, vb = viewbox, vbhx = currenthx, vbhy = currenthy,
        vblx = currentlx, vbly = currently, greatviewbox = gviewbox, area =arearesult))

except:
    #print("Content-Type: text/html")
    print("<!doctype html>")
    print("<html lang='en'>")
    print("<head>")
    print("<title>Something has gone wrong</title>")
    print("</head>")
    print("<body> Something has gone wrong. Please Check Permissions</body>")
    print("</html>")


if __name__ == '__main__':
    #whne executed over the shell, this function is called
    print_html()
