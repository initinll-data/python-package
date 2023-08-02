# pick specific object from module
from ecommerce.shopping.sales import calc_tax, calc_shipping

# pick any object from module
from ecommerce.shopping import sales

calc_tax()
calc_shipping()

sales.calc_tax()
sales.calc_shipping()
