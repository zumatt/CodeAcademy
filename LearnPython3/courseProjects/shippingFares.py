weight = 5 #Expressed in lb

#Flat carge variables
flatCharge_Ground = 20
flatCharge_GroundPremium = 125
flatCharge_Drone = 0
#Shipping cost variables
shippingCostGround = 0
shippingCostDrone = 0

#Ground shipping
if weight <= 2:
  shippingCostGround += flatCharge_Ground
  shippingCostGround += 1.50 * weight
  print("The ground shipping is:", shippingCostGround, "$")
elif (weight > 2) and (weight <= 6):
  shippingCostGround += flatCharge_Ground
  shippingCostGround += 3.00 * weight
  print("The ground shipping is:", shippingCostGround, "$")
elif (weight > 6) and (weight <= 10):
  shippingCostGround += flatCharge_Ground
  shippingCostGround += 4.00 * weight
  print("The ground shipping is:", shippingCostGround, "$")
elif weight > 10:
  shippingCostGround += flatCharge_Ground
  shippingCostGround += 4.75 * weight
  print("The ground shipping is:", shippingCostGround, "$")
else:
  print("Error")

#Ground shipping premium
print("The ground shipping premium is:", flatCharge_GroundPremium, "$")

#Drone Shipping
if weight <= 2:
  shippingCostDrone += flatCharge_Drone
  shippingCostDrone += 4.50 * weight
  print("The drone shipping is:", shippingCostDrone, "$")
elif (weight > 2) and (weight <= 6):
  shippingCostDrone += flatCharge_Drone
  shippingCostDrone += 9.00 * weight
  print("The drone shipping is:", shippingCostDrone, "$")
elif (weight > 6) and (weight <= 10):
  shippingCostDrone += flatCharge_Drone
  shippingCostDrone += 12.00 * weight
  print("The drone shipping is:", shippingCostDrone, "$")
elif weight > 10:
  shippingCostDrone += flatCharge_Drone
  shippingCostDrone += 14.25 * weight
  print("The drone shipping is:", shippingCostDrone, "$")
else:
  print("Error")

#Check the cheapest method
print("\nThe best option to ship is:")
if (shippingCostGround < flatCharge_GroundPremium) or (shippingCostDrone < flatCharge_GroundPremium):
  if (shippingCostGround < shippingCostDrone):
    print("Ground shipping for:", shippingCostGround, "$")
  if (shippingCostGround > shippingCostDrone):
    print("Drone shipping for:", shippingCostDrone, "$")
else:
  print("Ground shipping premium for:", flatCharge_GroundPremium, "$")

