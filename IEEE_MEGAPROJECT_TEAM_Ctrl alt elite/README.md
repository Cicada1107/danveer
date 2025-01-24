**COLLEGE: BIT Mesra, Ranchi**  
---------------------  
**TEAM DETAILS**  
Name: Ctrl Alt Elite  
Members: Arijit Dubey  
---------------------  
**PROJECT DOMAIN**  
Type: Web Development  
Stack: Python(Django) , Bootstrap + Vanilla CSS, Leaflet.js, Geopy, PostgreSQL  
Requirements: (Refer requirements.txt) Geopy, Pillow, Django, Python Dotenv, Pipenv, whitenoise    
---------------------  
**IDEA**  
In 2023, almost 700 million people worldwide lived on less than $2.15 per day.
Now more than ever, especially in countries like ours(India), people need to help the less fortunate.
However, realistically, the chances of an average citizen to seek out NGOs and go out of their way to help the needy,
is almost negligible, given how fast life is, and how scarce and of essence time is to people,
even if they have something they are willing to donate or how kind or passionate they are about helping the needy.  
  
"Daanveer" is a Web App aimed at bridging this gap between individuals who are willing to donate and NGOs.
The plan is to introduce an easy to use interface where people can simply discover what nearby NGOs or people nearby need
and talk to them directly about it, or just put out a notice about something they dont's need to be picked up as a donation by
NGOs nearby.  
**NOTABLE FEATURES**:  
1. _REGISTRATION AND PROFILE_: Create an account and login as a Donor or an NGO/Beneficiary on the Daanveer website.  
2. _DONATE/ REQUEST A DONATION_: If you have an item you don't need/ would like to get, Donate an item(Donor)/request a donation for an item(NGO), which will be displayed on the Explore page, for other users.  
3. _EXPLORE PAGE_: All the nearby happenings and requests are displayed on one single page, for intuitiveness, where you can interact with them.  
4. _GEOLOCATION_: Each user can input their preferred address, as per which, the donation requests/donated items will appear in closest-first basis, thus making it more likely for the request to get accepted/claimed by a Donor/NGo respectively. This is further made intuitive by the presence of a map view of all the requests from your location right on the explroe page.  
5. _ONLINE CHAT_: If you decide to Claim an item from a donor or Pledge to donate a request to an NGO, go ahead and chat with them about its details, discuss your deal/delivery on your own and the if settled, the request maker can approve the request on the click of a button.  
7. _DISPLAY SECTION_: Recently made donations are displayed on the top of the explore page to motivate and ecnourage users to donate.
------------------  
_Link to the project: https://daanveer.onrender.com_  
------------------  
**HOW TO RUN THE CODE SAMPLE**  
NOTE: I recommend to use pipenv and create a virtual environement for this project so as to not burden your pc with current specific verisions of dependencies (requirements.txt).  
_Prerequisites_:  
1. Before running this project, make sure you have the following installed:  
- Python 3.x  
- pip (Python package manager)  
- pipenv (pip install pipenv)  
2. Clone/Download and setup the repo's contents in your system.  
3. cd to the root directory (the directory that contains the "manage.py" file)  
4. Start a venv there using  
  ```
  pipenv shell
  ```
5. Install all the required packages as per requirements.txt
```
pip install -r requirements.txt
```
6. Create the database:  
```
python manage.py makemigrations
python manage.py migrate
```
7. Create a supreuser account for admin: (Optional)  
```
python manage.py createsuperuser
```
8. Run the development server:  
```
python manage.py runserver
```  
and open the localhost link from the terminal. Now you are runninng Daanveer.  
