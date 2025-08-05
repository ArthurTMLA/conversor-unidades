m=float(input('Qual o tamanho em metros?'))
um=str(input('Para qual unidade de medida deseja transformar esse valor? (utilize apenas a sigla ex: KM)')).upper().strip()

mm=m*1000
cm=m*100
dm=m*10
dam=m/10
hm=m/100
km=m/1000

if um =='KM':
    print('a medida de {:.2f} metros corresponde a {:.2f} quilometros'.format(m,km))
elif um =='HM' :
    print('a medida de {:.2f} metros corresponde a {:.2f} hectometros'.format(m, hm))
elif um =='DAM' :
    print('a medida de {:.2f} metros corresponde a {:.2f} decametros'.format(m, dam))
elif um =='DM':
    print('a medida de {:.2f} metros corresponde a {:.2f} decimetros'.format(m, dm))
elif um =='CM' :
    print('a medida de {:.2f} metros corresponde a {:.2f} centimetros'.format(m, cm))
elif um =='MM' :
    print('a medida de {:.2f} metros corresponde a {:.2f} milimetros'.format(m, mm))

else:
    print('Essa não é uma medida válida')