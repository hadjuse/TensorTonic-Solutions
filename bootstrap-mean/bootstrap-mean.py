import numpy as np

def bootstrap_mean(x: list, n_bootstrap: int = 1000, ci: float = 0.95, seed: int = 0) -> dict:
    """
    Returns a dictionary with bootstrap_mean, lower, and upper.
    """
    # Write code here
    x=np.asarray(x)
    rng = np.random.default_rng(seed)
    index_matrix =  rng.integers(0, x.size, size=(n_bootstrap, x.size))
    print(index_matrix[:10])
        # index_line = index_matrix[i]
    bootstrap_mean = x[index_matrix].mean(axis=1)

    alpha = 1 - ci
    inf_born = alpha / 2
    born_sup = 1 - (alpha / 2)
    lower = np.quantile(bootstrap_mean, inf_born)
    upper = np.quantile(bootstrap_mean, born_sup)
    # percentile_quart = np.percentile(bootstrap_mean, 0.25)
    # print("percentile", percentile)
    # percentile_third_quart = np.percentile(bootstrap_mean)
    return { "bootstrap_mean": bootstrap_mean.mean(), "lower": lower, "upper": upper }