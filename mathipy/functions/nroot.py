import numpy as np
from mathipy.math import _math, calculus


class NRoot(calculus.Function):
    """
    f(x) = a * root_n(kx + p) + b
    """
    
    function_type = 'Nth Root'

    def __init__(self, n: int = 2, **kwargs):
        self.a: float = kwargs.get('a', 1)
        self.n = n
        self.k: float = kwargs.get('k', 1)
        self.p: float = kwargs.get('p', 0)
        self.b: float = kwargs.get('b', 0)

        if n == 0:
            raise ValueError('Root index cannot be 0')

    def get_yint(self) -> float:
        return self(0)

    def find_roots(self):
        r = ((-self.b / self.a) ** self.n - self.p) / self.k
        return r if self(r) == 0 else np.nan

    def calculate_values(self, x):
        return self.a * _math.root_n((self.k * x + self.p), self.n, return_complex=False) + self.b

    def __call__(self, x):
        return self.calculate_values(x)

    def plot_func(self, ax):
        ax.scatter(0, self.get_yint(), color=calculus.Function.function_part['y-intercept'])
        ax.scatter(self.find_roots(), 0, color=calculus.Function.function_part['roots'])

    def __str__(self):
        representation = ''
        if self.a != 1:
            representation += f'{self.a} · '
        if self.n != 2:
            representation += f'Root{self.n}('
        else:
            representation += 'Sqrt('
        if self.k != 1:
            representation += f'{self.k}x'
        else:
            representation += 'x'
        if self.p != 0:
            representation += f' + {self.p})'
        else:
            representation += f')'
        if self.b != 0:
            representation += f' + {self.b}'
        return representation
