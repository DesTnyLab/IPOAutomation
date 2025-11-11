# 🚀 IPOAutomation

IPOAutomation is a web-based system that automates the process of applying for IPO shares in the **MeroShare** platform.
It simplifies and accelerates the IPO application process by automating repetitive steps such as login, selecting shares, and submitting applications — helping users save time and avoid manual errors.

## ✨ Features

- 🔁 **Automated IPO Application** — Apply for IPOs automatically through MeroShare.
- 👥 **Multiple Account Support** — Manage and apply from multiple DP accounts.
- 🕒 **Scheduled Applications** — Set tasks to run automatically using Celery Beat.
- 📊 **User Dashboard** — Track application status and logs from one place.
- 🔒 **Secure Credential Handling** — Credentials stored securely using environment variables.
- ⚙️ **Asynchronous Processing** — Celery handles background automation tasks efficiently.

## 🛠️ Tech Stack

| Component        | Technology Used      |
|-----------------|----------------------|
| **Backend**     | Django (Python)      |
| **Database**    | PostgreSQL           |
| **Task Queue**  | Celery               |
| **Broker**      | Redis                |
| **Frontend**    | Django Templates     |
| **Deployment (Optional)** | Docker, Nginx |

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/DesTnyLab/IPOAutomation.git
cd IPOAutomation
```

### 2️⃣ Create and Activate Virtual Environment
```bash
python3 -m venv env
source env/bin/activate        # On Windows: env\Scripts\activate
```

### 3️⃣ Install Required Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables
Copy the example file and update the credentials.
```bash
cp .env.example .env
```

### 5️⃣ Apply Database Migrations
```bash
python manage.py migrate
```

### 6️⃣ Run the Development Server
```bash
python manage.py runserver
```

### 7️⃣ Run Celery Worker
```bash
celery -A core worker -l info
```

### 8️⃣ Run Celery Beat Scheduler (for Scheduled IPO Tasks)
```bash
celery -A core beat -l info
```

## 🧩 Architecture Overview

```
Django Backend ─▶ PostgreSQL ─▶ Celery ─▶ Redis
```

## 📂 Folder Structure

```
IPOAutomation/
├── core/
├── accounts/
├── apply/
├── static/
├── templates/
├── requirements.txt
└── manage.py
```

## 🔐 Security Notes

- Do **not** store MeroShare credentials directly in the database.
- Use `.env` or secret management tools to protect sensitive data.
- Keep Redis password-protected if running in production.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📜 License

MIT License

## ⭐ Support

If you find this project useful, give it a star ⭐ on GitHub!