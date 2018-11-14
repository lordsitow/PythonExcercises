ciag_bin = '11111111111001111001010000001111000000001111111100000001111111000000000111111110000'

def bin_comp(ciag_we):
    ciag_wy=[]
    dlugosc_caigu=len(ciag_we)
    ilosc_powtu=1
    i=0
    for x in ciag_we:
        if i==0:
            i+=1
        elif i==dlugosc_caigu-1:
            if ciag_we[i]==ciag_we[i-1]:
                ciag_wy.append(ilosc_powtu + 1)
                return ciag_wy, ciag_we[0]
            else:
                ciag_wy.append(ilosc_powtu)
                return ciag_wy, ciag_we[0]
        else:
            if ciag_we[i]==ciag_we[i-1]:
                ilosc_powtu+=1
            else:
                ciag_wy.append(ilosc_powtu)
                ilosc_powtu=1
        i+=1
print(bin_comp(ciag_bin))