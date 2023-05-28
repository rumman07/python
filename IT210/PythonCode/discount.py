#computer bookstore kilobyte day example.

originalPrice = float(input("Please enter thr price: "))

#dicounted rates
if originalPrice < 128:
    discountRate = 0.92
else:
    discountRate = 0.84
discountedPrice = discountRate * originalPrice
print("Price $%.2f" % discountedPrice)

    
