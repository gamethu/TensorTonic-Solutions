def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    res = x0
    for i in range(steps):
        grads = 2*a*x0 + b
        
        x0  = x0 - lr*grads
        res = x0
    return res