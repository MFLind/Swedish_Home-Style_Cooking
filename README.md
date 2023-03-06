# SWEDISH HOME-STYLE COOKING

SWEDISH HOME-STYLE COOKING is the website for the resturant.

User can use the website for looking on the menu and read about what kind of resturant it is.

User can book a table and get feedback if fully booked at specific time.

It also possible to get a view of all the booking, with also to edit and delete a booking.

During the design process Figma was used for sketching the UX design, design was manually written with using bootstrap v5.

![bild](https://user-images.githubusercontent.com/106115510/223067696-a2bfb675-b33a-4975-97b4-544e012135f6.png)

Agile working methods with planning and iterative working was done during the process.

A live view of how the website locks on differant screens:


# Differant view on the website.
This is the home page where you can read about the resturant.
![bild](https://user-images.githubusercontent.com/106115510/223072514-41f58382-97d9-40bd-bcd1-9ac5d70af7ea.png)

This is the menu.
![bild](https://user-images.githubusercontent.com/106115510/223078028-1cdb59c2-a105-4de0-b133-595dd4ad671a.png)

This is where you comming when you click on booking.
![bild](https://user-images.githubusercontent.com/106115510/223078180-0bffef8d-32a0-4e75-82c1-b23a33995839.png)

After you have logged in you coming here where you can book table.
![bild](https://user-images.githubusercontent.com/106115510/223078287-5dde4302-d07e-4407-be5e-fbdff908c682.png)

Here is where you can see the reservations.
![bild](https://user-images.githubusercontent.com/106115510/223078340-2f296570-2ff0-439e-8798-38c5c816e080.png)

When you have clicked on logged out you coming here. 
![bild](https://user-images.githubusercontent.com/106115510/223078389-8fb41619-9723-4191-a640-af44550f7dc7.png)

# Features
- Book a table.
- Manager can see bookings.
- See the menu.
- Logging with a account so you can book in a name, number and persons.
- Sign up for a account.

## Future improvement
- Get a mail with a booking conformation.
- Reset your password. 
- Implementation of Django testing framework.

# Data model
Datamodel is implemented with Django framework.

![bild](https://user-images.githubusercontent.com/106115510/223066274-1284b0e4-b23f-4f1d-8a4d-dc27d8525c93.png)


# Testing

I have done manual testing with the following methods:
- Running thru pylint for PEP8 validation and getting no errors
- Test website both locally on my command prompt and also on Heroku: https://swedish-home-style-cooking.herokuapp.com/
- Testing inputs with both incorrect values and correct values

![bild](https://user-images.githubusercontent.com/106115510/223101370-a5bfa3a6-94e3-4855-b9d0-2a8c999014fa.png)


## Bugs
The development was done iterative and testing and finding bugs occure during the coding process.

## Remaining bugs
- In the booking/edit booking form, if time is set for a out-of-office time and the warning shows (check exists) the DatePicker Widget won't show in retry.

## Validator Testing
- PEP8 via pylint locally on my computer

## Deployment
The Website is deployed using Heroku webadmin.
- Steps
  - For or clone this repository
  - Create a new Heroku app
  - Set the buildpacks to to Python
  - Link the Heroku app to the github directory
  - Setup ElephantSQL database get the database string
  - Add enviroment variables for ElephantSQL and SECRET_KEY for django
  - Click on **Deploy**

# Credits
- pexels.com for pictur. The pepol a have take ther pictur is Karthik reddy, Chan Walrus and ROMAN ODINTSOV.
- Special thanks to Patrik Lindergren for sponsering with Heroku and Figma account.


