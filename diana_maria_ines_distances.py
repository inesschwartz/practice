`import random
import math
import matplotlib.pyplot as plt

# Constants for the region of interest (ROI)
lat_min = 38.7
lat_max = 38.78
lon_min = -9.2
lon_max = -9.1
coef_lat = 111120
coef_lon = 86672

def main():
    N = get_integer("Number of points: ", 2, 10)
    option = get_string("User provided (u) or random (r): ", ["u", "r"])
    
    # Create a dictionary of coordinates
    d = get_coordinates(N, option) #this is the dictionary
    
    # Determine the pair of points farthest apart
    max_dist = 0
    for name_1, P1 in d.items():
        for name_2, P2 in d.items():
            dist = compute_distance(P1, P2)
            if dist >= max_dist:
                max_dist = dist
                point_1, point_2 = name_1, name_2
    
    print(f"{point_1} and {point_2} are farthest apart")
    plot_scatter(d)

def plot_scatter(points: dict):
    x_vals = [point[0] for point in points.values()]
    y_vals = [point[1] for point in points.values()]
    plt.scatter(x_vals, y_vals)
    plt.xlabel('Lon')
    plt.ylabel('Lat')
    plt.title('Scatter Plot of Points')
    
    for label, point in points.items():
        plt.annotate(label, point, textcoords='offset points', xytext=(0, 10))
    
    plt.grid(True)
    plt.show()

def get_decimal(prompt: str, Min: float, Max: float) -> float:
    while True:
        try:
            x = float(input(prompt)) #makes it a decimal value
            if Min <= x <= Max:
                return x
            else:
                print(f"Value must be between {Min} and {Max}.")
        except ValueError:
            print("Invalid input. Please enter a decimal number.")

def get_integer(prompt: str, Min: int, Max: int) -> int:
    while True:
        try:
            x = int(input(prompt))
            if Min <= x <= Max:
                return x
            else:
                print(f"Value must be between {Min} and {Max}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_string(prompt: str, L: list) -> str:
    while True:
        x = input(prompt)
        if x in L: #makes sure we are pulling from list string
            return x
        else:
            print(f"Invalid input. Please enter one of {L}.")

def get_coordinates(N: int, option: str) -> dict:
    d = dict() #sets up our dictionary
    if option == 'u': #explains which values we will be pulling from d
        for i in range(N):
            name = input(f"Name for point {i + 1}: ")
            lon = get_decimal("Longitude: ", lon_min, lon_max)
            lat = get_decimal("Latitude: ", lat_min, lat_max)
            d[name] = (lon, lat) #[name] will call for lon and lat values that must be inside our given min and max
    elif option == 'r':
        for i in range(N):
            name = input(f"Name for point {i + 1}: ")
            lon = random.uniform(lon_min, lon_max)
            lat = random.uniform(lat_min, lat_max)
            d[name] = (lon, lat)
    return d

def compute_distance(P1: tuple, P2: tuple) -> float:
    # Input tuples
    lon1, lat1 = P1
    lon2, lat2 = P2

    # Calculate the difference in latitude and longitude
    lat_diff = lat2 - lat1
    lon_diff = lon2 - lon1

    # Calculate the approximate distance using the conversion factors
    distance = math.sqrt(((lat_diff * coef_lat) ** 2) + ((lon_diff * coef_lon) ** 2))

    return distance  # returns the calculated distance

main()