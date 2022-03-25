from statistics import variance
from math import sqrt


def rounding(number, dp=2):
        """Returns the input chosen decimal places. Default = 2"""

        number_str = str(number)
        number_list = []
        rnded_number = ""
        
        # creates a list where all the values are the input number as integers, for easy maneuverability.
        for value in number_str:
            if value != '.':
                number_list.append(int(value))
            else:
                number_list.append(value)

        # means it's a whole number
        if '.' not in number_list:
            return number
            
        else:
            dp_index = number_list.index('.')

            # gives the number of decimal places of the original number. 
            # If < required dp, returns the original number.    
            decimal_places = len(number_list) - (dp_index + 1)

            # General condition when rounding does not involve changing the left integer of the .
            if decimal_places > dp and dp >= 2:
                if number_list[dp_index + dp + 1] >= 5:

                    # Rounding from 09 to 10
                    if number_list[dp_index + dp] == 9:
                        number_list[dp_index + dp] = 0
                        number_list[dp_index + dp - 1] += 1

                    else:
                        number_list[dp_index + dp] += 1

                del number_list[dp_index + dp + 1:]

                for value in number_list:
                    rnded_number += str(value)

                rnded_number = float(rnded_number)
                return rnded_number

            # Next two elif conditions are specially for when rounding invloves changing the left integer of the . 

            elif decimal_places > dp and dp == 0:
                if number_list[dp_index + 1] >= 5:
                    number_list[dp_index + 1] = 0
                    number_list[dp_index - 1] += 1
                
                del number_list[dp_index:]

                for value in number_list:
                    rnded_number += str(value)

                rnded_number = int(rnded_number)
                return rnded_number
            
            elif decimal_places > dp and dp == 1:
                if number_list[dp_index + dp] >= 5:
                    number_list[dp_index + 1] = 0
                    number_list[dp_index - 1] += 1
                
                del number_list[dp_index + dp:]

                for value in number_list:
                    rnded_number += str(value)

                rnded_number = float(rnded_number)
                return rnded_number

            else:
                return number

class Dataset:
    """Class that will provide methods to calculate the location and spread of datasets"""

    def __init__(self, data, dp=2):
        self.data = data
        self.data_sorted = sorted(data)
        self.mean = rounding(self.get_mean(), dp)
        self.median = self.get_median()
        self.range = self.get_range()
        self.iqr = rounding(self.get_iqr(), dp)
        self.Q1 = rounding(self.get_Q1(), dp)
        self.Q3 = rounding(self.get_Q3(), dp)
        self.max = self.get_max()
        self.min = self.get_min()
        self.size = self.get_size()
        self.sd = rounding(self.get_sd(), dp)

    def __str__(self):
        """Returns a formatted string of the object's attributes."""

        return (f"Mean - {self.mean}\n"
                f"Median - {self.median}\n"
                f"Range - {self.range}\n"
                f"Min - {self.min}\n"
                f"Max - {self.max}\n"
                f"Q1 - {self.Q1}\n"
                f"Q3 - {self.Q3}\n"
                f"IQR - {self.iqr}\n"
                f"SD - {self.sd}\n"
                f"Size - {self.size}")
   
    def _check_if_even(self, *arg):
        """Checks if a list has got even or odd total numbers. Returns True if EVEN"""

        if len(arg) % 2 == 0:
            return True
        elif len(arg) % 2 == 1:
            return False

    def get_min(self):
        """Return the minimun value of the dataset"""
        
        return self.data_sorted[0]

    def get_max(self):
        """Returns the maximum value of the dataset""" 

        return self.data_sorted[-1]

    def get_size(self):
        """Returns the size of the dataset"""

        return len(self.data)

    def get_mean(self, *arg):
        """Returns the mean of the dataset"""

        if arg:
            total_sum = 0

            for value in arg:
                total_sum += value 

            mean = total_sum / len(arg)
            return mean
        
        else:
            total_sum = sum(self.data)
            mean = total_sum / len(self.data)
            return mean

    def get_median(self, *data):
        """Returns the mean of the dataset"""

        # Required when calculating the quartiles
        if data:
            if not self._check_if_even(*data):
                return data[int(len(data) / 2)]

            else:
                mean_of_middle_values = (data[int(len(data) / 2)] + data[int(len(data) / 2 -1)]) / 2
                return mean_of_middle_values
        
        # Calculating the input median
        else:
            if not self._check_if_even(*self.data_sorted):
                return self.data_sorted[int(len(self.data_sorted) / 2)]

            else:
                mean_of_middle_values = (self.data_sorted[int(len(self.data_sorted) / 2)] + self.data_sorted[int(len(self.data_sorted) / 2 -1)]) / 2
                return mean_of_middle_values

    def get_range(self):
        """Returns range of dataset"""

        rnge =  self.data_sorted[-1] - self.data_sorted[0]
        return rnge
    
    def get_Q1(self):
        """Returns the first quartile. If odd, it will automatically remove the median, because of the slice with int()"""

        first_half = self.data_sorted[:int(len(self.data_sorted) / 2)]

        # Calculate the median for the unpacked half
        first_quartile = self.get_median(*first_half)
        return first_quartile
    
    def get_Q3(self):
        """Returns the third quartile"""

        if self._check_if_even(*self.data_sorted):
            second_half = self.data_sorted[int(len(self.data_sorted) / 2):]

            # Calculate the median for the unpacked half
            second_quartile = self.get_median(*second_half)
            return second_quartile
        
        elif not self._check_if_even(self.data):
            second_half = self.data_sorted[int(len(self.data_sorted) / 2) + 1:]

            # Calculate the median for the unpacked halves
            second_quartile = self.get_median(*second_half)
            return second_quartile

    def get_iqr(self):
        """Returns IQR of dataset"""

        iqr = self.get_Q3() - self.get_Q1()
        return iqr

    def get_sd(self):
        """Returns the Standard Deviation (SD) of the dataset"""

        deviations = []
        squared_deviations = []

        # Subtract the mean to each value of the dataset
        for value in self.data_sorted:
            deviations.append(value - self.mean)
        
        # Square the deviations
        [squared_deviations.append(value ** 2) for value in deviations]

        # Get the mean of the squared deviations to find the variance
        variance = self.get_mean(*squared_deviations)

        # The SD will be the square root of the variance
        sd = sqrt(variance)

        return sd
