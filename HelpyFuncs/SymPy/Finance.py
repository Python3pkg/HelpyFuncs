import sympy
from . import sympy_vector_sum_elems


def pv(amount=0., discount_rate=0., nb_periods=0):
    return amount / (discount_rate ** nb_periods)


def npv(cash_flows=sympy.Matrix([0.]), discount_rate=0.):
    m, n = cash_flows.shape
    if m == 1:
        discount_vector = sympy.Matrix([[discount_rate ** -i for i in range(n)]])
    elif n == 1:
        discount_vector = sympy.Matrix([discount_rate ** -i for i in range(m)])
    return sympy_vector_sum_elems(discount_vector.multiply_elementwise(cash_flows))
