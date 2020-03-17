import numpy as np
from PIL import Image
import os
from numpy import asarray
from numpy import save

collect_row=[]
collect_all=[]
collect_labels=[]

for n in range(400):
	for m in range(10):
		collect_labels.append(m)

np_im=[]
collect_row=[]

for n in range(29):
	for x in range(400):
		#recorremos cada fila de nuestro dataset (20 filas)
		im = Image.open('tb'+str(n+1)+' ('+str(x+1)+').jpeg').convert('L')
		#Si se desea invertir a negativo cada imagen , adicionar la sgt linea
		#im=im.point(lambda x: 255 if x<140 else 0,'1')
		np_im = np.array(im)

		for i in np_im:
			for j in i:
				collect_row.append(j)

		collect_row.append(collect_labels[x])
		collect_all.append(collect_row)

		np_im=[]
		collect_row=[]

print(len(collect_all))

#definimos la data
data = asarray(collect_all)

#save to npy file
save('data_17_03.npy',data)
