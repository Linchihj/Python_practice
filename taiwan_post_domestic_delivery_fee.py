# weight variables
import sys

weight = int(input("Enter package weight in kilograms:"))
weight_delivery_cost = ""

# weight conditions

if weight <= 5:
    weight_delivery_cost = 100
elif weight <= 10:
    weight_delivery_cost = 125
elif weight <= 15:
    weight_delivery_cost = 150
elif weight <= 20:
    weight_delivery_cost = 180
else:
   print("Error. Your package exceeds the weight that can delivered through Taiwan postal service.")
   sys.exit()

print("Delivery cost by weight (NT$):", weight_delivery_cost)

# size variables
height = int(input("Enter package height in centimeters:"))
width = int(input("Enter package width in centimeters:"))
length = int(input("Enter package length in centimeters:"))
size = height + width + length
size_delivery_cost = ""

# size conditions
if size <= 60:
   size_delivery_cost = 100
elif size <= 90:
   size_delivery_cost = 125
elif size <= size <= 120:
   size_delivery_cost = 150
elif size <= 150:
   size_delivery_cost = 180
else:
    print ("Error. Your package exceeds the size that can be delivered through Taiwan postal service.")
    sys.exit()
print ("Delivery cost by size (NT$):", size_delivery_cost)

Total_cost= print ("Total delivery cost (NT$):", weight_delivery_cost + size_delivery_cost)
