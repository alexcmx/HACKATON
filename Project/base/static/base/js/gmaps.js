var customLabel = {
    restaurant: {
        label: 'R'
    },
    bar: {
        label: 'B'
    }
};

$(window).load(function() {
    $("#loaderInner").fadeOut();
    $("#loader").delay(400).fadeOut("slow");
});

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: new google.maps.LatLng(55.75370903771494, 37.61981338262558),
        zoom: 15,
        disableDefaultUI: true,
        fullscreenControl: true,
        styles: [

            {
                "elementType": "geometry",
                "stylers": [{
                    "color": "#ebe3cd"
                }]
            },
            {
                "elementType": "labels.text.fill",
                "stylers": [{
                    "color": "#523735"
                }]
            },
            {
                "elementType": "labels.text.stroke",
                "stylers": [{
                    "color": "#f5f1e6"
                }]
            },
            {
                "featureType": "administrative",
                "elementType": "geometry.stroke",
                "stylers": [{
                    "color": "#c9b2a6"
                }]
            },
            {
                "featureType": "administrative.land_parcel",
                "elementType": "geometry.stroke",
                "stylers": [{
                    "color": "#dcd2be"
                }]
            },
            {
                "featureType": "administrative.land_parcel",
                "elementType": "labels.text.fill",
                "stylers": [{
                    "color": "#ae9e90"
                }]
            },
            {
                "featureType": "landscape.natural",
                "elementType": "geometry",
                "stylers": [{
                    "color": "#dfd2ae"
                }]
            },
            {
                "featureType": "poi",
                "elementType": "geometry",
                "stylers": [{
                    "color": "#dfd2ae"
                }]
            },
            {
                "featureType": "poi",
                "elementType": "labels.text.fill",
                "stylers": [{
                    "color": "#93817c"
                }]
            },
            {
                "featureType": "poi.park",
                "elementType": "geometry.fill",
                "stylers": [{
                    "color": "#a5b076"
                }]
            },
            {
                "featureType": "poi.park",
                "elementType": "labels.text.fill",
                "stylers": [{
                    "color": "#447530"
                }]
            },
            {
                "featureType": "road",
                "elementType": "geometry",
                "stylers": [{
                    "color": "#f5f1e6"
                }]
            },
            {
                "featureType": "road.arterial",
                "elementType": "geometry",
                "stylers": [{
                    "color": "#fdfcf8"
                }]
            },
            {
                "featureType": "road.highway",
                "elementType": "geometry",
                "stylers": [{
                    "color": "#f8c967"
                }]
            },
            {
                "featureType": "road.highway",
                "elementType": "geometry.stroke",
                "stylers": [{
                    "color": "#e9bc62"
                }]
            },
            {
                "featureType": "road.highway.controlled_access",
                "elementType": "geometry",
                "stylers": [{
                    "color": "#e98d58"
                }]
            },
            {
                "featureType": "road.highway.controlled_access",
                "elementType": "geometry.stroke",
                "stylers": [{
                    "color": "#db8555"
                }]
            },
            {
                "featureType": "road.local",
                "elementType": "labels.text.fill",
                "stylers": [{
                    "color": "#806b63"
                }]
            },
            {
                "featureType": "transit.line",
                "elementType": "geometry",
                "stylers": [{
                    "color": "#dfd2ae"
                }]
            },
            {
                "featureType": "transit.line",
                "elementType": "labels.text.fill",
                "stylers": [{
                    "color": "#8f7d77"
                }]
            },
            {
                "featureType": "transit.line",
                "elementType": "labels.text.stroke",
                "stylers": [{
                    "color": "#ebe3cd"
                }]
            },
            {
                "featureType": "transit.station",
                "elementType": "geometry",
                "stylers": [{
                    "color": "#dfd2ae"
                }]
            },
            {
                "featureType": "water",
                "elementType": "geometry.fill",
                "stylers": [{
                    "color": "#b9d3c2"
                }]
            },
            {
                "featureType": "water",
                "elementType": "labels.text.fill",
                "stylers": [{
                    "color": "#92998d"
                }]
            }

        ]
    });
    infoWindow = new google.maps.InfoWindow();


    var directionsDisplay;


    function calcRoute(myLat, myLng, toLat, toLng, map, onAir = false, flightPlanCoordinates = []) {
        /*
        Рисует маршрут доставки на карте. Берет маршрут по дорогам у гугла.
        Для летательных аппаратов необходимо задавать флаг onAir и по желанию указывать маршрут.
        Если не указан строит прямую линию от начальной до конца.

        Путь задается в формате:

        var flightPlanCoordinates = [
          {lat: 37.772, lng: -122.214},
          {lat: 21.291, lng: -157.821},
          {lat: -18.142, lng: 178.431},
          {lat: -27.467, lng: 153.027}
        ];

        */
        placeMarker({lat:55.728484,lng:37.748107})

        placeMarker({lat:55.809843, lng:37.499758})

        placeMarker({lat:55.717426, lng:37.757728})

        placeMarker({lat:55.402122, lng:37.559514})

        placeMarker({lat:55.923392, lng:37.753452})
        // Настройки рендерера путей DirectionsService
        var polylineColorSettings = {
            // Настройки цвета линии
            strokeColor: "blue",
            geodesic: true,
            strokeOpacity: 0.4,
            strokeWeight: 5
        }
        var directionsService = new google.maps.DirectionsService();
        directionsDisplay = new google.maps.DirectionsRenderer({
            polylineOptions: polylineColorSettings
        });

        // Маркеры на начало и конец пути
        var start = new google.maps.LatLng(myLat, myLng);
        var end = new google.maps.LatLng(toLat, toLng);

        var startMarker = new google.maps.Marker({
            position: start,
            map: map,
            draggable: false,
//            icon: {
//                url: "http://maps.google.com/mapfiles/ms/icons/purple.png"
//            }
        });
        var endMarker = new google.maps.Marker({
            position: end,
            map: map,
            draggable: false,
//            icon: {
//                url: "http://maps.google.com/mapfiles/ms/icons/purple.png"
//            }
        });

        var bounds = new google.maps.LatLngBounds();
        bounds.extend(start);
        bounds.extend(end);
        map.fitBounds(bounds);

        if (!onAir) {

            var request = {
                origin: start,
                destination: end,
                travelMode: google.maps.TravelMode.WALKING
            };
            directionsService.route(request, function(response, status) {
                if (status == google.maps.DirectionsStatus.OK) {
                    directionsDisplay.setDirections(response);
                    directionsDisplay.setMap(map);
                    directionsDisplay.setOptions({
                        suppressMarkers: true
                    });
                    var distance = google.maps
                        .geometry.spherical.computeDistanceBetween(start, end);
                    //console.log( Math.round(distance) + "Km" );
                    console.log("Расстояние: " + Math.round(distance) / 1000 + " Км");
                } else {
                    alert("Directions Request from " + start.toUrlValue(6) + " to " + end.toUrlValue(6) + " failed: " + status);
                }
            });
        } else {

            // добавляем в путь начало и конец
            flightPlanCoordinates.unshift({
                lat: myLat,
                lng: myLng
            })
            flightPlanCoordinates.push({
                lat: toLat,
                lng: toLng
            })
            console.log(flightPlanCoordinates)
            polylineColorSettings['path'] = flightPlanCoordinates;
            polylineColorSettings['geodesic'] = true;

            var flightPath = new google.maps.Polyline(polylineColorSettings);
            var depCoord = flightPlanCoordinates [0];
             var departure = new google.maps.LatLng(depCoord['lat'], depCoord['lng']);

             var arrCoord = flightPlanCoordinates[flightPlanCoordinates.length-1];
            var arrival = new google.maps.LatLng(arrCoord['lat'], arrCoord['lng']);
            var step = 0;
        var numSteps = 250; //Change this to set animation resolution
        var timePerStep = 50; //Change this to alter animation speed
        var animStep= 0
        var interval = setInterval(function() {
     step += 1;
     if (step > numSteps) {
         clearInterval(interval);
     } else {
         var are_we_there_yet = google.maps.geometry.spherical.interpolate(departure,arrival,step/numSteps);
         flightPath.setPath([departure, are_we_there_yet]);
     }
        }, timePerStep);
        flightPath.setMap(map);
        }
        return 1;

    }


    var marker = null;
    var myPosLat;
    var myPosLon;

    function autoUpdate() {
        /*
                navigator.geolocation.getCurrentPosition(function(position) {
                    var newPoint = new google.maps.LatLng(position.coords.latitude,
                        position.coords.longitude);
                    myPosLat = position.coords.latitude;
                    myPosLon = position.coords.longitude;
                    console.log(position.coords.latitude,
                        position.coords.longitude);
                    var iconBase = 'https://maps.google.com/mapfiles/kml/shapes/';
                    var icons = {
                        parking: {
                            icon: iconBase + 'parking_lot_maps.png'
                        },
                        library: {
                            icon: iconBase + 'library_maps.png'
                        },
                        info: {
                            icon: iconBase + 'info-i_maps.png'
                        }
                    };



                        // Marker does not exist - Create it
                        marker = new google.maps.Marker({
                            position: newPoint,
                            map: map,
                            icon: "location.png"
                        });
                        marker.addListener('click', function() {
                            infoWindow.setContent("<div>Ваше местоположение</div>");
                            infoWindow.open(map, marker);
                        });


                    // Center the map on the new position
                    map.setCenter(newPoint);
                });
        */

    }

    autoUpdate();
    var coord  ={};
    axios.get('http://localhost/api-v1/router/track/11/').then(function (response) {
    coord = response.data.track;
    var array = coord.split('\n')
    console.log(array)
    lon_from = parseFloat(array[0].split(' ')[1])
    lat_from = parseFloat(array[0].split(' ')[0])
    lon_to = parseFloat(array[array.length-1].split(' ')[1])
    lat_to = parseFloat(array[array.length-1].split(' ')[0])
    var flightPath = [];
    if (array.length>2)
    {
        for (var i=1;i<array.length-1;i++)
        {
        flightPath.push({lng:parseFloat(array[i].split(' ')[0]), lat:parseFloat(array[i].split(' ')[1])})
        }

    }
    console.log(lon_from, lon_to, lat_to, lat_from)
    flightPath = [];


    var a = calcRoute(lat_from, lon_from, lat_to, lon_to, map, onAir = true, flightPlanCoordinates = []);
    console.log(a);



    })
    console.log(coord )


}



function placeMarker(location) {
    var marker = new google.maps.Marker({
        position: location,
        map: map
    });
}


function downloadUrl(url, callback) {
    var request = window.ActiveXObject ?
        new ActiveXObject('Microsoft.XMLHTTP') :
        new XMLHttpRequest;

    request.onreadystatechange = function() {
        if (request.readyState == 4) {
            request.onreadystatechange = doNothing;
            callback(request, request.status);
        }
    };

    request.open('GET', url, true);
    request.send(null);
}

