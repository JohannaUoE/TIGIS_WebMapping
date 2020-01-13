/* This Java Script file gives the background for the interactive bits of teh webpage */

// the follwoing fuction are used to change the colours of field and find svg
// and their rows when they are clicked
//they are similar to each other therefore only a few fucntions will be
// commented in detail. At the end of this collection
//is a combined unselect function to unselect everything when cklicked a specific button
//the names of teh functions are mostly selfexplornatory

function changecolourfind(id) {
    //function is called in the table, when clicked
    //the id of the element has to be parsed into the function, which is normally
    // the first row within the database
    // the id is appended to a variable
    searchid = "Find" + id
    searchid2 = "Findrow" + id
    // first find already selected find svg by inbuild javascript get ElementsByClassName
    //set the selectet to class unselected find svg and add the class hoverfind which was also deleted
    var x = document.getElementsByClassName("selectedfindsvg");
    if(x.length>0) {
        x[0].setAttribute("class", "unselectedfindsvg hoverfind")
      }
    // find the selected find row and give a the oldclass findrow again //
    var y = document.getElementsByClassName("selectedfindsrow");
      if(y.length>0) {
          y[0].setAttribute("class", "findrow")
    }
    //get each specific element by looking for the id that was given to it
    //searchid and change the class to selected
     // the appearance of the classes is specifies within the css file
    document.getElementById(searchid2).setAttribute("class", "selectedfindsrow");
    document.getElementById(searchid).setAttribute("class", "selectedfindsvg");
  }

function changecolourfindartefact(id) {
    searchid = "findart" + id
    searchid2 = "Classrow" + id
    if (typeof artefactype == 'undefined') {
            artefactype = "findart" + id  +" hoverfind"
          }
    else{
    // this function has to proceed slightly differently because
    // mulitple finds can be selected by one artefact
    //class, there for it loops over a list of elements that
    //it gets by the getElementsfunction
    var listeartefact = document.getElementsByClassName("selectedfindartefactsvg");
          for(indexartefacts = 0; indexartefacts < listeartefact.length; indexartefacts) {
              listeartefact[indexartefacts].setAttribute("class", artefactype);
        }

    var y = document.getElementsByClassName("selectedfindsartefactrow");
    if(y.length>0) {
      y[0].setAttribute("class", "findrow")
      }}
    artefactype = "findart" + id  +" hoverfind"

    document.getElementById(searchid2).setAttribute("class", "selectedfindsartefactrow");
    var index = 0
    var listeclass = document.getElementsByClassName(searchid);
      for (index = 0; index < listeclass.length; index) {
        listeclass[index].setAttribute("class", "selectedfindartefactsvg");
    }
      }

function changecolourfield(id, crop) {
// this function must also take the fact into account that the fields have
// different colours that are dependent on the
//croptype. Therefore it takes the croptype as a variable in the function.
// It also needs to check if the croptype class is already defined
//otheriwse it would always take the class of the previous, changing all classes.
  searchid = "Field" + id
  searchid2 = "Fieldrow" + id
  //check if the croptype is already defined, and define it
  if (typeof croptype == 'undefined') {
        croptype = "fields" + crop +" hoverfield"
        }
      // if its already defined use it and change the colour back to
  else {
    var x = document.getElementsByClassName("selectedfieldssvg");
    if(x.length>0) {
            x[0].setAttribute("class", croptype)
            }

    var y = document.getElementsByClassName("selectedfieldsrow");
        if(y.length>0) {
          y[0].setAttribute("class", "fieldrow")

    }
    // assign a new value to the croptype that then can be parsed into the next call of the function again
        croptype = "fields" + crop +" hoverfield"
      }

  document.getElementById(searchid2).setAttribute("class", "selectedfieldsrow");
  document.getElementById(searchid).setAttribute("class","selectedfieldssvg");

  }

  function changecolourfieldcrops(id) {
  //this function acts limilar to the previous one except that multiple fields
  //can be selected therefore it needs to iterate
  //over a list of elements
    if (typeof croptypes == 'undefined') {
          croptypes = "fields" + id +" hoverfield"
        }
      else {
    var indexcrops = 0
    var listecrops = document.getElementsByClassName("selectedfieldscropssvg");
    for(indexcrops = 0; indexcrops < listecrops.length; indexcrops) {
              listecrops[indexcrops].setAttribute("class", croptypes);
              }}
    var y = document.getElementsByClassName("selectedfieldscroprow");
        if(y.length>0) {
        y[0].setAttribute("class", "fieldrow")}
    croptypes = "fields" + id + " hoverfield"
    searchid = "fields" + id
    searchid2 = "Cropsrow" + id
    var index = 0
    var listeclass = document.getElementsByClassName(searchid);
          for (index = 0; index < listeclass.length; index) {
    listeclass[index].setAttribute("class", "selectedfieldscropssvg");
  }
  document.getElementById(searchid2).setAttribute("class", "selectedfieldscroprow");
  }


function highlightrowfind(id) {
// this function shall highlight the row in the table, when a find is
// clicked and also the find
    searchid = "Find" + id
    searchid2 = "Findrow" + id
    var x = document.getElementsByClassName("selectedfindsvg");
    if(x.length>0) {
        x[0].setAttribute("class", "unselectedfindsvg hoverfind")
      }
    var y = document.getElementsByClassName("selectedfindsrow");
    if(y.length>0) {
        y[0].setAttribute("class", "findrow")
    }
    document.getElementById(searchid2).setAttribute("class", "selectedfindsrow");
    document.getElementById(searchid).setAttribute("class", "selectedfindsvg");
  }

function highlightrowfield(id,crop) {
// similar as previous but needs to take the croptype into
//account to change the colour back to original again
  searchid = "Field" + id
  searchid2 = "Fieldrow" + id
  if (typeof croptype == 'undefined') {
            croptype = "fields" + crop +" hoverfield"
        }
  else {
    var x = document.getElementsByClassName("selectedfieldssvg");
    if(x.length>0) {
            x[0].setAttribute("class", croptype)
        }
    var y = document.getElementsByClassName("selectedfieldsrow");
      if(y.length>0) {
        y[0].setAttribute("class", "fieldrow")
    }
         croptype = "fields" + crop +" hoverfield"
       }
  document.getElementById(searchid2).setAttribute("class", "selectedfieldsrow");
  document.getElementById(searchid).setAttribute("class", "selectedfieldssvg");
    }

function unselectfunction(){
  // this function combines the first part of all other function and
  // combines them into a function that unselects everything that was
  //selected. This function is only calles within a button to reset the selections
  var listefindx = document.getElementsByClassName("selectedfindsvg");
  if(listefindx.length>0) {
  listefindx[0].setAttribute("class", "unselectedfindsvg")
   }
  var listefindy = document.getElementsByClassName("selectedfindsrow");
  if(listefindy.length>0) {
      listefindy[0].setAttribute("class", "findrow")}
  var listefieldx = document.getElementsByClassName("selectedfieldssvg");
  if(listefieldx.length>0) {
          listefieldx[0].setAttribute("class", croptype)
          }
  var listefieldy = document.getElementsByClassName("selectedfieldsrow");
    if(listefieldy.length>0) {
        listefieldy[0].setAttribute("class", "fieldrow")
  }
  var indexcrops = 0
  var listecropsx = document.getElementsByClassName("selectedfieldscropssvg");
          for(indexcrops = 0; indexcrops < listecropsx.length; indexcrops) {
              listecropsx[indexcrops].setAttribute("class", croptypes);
                }
  var listecropsy = document.getElementsByClassName("selectedfieldscroprow");
                if(listecropsy.length>0) {
                listecropsy[0].setAttribute("class", "fieldrow")}

  var indexartefacts = 0
  var listeartefactx = document.getElementsByClassName("selectedfindartefactsvg");
            for(indexartefacts = 0; indexartefacts < listeartefactx.length; indexartefacts) {
                    listeartefactx[indexartefacts].setAttribute("class", artefactype);
                }

  var listeartefacty = document.getElementsByClassName("selectedfindsartefactrow");
          if(listeartefacty.length>0) {
        listeartefacty[0].setAttribute("class", "findrow")
                }}


// the following three function are hiding or shwoing the fields, finds and then
// grid when a button is clicked.
//This is only done within html, where <g> got an id,
//which is then not displayed or displayed again
//Hide and Show functions are adopted from w3school

function hidefields() {
  // get the id of the <g>
    var clickedfields = document.getElementById("svgFields");
    // if its already turned off
    if (clickedfields.style.display === "none") {
      // turn on
          clickedfields.style.display = "block";
      // otherwise set it to not display
      } else {
          clickedfields.style.display = "none";
            }
          }

// similar to previous just with finds
function hidefinds() {
    var clickedfinds = document.getElementById("svgFinds");
    if (clickedfinds.style.display === "none") {
        clickedfinds.style.display = "block";
      } else {
      clickedfinds.style.display = "none";
                }
        }
// similar to previous just with the grid
function hidegrid() {
    var clickedgrid = document.getElementById("grid");
    if (clickedgrid.style.display === "none") {
        clickedgrid.style.display = "block";
          } else {
        clickedgrid.style.display = "none";
                  }
          }


function openPage(elmnt, pageName, color) {
// this function opens the new tabs, when clicking on teh buttons of the tabs
// this code is partlz taken from w3school.com but customized
// to fit my purpose
      var i, tabcontent, tablinks;
      // get the element by class name
      tabcontent = document.getElementsByClassName("tabcontent");
      // loop over the elements and turn them off
      for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
          }
        // do the same of class name tablink, if the
        // if the bacground colour is wanted to be changed
      tablinks = document.getElementsByClassName("tablink");
      for (i = 0; i < tablinks.length; i++) {
        tablinks[i].style.backgroundColor = "";
        }
      // get element by is, which is parsed in the function
      // and display it
      document.getElementById(pageName).style.display = "block";
      elmnt.style.backgroundColor = color;
            }
