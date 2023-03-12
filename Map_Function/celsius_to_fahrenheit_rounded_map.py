# Use map and lambda to convert a list of Celsius temperatures
# to Fahrenheit temperatures,
# and round the result to two decimal places.
# °F = (°C × 9/5) + 32

def main():
    celsius_list = [25.5, 18.7, 31.2, 27.9, 36.1, 22.3, 40.0, 20.6]
    fahrenheit_list = map(lambda x: round((x * (9 / 5) + 32), 2), celsius_list)
    print(f'{list(fahrenheit_list)}')


if __name__ == '__main__':
    main()
