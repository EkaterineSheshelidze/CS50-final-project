# GiveRadar
#### Video Demo:  https://youtu.be/m1FlB3IPme4?si=BwAF_GrZuFoCVfzD
#### Description:

**Welcome to GiveRadar** - CS50x Final Project, a responsive web application that displays volunteer's achievements along with detailed information about recycling, volunteering opportunities and programs provided by Georgian organizations with which I collaborated on the project.

I identified a gap in the market: there were no websites that offered certified resources, helped organizers and volunteers like myself, and simultaneously encouraged people to recycle and volunteer.

I sincerely thank **"Tene Recycling Company", "Helping Hand", And "Caritas Georgia"** for their help in gathering data such as recycling locations, donation centers, events, programs, and their feedback on the website.


## Features

1. **Secure user authentication** using Flask sessions.

2. **Profile Management:**
- **Change Profile Information:** Update your password and personalize your profile picture via Profile Settings on the Home page or Navigation bar.

- **Track your achievements:**
     - Monitor your achievements, total accumulated hours and earned points on your Home Page. Stay motivated by keeping track of your achievements over time.
    - Add progress to the Progress seciton on the Home Page via "Add Progess" button. Provide details such as organization name, type of work, date, and hours spent.

3. **Dynamic and Interactive UI:** Enjoy a seamless experience on any device with GiveRadar responsive design, ensuring the website looks great on both desktop and mobile.

4. **Interactive Map:** Explore areas all over Georgia where you can donate clothing, shoes, recycling materials like plastic, paper and old batteries using GiveRadar interactive map feature.

5. **Discover Page:** Stay informed with our Discover page, featuring ongoing programs and events organized by GiveRadar’s collaborators. Clicking on an event provides detailed information on a dedicated page.

## Installation

To get started with the project, follow these steps to install the required dependencies:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/EkaterineSheshelidze/CS50-final-project.git
   cd CS50-final-project

2. **Prerequisites:**
   - Ensure you have Python 3.6 or later installed: https://www.python.org/downloads/

3. **Install dependencies:**
   - Open a terminal in the project's root directory.
   - Run `pip install -r requirements.txt`

4. **(Optional) Activate virtual environment:**
   - If using a virtual environment, activate it before running `pip install`.

5. **PapaParse-5.0.2 is already installed in the static folder.**
## Database Setup

### Initializing the Database

For GiveRadar website to work, users, progress and discover Tables need to be created. 

1. **Create Database Tables in giveradar.db:**
   - Open a SQLite prompt and create the database:
      ```sqlite3 giveradar.db```
   - Import the schema:
      ```.read schema.sql```
   - Exit SQLite:
      ```.exit```
   
2. Database for the Discover page, **discover.csv**, is already installed in the static/databases folder.
3. Database for the Map, **map.csv**, is already installed in the static/databases folder. 

## Usage

## 1. Run the Application
- Open a Python prompt.
- Run the following command: ``` Flask run ```

### 2. Welcome Page
- Upon visiting the site, users are greeted with the welcome page, featuring animated statistics about GiveRadar's impact. 
- Users can click the "Join Now" or "Sign Up" button to create an account or Log into an existing account.

### 2. Home Page
After logging in, users can access their home page, featuring:

- **Profile Overview:**
  - View user profile details.
  - Check the total hours and points earned.

- **Profile Settings:**
  - Change profile picture.
  - Update password.

- **Your Progress Section:**
  - Add progress by clicking the "Add Progress" button.
  - Fill in organization name, type, date, and hours spent.

### 3. Discover Page

Explore ongoing programs and events organized by GiveRadar's collaborators:

- Click on an event to view detailed information on a dedicated page.

### 4. Interactive Map

Navigate the interactive map with vibrant markers displaying donation locations throughout Georgia:

- Explore areas to donate clothing, shoes, and recycling materials.
- Marker icons indicate accepted recycling materials at each location.
- Click on a marker for more detailed location information.

## Acknowledgements

All wonderful tools that have contributed to the success of this project:

- [Bootstrap](https://getbootstrap.com/) - A powerful CSS framework that helped enhance the project's visual appeal.
- [Leaflet](https://leafletjs.com/) - An open-source JavaScript library for interactive maps, adding a dynamic mapping feature to my application.
- [Papa Parse](https://www.papaparse.com/) - A fast, in-browser CSV parser that facilitated efficient data handling in my project.
- [FontAwesome](https://fontawesome.com/) - For providing a wide range of scalable vector icons, enhancing the user interface.
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) - The core scripting language that enabled dynamic behavior and interactions in my website.
- [CS50 Library](https://cs50.harvard.edu/lib/) - The CS50 library and course, provided by Harvard University, played a crucial role in shaping my understanding of computer science and programming.
- [GitHub](https://github.com/) - For providing a reliable version control and collaboration platform.

**Special thanks to all contributors and anyone who provided feedback, reported issues, or supported the project in any way. Your contributions are invaluable.**


## Future Plans

I want to thank the **CS50x course** for giving me great insights and increasing  my confidence as I begin my programming journey. I intend to upgrade GiveRadar in the future with more advanced features and enhanced security. A better user experience and an even more reliable platform are coming soon.