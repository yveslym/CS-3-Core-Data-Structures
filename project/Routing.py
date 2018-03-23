import time

class Routing:

    def __init__(self, cost_file, number_file=None):
        self.pricing = self.read_cost_file(cost_file)
        self.phone_nums = {}
        if number_file is not None:
            self.phone_nums = self.read_number_file(number_file)


    def read_cost_file(self, file_name):
        opened_file = open('{}'.format(file_name))
        file_lines = opened_file.read().splitlines()
        pricing = {}

        for line in file_lines:
            split = line.split(',')
            pricing[split[0]] = split[1]
        return pricing


    def cenario(self,number):
        """Cenario 1 retrieve best cost over 100 000 """
        listNumber = list(number)
        splitNumber = str(number)
        print(splitNumber)
        file = "data/route-costs-4.txt"

        cost = self.pricing
        print(cost)

        for x in range(0, len(listNumber)):
            if splitNumber in cost:
                return cost[splitNumber]
            else:
                splitNumber = splitNumber[:-1]
                print(splitNumber)
        return None

if __name__ == "__main__":
    route = Routing("data/route-costs-4.txt")
    number = '+1415654'
    price = route.cenario(number)
    print(price)
