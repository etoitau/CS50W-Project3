# CS50W-Project3
Web Programming with Python and JavaScript

## Pinnochio's Pizza

### Short Writeup 
#### From specifications:
In this project, you’ll build an web application for handling a pizza restaurant’s online orders. Users will be able to browse the restaurant’s menu, add items to their cart, and submit their orders. Meanwhile, the restaurant owners will be able to add and update menu items, and view orders that have been placed.

#### Personal Touch
Can delete from cart. From admin can mark order fulfilled.

### What's in each file
    .
    ├── orders                  # this app
    │   ├── migrations          # django system files
    │   ├── static/orders       # static files
    │   │   ├── cartscripts.js  # javascript for car page
    │   │   ├── favicon.ico     # bookmark icon
    │   │   ├── menuscripts.js  # javascript for menu page
    │   │   └── styles.css      # css definitions
    │   ├── templates/orders    # html templates
    │   │   ├── cart.html       # shopping cart page
    │   │   ├── index.html      # front page
    │   │   ├── layout.html     # other pages extend this. Navbar, etc
    │   │   ├── login.html      # login page
    │   │   ├── menu.html       # menu page
    │   │   └── register.html   # registration page
    │   ├── templatetags        # extending functionality of django's templating language w/ custom filters
    │   │   ├── __init__.py     # for django
    │   │   └── orders_tags.py  # tag for better accessibility of dictionaries in template, and currency formatting
    │   ├── __init__.py         # for django
    │   ├── admin.py            # register models and customize view
    │   ├── apps.py             # default django
    │   ├── models.py           # ORM definitions 
    │   ├── tests.py            # default django
    │   ├── urls.py             # app url routing
    │   └── views.py            # route handling
    ├── .gitignore              # exclude files only applicable to my machine
    ├── README.md               # this
    ├── manage.py               # main application file
    └── requirements.txt        # necessary to install these to run app

### Other info
Github:
https://github.com/etoitau/CS50W-Project3

Youtube walkthrough:
https://youtu.be/PXAU94GE54g