from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    



class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    
    
    FICTION = 'Fiction'
    NON_FICTION = 'Non-Fiction'
    SCIENCE = 'Science'
    HISTORY = 'History'

    CATEGORY_CHOICES = [
        (FICTION, 'Fiction'),
        (NON_FICTION, 'Non-Fiction'),
        (SCIENCE, 'Science'),
        (HISTORY, 'History'),
    ]
    
    
    title = models.CharField(max_length=200, unique=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default=FICTION)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=13, decimal_places=2)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True,
    blank=True)
    
    def __str__(self):
        return self.title

