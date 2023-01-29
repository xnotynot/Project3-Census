// Creating the map object
var myMap = L.map("map", {
  center: [27.96044, -82.30695],
  zoom: 7
});

// Adding the tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap);

// Load the GeoJSON data.
var geoData = "../static/data/FinalData.json";
var geojson;

d3.json(geoData).then(function(data) {
  for (let i = 0; i < data.length; i++){
    var county = data[i]
    L.geoJson(county, {
      color: "grey",
      fillColor: getColor(parseInt(county['properties']['2018']["Population"])),
      fillOpacity: 0.5
    }).bindPopup("<strong>County Name:</strong> " +
    county.properties.NAME + " " + county.properties.LSAD  + 
    "<br /><br /><strong>Population:</strong>" + parseInt(county['properties']['2018']["Population"])).addTo(myMap);

  }

});


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

