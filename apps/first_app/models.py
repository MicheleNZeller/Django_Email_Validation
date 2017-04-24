from __future__ import unicode_literals

from django.db import models

import re

EMAIL_REGEX = re.compile (r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class EmailManager(models.Manager):
    def stuff(self, postDataemail):
        print "EmailManager: " + postDataemail
    def validate(self, postData):
        error = ""
        if len(postData["email_post"]) < 1:
            error = "Email is required!"
        elif not EMAIL_REGEX.match(postData["email_post"]):
            error = "Invaild Email"

        if len(error) == 0:
            return(True, error)
        else :
            return(False, error)

class Email(models.Model):
    emails = models.CharField(max_length = 45)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    emailmanager = EmailManager()
