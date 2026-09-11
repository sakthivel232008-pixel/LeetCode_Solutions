class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        arr = []
        kelvin = celsius + 273.15
        fahreneit = celsius * 1.80 + 32.00
        arr.append(kelvin)
        arr.append(fahreneit)
        return arr
    