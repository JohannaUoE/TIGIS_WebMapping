# Technological-Infrastructure - TIGIS_WebMapping
These files are for the Web Mapping assignment of Technological Infrastructures at the University of Edinburgh (Msc Earth Observation and Geoinformation Management).
Website can be accessed under: https://www.geos.ed.ac.uk/~s1937352/cgi-bin/main.py
Exam No.: B154523

Following the files inside this repository are listed and shortly described.
Further explanations can be found in the comments of the files.

### tests
Additionally, a testsuit was built to test the connection of the Oracle database and to see if the database has changed. If the database has changed this test will fail. In case of a failed
test the changes of within the database should be carefully observed. Changes of the contents and extensions of rows are not harming the performance of the web page. Changes regarding the number of columns affects the web site. Therefore, the test should be run with "nosetests-3.6" in the shell (cgi-bin) before running the web-page.

### stylesheets.css
This file represents the css file of the web page. All layouts and spedicications are stored
inside the file. Inspiration for the styles were retrieved from w3school.com (2020) and
codepen.io (2020).


### functionfile.js
The functionfile.js stores the majority of JavaScript functions that were written to
make the web page interactive. The functions are changing the colour of fields and
finds in the svg or in the table, sorting table columns (codepen.io 2020), show and hide
grid, fields or finds and opening new tabs within the web-page (?).
### main.py
The main.py combines all functions and is the first one to be rendered. It only consists
of the function "renderhtml()" where it collects the variables from the Packages and
send them to the main.html
### main.html
This file is read by the Internet Explorer. It renders the webpage and prints the
variables, that were sent by main.py. Additionally it gives the frame for all html code,
that has to be hard coded. Soem JavaScript functions were included inside this file
because they relate to a specific area inside the file.
### inditable.py
This file is called, when the user clicks on "Make your own Table". A new file was
created for this query to clean the main page and have it in another file. Because the
page is refreshed, when sending the data, the tab was always jumping to the default
open. Therefore, an new file had to be created. The combines the input of the user
and inserts it into a SQL statement, that combines all tables.
### inditable.html
This html file renders the tab of the "Make your own table" tab. It is very similar to
teh main.html
### __init__.py
This file packages up the files in the folder and gives permission to all functions

### Fields.py
Fields.py exists of a class, that takes variables of each column of the fields database
and renders the tablerows and svg
### connectdbfield.py
This file connects to the field database and retrieves the data. It also looks for any
FieldStorage data to adjust the query to the database
### Find.py
Find.py exists of a class, that takes variables of each column of the finds database and
renders the tablerows and svg
### connectdbfind.py
This file connects to the find database and retrieves the data. It also looks for any
FieldStorage data to adjust the query to the database
### Map.py
The Map.py file renders the framework of the svg, like the viewbox, the gridlines and
the ticks. It is also responsive to the database. Therefore changes in the database
would lead to a different framework
### Class_crops.py
This file renders the Class and Crops table, which are displayed on the web page. It
also looks for FieldStorage regarding the "Period Query".
