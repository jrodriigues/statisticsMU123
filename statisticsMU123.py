class Dataset:
    """Class that will provide methods to calculate the location and spread of datasets"""

    def __init__(self, data):
        self.data = data
        self.data_sorted = sorted(data)
        self.mean = self.get_mean()
        self.median = self.get_median()
        self.range = self.get_range()
        self.iqr = self.get_iqr()
        self.Q1 = self.get_Q1()
        self.Q3 = self.get_Q3()

    def __str__(self):
        """Returns a formatted string of the object's attributes."""

        return f"Mean - {self.mean}\nMedian - {self.median}\nRange - {self.range}\nQ1 - {self.Q1}\nQ3 - {self.Q3}\nIQR - {self.iqr}"
 
    def _check_if_even(self, *arg):
        """Checks if a list has got even or odd total numbers. Returns True if EVEN"""

        if len(arg) % 2 == 0:
            return True
        elif len(arg) % 2 == 1:
            return False

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
