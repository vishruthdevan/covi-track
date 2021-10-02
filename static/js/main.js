// Create the script tag, set the appropriate attributes
var script = document.createElement('script');
script.src = 'https://maps.googleapis.com/maps/api/js?key=' + google_api_key + '&callback=initMap';
script.async = false;

function initMap(){}

let map;
let coords = JSON.parse(document.getElementById('coords').textContent);
window.initMap = function() {
    map = new google.maps.Map(document.getElementById("map"), {
        center: {lat: 11.349223, lng: 76.792558},
        zoom: 8,
    });

    const iconBase =
    "http://maps.google.com/mapfiles/kml/";

    const icons = {
        current : iconBase + "pushpin/blue-pushpin.png",
        zerodose : iconBase + "paddle/orange-circle.png",
        onedose : iconBase + "paddle/grn-blank.png",
        twodose : iconBase + "paddle/grn-circle.png",
        affected : iconBase + "paddle/red-circle.png",
    }
    console.log(coords)
    var marker, i;
    for (i = 1; i < coords.length; i++) {  
        marker = new google.maps.Marker({
             position: new google.maps.LatLng(coords[i].lat, coords[i].lng),
             icon: {
                 url: icons[coords[i].type],
                 scaledSize: new google.maps.Size(25, 25),
                 origin: new google.maps.Point(0,0),
                 anchor: new google.maps.Point(0, 0)
             },
             map: map
        });
    }
};

document.head.appendChild(script);
