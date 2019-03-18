// <!--
// Michelle Tang
// SoftDev2 pd6
// K#10 -- Ask Circles [Change || Die]
// 2019-03-13
// -->


var pic = document.getElementById("vimage");
var clear = document.getElementById('clear');

var create = function(x,y) {
  var circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
  circle.setAttribute("fill", "red");
  circle.setAttribute("cx", x);
  circle.setAttribute("cy", y);
  circle.setAttribute("r", "100")
  pic.appendChild(circle);
  circle.addEventListener('click', change);
  pic.appendChild(circle);
}

var change = function(e) {
  if(e.target.getAttribute('fill') === 'red') {
    e.target.setAttribute('fill', 'green');
  }
  else {
    pic.removeChild(e.target);
    create(Math.floor(Math.random() * 500), Math.floor(Math.random() * 500));
  }
}

pic.addEventListener('click', function(e) {
  if (e.target.getAttribute("id") == "vimage"){
    create(e.offsetX, e.offsetY);
  };
})

clear.addEventListener("click", function() {
	var blank = pic.firstChild;
	while(blank){
	    pic.removeChild(blank);
	    blank = pic.firstChild;
	}
});
