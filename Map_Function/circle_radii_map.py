# Write a function that takes a list of circle radii
# as input and returns a list of their corresponding areas.
import math

def area(radius_list):
    return list(map(lambda x: round((math.pi * x ** 2), 2), radius_list))
def main():
    circle_values = [2, 4, 6, 8, 10]
    circle_areas = area(circle_values)
    print(circle_areas)


if __name__ == '__main__':
    main()



