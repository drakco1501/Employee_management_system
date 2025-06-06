# Employee_management_system
The Employee Management System is a user-friendly web application designed to streamline employee data management. It enables users to efficiently view, add, update, and delete employee records in a standalone environment. This system simplifies administrative tasks, ensuring organized and accessible information for better workforce management.

#project sturcture

src_code/                # Main project folder
│
├── myproj/            # Django project directory
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py             # Project settings
│   ├── urls.py                 # Main URL configuration
│   └── wsgi.py
│
├── manage.py                   # Django management script
│
├── myapp/                   # App for testing home page
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py              
│   ├── urls.py
│   ├── views.py              
│   └── templates/myapp/
│       └── home.html
│
├── employee_management/                  # App for employee CURD operation
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── signals.py
│   ├── models.py              
│   ├── urls.py
│   ├── forms.py
│   ├── views.py                
│   └── templates/employee_management/
│       ├── employee.html      
│       ├── all_employee.html  
│       ├── employees_alter.html
│       └── add_employee.html
│       └── update_employee.html
│       └── delete_employee.html
│
├── templates/                  # Project-wide templates
│   ├── main.html               # Base template with common elements
│   ├── nav.html                # Navigation sidebar          
│   └── footer.html
│
└── static/                     # Static files
    ├── css/
    │   ├── navfooter.css            # Main stylesheet
    │   ├── myapp.css       # Dashboard specific styles
    │   └── employee.css      # Responsive design rules
    └── img/
        ├── home_img1.png 
        ├── home_img2.png 
        ├── home_img3.png 
        ├── insta_logo.png 
        ├── fb_logo.png  
        ├── linkedin.png  
        └── logo.png            # Company logo

# How to Run Localhost

1. move to src_code Directory : `cd hrms_project`
2. Activate env: `my_env\scripts\activate`
3. Install dependencies: `pip install -r requirement.txt`
4. Set up the database: `python manage.py makemigrations`
                        `python manage.py migrate`


6. Create super user to view admin page: `python manage.py createsuperuser`
7. Run the Django app: `python manage.py runserver`

if any `error` try install virtualenv: `pip install virutualenv` `python manage.py virutualenv env`
and check if django is installed : `pip install django`

#objective

"This project aims to streamline employee management by providing a web-based application where users can view, add, update, and delete employee details. The README.md file serves to guide users through the system's features, installation process, and usage instructions, ensuring a seamless experience for developers and end-users alike."
