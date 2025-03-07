from .calc import DESCRIPTION as calc_description
from .calc import generate_round as brain_calc
from .even import DESCRIPTION as even_description
from .even import generate_round as brain_even
from .gcd import DESCRIPTION as gcd_description
from .gcd import generate_round as brain_gcd
from .prime import DESCRIPTION as prime_description
from .prime import generate_round as brain_prime
from .progression import DESCRIPTION as prog_description
from .progression import generate_round as brain_progression

__all__ = [
    'brain_calc', 'calc_description',
    'brain_even', 'even_description',
    'brain_gcd', 'gcd_description',
    'brain_prime', 'prime_description',
    'brain_progression', 'prog_description',
]