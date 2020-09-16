from django.db import models
import datetime, re, bcrypt

class Project(models.Model):
    project_name = models.CharField(max_length=255)
    project_main_img = models.CharField(max_length=255)
    short_desc = models.TextField()
    role_heading = models.CharField(max_length=255)
    role_desc = models.TextField()
    background_heading = models.CharField(max_length=255)
    background_desc = models.TextField()
    problem_heading = models.CharField(max_length=255)
    problem_desc = models.TextField()
    challenges_heading = models.CharField(max_length=255)
    challenges_desc = models.TextField()
    user_research_heading = models.CharField(max_length=255)
    user_research_img1 = models.CharField(max_length=255)
    user_research_img2 = models.CharField(max_length=255)
    user_research_desc = models.TextField()
    solution_heading = models.CharField(max_length=255)
    solution_img = models.CharField(max_length=255)
    solution_desc1 = models.TextField()
    solution_desc2 = models.TextField()
    key_screen_heading = models.CharField(max_length=255)
    key_screen_img1 = models.CharField(max_length=255)
    key_screen_img2 = models.CharField(max_length=255)
    key_screen_img3 = models.CharField(max_length=255)
    key_screen_img4 = models.CharField(max_length=255)
    key_screen_img5 = models.CharField(max_length=255)
    key_screen_img6 = models.CharField(max_length=255)
    key_screen_img7 = models.CharField(max_length=255)
    key_screen_img8 = models.CharField(max_length=255)
    key_screen_img9 = models.CharField(max_length=255)
    learned_heading = models.CharField(max_length=255)
    learned_desc = models.TextField()
    results_heading = models.CharField(max_length=255)
    results_desc = models.TextField()
    results_data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email must be valid format!!"
        # registered email is unique
        elif User.objects.filter(email=postData['email']):
            errors['email'] = "Show email must be unique"
        if len(postData['pwd']) < 8:
            errors['pwd'] = "Password must be at least 8 characters!!"
        if postData['pwd'] != postData['confirm_pwd']:
            errors['confirm_pwd'] = "Password and confirm password do not match!!"
        # the secret key does not match
        if not bcrypt.checkpw(postData['secret_key'].encode(), User.objects.filter(email=postData['email'])[0].password.encode()):
            # if not bcrypt.checkpw(postData['secret_key'].encode(), User.objects.filter(email=postData['email'])[0].password.encode()):
            errors['secret_key'] = "Password do not match our record!!"
        return errors

    def login_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email must be valid format!!"
        # show error if email trying to log in does not exist
        elif not User.objects.filter(email=postData['email']):
            errors['email'] = "Email does not exist"
        # the password does not exist OR the form password is not the same as the password in the database
        elif not bcrypt.checkpw(postData['pwd'].encode(), User.objects.filter(email=postData['email'])[0].password.encode()):
            # User.objects.filter(email=postData['email'])[0].password != postData['pwd']:
            errors['pwd'] = "Password do not match our record!!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Competencies(models.Model):
    comp_heading = models.CharField(max_length=255)
    comp_subheading1 = models.CharField(max_length=255)
    comp_subdesc1 = models.TextField()
    comp_subheading2 = models.CharField(max_length=255)
    comp_subdesc2 = models.TextField()
    comp_subheading3 = models.CharField(max_length=255)
    comp_subdesc3 = models.TextField()
    comp_subheading4 = models.CharField(max_length=255)
    comp_subdesc4 = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class About(models.Model):
    about_short_heading = models.CharField(max_length=255)
    about_tagline = models.CharField(max_length=255)
    about_short_desc = models.TextField()
    about_profile_img = models.CharField(max_length=255)
    about_heading = models.CharField(max_length=255)
    about_main_img = models.CharField(max_length=255)
    about_me_heading = models.CharField(max_length=255)
    about_me_desc = models.TextField()
    about_me_img = models.CharField(max_length=255)
    got_here_heading = models.CharField(max_length=255)
    got_here_desc = models.TextField()
    values_heading = models.CharField(max_length=255)
    values_desc = models.TextField()
    values_subheading1 = models.CharField(max_length=255)
    values_subdesc1 = models.TextField()
    values_subheading2 = models.CharField(max_length=255)
    values_subdesc2 = models.TextField()
    values_subheading3 = models.CharField(max_length=255)
    values_subdesc3 = models.TextField()
    values_subheading4 = models.CharField(max_length=255)
    values_subdesc4 = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Contact(models.Model):
    contact_heading = models.CharField(max_length=255)
    contact_img = models.CharField(max_length=255)
    contact_subheading = models.CharField(max_length=255)
    contact_subdesc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    priority = models.CharField(max_length=255)
    msg = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)