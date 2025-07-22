# isell-Real-estate

# 🏠 iSell Real Estate Platform
iSell is a comprehensive Django-based web application that enables seamless interaction between property sellers and potential buyers. The platform provides a user-friendly interface for listing, browsing, booking, and managing properties. It simulates the functionality of modern real estate portals and is built with full role-based access control.

## 🔧 Features

### 👤 User Roles:
- **Seller**
  - Register and login
  - Add and manage properties
  - View, complete, or delete visit bookings
  - View number of properties on dashboard
  - Edit profile (name, address, mailid)

- **Buyer**
  - Register and login
  - View properties
  - Book a visit to a property
  - Sort and search properties
  - Add properties to favorites
  - Edit profile (name, mailid)
 
  - 
## 🛠️ Technologies Used

- Django (Backend Framework)
- MySQL (Database)
- HTML, CSS (Frontend)
- REST API

## steps to follow
- cd path
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver

## for api
- api/seller/properties(seller)
- api/buyer/bookings(buyer)

