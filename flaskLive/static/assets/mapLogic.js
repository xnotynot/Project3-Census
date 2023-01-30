// Creating the map object
function drawLeaflet(map_JSdataJSON){
var myMap = L.map("map", {
    center: [27.96044, -82.30695],
    zoom: 7
  });
  // Adding the tile layer
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(myMap);
  // Load the GeoJSON data.
  var geoData = map_JSdataJSON;
//   var geoData = "../static/data/FinalData.json";
  var geojson;
  // d3.json(geoData).then(function(data) {
    // for (let i = 0; i < data.length; i++){
      for (let i = 0; i < geoData.length; i++){
      var county = geoData[i]
      L.geoJson(county, {
        color: "grey",
        fillColor: getColor(parseInt(county['properties']['2020']["Population"])),
        fillOpacity: 0.5
      }).bindPopup("<h1>" +
      county.properties.NAME + " " + county.properties.LSAD  + 
      "</h1><br /><br /><h5><strong>Population:</strong>" + numeral(parseInt(county['properties']['2020']["Population"])).format('0,0') + "</h5>" +
      "<h5><strong>Poverty Rate:</strong>" + 
      Math.round((parseInt(county['properties']['2020']["Poverty Count"]) / parseInt(county['properties']['2020']["Population"]))*100) + "%"
      ).addTo(myMap);
      }
    
    
  // });
  function getColor(depth) {
    return depth > 1000000 ? '#800026' :
           depth > 500000  ? '#BD0026' :
           depth > 250000  ? '#E31A1C' :
           depth > 100000  ? '#FC4E2A' :
           depth > 50000  ? '#FD8D3C' :
           depth > 25000   ? '#FEB24C' :
           depth > 10000   ? '#FED976' :
                      '#FFEDA0';
  }
  var legend = L.control({position: 'topright'});
  legend.onAdd = function (myMap) {
    var div = L.DomUtil.create('div', 'info legend'),
        depth = [0, 10000, 25000, 50000 , 100000, 250000, 500000, 1000000],
        labels = [];
        var legendInfo = "<h1><strong>County Population</strong></h1>" 
      
        div.innerHTML = legendInfo;
    // loop through our depth intervals and generate a label with a colored square for each interval
    for (var i = 0; i < depth.length; i++) {
        div.innerHTML +=
            '<i style="background:' + getColor(depth[i] + 1) + '"></i> ' +
            numeral(depth[i]).format('0,0') + (depth[i + 1] ? '&ndash;' + numeral(depth[i + 1]).format('0,0') + '<br>' : '+');
    }
    return div;
  };
  legend.addTo(myMap);
}