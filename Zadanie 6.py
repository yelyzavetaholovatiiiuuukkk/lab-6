import math
import keyword

# Funkcje z modułu math
print("Funkcje w module math:")
print([name for name in dir(math) if callable(getattr(math, name))])

# Funkcje z modułu tuple 
print("\nFunkcje w module tuple:")
print([name for name in dir(tuple) if callable(getattr(tuple, name))])

# Funkcje z modułu keyword
print("\nFunkcje w module keyword:")
print([name for name in dir(keyword) if callable(getattr(keyword, name))])
