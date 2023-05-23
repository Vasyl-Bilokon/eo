import numpy as np

class BackpackTask:

    def __init__(self):

        # initialize instance variables:
        self.items = []
        self.maxCapacity = 0

        # initialize the data:
        self.__initData()

    def __len__(self):
        """
        :return: the total number of items defined in the problem
        """
        return len(self.items)

    def __initData(self):
        """initializes the RosettaCode.org knapsack 0-1 problem data
        """
        self.items = [
            ("Map", 9, 150),
            ("Compass", 13, 35),
            ("Water", 153, 200),
            ("Sandwich", 50, 160),
            ("Glucose", 15, 60),
            ("Mug", 68, 45),
            ("Banana", 27, 60),
            ("Apple", 39, 40),
            ("Cheese", 23, 30),
            ("Beer", 52, 10),
            ("Sunscreen cream", 11, 70),
            ("Camera", 32, 30),
            ("T-shirt", 24, 15),
            ("Trousers", 48, 10),
            ("Umbrella", 73, 40),
            ("Waterproof trousers", 42, 70),
            ("Waterproof raincoat", 43, 75),
            ("Тote-case", 22, 80),
            ("Sunglasses", 7, 20),
            ("Towel", 18, 12),
            ("Socks", 4, 50),
            ("Book", 30, 10)
        ]

        self.maxCapacity = 400

    def getValue(self, zeroOneList):
        """
        Calculates the value of the selected items in the list, while ignoring items that will cause the accumulating weight to exceed the maximum weight
        :param zeroOneList: a list of 0/1 values corresponding to the list of the problem's items. '1' means that item was selected.
        :return: the calculated value
        """

        totalWeight = totalValue = 0

        for i in range(len(zeroOneList)):
            item, weight, value = self.items[i]
            if totalWeight + weight <= self.maxCapacity:
                totalWeight += zeroOneList[i] * weight
                totalValue += zeroOneList[i] * value
        return totalValue

    def printItems(self, zeroOneList):
        """
        Prints the selected items in the list, while ignoring items that will cause the accumulating weight to exceed the maximum weight
        :param zeroOneList: a list of 0/1 values corresponding to the list of the problem's items. '1' means that item was selected.
        """
        totalWeight = totalValue = 0

        for i in range(len(zeroOneList)):
            item, weight, value = self.items[i]
            if totalWeight + weight <= self.maxCapacity:
                if zeroOneList[i] > 0:
                    totalWeight += weight
                    totalValue += value
                    print("- Adding {}: weight = {}, value = {}, accumulated weight = {}, accumulated value = {}".format(item, weight, value, totalWeight, totalValue))
        print("- Total weight = {}, Total value = {}".format(totalWeight, totalValue))


# testing the class:
def main():
    # create a problem instance:
    knapsack = BackpackTask()

    # creaete a random solution and evaluate it:
    randomSolution = np.random.randint(2, size=len(knapsack))
    print("Random Solution = ")
    print(randomSolution)
    knapsack.printItems(randomSolution)


if __name__ == "__main__":
    main()
