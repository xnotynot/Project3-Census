// read county
var counties_infojsonFile = "../../data/popincome_data_reduced.json";
var county_popinfo = []
var stateFieldName = "state";
var countyFieldName = "county";
d3.json(counties_infojsonFile).then(function (popinfo) {
  county_popinfo = popinfo;
});

var county_geojsonFile = "../../data/gz_2010_us_050_00_5m.json";
d3.json(county_geojsonFile).then(function (data) {
  // Once we get a response, send the data.features object to the createFeatures function.
  createFeatures(data.features,county_popinfo);
});

//nodejs
// const {MongoClient} = require('mongodb');
// mongodb://localhost:27017
// /**
//  * Connection URI. Update <username>, <password>, and <your-cluster-url> to reflect your cluster.
//  * See https://docs.mongodb.com/ecosystem/drivers/node/ for more details
//  */
// const uri = "mongodb+srv://<username>:<password>@localhost/test?retryWrites=true&w=majority";
// const client = new MongoClient(uri);
// await client.connect();
//------------------------------

for(var i = 0; i < county_popinfo.length; i++) {
  var obj = county_popinfo[i];
  console.log(obj.id,obj.name);
}

var popinfo = [];
function searchData(stateFIPS,countyFIPS){
  for (var i=0 ; i < county_popinfo.length ; i++){
    if (county_popinfo[i][stateFieldName] == stateFIPS  && county_popinfo[i][countyFieldName] == countyFIPS){
      return(county_popinfo[i]);
    }
  }
}
// createFeatures(data.features,county_popinfo);
function createFeatures(countyGeoData,county_popinfo) {

  // Define a function that we want to run once for each feature in the features array.
  function onEachFeature(feature, layer) {
    // var stateFIPS = feature.properties.STATE;
    // var stateFIPS = feature.properties.COUNTY;
    popinfo = [];
    popinfo = searchData(feature.properties.STATE,feature.properties.COUNTY)
    // layer.bindPopup(`<h3>${feature.properties.NAME}</h3><hr><p>FIPS_ID / ${feature.properties.STATE}+${feature.properties.COUNTY}</hr><hr>${popinfo[0].Population}</hr></p>`)
    layer.bindPopup(`<h3>${feature.properties.NAME}</h3><hr><p>FIPS_ID / ${feature.properties.STATE}+${feature.properties.COUNTY}</p>`)
  }

  // Create a GeoJSON layer that contains the features array on the earthquakeData object.
  // Run the onEachFeature function once for each piece of data in the array.
  var countyInfo = L.geoJSON(countyGeoData, {
    onEachFeature: onEachFeature
  });

  // Send our county info layer to the createMap function
  createMap(countyInfo);
}

function createMap(countyInfo) {

  // Create the base layers.
  var street = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  })

  var topo = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
    attribution: 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
  });

  // // Top 10 populated cities
  // var cities = L.layerGroup([littleton, denver, aurora, golden]);
  
  // Create a baseMaps object.
  var baseMaps = {
    "Street Map": street,
    "Topographic Map": topo
  };

  // Create an overlay object to hold our overlay.
  var overlayMaps = {
    Counties: countyInfo,
    // Population: popInfo
  };

  // Create our map, giving it the streetmap and earthquakes layers to display on load.
  var myMap = L.map("map", {
    center: [
      37.09, -95.71
    ],
    zoom: 5,
    layers: [street,countyInfo]
  });

  // var marker = L.marker([10.496093,-66.881935]).on('click', onClick);
  // function onClick(e) {alert(e.latlng);}
  // marker.addTo(map)

  // Create a layer control.
  // Pass it our baseMaps and overlayMaps.
  // Add the layer control to the map.
  L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
  }).addTo(myMap);

}

