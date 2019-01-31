// <!--
// Michelle Tang
// SoftDev2 PD6
// K#00 -- I See a Red Door *
// 2019-01-31
// -->
// * but you should paint it black

var c = document.getElementById("slate");
var ctx = c.getContext("2d");
var clear = document.getElementById("clear");

// Clear the canvas!
clear.addEventListener("click", function(e) { clear();});
var clear = function(e){
  var width = c.getAttribute("width");
  var height = c.getAttribute("height");
  ctx.clearRect(0,0,width, height);
}

// determines if it is dot mode or not, when toggle is pressed, switch
var dot = true;
var toggle = document.getElementById('toggle');
toggle.addEventListener('click', function() {
  dot = !dot;
  // Change the button so the user knows!
  if(dot) {
    this.innerHTML = "draw-a-rectangle!";
  }
  else {
    this.innerHTML = "draw-a-dot!";
  }
});


c.addEventListener('click', function(e) {
  // Finds out the location of your mouse when you click
  var x = e.pageX - e.currentTarget.offsetLeft;
  var y = e.pageY - e.currentTarget.offsetTop;
  // if you are in dot mode, make a circle with a radius of 5 and origin of the mouse
  if(dot) {
    console.log("Making some circles");
    ctx.fillStyle = '#000000';
    ctx.beginPath();
    ctx.ellipse(x , y , 5, 5, 0, 0, 2 * Math.PI);
    ctx.fill();
  }
  // else (in rect mode), make a rect with the mouse serving as the point in the topright side
  else {
    console.log("Making some rectangle");
    ctx.fillStyle = '#FF0000';
    ctx.fillRect(x, y, 50, 90);
  }
});
