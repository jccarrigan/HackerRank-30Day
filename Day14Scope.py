        self.maximumDifference = 0
    def computeDifference(self):
        for i in range(len(self.__elements)):
            for j in self.__elements[i:]:
                if abs(j-self.__elements[i]) > self.maximumDifference:
                    self.maximumDifference = abs(j-self.__elements[i])
