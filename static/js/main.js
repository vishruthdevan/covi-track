// Create the script tag, set the appropriate attributes
var script = document.createElement('script');
script.src = 'https://maps.googleapis.com/maps/api/js?key=' + google_api_key + '&callback=initMap';
script.async = false;

function initMap(){}

let map;
let coordinates = JSON.parse(document.getElementById('coords').textContent);
console.log(coordinates);
window.initMap = function() {
    map = new google.maps.Map(document.getElementById("map"), {
        center: {lat: 11.349223, lng: 76.792558},
        zoom: 8,
    });

    var marker, i;
    for (i = 0; i < coordinates.length; i++) {  
        marker = new google.maps.Marker({
             position: new google.maps.LatLng(coordinates[i][0], coordinates[i][1]),
             map: map
        });
    }
};

document.head.appendChild(script);
