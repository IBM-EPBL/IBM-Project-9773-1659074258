# Containment Zone Altering Application

Name:Covidsafe - be secure

Category: Cloud App Development 

Technology Used :
  IBM Cloud,HTML,Javascript,IBM Cloud Object Storage,Python-Flask,Kubernetes,Docker,IBM DB2,IBM Container Registry

Project Idea:

This application is intended to provide information about containment zones in a particular region by alerting people, through continuous monitoring of an individual's location.  Key benefits of the application are monitoring people's activity and alerting them of their safety movements.

Solution Requirement:
The project aims at building an application that provides information about the containment zones of a particular region by continuously monitoring an individual's location. Location of the individual must be stored in the Database. Alerts are sent using the notification service. 

Features of the Application

Admin App (portal):

They should login to the app and update the containment zones locations in the portal.  Based on the location a Geofence will be created within a 100 meters radius.  They should be able to see how many people are visiting that zone.

User App (Mobile App):

The app should have a user registration and login.  After the user logged into the app it will  track the user's location and update the database with the current location.  If the user is visiting the containment zone he will get an alert notification.
