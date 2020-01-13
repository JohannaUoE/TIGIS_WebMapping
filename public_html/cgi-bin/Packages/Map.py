import Packages
#import the other function s of the package

''' This file renders the map layout '''

class backgroundmap:
    #this is just a class to group some function. it
    #does not have to be necessarily a class

    def findshl(self):
        #this function looks for the highest/ lowest x and y value of the finds
        #get the oracle connector from the connectdbfinds.py
        findsc = Packages.connectdbfind()
        counterfind = 0

        for row in findsc:
            #loop over the database
            # assign the first row as given
            if counterfind == 0:
                findhx = (float(row[1]))
                findhy = (float(row[2]))
                findlx = (float(row[1]))
                findly = (float(row[2]))
            else:
            #loop through the data and test if the next value is higher/smaller then
            #the previous and replace respectively
                if (float(row[1])) > findhx:
                    findhx = (float(row[1]))
                if (float(row[2])) > findhy:
                    findhy = (float(row[2]))
                if (float(row[1])) < findlx:
                    findlx = (float(row[1]))
                if (float(row[2])) < findly:
                    findly = (float(row[2]))
            counterfind += 1
    #find highest and lowest values for the finds
        if findhx > findhy:
            highestfind = findhx + 2.0
        else:
            highestfind = findhy + 2.0

        if findlx < findly:
            lowestfind = findlx
            lowestfindgvb = findlx - 1.0
        else:
            lowestfind = findly
            lowestfindgvb = findly - 1.0
        #greater viewbox must be slightly bigger than the smaller one
        # it must be - 1 to the old

        return highestfind, lowestfind, lowestfindgvb, findhx, findhy, findlx, findly

    def fieldshl(self):
        #this function looks for the highest/ lowest x and y value of the fields
        #get the oracle connector from the connectdbfinds.py
        fieldsc= Packages.connectdbfieldmap()
         #this function shall find the highest and lowest x and y value to
         # to create the view box in the html. This not hardcoded bc more finds and Fields
         #might be added at a later point and then the script does not have to be changed
         # assign the first row as given
        counter = 0

        for row in fieldsc:
            #loop over teh database
            # assign the first row as given
            if counter == 0:
                currenthx = (float(row[3]))
                currenthy = (float(row[4]))
                currentlx = (float(row[1]))
                currently = (float(row[2]))
            else:
             #loop through the data and test if the next value is higher/smaller then
             #the previous and replace respectively
                if (float(row[3])) > currenthx:
                    currenthx = (float(row[3]))
                if (float(row[4])) > currenthy:
                    currenthy = (float(row[4]))
                if (float(row[1])) < currentlx:
                    currentlx = (float(row[1]))
                if (float(row[2])) < currently:
                    currently = (float(row[2]))
            counter += 1
            #viewbox must be a square and plus two of the higher number
            #small viewbox
            # must be checked against the highest lowest x and y of the finds,
            #bc they could be outside of the fields
            #find highest and lowest values for the fields
        if currenthx > currenthy:
            highestfield = currenthx + 2.0
        else:
            highestfield = currenthy + 2.0

        if currentlx < currently:
            lowestfield = currentlx
            lowestfieldgvb = currentlx - 1.0
        else:
            lowestfield = currently
            lowestfieldgvb = currently - 1.0
        #greater viewbox must be slightly bigger than the smaller owner
        # ist must be - 1 to the old findhighestlowestxy

        return highestfield, lowestfield, lowestfieldgvb, currenthx, currenthy, currentlx, currently
    #compare the highest and lowest values of both and just parse the highest and loewst

    def findhighestlowestxy(self):
        #this function takes the reuslt of the previous two and compares finds
        #against fields.
        highestfield, lowestfield, lowestfieldgvb, currenthx, currenthy, currentlx, currently = self.fieldshl()
        highestfind, lowestfind, lowestfindgvb, findhx, findhy, findlx, findly = self.findshl()
        #find the highest and lowest values of fields and finds

        if highestfind > highestfield:
            highest = highestfind
        else:
            highest = highestfield

        if lowestfind < lowestfield:
            lowest = lowestfind
        else:
            lowest = lowestfield

        if lowestfindgvb < lowestfieldgvb:
            lowestgvb = lowestfindgvb
        else:
            lowestgvb = lowestfieldgvb

        #find the highest and lowest values for the rectangle
        # field and find values will be compared
        if findhx > currenthx:
            highestx = findhx
        else:
            highestx = currenthx

        if findhy > currenthy:
            highesty = findhy
        else:
            highesty = currenthy

        if findlx < currentlx:
            lowestx = findlx
        else:
            lowestx = currentlx

        if findly < currently:
            lowesty = findly
        else:
            lowesty = currently

        viewbox =  str(lowest) + " " + str(lowest) + " " +  str(highest) + " " + str(highest)
        gviewbox =  str(lowestgvb) + " " + str(lowestgvb) + " " +  str(highest) + " " + str(highest)
        return viewbox , gviewbox, highestx, highesty, lowestx, lowesty


    def rendersvggrid(self):
        #this function renders the grid based on the input by the highest and lowest x and y values
        viewbox, gviewbox, hx, hy, lx, ly = self.findhighestlowestxy()
        gridsvgy = ''
        gridsvgx = ''
        for i in range(int(lx),int(hx)):
            gridsvgy += f'<line x1="{str(i)}" y1="{str(ly)}"'
            gridsvgy += f'x2="{str(i)}" y2="{str(hy)}" />'
        for i in range(int(ly),int(hy)):
            gridsvgx += f'<line x1="{str(lx)}" y1="{str(i)}"'
            gridsvgx += f'x2="{str(hx)}" y2="{str(i)}" />'
        return gridsvgx, gridsvgy

    def renderxticks(self):
        #this function generates x ticks, based on the input of the other function
        svgtickx = ''
        viewbox, gviewbox, hx, hy, lx, ly = self.findhighestlowestxy()
        for i in range(0,int(hx)+2,2): #must add plus two bc last value is not displayed
            svgtickx += f'<text x="{str(i)}" y="16.5"'
            svgtickx += f'font-size="0.4px">{str(i)}</text>'
        return svgtickx

    def renderyticks(self):
        #this function generates y ticks, based on the input of the other function
        svgticky = ''
        viewbox, gviewbox, hx, hy, lx, ly = self.findhighestlowestxy()
        hy = int(hy)
        for i in range(0,int(hy)+2,2): #must add plus two bc last value is not displayed
            svgticky += f'<text x="-0.3" y="{str(i)}" text-anchor="end"'
            svgticky += f'font-size="0.4px">{str(hy)}</text>'
            hy = hy-2
        return svgticky
