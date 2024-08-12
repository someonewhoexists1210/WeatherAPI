document.addEventListener('DOMContentLoaded', function() {
    var city = document.getElementById('city');
    if (city.innerHTML === 'None') {
        fetch('/api/get_city')
            .then(response => response.json())
            .then(data => {
                city.innerHTML = data.city;
            })
            .catch(error => {
                console.error('Error fetching city:', error);
            });
    }
});