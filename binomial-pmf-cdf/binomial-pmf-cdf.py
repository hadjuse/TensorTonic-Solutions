import math

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here
    binomial = (math.factorial(n) / (math.factorial(k) * math.factorial(n-k)))
    
    pmf = binomial * math.pow(p, k) * math.pow(1-p, n-k)
    cdf = 0

    for i in range(k+1):
        binomial_ctf = (math.factorial(n) / (math.factorial(i) * math.factorial(n-i)))
        cdf += binomial_ctf * math.pow(p, i) * math.pow(1-p, n-i)
    print(cdf)

    return {"pmf": pmf, "cdf": cdf}