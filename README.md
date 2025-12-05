# 🚀 Fullstack Person Profile Manager  
### Django REST Framework + React.js + JWT Authentication

A complete full-stack web application for managing person profiles, built using:

- **Django REST Framework**
- **JWT-based authentication**
- **React.js frontend**
- **Docker (optional)**
- **Clean UI for CRUD operations**

This project includes **Login, Register, Create, Edit, Delete, List** functionalities.

---

## ⭐ Features

### 🔐 Authentication
- Register new users  
- Login with JWT  
- Secure API endpoints  
- User-specific data isolation  

### 👤 Person Profile Management  
Each profile includes:

- First Name  
- Last Name  
- Gender  
- Date of Birth  
- Address  
- Phone Number  
- Email  

### 🖥️ Frontend Features (React.js)
- Modern UI  
- Form validation  
- Edit mode  
- Delete confirmation  
- Auto-refresh on CRUD  

### 🛠️ Backend Features (Django REST Framework)
- JWT Authentication (`SimpleJWT`)  
- ModelViewSet for CRUD operations  
- Serializer validation  
- Filter data per user (`Person.objects.filter(user=request.user)`)

