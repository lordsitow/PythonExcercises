ciag_we=input('Proszę podać ciąg znaków')
ciag_wy=''
j=0
ile_pod_rzad=0
dlugosc_ciagu_we=0
for p in ciag_we:
    dlugosc_ciagu_we+=1

for i in ciag_we:
    if j == 0:
        j+=1
        continue
    ile_pod_rzad+=1
    if ciag_we[j]==ciag_we[j-1]:
        b=1
    else:
        ciag_wy+=ciag_we[j-1]
        ciag_wy+=str(ile_pod_rzad)
        ile_pod_rzad=0
    j+=1
    if j==dlugosc_ciagu_we:
        ciag_wy+=ciag_we[j-1]
        ciag_wy+=str(ile_pod_rzad+1)

print(ciag_wy)
