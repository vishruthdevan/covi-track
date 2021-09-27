// Create the script tag, set the appropriate attributes
var script = document.createElement('script');
script.src = 'https://maps.googleapis.com/maps/api/js?key=' + google_api_key + '&callback=initMap';
script.async = false;

function initMap(){}

let map;

window.initMap = function() {
    map = new google.maps.Map(document.getElementById("map"), {
        center: {lat: 11.349223, lng: 76.792558},
        zoom: 8,
      });

    const marker = new google.maps.Marker({
      position: {lat: 11.349223, lng: 76.792558},
      map : map,
    });
};

document.head.appendChild(script);