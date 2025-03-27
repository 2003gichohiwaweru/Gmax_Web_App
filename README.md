GMax Car Listing Website
Overview
GMax Car Listing Website is a web application developed using Django, a high-level Python web framework. This application serves as a platform for users to browse and list cars for sale. It provides features for both buyers and sellers, facilitating the buying and selling process of cars.

Features
User Authentication: Users can sign up, log in, and manage their accounts.
Car Listing: Sellers can list cars for sale, providing details such as make, model, year, price, and description.
Search and Filtering: Users can search for cars based on various criteria such as make, model, year, and price range.
Car Details: Detailed information about each car listing, including images, specifications, and seller contact information.
User Dashboard: Users have a personalized dashboard where they can manage their listings, view their favorites, and update their profile.
Responsive Design: The website is designed to be responsive, ensuring a seamless experience across devices of all sizes.

Technologies Used
Django: The web framework used for backend development.
HTML/CSS/JavaScript: Frontend development technologies for creating the user interface and interactivity.
SQLite: The default database system used by Django for data storage.
Bootstrap: Frontend framework for building responsive and mobile-first websites.
The power of django form+ Django filters is such a great experience

Installation
Clone the repository:
bsh
Copy code
git clone https://github.com/2003gichohiwaweru/Gmax_Web_App
Navigate to the project directory:
bash
Copy code
cd Gmax_Web_App
Install dependencies:
Copy code
pip install -r requirements.txt
Run migrations:
Copy code
python manage.py migrate
Start the development server:
Copy code
python manage.py runserver
Open your web browser and navigate to http://127.0.0.1:8000/ to access the website.
Usage
As a seller, you can sign up for an account, list your cars for sale, and manage your listings from your dashboard.
As a buyer, you can browse through the listings, search for cars based on your preferences, and contact sellers for more information.
Contributing
Contributions are welcome! If you'd like to contribute to the development of GMax Car Listing Website, please fork the repository, make your changes, and submit a pull request.






1. Navigate to Your Project Directory
Open a terminal or command prompt and move to your project folder:

bash
Copy
Edit
cd /path/to/your/project
2. Activate the Virtual Environment (if applicable)
If you're using a virtual environment, activate it:

Windows (CMD/PowerShell):

bash
Copy
Edit
venv\Scripts\activate
macOS/Linux:

bash
Copy
Edit
source venv/bin/activate
3. Run Migrations (if needed)
Ensure your database is up to date:

bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
4. Create a Superuser (if not already created)
If you need an admin user, create one:

bash
Copy
Edit
python manage.py createsuperuser
Follow the prompts to set up a username and password.

5. Run the Development Server
Start the Django development server:

bash
Copy
Edit
python manage.py runserver
By default, this runs on http://127.0.0.1:8000/. If you want to use a different port (e.g., 8080):

bash
Copy
Edit
python manage.py runserver 8080
6. Access Your Project
Open your browser and go to http://127.0.0.1:8000/ to see your project.

If you need to access the admin panel, go to http://127.0.0.1:8000/admin/ and log in with the superuser credentials.