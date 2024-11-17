from flask import Flask, request, render_template_string
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# MySQL Database Configuration
DB_CONFIG = {
    'host': 'localhost',  # Replace with your host
    'user': 'root',       # Replace with your username
    'password': '12210812',  # Replace with your password
    'database': 'project' # Ensure this matches your new database
}

# HTML template to render the form
FORM_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Project Details</title>
</head>
<body>
    <h1>Enter Project Details</h1>
    <form action="/submit" method="POST">
        
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>

        <label for="number">Number:</label><br>
        <input type="text" id="number" name="number" required><br><br>

        <label for="start_date">Start Date:</label><br>
        <input type="date" id="start_date" name="start_date" required><br><br>

        <label for="status">Status:</label><br>
        <select id="status" name="status" required>
            <option value="lead_qualified">Lead Qualified</option>
            <option value="proposal_submitted">Proposal Submitted</option>
            <option value="ongoing">Ongoing</option>
            <option value="complete">Complete</option>
        </select><br><br>

        <label for="project_type">Project Type:</label><br>
        <select id="project_type" name="project_type" required>
            <option value="interior">Interior</option>
            <option value="architecture">Architecture</option>
        </select><br><br>

        <label for="site_address">Site Address:</label><br>
        <input type="text" id="site_address" name="site_address" required><br><br>

        <label for="city">City:</label><br>
        <input type="text" id="city" name="city" required><br><br>

        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>

        <label for="phone">Phone Number:</label><br>
        <input type="tel" id="phone" name="phone" required><br><br>

        <label for="marketer">Marketer:</label><br>
        <input type="text" id="marketer" name="marketer" required><br><br>

        <label for="expected_revenue">Expected Revenue:</label><br>
        <input type="number" id="expected_revenue" name="expected_revenue" step="0.01" required><br><br>

        <label for="manager">Manager:</label><br>
        <input type="text" id="manager" name="manager" required><br><br>

        <button type="submit">Submit</button>
    </form>
</body>
</html>
"""

@app.route('/')
def home():
    # Serve the HTML form
    return render_template_string(FORM_TEMPLATE)

@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    name = request.form.get('name')
    number = request.form.get('number')
    start_date = request.form.get('start_date')
    status = request.form.get('status')
    project_type = request.form.get('project_type')
    site_address = request.form.get('site_address')
    city = request.form.get('city')
    email = request.form.get('email')
    phone = request.form.get('phone')
    marketer = request.form.get('marketer')
    expected_revenue = request.form.get('expected_revenue')
    manager = request.form.get('manager')

    connection = None
    cursor = None

    try:
        # Connect to MySQL database
        connection = mysql.connector.connect(**DB_CONFIG)

        if connection.is_connected():
            cursor = connection.cursor()

            # Insert data into the table
            insert_query = """
                INSERT INTO client (
                    name, number, start_date, status, project_type, site_address, city, email, phone, marketer, expected_revenue, manager
                ) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, (
                name, 
                number, 
                start_date, 
                status, 
                project_type, 
                site_address, 
                city, 
                email, 
                phone, 
                marketer, 
                expected_revenue, 
                manager
            ))
            connection.commit()

            return f"Data submitted successfully! Name: {name}, Number: {number}, Project Type: {project_type}"

    except Error as e:
        return f"Error: {e}"

    finally:
        # Ensure both cursor and connection are closed properly
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

if __name__ == '__main__':
    app.run(debug=True)
