let plot1_name = 'Population Data'
let Plot1_title = `Population Comparison Data`
let layout1 = {title: Plot1_title };
var graph1 = {{total_pop_plotlyJSON | safe}};
Plotly.plot('mapPlotly1',graph1,layout1);