from django.db import models


class QueryType(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Contact(models.Model):
    message_name = models.CharField(max_length=60, null=False, blank=False)
    message_email = models.EmailField(null=False, blank=False)
    query_type = models.CharField(max_length=60, null=False, blank=False, default='product')
    message_body = models.CharField(max_length=300, null=False, blank=False)

    def __str__(self):
        return self.message_name
