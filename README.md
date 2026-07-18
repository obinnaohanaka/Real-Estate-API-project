# 🏡 Real Estate Sales & Leasing Management System API

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![Django](https://img.shields.io/badge/Django-6.0-092E20?logo=django)
![Django REST Framework](https://img.shields.io/badge/DRF-REST_Framework-red)
![JWT](https://img.shields.io/badge/Auth-JWT-orange)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite)
![Swagger](https://img.shields.io/badge/API-Swagger-85EA2D?logo=swagger)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📖 Project Overview

The **Real Estate Sales & Leasing Management System API** is a backend RESTful API developed using **Django** and **Django REST Framework**.

It provides a secure and scalable platform for managing real estate sales and rentals, allowing users to browse properties, agents to manage listings, and administrators to oversee the platform.

The API implements **JWT Authentication**, **role-based access control**, **search and filtering**, **pagination**, and **interactive API documentation** using Swagger and ReDoc.

---

# 🎯 Project Objectives

- Provide secure REST APIs for real estate management.
- Allow agents to register and manage property listings.
- Enable administrators to approve agent applications.
- Allow users to browse, search, and filter properties.
- Enable users to submit inquiries and book inspections.
- Demonstrate clean backend architecture using Django REST Framework.

---

# 🚀 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.14 | Programming Language |
| Django 6 | Backend Framework |
| Django REST Framework | REST API Development |
| SQLite | Development Database |
| Simple JWT | Authentication |
| Django Filter | Filtering |
| Pillow | Image Handling |
| Swagger (drf-yasg) | API Documentation |
| ReDoc | API Documentation |

---

# ✨ Features

## 🔐 Authentication

- [x] User Registration
- [x] User Login
- [x] JWT Authentication
- [x] Refresh Token
- [x] Logout

---

## 👨‍💼 Agent Module

- [x] Agent Registration
- [x] Admin Approval
- [x] Agent Dashboard

---

## 🏠 Property Listings

- [x] Create Listing
- [x] Update Listing
- [x] Delete Listing
- [x] View Listings
- [x] Property Categories
- [x] Search
- [x] Filtering
- [x] Pagination

---

## 🖼️ Property Images

- [x] Upload Property Images
- [x] Retrieve Property Images

---

## ❤️ Favorites

- [x] Save Property
- [x] Remove Favorite
- [x] View Favorites

---

## ⭐ Reviews

- [x] Create Reviews
- [x] View Reviews

---

## 💬 Inquiries

- [x] Submit Property Inquiry
- [x] View Inquiries

---

## 📅 Inspection Booking

- [x] Book Inspection
- [x] View Inspection Bookings
- [x] Approve Inspection
- [x] Reject Inspection
- [x] Complete Inspection

---

## 📚 API Documentation

- [x] Swagger UI
- [x] ReDoc

---

# 📊 API Modules

| Module | Status |
|---------|--------|
| Authentication | ✅ |
| Agents | ✅ |
| Categories | ✅ |
| Listings | ✅ |
| Property Images | ✅ |
| Favorites | ✅ |
| Reviews | ✅ |
| Inquiries | ✅ |
| Inspection Booking | ✅ |
| Swagger Documentation | ✅ |

---

# 🔐 Authentication

The API uses **JWT Authentication**.

After logging in, include your access token in every protected request.

Example:

```
Authorization: Bearer your_access_token
```

---

# 🌐 API Endpoints

## Authentication

| Method | Endpoint |
|---------|----------|
| POST | `/api/auth/register/` |
| POST | `/api/auth/login/` |
| POST | `/api/auth/logout/` |
| POST | `/api/auth/refresh/` |

---

## Agents

| Method | Endpoint |
|---------|----------|
| POST | `/api/agents/register/` |
| PATCH | `/api/agents/{id}/approve/` |
| GET | `/api/agents/dashboard/` |

---

## Categories

| Method | Endpoint |
|---------|----------|
| GET | `/api/categories/` |
| POST | `/api/categories/` |
| PUT | `/api/categories/{id}/` |
| DELETE | `/api/categories/{id}/` |

---

## Listings

| Method | Endpoint |
|---------|----------|
| GET | `/api/listings/` |
| POST | `/api/listings/` |
| GET | `/api/listings/{id}/` |
| PUT | `/api/listings/{id}/` |
| DELETE | `/api/listings/{id}/` |

---

## Property Images

| Method | Endpoint |
|---------|----------|
| POST | `/api/property-images/{listing_id}/upload/` |

---

## Favorites

| Method | Endpoint |
|---------|----------|
| GET | `/api/favorites/` |
| POST | `/api/favorites/` |
| DELETE | `/api/favorites/{id}/` |

---

## Reviews

| Method | Endpoint |
|---------|----------|
| GET | `/api/reviews/` |
| POST | `/api/reviews/` |

---

## Inquiries

| Method | Endpoint |
|---------|----------|
| GET | `/api/inquiries/` |
| POST | `/api/inquiries/` |

---

## Inspection Booking

| Method | Endpoint |
|---------|----------|
| GET | `/api/inspections/` |
| POST | `/api/inspections/book/` |
| PATCH | `/api/inspections/{id}/status/` |

---

# 📖 API Documentation

After running the server:

## Swagger UI

```
http://127.0.0.1:8000/swagger/
```

## ReDoc

```
http://127.0.0.1:8000/redoc/
```

---

# 📂 Project Structure

```
RealEstateAPI/

├── accounts/
├── agents/
├── categories/
├── favorites/
├── inquiries/
├── inspections/
├── listings/
├── property_images/
├── reviews/
├── config/
├── media/
├── manage.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/RealEstateAPI.git
```

## Navigate into the Project

```bash
cd RealEstateAPI
```

## Create a Virtual Environment

```bash
python -m venv venv
```

## Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Apply Migrations

```bash
python manage.py migrate
```

## Run the Development Server

```bash
python manage.py runserver
```

---

# 🛡️ User Roles

## 👑 Admin

- Approve agents
- Manage users
- Manage listings
- Manage categories

---

## 👨‍💼 Agent

- Manage property listings
- Upload images
- Approve inspections
- Access dashboard

---

## 👤 User

- Browse listings
- Search and filter properties
- Save favorites
- Send inquiries
- Book inspections
- Leave reviews

---

# 🚀 Future Improvements

- [ ] Email Verification
- [ ] Password Reset via Email
- [ ] Cloudinary Image Storage
- [ ] Google Maps Integration
- [ ] Property Comparison
- [ ] Recently Viewed Properties
- [ ] Featured Listings
- [ ] Docker Support
- [ ] CI/CD Pipeline
- [ ] Automated API Testing
- [ ] Deployment (Render/Railway)

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push to your branch.
5. Open a Pull Request.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Obinna Ohanaka**

Backend Developer

GitHub: https://github.com/obinnaoahanaka

Project Repository:
https://github.com/obinnaohanaka/RealEstateAPI

LinkedIn: https://www.linkedin.com/in/obinna-ohanaka-90440725b

---

⭐ If you found this project useful, consider giving it a star on GitHub.