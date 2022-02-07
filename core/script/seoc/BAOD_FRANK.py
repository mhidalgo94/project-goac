from numpy import cos, pi, rad2deg, arccos, log, exp
from datetime import date
p0=1013.25 #Presion de atmosfera standard nivel del mar (mbar)
p = 1013.25 #Presion en la Estacion CMW (mbar)
q = 1-p/p0 #Para Calculo de coeficientes
uns = 0.0002
u0 = 0.35 # Concentracion de Ozono troposferico en Unidades Dobson/1000
unt = 0.01
w = 1 # Contenido integral de vapor de agua en cm
Ebn=1000.0 # Irradiancia Directa (S) debe multiplicarse por el coseno angulo cenital
czsa = 0.07 # Coseno del angulo cenital

# Calculo de la irradiancia extraterrestre
djul=date.toordinal(date(2021,4,18))-date.toordinal(date(2021-1,12,31))
Eo=1+0.033*cos((2*pi*djul)/365)
E0n=1367*Eo*czsa
Z=rad2deg(arccos(czsa))
fraccion=E0n/Ebn


# czsa es el coseno del angulo cenital que esta en el csv
Z = rad2deg(arccos(czsa))
mr=(czsa+(0.45665*Z**0.007)*(96.4836-Z)**-1.6970)**-1
mw=(czsa+(0.031141*Z**0.1)*(92.4710-Z)**-1.3814)**-1
ma=mw
mnt=mw



####################################################################
# Clean Atmosphere (dc)%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
## Coeficientes para funciones param deltac Apendice Gueymard98 pag(432) 
a0 = 1-0.98173*q
a1 = 0.18164-0.24259*q+0.050739*(q**2)
a2 = 0.18164-0.17005*q-0.0084949*(q**2)
b0 = -0.0080617+0.028303*u0-0.014055*(u0**2)
b1 = 0.011318-0.041018*u0+0.023471*(u0**2)
b2 = -0.0044577+0.016728*u0-0.01091*(u0**2)
c0 = 0.0036916+0.047361*u0+0.0058324*(u0**2)
c1 = 0.015471+0.061662*u0-0.044022*(u0**2)
c2 = 0.039904-0.038633*u0+0.054899*(u0**2)
### funciones param deltac Apendice Gueymard98 pag(432) 
f1 = (a0+a1*mr)/(1+a2*mr)
f2 = b0+b1*(mr**0.25)+b2*log(mr)
f3 = (0.19758+0.00088585*mr-0.097557*(mr**0.2))/(1+0.0044767*mr)
f4 = (c0+c1*(mr**-0.72))/(exp(1+c2*mr))
f5 = uns*(2.8669-0.078633*(log(mr)**(2.36)))
dc = f1*(f2+f3)+f4+f5  #Gueymard98 eq(9) parametrizacion de deltac (espesor optico de clean atmosfera) a partir de ajustes con calculos realizados con SMARTS2
# Water vapor (dw)%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
### Coeficientes para funciones param deltaw Apendice Gueymard98 pag(432 y 433) 
M = (1.7135+0.10004*mw+0.00053986*(mw**2))/(1.7149+0.097294*mw+0.002567*(mw**2))
v1 = 3.3704+6.8096*q
v2 = (12.487-18.517*q-0.4089*(q**2))/(1-1.4104*q)
v3 = (2.5024-0.56834*q-1.4623*(q**2))/(1-1.0252*q)
v4 = (-0.030833-1.172*q-0.98878*(q**2))/(1+31.546*q)
kap1 = (-0.1857+0.23871*q)/(1-0.84111*q)
kap2 = (-0.022344-0.19312*q)/(1+6.2169*q)
kap3 = (2.1709+1.6423*q)/(1+0.062545*q)
fi1 = (0.63889-0.81121*q)*(1-0.79988*q)
fi2 = (0.06836+0.49008*q)/(1+4.7234*q)
fi3 = (2.1567+1.4546*q)/(1+0.038808*q)
gamma1 = (1.728-2.1451*q)/(1-0.96212*q)
gamma2 = (0.37042+0.64537*q)/(1+0.94528*q)
gamma3 = (3.5145-0.12483*q)/(1-0.34018*q)
### funciones param deltaw Apendice Gueymard98 pag(432) 
g1 = (gamma1*w+gamma2*w**1.6)/(1+gamma3*w)
g2 = (fi1*w+fi2*w**1.6)/(1+fi3*w)
g3 = (kap1*w+kap2*w**1.6)/(1+kap3*w)
g4 = (v1*w+v2*w**0.62)/(1+v3*w+v4*w**2)   #ok Revisar esta elevado a la 2
dw = M*(g1+g2*M*mw+g3*(M*mw)**1.28)/(1+g4*M*mw)
## Nitrogen Dioxide (dnt) %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

dnt = unt*(2.8669-0.078633*(log(mnt))**2.36)    #Gueymard98 eq(11) deltant espesor optico de dioxido de nitrogeno
# Broadband Aerosol Optical Depth (da)
da = (1/ma)*(log(fraccion)-mr*dc)-dw-dnt   #Con NO2 Gueymard98 eq(15) y eq(7)
da2 = (1/ma)*(log(E0n/Ebn)-mr*dc)-dw  #Sin NO2 Gueymard98 eq(15) y eq(7) 

# Hallando radiacion directa sin el efecto de los aerosoles
Ebn2=E0n*exp(-mr*dc-mw*dw-mnt*dnt)
print(dc)
print(dw)
print(dnt)
print(da)
print(da2)
print(Ebn2)
