# Importing the Libraries
import math

# Defining a Gaussian Distribution:
def get_norm_dist_func(x, mu, sigma):
    return (1/math.sqrt(2*math.pi*sigma*sigma))*math.exp((-1/(2*sigma*sigma))* (x-mu)*(x-mu))
