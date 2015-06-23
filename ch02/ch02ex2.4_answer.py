

# Celsius to Fahrenheit
def ctof(temp):
    return temp * 9.0 / 5.0 + 32

# Fahrenheit to Celsius
def ftoc(temp):
    return (temp - 32) * 5.0 / 9.0


if __name__ == '__main__':
    # simple tests
    if ctof(0) - 32 >= 0.0001: 
        print('Failed: 0 C should be 32 F')
    if ctof(100) - 212 >= 0.0001: 
        print('Failed: 100 C should be 212 F')
    
    if ftoc(32) - 0 >= 0.0001: 
        print('Failed: 32 F should be 0 C')
    if ftoc(212) - 100 >= 0.0001: 
        print('Failed: 212 F should be 100 C')

