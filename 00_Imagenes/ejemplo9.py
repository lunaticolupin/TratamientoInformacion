
# importamos el modulo pyplot, y lo llamamos plt
import matplotlib.pyplot as plt

from skimage import io
plt.rcParams['image.cmap'] = 'gray'


image=io.imread("lena_gray.png")# imread lee las imagenes con los pixeles codificados como enteros 
# en el rango 0-255. Por eso la convertimos a flotante y en el rango 0-1

print("- Dimensiones de la imagen:")

#plt.imshow(image)
#plt.show()

histograma = []

for i in range(511):
    for j in range(511):
        histograma.append(image[i,j])
    
plt.hist(histograma, 5, facecolor='black')
plt.ylabel('frequencia')
plt.xlabel('valores')
plt.title('Histograma')
plt.show()