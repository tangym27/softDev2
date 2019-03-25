
var IDs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
var age =[44, 33, 22, 11, 49, 13, 32, 27, 23, 23]

var width = 1000;
var height = 1000;
var svg = d3.select(".chart").attr("width", width).attr("height", height)

var i = 0;
while (i < IDs.length){
  var circle = svg.append("circle")
      .attr("cx", function(e){return 50+100*IDs[i]})
      .attr("cy", function(e){return ((100+(d3.max(age)+1)*6)-(6*age[i]))})
      .attr("r", 5);
  i += 1;
}


var x_scale = d3.scaleLinear()
    .domain([0,d3.max(IDs)+2])
    .range([0, (d3.max(IDs)+2)*100]);

var y_scale = d3.scaleLinear()
    .domain([0,d3.max(age)+1])
    .range([30+(d3.max(age)+1)*6,0]);

var x = d3.axisBottom()
    .scale(x_scale)

var y_axis = d3.axisLeft()
    .scale(y_scale)

var chart = d3.select(".chart")
chart.append('g')
    .attr("transform","translate (50,420)")
    .call(x)

chart.append('g')
    .attr("transform","translate (50,100)")
    .call(y_axis)

chart.append("text")
    .attr("x",width / 2 - 150)
    .attr("y", 0)
    .attr("dy","2em")
    .text("Peeps from Notes and Code");

chart.append("text")
    .attr("x",width/2-150)
    .attr("y",height/2-70)
    .attr("dy","2em")
    .text("ID");

chart.append("text")
    .attr("transform","rotate(-90)")
    .attr("x",-240)
    .attr("y",10)
    .attr("dy","1em")
    .text("Ages");
