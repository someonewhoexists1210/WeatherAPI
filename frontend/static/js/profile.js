document.addEventListener('DOMContentLoaded', function() {
    var city = document.getElementById('city');
    var latitude = parseFloat(document.getElementById('latitude').innerHTML);
    var longitude = parseFloat(document.getElementById('longitude').innerHTML);
    if (city.innerHTML === 'None') {
        fetch('/api/get_city?lat=' + latitude + '&lon=' + longitude)
            .then(response => response.json())
            .then(data => {
                city.innerHTML = data.city;
            })
            .catch(error => {
                console.error('Error fetching city:', error);
            });
    }
});