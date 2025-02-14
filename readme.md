# FireWatch 🔥🚒  
*A Django-based Web Application for Fire and Smoke Detection*  

![FireWatch Banner](https://via.placeholder.com/1000x300?text=FireWatch+🔥🚒)  

## Table of Contents  
- [About FireWatch](#about-firewatch)  
- [Features](#features)  
- [Installation & Setup](#installation--setup)  
  - [1. Clone the Repository](#1-clone-the-repository)  
  - [2. Setup Environment Variables](#2-setup-environment-variables)  
  - [3. Install Dependencies](#3-install-dependencies)  
  - [4. Apply Database Migrations](#4-apply-database-migrations)  
  - [5. Run the Development Server](#5-run-the-development-server)  
- [Usage](#usage)  
- [Contributing](#contributing)  
- [License](#license)  

---

## About FireWatch  

**FireWatch** is a web-based application built using Django and Convolutional Neural Networks (CNN) to detect fire and smoke from images. This project enables users to upload images, preview them, and even use live capture features for real-time fire detection.  

---

## Features  

✅ **User Authentication** – Secure user registration and login system.  
✅ **Image Upload & Preview** – Easily upload images for fire detection analysis.  
✅ **Live Capture View** – Get real-time fire and smoke detection via webcam or connected cameras.  
✅ **CNN-Based Detection** – Uses deep learning models to analyze images and detect fire/smoke.  
✅ **Django-Powered Backend** – Robust and scalable framework for web applications.  

---

## Installation & Setup  

Follow these steps to get FireWatch up and running on your local machine.  

### 1. Clone the Repository  
```sh
git clone https://github.com/your-username/firewatch.git  
cd firewatch  
```  

### 2. Setup Environment Variables  
Create a `.env` file in the root directory and add the following:  
```sh
SECRET_KEY=your_secret_key_here  
DEBUG=True  
```  

### 3. Install Dependencies  
Install required Python packages using:  
```sh
pip install -r requirements.txt  
```  

### 4. Apply Database Migrations  
Run the following commands to set up the database:  
```sh
python manage.py makemigrations  
python manage.py migrate  
```  

### 5. Run the Development Server  
Start the Django server using:  
```sh
python manage.py runserver  
```  

The app will now be available at **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**.  

---

## Usage  

1. **Open FireWatch** in your browser: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  
2. **Register or log in** with an existing account.  
3. **Upload an image** to check for fire or smoke.  
4. **Use the live capture feature** for real-time fire detection.  

---

## Contributing  

We welcome contributions! To contribute:  
1. **Fork** the repository.  
2. **Create a new branch**: `git checkout -b feature-branch`  
3. **Commit your changes**: `git commit -m "Add new feature"`  
4. **Push to your fork**: `git push origin feature-branch`  
5. **Submit a Pull Request**.  

---

## License  

This project is licensed under the **MIT License**. See the `LICENSE` file for details.  

---

🔥 **Stay Safe. Detect Fire Before It Spreads.** 🔥