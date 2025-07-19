# Health Carrie Dashboard

A Django-based dashboard for managing patients and tracking session adherence.

---

## Table of Contents

1. [Overview](#overview)  
2. [Technologies & Requirements](#technologies--requirements)  
3. [Models & Database Tables](#models--database-tables)  
4. [Cloning & Environment Setup](#cloning--environment-setup)    

---

## Overview

This project provides:

- CRUD operations for **Patients**  
- Tracking of **alerts** per patient  
- Recording of **session adherence results** (medication, diet, exercise)  
- Real-time charts via JSON endpoints  

---

## Technologies & Requirements

- Python ≥ 3.9  
- Django ≥ 4.2  
- PostgreSQL  
- `psycopg2-binary`  
- `python-dotenv`  

---

## Models & Database Tables

| Model                       | Table Name                          | Key Fields                                                                 |
|-----------------------------|-------------------------------------|----------------------------------------------------------------------------|
| **Provider**                | `patients_provider`                 | `id`, `name`                                                               |
| **Diagnosis**               | `patients_diagnosis`                | `id`, `name`                                                               |
| **Patient**                 | `patients_patient`                  | `first_name`, `last_name`, `mrn` (unique), `provider_id`, `diagnosis_id`,<br>`status`, `last_session_date`, `notifications`, `age` |
| **PatientSession**          | `patients_patientsession`           | `patient_id`, `session_date`, `status`                                     |
| **SessionAlert**            | `patients_sessionalert`             | `patient_id`, `alert_type`                                                 |
| **SessionAdherenceResult**  | `patients_sessionadherenceresult`   | `session_id`, `medication`, `diet`, `exercise`                             |

---

## Cloning & Environment Setup

```bash
# 1) Clone the repository
git clone https://github.com/perronirafael/carrie_dashboard.git
cd carrie_dashboard

# 2) Create & activate virtual environment
python -m venv venv

# macOS/Linux
source venv/bin/activate

# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# 3) Install dependencies
pip install -r requirements.txt
```

## Running the project

```bash
# 1) Make migrations for the 'patients' app
py manage.py makemigrations patients

# 2) Apply all migrations
py manage.py migrate

# 3) Seed initial data (fixture)
py manage.py seed_data

# 4) Running
py manage.py runserver
```

