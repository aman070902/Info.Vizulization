// Define chart dimensions
var margin = {top: 50, right: 50, bottom: 50, left: 50},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

// Define x and y scales
var x = d3.scaleBand()
    .range([0, width])
    .padding(0.1);

var y = d3.scaleLinear()
    .range([height, 0]);

// Create SVG element and set dimensions
var svg = d3.select("#chart")
  .append("svg")
  .attr("width", width + margin.left + margin.right)
  .attr("height", height + margin.top + margin.bottom)
  .append("g")
  .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

// Load data from CSV file
d3.csv("data.csv").then(function(data) {

  // Format data
  data.forEach(function(d) {
    d.State = d.State;
    d.Rice2011 = +d['Rice - 2011-12'];
    d.Rice2012 = +d['Rice - 2012-13'];
    d.Rice2013 = +d['Rice - 2013-14'];
    d.Rice2014 = +d['Rice - 2014-15'];
    d.Rice2015 = +d['Rice - 2015-16*'];
  });

  // Define x and y domains
  x.domain(data.map(function(d) { return d.State; }));
  y.domain([0, d3.max(data, function(d) { return d.Rice2015; })]);

  // Create x and y axes
  var xAxis = d3.axisBottom(x);
  var yAxis = d3.axisLeft(y);

  // Add x and y axes to chart
  svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);

  svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
    .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", "-2em")
      .style("text-anchor", "end")
     
