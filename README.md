# 📄 Resume Builder (Django Project)

[![Made with Django](https://img.shields.io/badge/Made%20with-Django-092E20?style=for-the-badge&logo=django)](https://www.djangoproject.com/)  
[![GitHub stars](https://img.shields.io/github/stars/ISSEI-77/resume-builder?style=for-the-badge)](https://github.com/ISSEI-77/resume-builder/stargazers)  
[![GitHub forks](https://img.shields.io/github/forks/ISSEI-77/resume-builder?style=for-the-badge)](https://github.com/ISSEI-77/resume-builder/network/members)  
[![License](https://img.shields.io/github/license/ISSEI-77/resume-builder?style=for-the-badge)](./LICENSE)  

A simple **Resume Builder Web Application** built with **Django, HTML, and CSS**.  
This project allows users to input their details in a single responsive form and generate a **professional resume** instantly using **two different high-quality templates**.  

✅ **No authentication, APIs, or internet usage** – just a basic, offline Django project.  
✅ **Responsive design** – works on desktop and mobile.  
✅ **ATS-friendly professional resumes** – recruiter-ready.  
✅ **Two templates included** – Corporate (one-column) and Modern (two-column).  

---

## 🚀 Features
- Fill out your details in a single-page form:
  - Name, Job Title, Email, Phone
  - Professional Summary
  - Skills (comma separated)
  - Work Experience (one per line)
  - Education (one per line)
- Choose between **Template 1 (Corporate)** or **Template 2 (Modern)**
- Instantly view a professional resume
- Resume layouts are **print-ready** (export to PDF via browser print)

---

## 🛠️ Tech Stack
- **Frontend**: HTML5, Classic CSS (responsive design)  
- **Backend**: Django (Python)  
- **No JS libraries / APIs / Authentication** – clean and minimal  

---

## 📂 Project Structure
```
resume_builder/
│
├── manage.py
├── resume_builder/        # Project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── builder/               # Django app
│   ├── __init__.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   ├── index.html
│   │   ├── resume1.html
│   │   └── resume2.html
│   └── static/
│       └── style.css
```

---

## ⚙️ Installation & Setup

Follow these steps to set up the project locally:

```bash
# 1. Clone the repository
git clone https://github.com/ISSEI-77/resume-builder.git
cd resume-builder

# 2. Create a virtual environment
python -m venv venv

# 3. Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install django

# 5. Apply database migrations
python manage.py migrate

# 6. Run the development server
python manage.py runserver
```

Now open your browser and visit:
```
http://127.0.0.1:8000/
```

---

## 🖼️ Screenshots (Demo)

### Resume Form Page
![Form Page](./screenshots/form.png)

### Template 1 (Corporate Resume)
![Corporate Template](./screenshots/resume1.png)

### Template 2 (Modern Resume)
![Modern Template](./screenshots/resume2.png)

---

## 📑 Usage
1. Enter your personal and professional details in the form.  
2. Click **Generate Resume (Template 1)** or **Generate Resume (Template 2)**.  
3. Your professional resume is instantly generated.  
4. To save as PDF → **Print (Ctrl+P / Cmd+P)** → Choose *Save as PDF*.  

---

## 📌 Future Improvements
- Add **direct PDF download** option with WeasyPrint / xhtml2pdf.  
- Support for **multiple experiences & education with structured fields**.  
- More professional resume templates.  

---

## 👨‍💻 Author
- **ISSEI-77**  
- [GitHub Profile](https://github.com/ISSEI-77)  

---

## 📜 License
This project is licensed under the **MIT License** – free to use and modify.  
