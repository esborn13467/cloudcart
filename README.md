# CloudCart Project

## Getting Started

These instructions will help you set up the project on your local machine for development and contribution purposes.

### Prerequisites

- Python 3.12
- Git
- Virtualenv

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/esborn13467/cloudcart.git
   cd cloudcart
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

### Contributing

1. **Create a new branch for your feature or bugfix:**

   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes and commit them:**

   ```bash
   git add .
   git commit -m "Add your commit message"
   ```

3. **Push your changes to the remote repository:**

   ```bash
   git push origin feature/your-feature-name
   ```

### License

This project is licensed under the MIT License - see the `LICENSE` file for details.