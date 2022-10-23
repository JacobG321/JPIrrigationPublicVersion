from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class Customer:
    db= 'jpirrigation'
    def __init__(self, data):
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.phone=data['phone']
        self.comments=data['comments']
        self.contact_method=data['contact_method']

    @classmethod
    def save_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, phone, comments, contact_method) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(phone)s, %(comments)s, %(contact_method)s)"
        return connectToMySQL(cls.db).query_db(query, data)

    
    @classmethod
    def get_customer_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL(cls.db).query_db(query, data)
        if not results:
            return False
        return cls(results[0])

    
    @classmethod
    def get_user_by_last_name(cls,data):
        query = "SELECT * FROM users WHERE last_name = %(last_name)s"
        results = connectToMySQL(cls.db).query_db(query, data)
        if not results:
            return False
        return cls(results[0])

    @staticmethod
    def new_quote_validation(data):
        is_valid=True
        if not EMAIL_REGEX.match(data["email"].strip()):
            flash('Invalid Email', 'register')
            is_valid = False
        if len(data['first_name'].strip()) < 3:
            flash('First name must be more than 3 characters', 'register')
            is_valid = False
        if len(data['last_name'].strip()) < 3:
            flash('Last name must be more than 3 characters', 'register')
            is_valid = False
        if len(data['phone'].strip()) < 7:
            flash('Phone number must be at least 7 digits', 'register')
            is_valid = False
        if len(data['phone'].strip()) > 11:
            flash('Phone number must be less than 12 digits', 'register')
            is_valid = False
        if len(data['comments']) > 300:
            flash('Comments must be less than 301 characters', 'register')
            is_valid = False
        if len(data['contact_method'].strip()) < 4:
            flash('Please select a preferred contact method', 'register')
            is_valid = False
        return is_valid
        
