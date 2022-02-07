from numpy import cos, rad2deg, arccos, pi, exp, log
from datetime import date


class Datos(object):
    def __init__(self):
        # Ozono troposferico en la Unidades Dobson/1000
        # Este diccionario contiene el ozono de todas las estaciones.
        self.lista_ozono_mensual = {
            'D':[0,0.2489,0.2567,0.2682,0.286,0.2948,0.2946,0.2947,0.2891,0.2812,0.2692,0.2563,0.2512],
            'T': [0,2.7182883022,2.6788544517,2.7478835443,3.0067272416,3.7875280252,4.5679266477,4.4271210532,4.5779973813,4.7153723054,4.2477100549,3.4334583002,2.9474559955],
            'J':[0,2.7285765051,2.7040952932,2.7593758516,3.0110972459,3.8038418204,4.6704633926,4.5720337453,4.7223263778,4.8287837094,4.2717533711,3.4169055998,2.9551016587],
            'F':[0,2.9002286741,2.8180043844,2.8103021414,3.0668935298,3.8495531559,4.707173691,4.56022434,4.7313450018,4.9070830471,4.3941650681,3.5642087163,3.1324790762]
            }
        # Contenido integral de vapor de agua 12 meses
        self.lista_vapor_agua_mensual = [0,2.7554,2.7121,2.578,3.1423,3.4297,4.2935,4.112,4.3119,4.4321,4.1999,3.197,2.8124] 

class SEOC(Datos):
    
    # def __init__(self,**kwargs):
    def __init__(self, estacion = None,fecha= None, presion_estacion = None, presion_admosferica= None, czsa = None, nubosidad = None, iDirecta = None, dSolar= None):
        super().__init__()
        '''
        Esta son las condiciones obligatorias para que se deben insertar
        en la clase para el calculo general, donde debe incluir 
        (estacion, fecha, presion estacion, presion admosferica, nubosidad total ,
        coseno angulo cenital, disco solar, irradance directa ) para poder lograr los calculos correspondientes
        donde se pide estacion para poder seleccionar el ozono mensual que no es igual en cada estacion
        la fecha corresponde en la que esta en el csv para hacer el calculo dependiendo el mes y tambien sacar
        el dia juliano
        '''
        if estacion == None:
            raise Exception('No ha ingresado la Estacion (variable es estacion = [D,F,T,J] dependiendo la estacion)')
        elif estacion not in self.lista_ozono_mensual.keys():
            raise Exception('Esta estacion no esta registrada ingrese la estacion valida (estacion = [D,F,T,J])')
        elif fecha == None:
            raise Exception('No ha ingresado la Fecha (variable es fecha -  formato: %Y%m%d)')
        elif presion_estacion == None:
            raise Exception('No ha ingresado la Presion de la Estacion (variable es presion_estacion)')
        elif presion_admosferica == None:
            raise Exception('No ha ingresado la Presion Admosferica (variable es presion_admosferica)')
        elif czsa == None:
            raise Exception('No ha ingresado el Coseno del Angulo Cenital (variable es czsa)')
        elif nubosidad == None:
            raise Exception('No ha ingresado la Nubosidad (variable es nubosidad)')
        elif iDirecta == None:
            raise Exception('No ha ingresado la Irradiancia Directa (variable es iDirecta)')
        elif dSolar == None:
            raise Exception('No ha ingresado el Disco Solar (variable es dSolar 0/4)')

        '''
        Se requiere que ingrese el mes asi se escoge el valor de la lista 
        de ozono y de vapor de agua mensual
        '''
        if "/" in fecha:
            fecha = fecha.replace("/","")
            self.dd, self.mm, self.yyyy = int(fecha[0:2]), int(fecha[2:4]), int(fecha[4:8])

        elif "-" in fecha:
            fecha = fecha.replace("-", "")
            self.dd, self.mm, self.yyyy = int(fecha[0:2]), int(fecha[2:4]), int(fecha[4:8])
        else:
            self.yyyy = int(fecha[0:4]) # Optener anio de var fecha
            self.mm = int(fecha[4:6])   # Optener mes de var fecha
            self.dd = int(fecha[6:8])   # Optener dia de var fecha

        '''
        En estas dos varibales se selecciona el ozono mensual y el vapor de agua mensual
        correspondiente al mes que corresponde en la fecha actual
        '''            
        self.u0 = self.lista_ozono_mensual[estacion][self.mm] # Seleccionar Ozono de la estacion por el valor del mes 
        self.w = self.lista_vapor_agua_mensual[self.mm]  # Seleccionar vapor de agua por mes

        '''
        Ingresando los datos de presion admosferica 
        y la presion de la estacion
        '''
        self.p0 = presion_admosferica
        self.p = presion_estacion

        self.q = 1-self.p/self.p0 #Para Calculo de coeficientes
        self.uns = 0.000204 # NO2 Estratosferico
        self.unt = 0.00034012 # NO2 Troposferico 
        self.czsa = czsa # czsa es el coseno del angulo cenital que esta en el csv

        self.Ebn= iDirecta # Irradiancia Directa (S) debe multiplicarse por el coseno angulo cenital

        # Calculo de la irradiancia extraterrestre
        self.djul=date.toordinal(date(self.yyyy,self.mm,self.dd))-date.toordinal(date(self.yyyy-1,12,31))
        self.Eo=1+0.033*cos((2*pi*self.djul)/365)
        self.E0n=1367*self.Eo*self.czsa
        self.Z=rad2deg(arccos(self.czsa))

        self.fraccion= self.E0n/self.Ebn

        self.mr=(self.czsa+(0.45665*self.Z**0.007)*(96.4836-self.Z)**-1.6970)**-1
        self.mw=(self.czsa+(0.031141*self.Z**0.1)*(92.4710-self.Z)**-1.3814)**-1
        self.ma=self.mw
        self.mnt=self.mw

        self.EOA = -999
        self.EOAN = -999

        if iDirecta == 0 or iDirecta == -999:
            self.dc = -999
            self.dw = -999
            self.dnt = -999
            self.EOA = -999
            self.EOAN = -999
        else:
            ####################################################################
            # Clean Atmosphere (dc)%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            ## Coeficientes para funciones param deltac Apendice Gueymard98 pag(432) 
            a0 = 1-0.98173*self.q
            a1 = 0.18164-0.24259*self.q+0.050739*(self.q**2)
            a2 = 0.18164-0.17005*self.q-0.0084949*(self.q**2)
            b0 = -0.0080617+0.028303*self.u0-0.014055*(self.u0**2)
            b1 = 0.011318-0.041018*self.u0+0.023471*(self.u0**2)
            b2 = -0.0044577+0.016728*self.u0-0.01091*(self.u0**2)
            c0 = 0.0036916+0.047361*self.u0+0.0058324*(self.u0**2)
            c1 = 0.015471+0.061662*self.u0-0.044022*(self.u0**2)
            c2 = 0.039904-0.038633*self.u0+0.054899*(self.u0**2)
            ### funciones param deltac Apendice Gueymard98 pag(432) 
            f1 = (a0+a1*self.mr)/(1+a2*self.mr)
            f2 = b0+b1*(self.mr**0.25)+b2*log(self.mr)
            f3 = (0.19758+0.00088585*self.mr-0.097557*(self.mr**0.2))/(1+0.0044767*self.mr)
            f4 = (c0+c1*(self.mr**-0.72))/(exp(1+c2*self.mr))
            f5 = self.uns*(2.8669-0.078633*(log(self.mr)**(2.36)))
            self.dc = f1*(f2+f3)+f4+f5  #Gueymard98 eq(9) parametrizacion de deltac (espesor optico de clean atmosfera) a partir de ajustes con calculos realizados con SMARTS2
            # Water vapor (dw)%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            ### Coeficientes para funciones param deltaw Apendice Gueymard98 pag(432 y 433) 
            M = (1.7135+0.10004*self.mw+0.00053986*(self.mw**2))/(1.7149+0.097294*self.mw+0.002567*(self.mw**2))
            v1 = 3.3704+6.8096*self.q
            v2 = (12.487-18.517*self.q-0.4089*(self.q**2))/(1-1.4104*self.q)
            v3 = (2.5024-0.56834*self.q-1.4623*(self.q**2))/(1-1.0252*self.q)
            v4 = (-0.030833-1.172*self.q-0.98878*(self.q**2))/(1+31.546*self.q)
            kap1 = (-0.1857+0.23871*self.q)/(1-0.84111*self.q)
            kap2 = (-0.022344-0.19312*self.q)/(1+6.2169*self.q)
            kap3 = (2.1709+1.6423*self.q)/(1+0.062545*self.q)
            fi1 = (0.63889-0.81121*self.q)*(1-0.79988*self.q)
            fi2 = (0.06836+0.49008*self.q)/(1+4.7234*self.q)
            fi3 = (2.1567+1.4546*self.q)/(1+0.038808*self.q)
            gamma1 = (1.728-2.1451*self.q)/(1-0.96212*self.q)
            gamma2 = (0.37042+0.64537*self.q)/(1+0.94528*self.q)
            gamma3 = (3.5145-0.12483*self.q)/(1-0.34018*self.q)
            ### funciones param deltaw Apendice Gueymard98 pag(432) 
            g1 = (gamma1*self.w+gamma2*self.w**1.6)/(1+gamma3*self.w)
            g2 = (fi1*self.w+fi2*self.w**1.6)/(1+fi3*self.w)
            g3 = (kap1*self.w+kap2*self.w**1.6)/(1+kap3*self.w)
            g4 = (v1*self.w+v2*self.w**0.62)/(1+v3*self.w+v4*self.w**2)   #ok Revisar esta elevado a la 2
            self.dw = M*(g1+g2*M*self.mw+g3*(M*self.mw)**1.28)/(1+g4*M*self.mw)
            ## Nitrogen Dioxide (dnt) %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

            self.dnt = self.unt*(2.8669-0.078633*(log(self.mnt))**2.36)    #Gueymard98 eq(11) deltant espesor optico de dioxido de nitrogeno
            # Broadband Aerosol Optical Depth (da)
            self.da = (1/self.ma)*(log(self.fraccion)-self.mr*self.dc)-self.dw-self.dnt   #Con NO2 Gueymard98 eq(15) y eq(7)
            self.da2 = (1/self.ma)*(log(self.E0n/self.Ebn)-self.mr*self.dc)-self.dw  #Sin NO2 Gueymard98 eq(15) y eq(7) 

            # Hallando radiacion directa sin el efecto de los aerosoles
            self.Ebn2=self.E0n*exp(-self.mr*self.dc-self.mw*self.dw-self.mnt*self.dnt)


    
        
    def values(self):
        data = dict()
        data['presion_admosferica'] = self.p0
        data['presion_estacion'] = self.p
        data['coeficientes'] = self.q
        data['uns'] = self.uns
        data['unt'] = self.unt
        data['u0'] = self.u0
        data['w'] = self.w
        data['Ebn'] = self.Ebn
        data['E0n'] = self.E0n
        data['fraccion'] = self.fraccion
        data['mr'] = self.mr
        data['ma']= self.ma
        data['mw']= self.mw
        data['mnt']= self.mnt

        return data

    def get_ozono_mensual(self):
        return self.lista_ozono_mensual

    def get_vapor_agua(self):
        return self.lista_vapor_agua_mensual

    def get_data(self):
        data = dict()
        data['dc'] = self.dc
        data['dw'] = self.dw
        data['dnt'] = self.dnt
        data['da'] = self.da
        data['da2'] = self.da2
        data['Ebn2'] = self.Ebn2
        return data



obj = SEOC(presion_estacion=1008.9, fecha = '2021-05-11', presion_admosferica=1013.25, )
# obj = obj.get_data()

# print(obj)
print([obj.get_dc(),obj.get_dw(), obj.get_dnt(), obj.get_da(), obj.get_da2(), obj.get_Ebn2() ])

