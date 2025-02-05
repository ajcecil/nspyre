def median(data):
    if not data:
        raise ValueError("Dataset cannot be empty")

    sorted_data = sorted(data)  # Sort the dataset
    n = len(sorted_data)
    mid = n // 2  # Find the middle index

    if n % 2 == 0:  # If even, average the two middle values
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:  # If odd, return the middle value
        return sorted_data[mid]

def mean(data):
    total = sum(data)
    n = len(data)
    mean_value =total/n
    
    return mean_value 

def confidence(error_rate):
    # error_rate should be alpoha or beta for type i or type ii    
    coefficient = 1 - error_rate
    
    return coefficient


def fivenum(data):
    # Setting the five number summary variables to be globally accesable
    global q1
    global q2
    global q3
    global minmum
    global maximum
    
    q1_data = [] # dataset which will be used to find the lower quartile
    q3_data = [] # dataset which will be used to find the upper quartile
    
    q2 = median(data) # median of the data
    
    for num in data:
        if num < q2:
            q1_data.append(num)
            
            q1_data = sorted(q1_data)
            
        elif num > q2:
            q3_data.append(num)
            
            q3_data = sorted(q3_data)
    
    q1 = median(q1_data)
    q3 = median(q3_data)
    minmum = min(data)
    maximum = max(data)
    
    
    
    return minmum, q1, q2, q3, maximum

def s_variance(data):
    #set initial variable to be used later in function
    numerator = 0
    n = len(data)
    denominator = n-1
    xbar = mean(data)
    
    for num in data:
        numerator = numerator + ((num + xbar)**2)

    sample_var = numerator/denominator
    
    return sample_var

def stnd_dev(data):
    standard_dev = (s_variance(data)**0.5)
    return standard_dev

def con_int(data, mu):
    xbar = mean(data)
    n = len(data)
    s = stnd_dev(data)
    
    T =  (xbar-mu)/(s/(n ** 0.5))
    
    return T

def solve_mu(data, T):
    xbar = mean(data)
    n = len(data)
    s = stnd_dev(data)
    
    mu_lower = (xbar - (T*(s/(n**0.5))))
    mu_upper = (xbar + (T*(s/(n**0.5))))
    
    return mu_lower, mu_upper

if __name__ == "__main__":
    test_data = [1,2,3,4,5,6,7]
    alpha = 0.05
    
    #region - Testing Median Function
    median_test = median(test_data)
    print("the median of the tested data is: " + str(median_test))
    #endregion
    
    #region = Testing Five Number Sumary Function
    fivenum_test = fivenum(test_data)
    print(f"five number summary of provided dataset: \nMin: {minmum:f}\nQ1: {q1:f}\nMedian: {q2:f}\nQ3: {q3:f}\nMax: {maximum:f}")
    print(fivenum_test)
    #endregion
    
    #region - Testing confidence coeficiant function
    
    con = confidence(alpha)
    con_per = 100*con
    print(f"Coefficient of confidence: {con:f} or {con_per:.1f}%")
    #endregion
    
    #region - Testing Mean Function
    avg = mean(test_data)
    print(f"the mean value for the dataset is: {avg:f}")
    #endregion
    
    #region - Testing Sample Variance Function
    variance = s_variance(test_data)
    print(f"the variance is: {variance:f}")
    #endregion
    
    #region Testing Standard deviation Function
    stndard_dev = stnd_dev(test_data)
    print(f"the standard deviation is: {stndard_dev:f}")
    #endregion
    
    #region - Testing Confidence interval function
    interval = con_int(test_data, 1)
    print(f"the confidence interval is: {interval:f}")
    #endregion
    
    #region - Testing Mu Function
    value = solve_mu(test_data, interval)
    
    print(f"the found mu values are: {value}")