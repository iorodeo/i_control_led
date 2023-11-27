import numpy as np

# Get approximate values
r1 = 10.0
r2 = 24000.0
curr = 0.024


vcc = 10.0
tol = 0.01
digits2 = 2
digits3 = 2

Vset = curr*r1
r3 = r2*(Vset/vcc)/(1 - Vset/vcc)

print()
print('initial component estimates')
print('---------------------------')
print(f'vcc      = {vcc} (V)')
print(f'Vset     = {Vset} (V)')
print(f'curr     = {curr} (A)')
print(f'tol      = {tol}')
print()
print(f'r1       = {r1} (Ohm)')
print(f'r2       = {r2} (Ohm)')
print(f'r3       = {r3} (Ohm)')
print()

# Actual components - round to neared see how much tol matters
n2 = int(np.floor(np.log10(r2))) - (digits2-1) 
r2 = round(r2,-n2)
n3 = int(np.floor(np.log10(r3))) - (digits3-1)
r3 = round(r3,-n3)

r2_vals = r2 + np.array([-1.0, 1.0])*tol*r2
r3_vals = r3 + np.array([-1.0, 1.0])*tol*r3
vset_vals = []
for r2_w_err in r2_vals:
    for r3_w_err in r3_vals:
        vset = vcc*r3_w_err/(r2_w_err + r3_w_err)
        vset_vals.append(vset)

print('rounded values with error')
print('-------------------------')
print(f'r2       = {r2} (Ohm)')
print(f'r3       = {r3} (Ohm)')
print(f'min Vset = {min(vset_vals)}')
print(f'max Vset = {max(vset_vals)}')







