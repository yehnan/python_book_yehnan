

stock = {
    'Apple': 655.95, 'IBM': 202.13, 'HP': 45.51, 'Facebook': 12.11,
    'Intel': 40.51, 'Atmel': 10.23, 'Amazon': 305.35, 'Google': 535.81
}

stock_new0 = {}
for k, v in stock.items():
    if v >= 100:
        stock_new0[k] = v
        
print(stock_new0)


stock_new1 = {k: v for k, v in stock.items() if v >= 100}
        
print(stock_new1)


