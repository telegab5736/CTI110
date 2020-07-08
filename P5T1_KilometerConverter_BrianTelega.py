#Kilometer Conversion Calculator
#8JULY2020
#CTI-110 P5T1_KilometerConverter 
#Brian Telega


CONVERSION_FACTOR = 0.6214

#Ask user for input in kilometers and calls the show_miles function to convert it.
def main():
    kilometers = float(input('Enter a distance in kilometers:'))
#Display distance in miles
    show_miles(kilometers)
    


#Convert miles to kilometers
#Show_miles function converts the parameter km from kilometers to miles and display results.
def show_miles(km):
    miles = km * CONVERSION_FACTOR

#Display miles.
    print(km,'kilometers equals', miles, 'miles.')
    
#Call the main function.   
main()
