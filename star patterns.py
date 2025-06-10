# -*- coding: utf-8 -*-
"""
Created on Tue May 27 22:29:28 2025

@author: Kshitija
"""

# lower triangle
n = 5
for i in range(1, n + 1):
    print("* " * i)
print()

# upper triangle
rows = 5
for i in range(rows, 0, -1):
    print("* " * i)
print()

# pyramid
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)
