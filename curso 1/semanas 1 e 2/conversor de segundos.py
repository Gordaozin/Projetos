segundos = int(input("Por favor, entre com o número de segundos que deseja converter:\n"))

anos = segundos // (12*(30*(3600*24)))
segundos_restantes_anos = segundos % (12*(30*(3600*24)))
meses = segundos_restantes_anos // (30*(3600*24))
segundos_restantes_meses = segundos_restantes_anos % (30*(3600*24))
dia = segundos_restantes_meses // (3600*24)
segundos_restantes_dia = segundos_restantes_meses % (3600*24)
horas =  segundos_restantes_dia // 3600
segundos_restantes = segundos % 3600
minutos = segundos_restantes // 60
segundos_rest_final = segundos_restantes % 60

print(anos,"anos",meses,'meses',dia,'dias,',horas,'horas,',minutos,'minutos e',segundos_rest_final,'segundos.')
