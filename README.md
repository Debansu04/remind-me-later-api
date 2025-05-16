# Remind-me-later API

This is a Django REST API that allows users to create reminders by specifying a date, time, message, and delivery method (e.g., SMS, Email). This backend is intended to be used with a frontend built by JavaScript developers.

## ✨ Features

- Create reminders using `POST /api/reminders/`
- Stores reminders in a SQLite database (can be configured for PostgreSQL)
- Designed to support more reminder delivery methods in future

## 🧱 Tech Stack

- Python 3.10+
- Django 4.x
- Django REST Framework

## 🚀 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/Debansu04/remind-me-later-api.git
cd remind-me-later-api
