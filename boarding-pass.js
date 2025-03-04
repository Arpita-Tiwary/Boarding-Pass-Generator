document.getElementById('fetch-boarding-pass').addEventListener('click', async () => {
    // Get user input
    const name = document.getElementById('name').value;
    const mobile = document.getElementById('mobile').value;

    // Check if both fields are filled out
    if (!name || !mobile) {
        alert('Please enter both your name and mobile number.');
        return;
    }

    try {
        // Fetch boarding pass data from the backend based on user input
        const response = await fetch(`http://127.0.0.1:8089/boarding-pass?name=${name}&mobile=${mobile}`);
        const boardingPassData = await response.json();

        if (response.ok) {
            // Populate the boarding pass with data
            document.getElementById('boarding-pass').style.display = 'block';
            document.getElementById('passenger-name').innerText = boardingPassData.passenger_name;
            document.getElementById('flight-number').innerText = boardingPassData.flight_number;
            document.getElementById('departure').innerText = boardingPassData.departure;
            document.getElementById('destination').innerText = boardingPassData.destination;
            document.getElementById('flight-date').innerText = boardingPassData.flight_date;
            document.getElementById('seat').innerText = boardingPassData.seat;
        } else {
            alert('Error: ' + boardingPassData.error);
        }
    } catch (error) {
        console.error('Error fetching boarding pass:', error);
    }
});
