import numpy as np
import pandas as pd


def encode_cyclical(x, max_x):
    sin = np.sin(2 * np.pi * x / max_x)
    cos = np.cos(2 * np.pi * x / max_x)
    return sin, cos


def encode_hour(x):
    return encode_cyclical(x, 24)


def encode_day(x):
    return encode_cyclical(x, 31)


def encode_month(x):
    return encode_cyclical(x, 12)


def encode_second(x):
    x_hour = (x / (60 * 60)) % 24
    return encode_hour(x_hour)


def rand_times(n):
    """Generate n rows of random 24-hour, 12-month and 31-days"""
    rand_hours = np.random.randint(0, 24, n)
    rand_days = np.random.randint(1, 31, n)
    rand_months = np.random.randint(1, 12, n)

    return pd.DataFrame(data=dict(hours=rand_hours, days=rand_days, months=rand_months))
