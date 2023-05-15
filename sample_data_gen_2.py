import csv
import random

class DummyDataGenerator:
    def __init__(self):
        self.num_entries = 5000

    def generate_dummy_data(self):
        latitude = random.uniform(34.16, 34.20)
        longitude = random.uniform(-118.49, -118.43)
        zip_code = random.randint(91401, 91410)
        distance_to_airport = round(random.uniform(0, 10), 2)
        noise_level = round(random.uniform(0, 100), 2)
        convenience_score = round(random.uniform(0, 5), 2)
        employment_opportunities = round(random.uniform(0, 10), 2)
        air_quality_index = round(random.uniform(0, 100), 2)
        average_height_commercial = round(random.uniform(1, 10), 2)
        average_height_residential = round(random.uniform(1, 10), 2)
        housing_price = random.randint(100000, 500000)

        return [latitude, longitude, zip_code, distance_to_airport, noise_level,
                convenience_score, employment_opportunities, air_quality_index,
                average_height_commercial, average_height_residential, housing_price]

    def generate_sample_data(self):
        for _ in range(self.num_entries):
            data = self.generate_dummy_data()
            yield data

    def generate_sample_csv(self, file_path):
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Latitude', 'Longitude', 'Zip_Code', 'Distance_to_airport',
                             'Noise_level', 'Convenience_score', 'Employment_opportunities',
                             'Air_quality_index', 'Average_height_commercial',
                             'Average_height_residential', 'Housing_price'])

            for data in self.generate_sample_data():
                writer.writerow(data)

        print(f"Sample CSV file generated with {self.num_entries} entries: {file_path}")

# Create an instance of the DummyDataGenerator class
generator = DummyDataGenerator()

# Generate the sample CSV file
generator.generate_sample_csv('sample_data.csv')
