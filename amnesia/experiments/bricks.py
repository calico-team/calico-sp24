"""Calculate the prices of bronze, silver, and gold bricks

This for prototyping an earlier version of this problem but is no longer used.

Sources:
https://757brick.com/blog/a-guide-to-brick-shapes-and-sizes/
https://www.livecharts.co.uk/MarketCharts/bronze.php
https://www.livecharts.co.uk/MarketCharts/silver.php
https://www.livecharts.co.uk/MarketCharts/gold.php
https://www.thomasnet.com/articles/metals-metal-products/bronze-vs-brass-what-s-the-difference/
https://en.wikipedia.org/wiki/Silver
https://en.wikipedia.org/wiki/Gold
"""

BRICK_VOLUME_IN3 = (3 + 5/8) * (2 + 1/4) * (7 + 5/8)

class Metal:
    def __init__(self, price_usd_oz, density_g_cm3):
        self.price_usd_oz = price_usd_oz
        self.density_g_cm3 = density_g_cm3
    
    def brick_price(self):
        volume_cm3 = BRICK_VOLUME_IN3 * 16.3871
        mass_g = volume_cm3 * self.density_g_cm3
        mass_oz = mass_g / 28.35
        price = mass_oz * self.price_usd_oz
        return price

gold = Metal(2322.66, 19.3)
silver = Metal(27.265, 10.49)
bronze = Metal(0.16, 8.8)

print('Gold', gold.brick_price())
print('Silver', silver.brick_price())
print('Bronze', bronze.brick_price())
