# dj_small_shop

## Setup Instructions

### Prerequisites
Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

### Install Dependencies

# Go to Terminal 
### Go to Terminal 

1. **Create a Virtual Environment** (recommended):

   ```bash
    python -m venv venv
    ```

2. **Install Django Framework**

    ```bash
   pip install django
    ```


3. **Install Pillow Library**

    ```bash
    pip install pillow
    ```
4. **Install PDF Library**
    ```bash
   pip install xhtml2pdf
    ```

# Install Django Framework
# pip install django
5. **Install Django Cross-Origin Resource Sharing (CORS)**
    ```bash
    pip install django-cors-headers
    ```

# Install Pillow Library
# pip install pillow

# Install PDF Library
# pip install xhtml2pdf
6. **Project Setup**
    ```bash
    django-admin startproject config .
    ```

# Install Django Cross-Origin Resource Sharing (CORS)
# pip install django-cors-headers

# Project Setup
# django-admin startproject config .
7. **Create Backend App**
    ```bash
    python manage.py startapp backend
    ```

# Create Backend App
# python manage.py startapp backend

# Create API V1 App
# python manage.py startapp api_v1
8. **Create API V1 App**
    ```bash
    python manage.py startapp api_v1
    ```

# Create API V2 App
# python manage.py startapp api_v2
9. **Create API V2 App**
    ```bash
    python manage.py startapp api_v2
    ```