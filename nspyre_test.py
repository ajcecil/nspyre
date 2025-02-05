from nspyre import statistics

test_data = [1,2,3,4,5,6,7]
alpha = 0.05

median_test = median(test_data)
print("median: ")
print(median_test)

fivenum_test = fivenum(test_data)
print("fivenum:")
print(fivenum_test)

con = confidence(alpha)
con_per = 100*con
print("confidence: ")
print(con)
print("confidence percentage: ")

avg = mean(test_data)
print("mean: ")
print(avg)

variance = s_variance(test_data)
print("variance: ") 
print(variance)

stndard_dev = stnd_dev(test_data)
print("standard deviation: ")
print(stndard_dev)

interval = con_int(test_data, 1)
print("confidence interval: ")
print(interval)

value = solve_mu(test_data, interval)

print("the found mu values are: ")
print(value)