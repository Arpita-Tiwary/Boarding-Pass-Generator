from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS
import mysql.connector

app = Flask(__name__)

# MySQL database connection settings
db_config = {
    'host': 'localhost',  # Change to your MySQL host if necessary
    'user': 'root',  # Your MySQL username
    'password': 'Viekhyat',  # Your MySQL password
    'database': 'booked_flight'  # Your MySQL database name
}
# Enable CORS for all origins (you can restrict it to specific domains if needed)
CORS(app)

# Function to fetch boarding pass data from the database
def get_boarding_pass_data(name, mobile):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)

        # SQL query to fetch confirmed booking details
        query = """
            SELECT passenger_name, flight_number, departure, destination, flight_date, seat
            FROM booked
            WHERE passenger_name = %s AND mobile_number = %s AND booking_status = 'confirmed';
        """
        cursor.execute(query, (name, mobile))
        result = cursor.fetchone()  # Fetch one matching record

        cursor.close()
        connection.close()

        return result
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

@app.route('/boarding-pass', methods=['GET'])
def boarding_pass():
    name = request.args.get('name')      # Get name from query parameters
    mobile = request.args.get('mobile')  # Get mobile number from query parameters

    if not name or not mobile:
        return jsonify({"error": "Name and mobile number are required."}), 400

    # Fetch the boarding pass data
    boarding_pass_data = get_boarding_pass_data(name, mobile)

    if boarding_pass_data:
        return jsonify(boarding_pass_data)  # Return the boarding pass details
    else:
        return jsonify({"error": "No confirmed booking found for the provided details."}), 404

if __name__ == '__main__':
    app.run(debug=True, port=8089)
