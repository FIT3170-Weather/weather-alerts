# CliMate Weather App Alerts System

## Table of Contents
1. [Project Overview](#project-overview)
2. [Software Requirements](#software-requirements)
3. [Setup and Installation Instructions](#setup-and-installation-instructions)
4. [How to Run the Project](#how-to-run-the-project)
5. [Common Issues and Troubleshooting](#common-issues-and-troubleshooting)
6. [Additional Notes](#additional-notes)
7. [Contact Information](#contact-information)

## Project Overview
- Provides alerts for weather 'warnings' for locations that have been selected by the user.
- Decoupled from the main CliMate application.
- Alerts are sent via email.
- Uses https://developer.data.gov.my/realtime-api/weather#warning-forecast to get the weather warnings.
- Uses the main CliMate application's database to get the user's selected locations and email addresses.
- Warning forecasts are checked every 5 minutes.
- If a new warning is found, an email is sent to the user.
- The email contains the warning message and the location of the warning.
- Currently, the email is sent via a Gmail account.
- A template .env file is provided for the user to fill in their email and password.

## Software Requirements

- Python 3.12.5
- pip


## Setup and Installation Instructions
- Clone the repository
- Install the required packages using the following command: `pip install -r requirements.txt`
- Fill in the .env file with your email and app password

## How to Run the Project
- Run the script using the following command: `python main.py` or `python3 main.py` (depending on your system)


## Common Issues and Troubleshooting

### Issue 1: App password not working
1. Ensure you have no spaces in your email and password in the .env file
2. Make sure 2FA is activated on your email account
3. Make sure you have generated an app password for your email account

### Issue 2: No email is being sent
1. Ensure you have filled in the .env file with your email and password
2. Ensure the user has selected a location in the main CliMate application
3. Ensure that there has been a new warning forecast in the last 5 minutes
4. Ensure that the email is not in the spam folder

### Issue 3: The script is not running
1. Ensure you have installed the required packages using the following command: `pip install -r requirements.txt`
2. Ensure you have filled in the .env file with your email and password

## Additional Notes
The API being used to obtain the weather alerts is quite poorly documented. Thus, no further granularity in alerts can 
be provided.

## Contact Information

| Name                         | Email                       | Student ID |
|------------------------------| --------------------------- | ---------- |
| **Suman Datta** (maintainer) | sdat0004@student.monash.edu | 30668786   |
| Daryl Lim                    | dlim0036@student.monash.edu | 33560757   |
| Ryan Choo Yan Jhie           | rcho0046@student.monash.edu | 33455775   |
| Nicholas Yew                 | nyew0001@student.monash.edu | 33642478   |
| Lim Zhi Cheng                | zlim0052@student.monash.edu | 33204128   |
| Mohamed Ammar Ahamed Siraj   | amoh0157@student.monash.edu | 33187762   |
| Nicholas Lee                 | nlee0060@student.monash.edu | 32840594   |
| Shyam Borkar                 | sbor0018@student.monash.edu | 32801459   |
| Lai Carson                   | lcar0029@student.monash.edu | 32238436   |
| Hanideepu Kodi               | hkod0003@student.monash.edu | 33560625   |
