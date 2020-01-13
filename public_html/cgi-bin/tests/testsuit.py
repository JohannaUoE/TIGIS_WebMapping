#Import the functions that are needed
import Packages
#testing will be performed with nosetest 3.6
from nose.tools import assert_equal, raises
import cx_Oracle


''' This file represents a small testsuit that should be executed before
running the webpage. The two tests are connecting to the database and are
checking the data inside it. This test should wpould raise in error,
if rows or columns are added to teh database. Although additional rows
would not be an issue for the database, additional columns would be
Also, this test is useful to see if the connection to teh database
for fields and finds works'''
#test to check if the database works
def test_finddb():
    #get the rows from the function of the webpage
    is_string = ''
    cpage = Packages.connectdbfind()
    for i in cpage:
        is_string+= str(i)
    #this is how the database should look like
    should_be2 ="(1, 4, 1, 1, 0.67, 'Found In Some Clay')"
    should_be2 +="(2, 8, 5, 1, 0.79, 'Several Similar Pieces Found Together')"
    should_be2 +="(3, 8, 14, 3, 1.21, 'Found Embeded In A Bone')"
    should_be2 +="(4, 7, 12, 4, 1.37, 'A Small Bone Fragment')"
    should_be2 +="(5, 4, 7, 4, 1.01, 'Markings Suggest Killed For Food')"
    should_be2 +="(6, 11, 9, 2, 0.91, 'Very Corroded')"
    should_be2 +="(7, 12, 2, 1, 0.54, 'Part Of Drinking Vessel ?')"
    should_be2 +="(8, 3, 14, 2, 0.62, 'Refined Craftwork, Found With Others')"

    #Are both equal?
    assert_equal(is_string,should_be2)

def test_fielddb():
    #get the rows from the function of the webpage
    is_string1 = ''
    cpage = Packages.connectdbfieldmap()
    for i in cpage:
        is_string1 += str(i)

    #this is how the database should look like
    should_be = ("(1, 2, 0, 6, 6, 3.56, 'Farmer Brown', 4)"
    "(2, 2, 6, 6, 11, 2.97, 'Farmer Brown', 2)"
    "(3, 6, 0, 10, 6, 3.56, 'Farmer Green', 3)"
    "(4, 6, 6, 10, 11, 2.97, 'Farmer Black', 2)"
    "(5, 10, 0, 12, 11, 3.2600000000000002, 'Farmer Green', 4)"
    "(6, 6, 11, 12, 15, 3.56, 'Farmer Black', 1)"
    "(7, 3, 12, 5, 15, 0.89, 'Farmer White', 5)"
    "(8, 0, 12, 3, 16, 1.78, 'Farmer White', 3)")



    #cpage = Packages.connectdbfieldmap()
    #for i in cpage:
        #should_be += str(i)
            #Are both equal?
    assert_equal(is_string1,should_be)





if __name__ == '__main__':
    #test_neigh()
    test_fielddb()
    test_finddb()
