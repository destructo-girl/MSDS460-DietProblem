## Implementing solution in python - Part 3

import pandas as pd
from pulp import *

# Create the 'prob' variable to contain the problem data
prob = LpProblem("Diet_Problem", LpMinimize)


# declaring decision variables
cc        = LpVariable("cottageCheese",0,cat='Continuous')
chocolate = LpVariable("chocolate",0,cat='Continuous')
tuna      = LpVariable("tuna", 0,cat='Continuous')
banana    = LpVariable("banana", 0,cat='Continuous')
beans     = LpVariable("beans", 0,cat='Continuous')


# defining constraints
prob += 320*cc + 0*chocolate   + 380*tuna + 1*banana   + 410*beans <= 2300           # Sodium
prob += 110*cc + 170*chocolate + 230*tuna + 105*banana + 130*beans <= 1225           # Energy
prob += 12*cc  + 2*chocolate   + 29*tuna  + 1.3*banana + 8*beans   >= 122            # Protein
prob += 5*cc   + 15*chocolate  + 13*tuna  + 0.4*banana + 0.5*beans <= 41             # Fats
prob += 5*cc   + 14*chocolate  + 0*tuna   + 27*banana  + 23*beans  <= 92             # Carbs
prob += 75*cc  + 200*chocolate + 150*tuna + 422*banana + 550*beans >= 2600           # Potassium
prob += 0*cc   + 3*chocolate   + 0*tuna   + 3.1*banana + 6*beans   >= 25             # Fiber


# defining objective function coefficients to maximize 
price_cc = 2.99
price_chocolate = 5.99
price_tuna = 2.99
price_banana = 0.25
price_beans = 1.59

serving_cc = 4
serving_chocolate = 3.5
serving_tuna = 1
serving_banana = 1
serving_beans = 3.5

# Price per serving
coef_cc = price_cc / serving_cc
coef_chocolate = price_chocolate / serving_chocolate
coef_tuna = price_tuna / serving_tuna
coef_banana = price_banana / serving_banana
coef_beans = price_beans / serving_beans

# Objective function
prob  += coef_cc*cc + coef_chocolate*chocolate + coef_tuna*tuna + coef_banana*banana + coef_beans*beans 

status = prob.solve()  # Solver
LpStatus[status];     # The solution status

# Printing solution
print('PuLp Solutions for cottageCheese, chocolate, tuna, pb, and beans are: ')
print(value(cc), value(chocolate), value(tuna), value(banana), value(beans))
print('The Minimize cost is ', coef_cc*value(cc) + coef_chocolate*value(chocolate) + coef_tuna*value(tuna) + coef_banana*value(banana) + coef_beans*value(beans))

# Printing to how nutrition is met
print("Sodium, max 2300: ", 320*value(cc) + 0*value(chocolate) + 380*value(tuna) + 1*value(banana) + 410*value(beans))
print("Calories, max 1225: ", 110*value(cc) + 170*value(chocolate) + 230*value(tuna) + 105*value(banana) + 130*value(beans))
print("Protein, min 122: ", 12*value(cc)  + 2*value(chocolate)   + 29*value(tuna)  + 1.3*value(banana) + 8*value(beans))
print("Fats, max 41: ", 5*value(cc)   + 15*value(chocolate)  + 13*value(tuna)  + 0.4*value(banana) + 0.5*value(beans))
print("Carbs, max 92: ", 5*value(cc)   + 14*value(chocolate)  + 0*value(tuna)   + 27*value(banana)  + 23*value(beans))
print("Potassium, min 2600: ", 75*value(cc)  + 200*value(chocolate) + 150*value(tuna) + 422*value(banana) + 550*value(beans))
print("Fiber, min 25: ", 0*value(cc)   + 3*value(chocolate)   + 0*value(tuna)   + 3.1*value(banana) + 6*value(beans))


## Adding new nutritional constraints - Part 5

# Create the 'prob' variable to contain the problem data
prob2 = LpProblem("Diet_Problem_Extra", LpMinimize)

# declaring decision variables
cc      = LpVariable("cottageCheese",0,cat='Continuous')
chocolate = LpVariable("chocolate",0,cat='Continuous')
tuna      = LpVariable("tuna", 0,cat='Continuous')
banana        = LpVariable("banana", 0,cat='Continuous')
beans     = LpVariable("beans", 0,cat='Continuous')


# defining constraints
prob2 += 320*cc + 0*chocolate   + 380*tuna      + 1*banana         + 410*beans <= 2300           # Sodium
prob2 += 110*cc + 170*chocolate + 230*tuna      + 105*banana       + 130*beans <= 1225           # Energy
prob2 += 12*cc  + 2*chocolate   + 29*tuna       + 1.3*banana       + 8*beans   >= 122            # Protein
prob2 += 5*cc   + 15*chocolate  + 13*tuna       + 0.4*banana       + 0.5*beans <= 41             # Fats
prob2 += 5*cc   + 14*chocolate  + 0*tuna        + 27*banana        + 23*beans  <= 92             # Carbs
prob2 += 75*cc  + 200*chocolate + 150*tuna      + 422*banana       + 550*beans >= 2600           # Potassium
prob2 += 0*cc   + 3*chocolate   + 0*tuna        + 3.1*banana       + 6*beans   >= 25             # Fiber
prob2 += 0*cc   + 0*chocolate   + (0.9)*14*tuna + (0.05)*14*banana + 0*beans   >= 14             # NEW - Niacin (Vitamin B3)
prob2 += 0*cc   + 0*chocolate   + (0.8)*2.4*tuna        + 0*banana + 0*beans   >= 2.4            # NEW - Vitamin B12

# defining objective function coefficients to maximize 
price_cc = 2.99
price_chocolate = 5.99
price_tuna = 2.99
price_banana = 0.25
price_beans = 1.59

serving_cc = 4
serving_chocolate = 3.5
serving_tuna = 1
serving_banana = 1
serving_beans = 3.5

# Price per serving
coef_cc = price_cc / serving_cc
coef_chocolate = price_chocolate / serving_chocolate
coef_tuna = price_tuna / serving_tuna
coef_banana = price_banana / serving_banana
coef_beans = price_beans / serving_beans

# Objective function
prob2  += coef_cc*cc + coef_chocolate*chocolate + coef_tuna*tuna + coef_banana*banana + coef_beans*beans 


status2 = prob2.solve()  # Solver
LpStatus[status2];     # The solution status


# Printing solution
print('PuLp Solutions for cottageCheese, chocolate, tuna, pb, and beans are: ')
print(value(cc), value(chocolate), value(tuna), value(banana), value(beans))
print('The Minimize cost is ', coef_cc*value(cc) + coef_chocolate*value(chocolate) + coef_tuna*value(tuna) + coef_banana*value(banana) + coef_beans*value(beans))


print("Sodium, max 2300: ", 320*value(cc) + 0*value(chocolate) + 380*value(tuna) + 1*value(banana) + 410*value(beans))
print("Calories, max 1225: ", 110*value(cc) + 170*value(chocolate) + 230*value(tuna) + 105*value(banana) + 130*value(beans))
print("Protein, min 122: ", 12*value(cc)  + 2*value(chocolate)   + 29*value(tuna)  + 1.3*value(banana) + 8*value(beans))
print("Fats, max 41: ", 5*value(cc)   + 15*value(chocolate)  + 13*value(tuna)  + 0.4*value(banana) + 0.5*value(beans))
print("Carbs, max 92: ", 5*value(cc)   + 14*value(chocolate)  + 0*value(tuna)   + 27*value(banana)  + 23*value(beans))
print("Potassium, min 2600: ", 75*value(cc)  + 200*value(chocolate) + 150*value(tuna) + 422*value(banana) + 550*value(beans))
print("Fiber, min 25: ", 0*value(cc)   + 3*value(chocolate)   + 0*value(tuna)   + 3.1*value(banana) + 6*value(beans))
print("Niacin, min 14: ", (0.9)*14*value(tuna)   + (0.05)*14*value(banana))
print("B12, min 2.4: ", (0.8)*2.4*value(tuna))
