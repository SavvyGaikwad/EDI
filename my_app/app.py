from flask import Flask, render_template, request
import pandas as pd
from datetime import datetime
import os  # Import os to check if the file exists
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "ai.based.crm@gmail.com"
SENDER_PASSWORD = "zewm wckj nemc usmm"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit_form():
    # Get form data
    project_name = request.form["project_name"]
    project_site = request.form["project_site"]
    client_name = request.form["client_name"]
    phone_number = request.form["phone_number"]
    email = request.form["email"]
    status = request.form["status"]
    expected_timeline = request.form["expected_timeline"]
    remarks = request.form["remarks"]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Define the Excel file name based on the project name
    excel_file = f"{project_name}.xlsx"

    # Prepare data to be saved
    data = {
        "Project Name": project_name,
        "Project Site": project_site,
        "Client Name": client_name,
        "Phone Number": phone_number,
        "Email": email,
        "Status": status,
        "Expected Timeline": expected_timeline,
        "Remarks": remarks,
        "Timestamp": timestamp,
        "Action": "Submitted"  # Set the action status to "Submitted"
    }

    # Convert the data into a DataFrame
    new_data_df = pd.DataFrame([data])

    # Check if the Excel file for this project exists
    if os.path.exists(excel_file):
        # Load the existing Excel file
        existing_df = pd.read_excel(excel_file)
        # Append the new data to the existing DataFrame
        updated_df = pd.concat([existing_df, new_data_df], ignore_index=True)
    else:
        # If the file doesn't exist, create a new DataFrame with the new data
        updated_df = new_data_df

    # Save the data back to the Excel file (create or update)
    updated_df.to_excel(excel_file, index=False)

    # Send email to the client
    send_email_to_client(email, data)

    return f"Form submitted and email sent to the client successfully! Excel file created: {excel_file}"

def send_email_to_client(client_email, data):
    try:
        # Create the email content
        message = MIMEMultipart()
        message["From"] = SENDER_EMAIL
        message["To"] = client_email
        message["Subject"] = f"Project Details: {data['Project Name']}"

        # Create the email body
        body = f"""
        Dear {data['Client Name']},

        The following are the updates of the details for the project "{data['Project Name']}".
        Here are the details:

        Project Name: {data['Project Name']}
        Project Site: {data['Project Site']}
        Status: {data['Status']}
        Expected Timeline: {data['Expected Timeline']}
        Remarks: {data['Remarks']}

        We will keep you updated on the status of your project.

        Best regards,
        VastuShastra
        """
        message.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server and send the email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(message)
        server.quit()

        print(f"Email sent to {client_email} successfully.")

    except Exception as e:
        print(f"Failed to send email to {client_email}. Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
