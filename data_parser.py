class DataParser:
    @staticmethod
    def parse(response, fields):
        
        data = []
        city = response['location']['name']
        data.append(city)

        current = response['current']


        for field in fields:
            data.append(current[field])
        
        return data

