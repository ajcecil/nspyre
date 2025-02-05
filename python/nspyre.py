class statistics:
    
    def median(self, data):
        if not data:
            raise ValueError("Dataset cannot be empty")

        sorted_data = sorted(data)  # Sort the dataset
        n = len(sorted_data)
        mid = n // 2  # Find the middle index

        if n % 2 == 0:  # If even, average the two middle values
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:  # If odd, return the middle value
            return sorted_data[mid]

    def mean(self, data):
        total = sum(data)
        n = len(data)
        mean_value = total / n
        return mean_value 

    def confidence(self, error_rate):
        # error_rate should be alpha or beta for type I or type II    
        coefficient = 1 - error_rate
        return coefficient

    def fivenum(self, data):
        # Compute the five-number summary without using global variables
        q1_data = []  # Dataset for lower quartile
        q3_data = []  # Dataset for upper quartile

        q2 = self.median(data)  # Median of the data

        for num in data:
            if num < q2:
                q1_data.append(num)
            elif num > q2:
                q3_data.append(num)

        q1_data = sorted(q1_data)
        q3_data = sorted(q3_data)

        q1 = self.median(q1_data)
        q3 = self.median(q3_data)
        minimum = min(data)
        maximum = max(data)

        return minimum, q1, q2, q3, maximum

    def s_variance(self, data):
        # Set initial variable to be used later in the function
        numerator = 0
        n = len(data)
        denominator = n - 1
        xbar = self.mean(data)

        for num in data:
            numerator += (num - xbar) ** 2  # Corrected the formula

        sample_var = numerator / denominator
        return sample_var

    def stnd_dev(self, data):
        standard_dev = self.s_variance(data) ** 0.5
        return standard_dev

    def con_int(self, data, mu):
        xbar = self.mean(data)
        n = len(data)
        s = self.stnd_dev(data)

        T = (xbar - mu) / (s / (n ** 0.5))
        return T

    def solve_mu(self, data, T):
        xbar = self.mean(data)
        n = len(data)
        s = self.stnd_dev(data)

        mu_lower = (xbar - (T * (s / (n ** 0.5))))
        mu_upper = (xbar + (T * (s / (n ** 0.5))))

        return mu_lower, mu_upper


# Test Script
if __name__ == "__main__":
    #region - Test Statistics Class
    # Initialize the Statistics object
    stats = statistics()

    # Test data and alpha
    test_data = [1, 2, 3, 4, 5, 6, 7]
    alpha = 0.05
    
    # Test Median Function
    median_test = stats.median(test_data)
    print(f"The median of the tested data is: {median_test}")

    # Test Five Number Summary Function
    minmum, q1, q2, q3, maximum = stats.fivenum(test_data)
    print(f"Five number summary of provided dataset:\nMin: {minmum:f}\nQ1: {q1:f}\nMedian: {q2:f}\nQ3: {q3:f}\nMax: {maximum:f}")

    # Test Confidence Coefficient Function
    con = stats.confidence(alpha)
    con_per = 100 * con
    print(f"Coefficient of confidence: {con:f} or {con_per:.1f}%")

    # Test Mean Function
    avg = stats.mean(test_data)
    print(f"The mean value for the dataset is: {avg:f}")

    # Test Sample Variance Function
    variance = stats.s_variance(test_data)
    print(f"The variance is: {variance:f}")

    # Test Standard Deviation Function
    stnd_dev = stats.stnd_dev(test_data)
    print(f"The standard deviation is: {stnd_dev:f}")

    # Test Confidence Interval Function
    interval = stats.con_int(test_data, 1)
    print(f"The confidence interval is: {interval:f}")

    # Test Mu Function
    value = stats.solve_mu(test_data, interval)
    print(f"The found mu values are: {value}")
    #endregion