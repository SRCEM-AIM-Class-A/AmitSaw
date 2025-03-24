Project Overview: 
The StudentProject is a simple Django multi-app project consisting of two applications: app1 and app2. The project does not use a database but includes static views and templates. It is fully containerized using Docker and integrated with Jenkins for CI/CD automation. The application serves basic pages such as Home, About, Contact, and Services.

Features
Multiple Django apps (app1 and app2)

Static pages using Django templates (Home, About, Contact, Services)

Containerized with Docker for easy deployment

Automated build and push to Docker Hub using Jenkins

Project Structure
The directory structure of the project is as follows:


Folder Structure:
StudentProject/
│── app1/                  # First Django app
│── app2/                  # Second Django app
│── StudentProject/        # Main Django project directory
│── templates/             # HTML templates for the project
│── static/                # Static files (CSS, JS, images)
│── Dockerfile             # Docker configuration file
│── Jenkinsfile            # Jenkins pipeline script
│── requirements.txt       # Python dependencies file
│── manage.py              # Django management script
│── README.md              # Project documentation file


Setup Instructions :
1. Clone the Repository
To get started, clone the project from GitHub using the following command:

git clone docker tag studentproject your-dockerhub-username/studentproject


2. Install Dependencies
Ensure you have Python 3.12+ installed, and then install the required dependencies using:

pip install -r requirements.txt
This command installs all necessary Python packages listed in requirements.txt.

3. Run the Django Project
Once dependencies are installed, start the Django development server with:


python manage.py runserver
Now, open your browser and visit: http://127.0.0.1:8000/ to view the application.

Running with Docker
1. Build the Docker Image
To containerize the project, build the Docker image using:

docker build -t studentproject .
This command creates a Docker image named studentproject under the Docker Hub username amitsaw.

2. Run the Docker Container
Once the image is built, run the container with:

docker run -p 8000:8000 amitsaw/studentproject
Now, visit http://localhost:8000/ in your browser to access the Django app inside the Docker container.

Pushing to Docker Hub
To push the Docker image to Docker Hub, follow these steps:

1. Tag the Docker Image:

docker tag amitsaw/studentproject amitsaw/studentproject:latest
2. Push the Image to Docker Hub:

docker push amitsaw/studentproject:latest
The image will now be available on Docker Hub. You can check it at Docker Hub Repository.

CI/CD with Jenkins
To automate the Docker image build and push process, use Jenkins with the provided Jenkinsfile.

1. Configure Jenkins Pipeline:
Add a Jenkins pipeline using the Jenkinsfile provided in the repository.

Ensure Jenkins has access to Docker and Git.

2. Add Docker Hub Credentials in Jenkins:
In Jenkins, go to Manage Jenkins → Manage Credentials.

Add Docker Hub credentials for authentication.

3. Run the Pipeline:
Start the Jenkins pipeline job.

The pipeline will automatically pull code, build the Docker image, and push it to Docker Hub.



Setup Instructions
1. Setup Python Virtual Environment
Before starting, ensure Python and pip are installed. Then, create and activate a virtual environment:

# Create a virtual environment
python -m venv env
# Activate the virtual environment (Windows)
env\Scripts\activate
# Activate the virtual environment (Linux/Mac)
source env/bin/activate

2. Install Django and Start the Project

# Install Django
pip install django
# Create a Django project named StudentProject
django-admin startproject StudentProject .

3. Create Django Apps
# Create two Django apps: app1 and app2
python manage.py startapp app1
python manage.py startapp app2

4. Run the Django Development Server
# Start the Django development server
python manage.py runserver
Now, visit http://127.0.0.1:8000/ in your browser to view the application.

5. Install Required Dependencies and Create requirements.txt
To install dependencies, use:
pip install -r requirements.txt

To generate the requirements.txt file, run:
pip freeze > requirements.txt

6. Initialize Git and Push Code to GitHub
# Initialize Git repository
git init
# Add files to the repository
git add .
# Commit changes
git commit -m "Initial commit"
# Add the GitHub remote repository
git remote add origin https://github.com/SRCEM-AIM-Class-A/AmitSaw.git
# Push code to GitHub
git push origin main

7. Create and Test Docker Image
To create and test the Docker image, follow these steps:
# Build the Docker image
docker build -t amitsaw/studentproject .

# Run the container
docker run -p 8000:8000 amitsaw/studentproject
Now, visit http://localhost:8000/ to see the project running in Docker.

8. Tag and Push Docker Image to Docker Hub
To tag and push the Docker image to Docker Hub:
# Tag the Docker image
docker tag amitsaw/studentproject amitsaw/studentproject:latest
# Push the image to Docker Hub
docker push amitsaw/studentproject:latest
You can check the image on Docker Hub Repository.

9. Setup Jenkins Pipeline
To set up Jenkins:
Inside Jenkins, create a new pipeline job.
Use the Jenkinsfile script from the project repository to configure the pipeline.
The pipeline will pull the code, build the Docker image, and push it to Docker Hub automatically.

Final Steps
To ensure everything is up to date:
# Add all changes to Git
git add .

# Commit changes
git commit -m "Updated project with Docker and Jenkins integration"

# Push updates to GitHub
git push origin main