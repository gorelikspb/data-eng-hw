import csv


class DataWriter:
    @staticmethod
    def write2csv(filepath, headers, data):
        with open (filepath, 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter = ';')

            csv_writer.writerow(headers)
            csv_writer.writerows(data)

