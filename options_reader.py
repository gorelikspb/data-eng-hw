import yaml

class OptionsReader:
    @staticmethod
    def read_cities(filepath):
        with open (filepath, 'r') as file:
            options = yaml.load(file, Loader=yaml.FullLoader)
            return (options['cities'])

if __name__ == "__main__":
    print(OptionsReader.read_cities('cities.yaml'))