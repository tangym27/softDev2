// <!--
// Michelle Tang
// SoftDev2 pd6
// K#11 -- Ask Circles [Change || Die]…While On The Go
// 2019-03-17
// -->

var pic = document.getElementById("vimage");
var clear = document.getElementById('clear');
var move = document.getElementById('move');
var random = document.getElementById('?');
var requestID;
var start = true;
var moving = false;

var create = function(x,y) {
  var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    c.setAttribute("cx", x);
    c.setAttribute("cy", y);
    c.setAttribute("vx", 1);
    c.setAttribute("vy", 1);
    c.setAttribute("r", "15");
    c.setAttribute("fill", "red");
    c.addEventListener('click', change);
  pic.appendChild(c);
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

var move_dot = function() {
    for(i = 0; i < pic.children.length; i++) {
      c = pic.children[i];
      // console.log(i);
      c.setAttribute("cx", Number(c.getAttribute("cx")) + Number(c.getAttribute("vx")));
      // console.log(Number(c.getAttribute("cx")) + Number(c.getAttribute("vx")));
      c.setAttribute("cy", Number(c.getAttribute("cy")) + Number(c.getAttribute("vy")));

      if(Number(c.getAttribute("cx")) <= 0 || (Number(c.getAttribute("cx"))  + Number(c.getAttribute("r")) >= Number(pic.getAttribute("width")))){
        c.setAttribute("vx", Number(c.getAttribute("vx") * -1));
      }
      if(Number(c.getAttribute("cy")) <= 0 || (Number(c.getAttribute("cy"))  + Number(c.getAttribute("r")) >= Number(pic.getAttribute("height")))){
        c.setAttribute("vy", Number(c.getAttribute("vy") * -1));
      }

    }
  requestID = window.requestAnimationFrame(move_dot);
}

pic.addEventListener('click', function(e) {
  e.preventDefault();
  if (e.target.getAttribute("id") == "vimage"){
        create(e.offsetX,e.offsetY);
    }
})

clear.addEventListener('click', function(e) {
  pic.innerHTML = '';
  var start = true;
})

move.addEventListener('click', function(e) {
  if(!moving) {
    moving = true;
    window.cancelAnimationFrame(requestID);
    move_dot();
  }
})

random.addEventListener('click', function(e) {
  for(i = 0; i < pic.children.length; i++) {
    c = pic.children[i];
    var radius = Number(c.getAttribute("r"));
    c.setAttribute("r", radius - 1);
  }
})
