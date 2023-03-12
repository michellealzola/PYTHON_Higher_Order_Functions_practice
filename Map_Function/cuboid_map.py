# 10.3	Write a function that takes a list of cuboid dimensions
# (length, width, height) and returns a list of their corresponding volumes.

def volume(cuboid_list):
    return list(map(lambda x: x[0] * x[1] * x[2], cuboid_list))


def main():
    cuboid_list = [(2, 4, 6), (3, 5, 7), (4, 6, 8), (5, 7, 9), (6, 8, 10)]
    volume_list = volume(cuboid_list)
    print(volume_list)


if __name__ == "__main__":
    main()
