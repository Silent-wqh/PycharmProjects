from django.db import models


class Pie(models.Model):
    """披萨模型"""
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Topping(models.Model):
    """配料"""
    pie = models.ForeignKey(Pie, on_delete=models.CASCADE)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if len(self.name) < 30:
            return f'{self.pie}的配料：{self.name}'
        else:
            return f'{self.pie}的配料：{self.name[:30]}...'
