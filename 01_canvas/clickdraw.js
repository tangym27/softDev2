// <!--
// a-DOOR-able:  Michelle Tang & Kyle Tau
// SoftDev2 PD6
// K#01 -- ...and I want to Paint It Btter
// 2019-01-31
// -->


var c = document.getElementById("slate");
var ctx = c.getContext("2d");
var clear = document.getElementById("clear");
var warning = document.getElementById("warning");
var drawnOn = false;

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
}

// determines if it is isDot mode or not, when toggle is pressed, switch
var isDot = true;
var toggle = document.getElementById('toggle');
toggle.addEventListener('click', function() {
  isDot = !isDot;
  // Change the button so the user knows!
  if(isDot) {
    warning.innerHTML = "You are drawing dots!"
    this.innerHTML = "draw-a-rectangle!";
  }
  else {
    warning.innerHTML = "You are drawing rectangles!"
    this.innerHTML = "draw-a-isDot!";
  }
});


c.addEventListener('click', function(e) {
  // Finds out the location of your mouse when you click by removing previous padding
  var x = e.offsetX;
  var y = e.offsetY;
  // if you are in isDot mode, make a circle with a radius of 5 and origin of the mouse
  if(isDot) {
    console.log("Making some circles");
    ctx.fillStyle = '#000000';
    ctx.beginPath(); // resets the path so your isDots are individual of each other (instead of connecting the dots)
    ctx.ellipse(x , y , 5, 5, 0, 0, 2 * Math.PI);
    ctx.fill();
  }
  // else (in rect mode), make a rect with the mouse serving as the point in the upper left corner
  else {
    console.log("Making some rectangle");
    ctx.fillStyle = '#FF0000';
    ctx.beginPath(); // resets the path so your isDots are individual of each other (instead of connecting the rect)
    ctx.fillRect(x, y, 50, 90);
  }
  drawnOn= true; // the user has drawn something
  warning.innerHTML = ""; // gets rid of any previous warnings
});
