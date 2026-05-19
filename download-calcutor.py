tamMB = float(input('tamanho do arquivo (MB): \t\t(obs, MB -> GB = GB x 1024)'))
vel = float(input('\nvelocidade da internet (Mbps):'))

tamMb = tamMB * 8 
tempo_s = tamMb / vel 

horas = int(tempo_s // 3600)
minutos = int((tempo_s % 3600) // 60)
segundos = int(tempo_s % 60)


print(f'\ntempo de download: {horas} hora(s), {minutos} minuto(s), {segundos} segundo(s)')



