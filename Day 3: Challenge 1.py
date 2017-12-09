a = input()
i = 1
layers = 1
while(i**2 < a):
    layers += 1
    i += 2
# Here, layers represents the number of complete spins that have been made before finally reaching the layer that has the input in it. Knowing the layer allows us to quickly get rid of the large part of the calculation, and focus on the specific location of the number in the spiral instead. Calculation works on the basis that every number to the bottom right corner of each layer is the square of the next odd number (1,9,25,49..). 

# Now, layers gives us the specific spiral, so we know we will have to take *atleast* that many steps, if it is perfectly north, south, east, or west of 1. If it deviates from the perfect cardinal directions, then we will have to move to the closest one, and then walk exactly 'layers' number of steps. 

eastExtreme = ((i-2)**2)+(layers-1)
northExtreme = eastExtreme + (i-1)
westExtreme = northExtreme + (i-1)
southExtreme = westExtreme + (i-1)

eastDiff = abs(eastExtreme - a) - 1
northDiff = abs(northExtreme - a) - 1
westDiff = abs(westExtreme - a) - 1
southDiff = abs(southExtreme - a) - 1

print min(eastDiff, northDiff, westDiff, southDiff)+layers , eastExtreme, northExtreme, westExtreme, southExtreme, layers

