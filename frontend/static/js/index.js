function updateFormFields() {
    var view = document.getElementById("viewSelect").value;
    var nl = document.getElementById("keyInputselect").value;
    console.log(nl);

    document.getElementById("dateInput").style.display = 'none';
    document.getElementById("dateRangeInputs").style.display = 'none';
    document.getElementById("numberInput").style.display = 'none';
    document.getElementById("keyInput").style.display = 'none';
    document.getElementById("keyInputtty").style.display = 'none';
    document.getElementById("keyInputto").style.display = 'none';
    document.getElementById("weekdayInput").style.display = 'none';

    if (view === "day") {
        document.getElementById("dateInput").style.display = 'block';
    } else if (view === "tty") {
        document.getElementById("keyInputtty").style.display = 'block';
    } else if (view === "range") {
        document.getElementById("dateRangeInputs").style.display = 'block';
    } else if (view === "next" || view === "last") {
        document.getElementById("numberInput").style.display = 'block';
        document.getElementById("keyInput").style.display = 'block';
        if (nl === "weekday") {
            document.getElementById("numberInput").style.display = 'none';
            document.getElementById("weekdayInput").style.display = 'block';
        }
    } else if (view === "to_date") {
        document.getElementById("keyInputto").style.display = 'block';
    }
}

document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('weatherForm').addEventListener('submit', (event) => {
        event.preventDefault();
        let filled = true;
        const fields = document.querySelectorAll('#weatherForm input, #weatherForm select');
        fields.forEach(field => {
            if (field.style.display === 'none' || field.closest('div').style.display === 'none') {
                field.disabled = true;
            } else {
                field.disabled = false;
                if (field.value === '') {
                    filled = false;
                }
                if (field.type === 'date') {
                    const currentDate = new Date();
                    const selectedDate = new Date(field.value);
                    const oneYearAgo = new Date(currentDate.getFullYear() - 1, currentDate.getMonth(), currentDate.getDate());
                    const fifteenDaysLater = new Date(currentDate.getFullYear(), currentDate.getMonth(), currentDate.getDate() + 15);

                    if (selectedDate < oneYearAgo || selectedDate > fifteenDaysLater) {
                        filled = false;
                        alert("Please select a date within the range of 1 year ago and 15 days later.");
                    }
                }
                if (field.type === 'number') {
                    if (field.value < 1) {
                        filled = false;
                        alert("Please enter a number greater than 0.");
                    }
                    if (field.value > 15) {
                        filled = false;
                        alert("Please enter a number less than 16.");
                    }
                }
            }
        });
        if (filled) {
            event.target.submit();
            enableAllFields();
        } else {
            alert("Please fill in all inputs");
        }
    });
});

function enableAllFields() {
    const fields = document.querySelectorAll('#weatherForm input, #weatherForm select');
    fields.forEach(field => {
        field.disabled = false;
    });
}