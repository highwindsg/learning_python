#!/usr/bin/env python3

# The line below will import the 'ecommerce' package, which is a subfolder in
# the current working dir and use the 'shipping' module.
from ecommerce.shipping import calc_shipping

# Alternatively, from the ecommerce package, can just import the shipping module.
# So as to allow using all the methods in the shipping module.
from ecommerce import shipping

calc_shipping()
shipping.calc_tax()

