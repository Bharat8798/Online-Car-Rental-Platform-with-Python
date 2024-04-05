#!/usr/bin/env python
# coding: utf-8

# In[31]:


import datetime as dt


# In[32]:


class CarRental:
    def __init__(self):
        self.available_cars =["SUV","Sedan","Hatchback"]
        
    def display_car_availability(self):
        print("Available cars for rent:")
        for car in self.available_cars:
            print(car)

    def rent_hourly(self, hours, requested_cars):
        if requested_cars > 0 and requested_cars <= self.available_cars:
            print(f"You have rented {requested_cars} car(s) for {hours} hours.")
        else:
            print("Invalid number of requested cars. Please try again.")

    def rent_daily(self, days, requested_cars):
        if requested_cars > 0 and requested_cars <= self.available_cars:
            print(f"You have rented {requested_cars} car(s) for {days} days.")
        else:
            print("Invalid number of requested cars. Please try again.")

    def rent_weekly(self, weeks, requested_cars):
        if requested_cars > 0 and requested_cars <= self.available_cars:
            print(f"You have rented {requested_cars} car(s) for {weeks} weeks.")
        else:
            print("Invalid number of requested cars. Please try again.")
            
    def calculate_bill(rental_time, rental_mode, num_cars):
        if rental_mode == "hourly":
            rate = 10  
            total_cost = rental_time * rate * num_cars
        elif rental_mode == "daily":
            rate = 50  
            total_cost = rental_time * rate * num_cars
        elif rental_mode == "weekly":
            rate = 200  
            total_cost = rental_time * rate * num_cars
        else:
                return "Invalid rental mode!"
        return total_cost
    
    def return_car(inventory, rental_start_time, rental_end_time, rental_rate):
        # Update inventory stock
        inventory -= 1

        # Calculate rental period
        rental_period = rental_end_time - rental_start_time

        # Generate the final bill
        final_bill = rental_period * rental_rate

        return inventory, rental_period, final_bill        


# In[33]:


class Customer:
    def __init__(self, name):
        self.name = name
        self.rented_cars = []

    def request_car(self, car):
        self.rented_cars.append(car)
        print(f"{self.name} has requested the {car}.")

    def return_car(self, car):
        if car in self.rented_cars:
            self.rented_cars.remove(car)
            print(f"{self.name} has returned the {car}.")
        else:
            print(f"{self.name} did not rent the {car}.")


# In[ ]:




