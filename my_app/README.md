A Flask-based web application for managing architecture projects with automated client communication and data visualization features.

Features
📋 Project Data Management

Web Form Interface: Clean, responsive form for capturing project details including:

Project name and site location
Client contact information
Project status and timeline
Additional remarks


Excel Data Storage: Automatically creates/updates Excel files named after each project

Data Persistence: Appends new entries to existing project files for historical tracking

📧 Automated Email Communication

Instant Client Updates: Automatically sends project details to clients upon form submission

Professional Email Templates: Branded emails from VastuShastra with comprehensive project information

SMTP Integration: Configured with Gmail SMTP for reliable email delivery

📊 Data Visualization

Project Timeline Visualization: Generates timeline charts showing project progression

Status Tracking: Visual representation of project milestones and status updates

Client-Friendly Reports: Clean, professional charts suitable for client presentations

Key Components

Form Submission Handler: Processes project data and saves to Excel

Email Service: Sends automated updates to clients

Data Visualization Module: Creates timeline charts from project data

File Management: Handles Excel file creation and updates per project

Use Case - Ideal for architecture firms and project managers who need to:
Track multiple projects with different clients,
Maintain client communication,
Generate visual project reports,
Store project data in organized Excel files

Technical Stack

Backend: Flask (Python)

Data Processing: Pandas for Excel file manipulation

Visualization: Matplotlib and Seaborn for chart generation

Email: SMTP integration for automated communications

Frontend: HTML/CSS with custom styling
