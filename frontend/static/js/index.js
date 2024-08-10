function updateFormFields() {
    var view = document.getElementById("viewSelect").value;
    var nl = document.getElementById("keyInputselect").value;
    console.log(nl)

    
    document.getElementById("dateInput").style.display = 'none';
    document.getElementById("dateRangeInputs").style.display = 'none';
    document.getElementById("numberInput").style.display = 'none';
    document.getElementById("keyInput").style.display = 'none';
    document.getElementById("keyInputtty").style.display = 'none';
    document.getElementById("keyInputto").style.display = 'none';
    document.getElementById("weekdayInput").style.display = 'none';


    if (view === "day") {
        document.getElementById("dateInput").style.display = 'block';
    } else if (view === "tty"){
        document.getElementById("keyInputtty").style.display = 'block';
    }else if (view === "range") {
        document.getElementById("dateRangeInputs").style.display = 'block';
    } else if (view === "next" || view === "last") {
        document.getElementById("numberInput").style.display = 'block';
        document.getElementById("keyInput").style.display = 'block';
        if (nl === "weekday") {
            document.getElementById("numberInput").style.display = 'none';
            document.getElementById("weekdayInput").style.display = 'block';
        }
    } else if (view === "to_date") {
        document.getElementById("dateInput").style.display = 'block';
        document.getElementById("keyInputto").style.display = 'block';
    }
}

function disableHiddenFields() {
    const fields = document.querySelectorAll('#weatherForm input, #weatherForm select');
    fields.forEach(field => {
        if (field.style.display === 'none' || field.closest('div').style.display === 'none') {
            field.disabled = true;
        } else {
            field.disabled = false;
        }
    });
}

document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('weatherForm').addEventListener('submit', disableHiddenFields);
});