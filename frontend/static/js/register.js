function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition, showError);
    } else {
        alert("Geolocation is not supported by this browser.");
    }
}
function showPosition(position) {
    document.getElementById('id_latitude').value = position.coords.latitude;
    document.getElementById('id_longitude').value = position.coords.longitude;
    fetch('/api/get_city?lat=' + position.coords.latitude + '&lon=' + position.coords.longitude)
    .then(response => response.json())
    .then(data => document.getElementById('id_city').value = data.city);
}
function showError(error) {
    switch(error.code) {
        case error.PERMISSION_DENIED:
            alert("User denied the request for Geolocation.");
            break;
        case error.POSITION_UNAVAILABLE:
            alert("Location information is unavailable.");
            break;
        case error.TIMEOUT:
            alert("The request to get user location timed out.");
            break;
        case error.UNKNOWN_ERROR:
            alert("An unknown error occurred.");
            break;
    }
}

document.addEventListener('DOMContentLoaded', () => {
    getLocation();
});