if __name__ == '__main__':
    car_mpg = float(input())
    gas_price = float(input())

def driving_cost(driven_miles, miles_per_gallon, dollars_per_gallon):
    '''
    10 (miles driven) / 20 (mpg) = 0.5
    0.5 (miles / mpg) * 3.1599 (fuel cost) = 1.58
    '''
    drange = driven_miles / miles_per_gallon
    cost_per_mile = drange * dollars_per_gallon
    return(cost_per_mile)

for miles in [10, 50, 400]:
    print('{:.2f}'.format(driving_cost(miles, car_mpg, gas_price)))

