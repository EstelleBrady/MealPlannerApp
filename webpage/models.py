from django.db import models


class Roles(models.Model):
    role_id = models.IntegerField(primary_key=True)
    role_name = models.CharField(max_length=30)
    role_desc = models.CharField(max_length=1000)


class Users(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField()
    role_id = models.ForeignKey("Roles", on_delete=models.CASCADE)
    user_pass = models.CharField(max_length=50)


class Recipes(models.Model):
    recipe_id = models.IntegerField(primary_key=True)
    recipe_name = models.CharField(max_length=200)
    recipe_desc = models.CharField(max_length=10000)
    user_id = models.ForeignKey("Users", on_delete=models.CASCADE)


class Ingredients(models.Model):
    ingredient_id = models.IntegerField(primary_key=True)
    ingredient_name = models.CharField(max_length=100)
    calories = models.IntegerField()
    total_fat = models.IntegerField()
    # Add anything else you can think of


class MeasurementUnits(models.Model):
    unit_id = models.IntegerField(primary_key=True)
    measurement_desc = models.CharField(max_length=500)


class MeasurementQty(models.Model):
    qty_id = models.IntegerField(primary_key=True)
    qty_desc = models.CharField(max_length=200)


class RecipeIngredients(models.Model):
    recipe_id = models.ForeignKey("Recipes", on_delete=models.CASCADE)
    unit_id = models.ForeignKey("MeasurementUnits", on_delete=models.CASCADE)
    qty_id = models.ForeignKey("MeasurementQty", on_delete=models.CASCADE)
    ingredient_id = models.ForeignKey("Ingredients", on_delete=models.CASCADE)
