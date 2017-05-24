#!/usr/bin/python
import matplotlib.pyplot as pl

import numpy as np

allocs = np.genfromtxt('allocs')
pl.hist(allocs, bins=50)
pl.ylabel('Number of nofib modules')
pl.xlabel('% change in compiler allocations')
pl.savefig('allocs.pdf')
pl.savefig('allocs.svg')
