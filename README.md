# Flask API Sample App

Hello! If you are reading this, you have come across my sample app used to help teach people how to create APIs using Flask and Flask-RESTful. You can find a link to my blog post that walks through the topic here: https://medium.com/@hollyawheeler96/building-apis-and-restful-apis-in-flask-98b894507f76

Please fork the repo before cloning it to ensure others can access it at its base state. 

# Prerequisites 
To run this application, you will need Python and Flask installed on your system.

# Installation 
1. Fork the repo 
2. Copy the SSH link from your forked repo 
3. In your CLI, run: git clone [add your ssh link here]
4. cd flask-api-example

To start the server, run the following commands in the CLI
1. pipenv install && pipenv shell
2. cd server
3. flask db init
4. flask db migrate -m 'initial migration'
5. flask db upgrade head 
6. python seed.py
7. export FLASK_APP=app.py
8. export FLASK_RUN_PORT=5555
9. python app.py