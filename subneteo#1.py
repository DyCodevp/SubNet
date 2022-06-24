
#objetivo crear una aplicacion que me haga el subneteo nadamas pediendome los host

def main(Tipo_de_subneteo):
      #VALIDAMOS LA ENTRADA
      while Tipo_de_subneteo != "a" and Tipo_de_subneteo != "b" and Tipo_de_subneteo != "c":
            print("ingresa un tipo de subneteo valido (a, b , c)")
            Tipo_de_subneteo = input("tipo de subneteo: ") 
            Tipo_de_subneteo = Tipo_de_subneteo.lower()
            print(Tipo_de_subneteo)
            if Tipo_de_subneteo == "no" or Tipo_de_subneteo == "n":
                  break
      if Tipo_de_subneteo == "a" or Tipo_de_subneteo == "b" or Tipo_de_subneteo == "c":
            return Tipo_de_subneteo
def Host(Host):
      #las lans me dan cuantas redes de lan hay y el tamano
      LANS = int(Host)
      hostnames = []
      i = 0
      for i in range(LANS):
            h = int(input("Cuantos host de la lan # "+str(i)+":"))
            hostnames.append(["LAN #"+str(i),(h)])
      print (hostnames)
      return hostnames
def dosAlaN(bitsUsados,host):
      for j in bitsUsados :
            diferenciaDeDos =  j - host
            # print("soy j ",j)
            # print("soy host ",host)
            # print("HOLAAAAA soy la diferencia", diferenciaDeDos)
            if diferenciaDeDos < 2:
                  host+=2
                  # print("soy el host de:",host, "y mi diferencia con este bit es de:",diferenciaDeDos)
                  return host

def subneteoA(Hostnames):
      ipClaseA = input("ingresa la ip con un espacio de por medio:")
# Usamos slit para dividir los octetos y poder trabajar con  el ultimo que Usamos
      ipClaseA = ipClaseA.split(" ")

      MascaraClaseA = input("ingresa la mascara con un espacio de por medio:")
      MascaraClaseA = MascaraClaseA.split(" ")

      cantidadHost = 1
      bitsUsados = [128,64,32,16,8,4,2,1]
            

      for i in range(len(Hostnames)):
            host = Hostnames[i][cantidadHost]
            host = dosAlaN(bitsUsados,host)

            if host < bitsUsados[0] and host > bitsUsados[1] and i == 0:
                  ipClaseA[3] = str(0 + int(ipClaseA[3]))
                  if int(ipClaseA[3]) >=256:
                        ipClaseA[2] = str(1 + int(ipClaseA[2]))
                        ipClaseA[3] = str(0)
                  MascaraClaseA[3] = "128"  
                  LAN = ""
                  LAN += str(Hostnames[i][cantidadHost]) + " IP:" + str(ipClaseA) + " Mascara:" + str(MascaraClaseA)
                  print(LAN)
                  ipClaseA[3] = str(128 + int(ipClaseA[3]))

            if host < bitsUsados[0] and host > bitsUsados[1] and i != 0:
                  if int(ipClaseA[3]) >=256:
                        ipClaseA[2] = str(1 + int(ipClaseA[2]))
                        ipClaseA[3] = str(0)
                  MascaraClaseA[3] = "128"  
                  LAN = ""
                  LAN += str(Hostnames[i][cantidadHost]) + " IP:" + str(ipClaseA) + " Mascara:" + str(MascaraClaseA)
                  print(LAN)
                  ipClaseA[3] = str(128 + int(ipClaseA[3]))

            elif host < bitsUsados[1] and host > bitsUsados[2] :
                  if int(ipClaseA[3]) >=256:
                        ipClaseA[2] = str(1 + int(ipClaseA[2]))
                        ipClaseA[3] = str(0)
                  MascaraClaseA[3] = "192"  
                  LAN = ""
                  LAN += str(Hostnames[i][cantidadHost]) + " IP:" + str(ipClaseA) + " Mascara:" + str(MascaraClaseA)
                  print(LAN)
                  ipClaseA[3] = str(64 + int(ipClaseA[3]))

            elif host < bitsUsados[2] and host > bitsUsados[3] :

                  if int(ipClaseA[3]) >=256:
                        ipClaseA[2] = str(1 + int(ipClaseA[2]))
                        ipClaseA[3] = str(0)
                  MascaraClaseA[3] = "224"  
                  LAN = ""
                  LAN += str(Hostnames[i][cantidadHost]) + " IP:" + str(ipClaseA) + " Mascara:" + str(MascaraClaseA)
                  print(LAN)
                  ipClaseA[3] = str(32 + int(ipClaseA[3]))

            elif host < bitsUsados[3] and host > bitsUsados[4] :
                  if int(ipClaseA[3]) >=256:
                        ipClaseA[2] = str(1 + int(ipClaseA[2]))
                        ipClaseA[3] = str(0)
                  MascaraClaseA[3] = "240"  
                  LAN = ""
                  LAN += str(Hostnames[i][cantidadHost]) + " IP:" + str(ipClaseA) + " Mascara:" + str(MascaraClaseA)
                  print(LAN)
                  ipClaseA[3] = str(16 + int(ipClaseA[3]))

            elif host < bitsUsados[4] and host > bitsUsados[5] :
                  if int(ipClaseA[3]) >=256:
                        ipClaseA[2] = str(1 + int(ipClaseA[2]))
                        ipClaseA[3] = str(0)
                  MascaraClaseA[3] = "248"  
                  LAN = ""
                  LAN += str(Hostnames[i][cantidadHost]) + " IP:" + str(ipClaseA) + " Mascara:" + str(MascaraClaseA)
                  print(LAN)
                  ipClaseA[3] = str(8 + int(ipClaseA[3]))

            elif host <= bitsUsados[5] and host >= bitsUsados[6] :
                  if int(ipClaseA[3]) >=256:
                        ipClaseA[2] = str(1 + int(ipClaseA[2]))
                        ipClaseA[3] = str(0)
                  MascaraClaseA[3] = "252"  
                  LAN = ""
                  LAN += str(Hostnames[i][cantidadHost]) + " IP:" + str(ipClaseA) + " Mascara:" + str(MascaraClaseA)
                  print(LAN)
                  ipClaseA[3] = str(4 + int(ipClaseA[3]))

            elif host < bitsUsados[6] and host > bitsUsados[7] :
                  if int(ipClaseA[3]) >=256:
                        ipClaseA[2] = str(1 + int(ipClaseA[2]))
                        ipClaseA[3] = str(0)
                  MascaraClaseA[3] = "254"  
                  LAN = ""
                  LAN += str(Hostnames[i][cantidadHost]) + " IP:" + str(ipClaseA) + " Mascara:" + str(MascaraClaseA)
                  print(LAN)
                  ipClaseA[3] = str(2 + int(ipClaseA[3]))

            elif host < bitsUsados[7] :
                  if int(ipClaseA[3]) >=256:
                        ipClaseA[2] = str(1 + int(ipClaseA[2]))
                        ipClaseA[3] = str(0)
                  MascaraClaseA[3] = "255"  
                  LAN = ""
                  LAN += str(Hostnames[i][cantidadHost]) + " IP:" + str(ipClaseA) + " Mascara:" + str(MascaraClaseA)
                  print(LAN)
                  ipClaseA[3] = str(1 + int(ipClaseA[3]))


tipo_subneteo = main(input("dime el tipo de subneteo: "))
hostnames = Host(input("dime la cantidad de LAN:"))
if tipo_subneteo == "a" or tipo_subneteo == "A":
      subneteoA(hostnames)
