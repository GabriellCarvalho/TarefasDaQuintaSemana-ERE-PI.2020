# -*- coding: utf-8 -*-

import cv2
from matplotlib import pyplot as plt

#Carrega a imagem
img = cv2.imread('imagemAtv2.png', 0)

#Cria o histograma da imagem
plt.hist(img.ravel(), 256, [0, 256])
plt.show()

#Equaliza a imagem 
newImg = cv2.equalizeHist(img)

#Cria o histograma da imagem equalizada
plt.hist(newImg.ravel(), 256, [0, 256])
plt.show()

#Mostra as imagens
cv2.imshow('Imagem Original', img)
cv2.imshow('Imagem Equalizada', newImg)
cv2.waitKey()
cv2.destroyAllWindows()