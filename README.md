## Social-media-clone-using-Django
This project aims to create a social media platform using the Django web framework, inspired by popular social media platforms. The application will include functionalities for user registration, login, profile management, posting, following other users, and more, providing a basic yet functional social media experience.

## Quick Start Guide

1. Clone the repository:
    ```bash
    git clone https://github.com/realsanjeev/Social-media-clone-using-Django.git social-clone
    cd social-clone
    ```

2. Create a virtual environment:  
   **For Linux and macOS:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
   **For Windows:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Start the web server:
    ```bash
    python manage.py runserver
    ```

For demo login, use **admin** as both the username and password.

### Features:
- User registration and authentication system
- User profile management (bio, avatar, and other details)
- Post and share updates, images, and multimedia content
- News feed showing posts from followed users
- Follow/unfollow functionality to connect with others

### Ouput Preview
#### SignIn
![signin](https://github.com/realsanjeev/Social-media-clone-using-Django/assets/45820805/36823b86-4a99-408a-98c5-c85f740308e4)
#### Home
![home](https://github.com/realsanjeev/Social-media-clone-using-Django/assets/45820805/8a9acb3d-c5aa-4898-8370-1cffcadfd3a4)

#### Profile
![userprofile](https://github.com/realsanjeev/Social-media-clone-using-Django/assets/45820805/4f6b036b-8f1a-4990-945c-06cf042491af)

> To run with debug=False in localmachine use python manage.py runserver --insecure