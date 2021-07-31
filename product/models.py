from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
# Create your models here.

class Product(models.Model) :
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    info = models.CharField(max_length=10000)
    price = models.IntegerField()
    # date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='product', on_delete=models.CASCADE)
    highlighted = models.TextField()

    # def save(self, *args, **kwargs):
    #     # lexer = get_lexer_by_name(self.name)
    #     # linenos = 'table' if self.brand else False
    #     options = {'name': self.name} if self.name else {}
    #     formatter = HtmlFormatter(full=True, **options)
    #     self.highlighted = highlight(self.name, formatter)
    #     super(Product, self).save(*args, **kwargs)

    def __str__(self) :
        return self.name