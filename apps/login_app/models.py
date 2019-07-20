from __future__ import unicode_literals
from django.db import models
from django.contrib import messages

class UserManager(models.Manager):
    def basic_validator_register(self, postData):
        errors = {}
        if len(postData['input_first_name']) < 2:
            errors["valid_first_name"] = "First name should be at least 2 characters"
        if len(postData['input_last_name']) < 2:
            errors["valid_last_name"] = "Last name should be at least 2 characters"
        if '@' not in postData['input_email']:
            errors["valid_email"] = "Email address should include @ sign"
        if len(postData['input_password']) < 8:
            errors["valid_password_length"] = "Password should be at least 8 characters"
        if postData['input_password'] != postData['input_confirm_password']:
            errors["valid_password_match"] = "Password should match with Confirm PW"
        return errors

    def basic_validator_login(self, postData):
        errors = {}
        if '@' not in postData['input_email']:
            errors["valid_email"] = "Email address should include @ sign"
        if len(postData['input_password']) < 8:
            errors["valid_password_length"] = "Password should be at least 8 characters"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    objects = UserManager()
