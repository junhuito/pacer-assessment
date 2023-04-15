# Task 1 Simple Backend Endpoint

### Create a simple Python Django app that has the following features

1. a backend API endpoint called  get_score  with a simple dummy formula that could be anything e.g.  result = input + 1

    - [get_score](http://54.169.102.189:8000/app/get_score?input=4)

2. a PostgreSQL database that the backend API uses to log the user ID and the score

    - [get_all_user](http://54.169.102.189:8000/app/user)

3. demonstrate that the endpoint is behaving as expected (how do we test it? how can we prove that it is working as expected?)

    - Run command below in <b>app/</b> directory 
        ```
        python manage.py test
        ```

4. More
    - [Api Documentation](http://54.169.102.189:8000/swagger)

# Task 2 Admin Panel
### Create a simple admin panel where operations staff can use to manage the database:

1. a non engineer should be able to view the SQL tables, and search/make queries

    - [Admin Page](http://54.169.102.189:8000/admin)

    - Admin Site Developer Credentials
        ```
        Username: tester@1
        Password: o84x2Z^UL5p8
        ```

2. even better if the staff can edit the entries too
    - [Admin Page](http://54.169.102.189:8000/admin)

    - Admin Site Superuser Credentials
        ```
        Username: tojunhui
        Password: Junhui8888
        ```


# Task 3 Database Migration
### If we want to change the schema of the database, say we want to add, edit, or remove columns:

1. demonstrate a process or script, or a demo video of the schema update process
    - Original schema
    ![Datbase summary](/assets/1.png)
    
    - Update the schema
    ![Datbase summary](/assets/2.png)

    - Make migration
        ```
        python manage.py makemigrations
        ```

    - Migrate
        ```
        python manage.py migrate
        ```

2. demonstrate that the endpoints and the services are not affected, and the tests are 
running fine
    - Run the test
        ```
        python manage.py migrate
        ```
    - All tests are past after altering the db schema
    ![Datbase summary](/assets/3.png)


# Bonus Task: Deployment to cloud
### Demonstrate the tasks above can be deployed end to end on cloud (preferably on AWS)

1. dockerise the app
    - [docker.md](/docker.md)

2. set up CI/CD pipelines or automated unit testing
    - Pending

3. host the app on serverless hosting on AWS e.g. container / cluster hosting services
    - [ec2.md](/ec2.md)

4. connect to a database that is on the cloud
    - In this project, Amazon RDS is used for the database
    ![Datbase summary](/assets/db.png)




