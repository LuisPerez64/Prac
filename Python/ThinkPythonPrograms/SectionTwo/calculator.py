# Sphere calculation algorithm point
def volumeOfASphere (inputRadius):
    PI = 3.14
    sphereVolume = (4/3) * PI * inputRadius ** 3
    return str(sphereVolume)
    
inputRadius = 5

print "Volume of a sphere with " + str(inputRadius) + " for it's radius is " + volumeOfASphere(inputRadius)  

# Book discount point
def bookPrice(discountRate, initialPricePoint, totalBooks):
    totalPrice = 0
    discountedPricePoint = discountRate * initialPricePoint
    if totalBooks >= 1:
        totalBooks -= 1 # First book is made at the full price.
        totalPrice += discountedPricePoint + 3.00 # The 3 for the     
    totalPrice += (discountedPricePoint + 0.75) * totalBooks
    return str(totalPrice)

print bookPrice(.60, 24.95, 30) 
print totalPrice
#
