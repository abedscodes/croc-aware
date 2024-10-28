# Crocodile Detection Safety Dashboard

## Project Overview

This Tkinter-based application serves as a demo dashboard for monitoring and updating the safety status of various water bodies based on crocodile detection data from sonar sensors. The application is designed for use by administrators who can manually update safety statuses for different locations affected by potential crocodile presence. This tool aims to enhance public safety by providing real-time information on water body conditions.

## Features

- **Admin Dashboard**: Admin users can log in to access and manage the application.
- **Sonar Management**: Ability to add Sonar IDs and assign them to multiple locations where crocodiles could be detected.
- **Location-Based Safety Status**: Each sonar can monitor safety for multiple locations, allowing updates for multiple points based on a single detection.
- **Manual Safety Status Updates**: Admins can update the safety status for each location based on sonar data.
  
### Future Work
- **Automated Status Updates**: Future versions will aim to reduce manual intervention by automating safety status updates across all affected locations, based on real-time detection.

## Installation and Setup

1. **Clone or Download the Repository**
   ```bash
   git clone https://github.com/username/crocodile-safety-dashboard.git
   ```

2. **Install Dependencies**
   - Ensure Python and Tkinter are installed on your system.

3. **Run the Application**
   ```bash
   python app.py
   ```

## Usage

1. **Admin Login**: 
   - Username: `admin`
   - Password: `Admin`
   
2. **Dashboard Access**:
   - Once logged in, admins can add Sonar IDs, update locations, and set the safety status for each monitored location.

3. **Updating Safety Status**:
   - Each Sonar ID can be linked to multiple locations. Update safety statuses to reflect current conditions and ensure public safety.

