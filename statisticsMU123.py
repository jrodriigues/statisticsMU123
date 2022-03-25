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

            if decimal_places > dp:
                if number_list[dp_index + dp + 1] >= 5:
                    number_list[dp_index + dp] += 1

                del number_list[dp_index + dp + 1:]

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

    def __str__(self):
        """Returns a formatted string of the object's attributes."""

        return f"Mean - {self.mean}\nMedian - {self.median}\nRange - {self.range}\nMin - {self.min}\nMax - {self.max}\nQ1 - {self.Q1}\nQ3 - {self.Q3}\nIQR - {self.iqr}\nSize - {self.size}"
   
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

    def get_mean(self):
        """Returns the mean of the dataset"""
  
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
