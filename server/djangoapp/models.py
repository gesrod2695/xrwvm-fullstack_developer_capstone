# Uncomment the following imports before adding the Model code
from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

# Create a Car Make model `class CarMake(models.Model)`:
class CarMake(models.Model):
    name = models.CharField(max_length=100, help_text='Enter car make name (e.g. BMW, Toyota)')
    description = models.TextField(max_length=1000, help_text='Enter a brief description of the car make')
    
    # Additional fields you might want to include
    founded_year = models.IntegerField(null=True, blank=True, help_text='Year the company was founded')
    headquarters = models.CharField(max_length=100, null=True, blank=True, help_text='Company headquarters location')
    
    def __str__(self):
        return self.name  # Return the name when printed

# Create a Car Model model `class CarModel(models.Model):`:
class CarModel(models.Model):
    # Type choices for the car model
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    HATCHBACK = 'Hatchback'
    COUPE = 'Coupe'
    CONVERTIBLE = 'Convertible'
    TRUCK = 'Truck'
    
    CAR_TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (HATCHBACK, 'Hatchback'),
        (COUPE, 'Coupe'),
        (CONVERTIBLE, 'Convertible'),
        (TRUCK, 'Truck'),
    ]
    
    # Many-To-One relationship to Car Make model (One Car Make has many Car Models)
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    
    # Dealer ID (refers to dealer in external database)
    dealer_id = models.IntegerField()
    
    # Name of the car model
    name = models.CharField(max_length=100, help_text='Enter car model name (e.g. Camry, Accord)')
    
    # Type with limited choices
    type = models.CharField(
        max_length=20, 
        choices=CAR_TYPES, 
        default=SEDAN,
        help_text='Select car type'
    )
    
    # Year with min value 2015 and max value 2023
    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ],
        help_text='Enter year (2015-2023)'
    )
    
    # Additional 
    color = models.CharField(max_length=50, null=True, blank=True, help_text='Car color')
    mileage = models.IntegerField(default=0, help_text='Car mileage')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text='Car price')
    
    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"  # Return car make and model when printed