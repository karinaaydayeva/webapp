Web Application: Student Marks Management

Overview of the Application

This project is a full-stack web application that allows users to view, add, and delete student records containing subject scores. It is built using:

Amazon RDS (PostgreSQL) for database storage

Amazon EC2 (Ubuntu + Flask) for backend deployment

Amazon S3 for static frontend hosting

HTML + JavaScript for the user interface

The main goal of this application is to demonstrate the ability to deploy a working web app using AWS services. The web interface displays a table of student records retrieved from a PostgreSQL database. Users can add a new student or delete an existing one by student ID. All changes are immediately reflected in the live database.

How to Run the Application

Backend Setup (EC2 + Flask)

Launch an EC2 instance with Ubuntu

Connect to the instance via SSH

Install required packages:
sudo apt update
sudo apt install python3-pip
pip3 install flask psycopg2-binary flask-cors

Upload the app.py file to the EC2 instance

Run the backend using: python3 app.py

The backend runs on: http://3.109.123.174:5000

Database Setup (Amazon RDS)

Create a PostgreSQL RDS instance

Create a database named db_karina

Create a table named tbl_karina_data with columns for student ID and subject scores

Import data from a CSV file using psql or DBeaver

Frontend Setup (Amazon S3)

Create an S3 bucket

Enable static website hosting in the bucket settings

Upload the index_karina.html file

Set the bucket policy to allow public access

Open the frontend via the public static website URL

Deployed Resources

Frontend (S3 Static Hosting):
https://2t-karina.s3.ap-south-1.amazonaws.com/index_karina.html

Backend (EC2 - Flask API):
http://3.109.123.174:5000/data

Database (RDS - PostgreSQL):
Hosted on Amazon RDS under database name db_karina
Note: RDS is not publicly browsable — it connects through the backend only

Project Files

app.py – Flask backend application connected to RDS
index_karina.html – Frontend interface hosted on S3
student_marks.csv – Dataset used to populate the database
README.md – Project documentation