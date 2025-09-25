#	Using Python, compute the Z-transform of the sequence x[n]=3^n u[n].
import sympy as sp
n,z,a = sp.symbols('n z 3')
x_n = 3 ** n
X_z = sp.summation(x_n*z**(-n),(n,0,sp.oo))
print("z-transform of x[n] = 3^n u[n]:")
sp.pprint(X_z, use_unicode = True)