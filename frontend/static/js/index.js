fetch('/api/weather').then(response => response.json())
.then(data => document.getElementById('mess').innerHTML = JSON.stringify(data));