(function(){
    var fName = "keren";
    var lName = "halpert";

    var fNum = fName.length;
    var lNum = lName.length;

    generateBoxes(fNum * lNum);    
})();

function generateBoxes(num)
{
    var sections = "";

    sections += '<section onmouseover="hoverOnLetter()" onmouseout="hoverOffLetter()"></section>';

    for (i=1; i < num; i++)
        sections += '<section></section>';

    var L3 = document.getElementById("L3");
    L3.innerHTML = sections;
}

function colorFunction()
{
    var L3 = document.getElementById("L3");
    var section = L3.getElementsByTagName("section");
    for (i = 0; i < 5; i++) 
        section[i].style.backgroundColor = "#3f3f3f";  
}

function undoFunction()
{
    var L3 = document.getElementById("L3");
    var section = L3.getElementsByTagName("section");
    for (i = 0; i < 5; i++) 
        section[i].style.backgroundColor = "#ffffff";  
}

function hoverOnLetter()
{
    var L3 = document.getElementById("L3");
    var section = L3.getElementsByTagName("section")[0];
    
    if(section.style.backgroundColor == "rgb(63, 63, 63)")
        section.style.backgroundImage = "url('images/letterKdark.png')";
    else
        section.style.backgroundImage = "url('images/letterK.png')";
}

function hoverOffLetter()
{
    var L3 = document.getElementById("L3");
    var section = L3.getElementsByTagName("section")[0];
    
    section.style.backgroundImage = "none";
}



