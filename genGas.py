import random
import csv

random.seed(1)


def main():
    with open('gasValues.csv', 'w', newline='') as file:
        fieldnames = ['latitude', 'longitude', 'intensity']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for x in range(10000):
            #lat = random.randrange(-90, 90)
            lat = random.random()
            lat = format((lat * 180.00) - 90, "0.5f")
            #lon = random.randrange(-180, 180)
            lon = random.random()
            lon = format((lon * 360.00) - 180, "0.5f")
            #intensity = random.randrange(0, 100)
            intensity = random.random()
            intensity = format((intensity * 100.00), "0.5f")
            writer.writerow({'latitude': str(lat), 'longitude': str(lon), 'intensity': str(intensity)})


if __name__ == "__main__":
    main()