// <!--
// a-DOOR-able:  Michelle Tang & Kyle Tau
// SoftDev2 PD6
// K#02
// 2019-02-01
// -->

var c = document.getElementById("playground");
var ctx = c.getContext("2d");
var clear = document.getElementById("clear");
var warning = document.getElementById("warning");
var drawnOn = false;
var first = true;

// Clear button (checks if there is anything to clear)
clear.addEventListener("click", function(e) {
  if (drawnOn){ // check if the user has drawn something
    clear()
  }
  else { // if the user hasn't, prevent them from the default (clearing) aka cancels the clear. Gives a warning to the user!
    console.log("stop clearing");
    warning.innerHTML = "Can't clear, draw something!"
    e.preventDefault();
  }
});

// Clear the canvas
var clear = function(e){
  var width = c.getAttribute("width");
  var height = c.getAttribute("height");
  ctx.clearRect(0,0,width, height);
  drawnOn = false; // once cleared, the canvas is not drawn on
  first = true;
}


c.addEventListener('click', function(e) {
  // Finds out the location of your mouse when you click by removing previous padding
  var x = e.offsetX;
  var y = e.offsetY;
  if (first){ // if this is the first time you are drawing on the canvas, it will save the previous coordinates as the first
    ctx.beginPath();
    lastx = x;
    lasty = y;
    first = false; //already has baseline
  }
    console.log("Making some circles");
    ctx.moveTo(lastx, lasty); // find from old spot
    ctx.lineTo(x, y); // draw line to next point
    ctx.stroke(); // draws the line
    ctx.beginPath();
    ctx.ellipse(x , y , 10, 10, 0, 0, 2 * Math.PI); // creates the circle
    ctx.stroke(); // draws the circle
  drawnOn= true; // the user has drawn something
  warning.innerHTML = ""; // gets rid of any previous warnings
  // update to new coordinates
  if (!first){
    lastx = x;
    lasty = y;
  }
});
