import math


def convert_secant_di_to_nominal(secant_di, b_factor):
    """ Converts secant decline rate which most people assume 
        for decline rates to nominal for decline curve equations
        
"""

    nominal_di = (((1 - secant_di) ** (-b_factor)) - 1) / b_factor

    return nominal_di


def hyp_decline_rate_q(qi, b_factor, nominal_di, delta_time):
    """Returns production rate at time t for hyperbolic decline"""

    q_delta_time = qi / ((1 + b_factor * nominal_di * delta_time) ** (1 / b_factor))

    return q_delta_time


def exp_decline_rate_q(qi, nominal_di, delta_time):
    """Returns production rate at time t for exponential decline"""

    q_delta_time = qi * math.exp(-(nominal_di * delta_time))

    return q_delta_time


def ann_to_monthly_disc_rate(annual_disc_rate):
    """ Given discount rate returns effective monthly discount rate

        Example: convert 10% annual, ann_to_monthly_disc_rate(0.10)
    """

    monthly_disc_rate = ((1 + annual_disc_rate) ** (1 / 12)) - 1

    return monthly_disc_rate


def irr(values: list, monthly=False) -> float:
    """ Given values returns annual IRR to 1% accuracy,
        assuming one negative cashflow beginning which should yield one solution for IRR

        Defaults to annual input values, set monthly=True for monthly values

        IRR returned as float, ex: 10% IRR returned as 0.10

    """

    if sum(values) <= 0:
        return 0

    irr = 0
    npv_rate = 1

    npv_rates = []

    while npv_rate > 0 and irr < 101:

        irr += 1
        npv_values = []

        for time, value in enumerate(values):
            npv_value = (value) / ((1 + (irr / 100)) ** time)
            npv_values.append(npv_value)

        npv_rate = sum(npv_values)
        npv_rates.append(npv_rate)

    if monthly:
        return ((1 + (irr / 100)) ** 12) - 1
    else:
        return irr / 100
