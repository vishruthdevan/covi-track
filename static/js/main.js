// Create the script tag, set the appropriate attributes
var script = document.createElement('script');
script.src = 'https://maps.googleapis.com/maps/api/js?key=' + google_api_key + '&callback=initMap';
script.async = false;

function initMap(){}

let map;
let coords = JSON.parse(document.getElementById('coords').textContent);
let centre = JSON.parse(document.getElementById('centre').textContent);

window.initMap = function() {
    map = new google.maps.Map(document.getElementById("map"), {
        center: new google.maps.LatLng(centre.lat, centre.lng),
        zoom: 8,
    });
    const iconBase =
    "http://maps.google.com/mapfiles/kml/";

    const icons = {
        current : iconBase + "pushpin/blue-pushpin.png",
        zerodose : iconBase + "paddle/orange-circle.png",
        onedose : iconBase + "paddle/grn-blank.png",
        twodoses : iconBase + "paddle/grn-circle.png",
        affected : iconBase + "paddle/red-circle.png",
    }
    var marker, i;
    for (i = 0; i < coords.length; i++) {  
        marker = new google.maps.Marker({
             position: new google.maps.LatLng(coords[i].lat, coords[i].lng),
             icon: {
                 url: icons[coords[i].type],
                 scaledSize: new google.maps.Size(25, 25),
                 origin: new google.maps.Point(0,0),
                 //anchor: new google.maps.Point(0, 0)
             },
             map: map
        });
    }
};

document.head.appendChild(script);
