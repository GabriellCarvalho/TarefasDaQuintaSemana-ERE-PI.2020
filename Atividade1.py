# -*- coding: utf-8 -*-

import cv2
from matplotlib import pyplot as plt

#Carregar as imagens
imagem = cv2.imread('imagemPB.jpg', 0)
imagemColorida = cv2.imread('imagemColorida.jpg')

#Criar e mostrar o histograma da imagem em preto e branco
plt.hist(imagem.ravel(), 256, [0, 256])
plt.xlim(0, 256)
plt.show()

#Criar e mostrar o histograma da imagem colorida
color = ('b', 'g', 'r')
for i,cor in enumerate(color):
    hist = cv2.calcHist([imagemColorida], [i], None, [256], [0, 256])
    plt.plot(hist, color = cor)
    plt.xlim([0, 256])
plt.show()

#Mostrar as imagens na tela
#cv2.imshow('ImagemPB', imagem)
#cv2.imshow('Imagem Colorida', imagemColorida)
cv2.waitKey(0)
cv2.destroyAllWindows()