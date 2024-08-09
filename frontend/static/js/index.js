fetch('/api/weather?location=Jaipur')
.then(response => response.json())
.then(data => console.log(data));