# Use map and lambda to convert a list of Celsius
# temperatures to Fahrenheit temperatures.
# °F = (°C × 9/5) + 32

def main():
    celsius_list = [25.5, 18.7, 31.2, 27.9, 36.1, 22.3, 40.0, 20.6]
    fahrenheit_list = map(lambda x: x * (9 / 5) + 32, celsius_list)
    print(f'{list(fahrenheit_list)}')


if __name__ == '__main__':
    main()
