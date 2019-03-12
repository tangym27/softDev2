// <!-- Michelle Tang
// SoftDev2 pd6
// K#09 -- Connect the Dots
// 2019-03-12 -->

var pic = document.getElementById("vimage");

var clear = document.getElementById("clear");

var lastX = 0;
var lastY = 0;

var create = function(e){
    if (lastX){
      var line = document.createElementNS("http://www.w3.org/2000/svg", "line");
      line.setAttribute("x1", lastX);
      line.setAttribute("y1", lastY);
      line.setAttribute("x2", e.offsetX);
      line.setAttribute("y2", e.offsetY);
      line.setAttribute("stroke", "black")
      pic.appendChild(line);
    }

    var circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    circle.setAttribute("fill", "red");
    circle.setAttribute("cx", e.offsetX);
    circle.setAttribute("cy", e.offsetY);
    circle.setAttribute("r", "10")
    pic.appendChild(circle);

    lastX = e.offsetX;
    lastY = e.offsetY;
}

pic.addEventListener("click", create);

clear.addEventListener("click", function() {
	var blank = pic.firstChild;
	while(blank){
	    pic.removeChild(blank);
	    blank = pic.firstChild;
	}
	lastX = 0;
	lastY = 0;
});
