function updateForm() {
    var view = document.getElementById("viewSelect").value;
    
    document.getElementById("date1Input").style.display = 'none';
    document.getElementById("date2Input").style.display = 'none';
    document.getElementById("daysInput").style.display = 'none';
    
    if (view === "day" || view === "to_date") {
        document.getElementById("date1Input").style.display = 'block';
    } else if (view === "range") {
        document.getElementById("date1Input").style.display = 'block';
        document.getElementById("date2Input").style.display = 'block';
    } else if (view === "next" || view === "last") {
        document.getElementById("daysInput").style.display = 'block';
    }
}

let form = document.getElementById("weatherForm");
form.addEventListener("submit", function(event) {
    event.preventDefault();
    console.log(document.getElementById("viewSelect").value);
    if (document.getElementById("viewSelect").value === "placeholder") {
        alert("Please select a view");
    }
    
});