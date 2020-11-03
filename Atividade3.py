# -*- coding: utf-8 -*-

import cv2
import math

def compareHist(S1):
        
    #Lendo as imagens da pasta
    S2 = cv2.imread('imagensAtv3\S2.jpg', 0)
    D1 = cv2.imread('imagensAtv3\D1.jpg', 0)
    D2 = cv2.imread('imagensAtv3\D2.jpg', 0)
    D3 = cv2.imread('imagensAtv3\D3.jpg', 0)
    
    #Calculando os histogramas
    histS1 = cv2.calcHist([S1], [0], None, [256], [0, 256])
    histS2 = cv2.calcHist([S2], [0], None, [256], [0, 256])
    histD1 = cv2.calcHist([D1], [0], None, [256], [0, 256])
    histD2 = cv2.calcHist([D2], [0], None, [256], [0, 256])
    histD3 = cv2.calcHist([D3], [0], None, [256], [0, 256])
    
    #Comparando os histogramas
    #S1 com S2
    corr_S2 = cv2.compareHist(histS1, histS2, cv2.HISTCMP_CORREL)
    chi_sq_S2 = cv2.compareHist(histS1, histS2, cv2.HISTCMP_CHISQR)
    bhatta_S2 = cv2.compareHist(histS1, histS2, cv2.HISTCMP_BHATTACHARYYA)
    #S1 com D1
    corr_D1 = cv2.compareHist(histS1, histD1, cv2.HISTCMP_CORREL)
    chi_sq_D1 = cv2.compareHist(histS1, histD1, cv2.HISTCMP_CHISQR)
    bhatta_D1 = cv2.compareHist(histS1, histD1, cv2.HISTCMP_BHATTACHARYYA)
    #S1 com D2
    corr_D2 = cv2.compareHist(histS1, histD2, cv2.HISTCMP_CORREL)
    chi_sq_D2 = cv2.compareHist(histS1, histD2, cv2.HISTCMP_CHISQR)
    bhatta_D2 = cv2.compareHist(histS1, histD2, cv2.HISTCMP_BHATTACHARYYA)
    #S1 com D3
    corr_D3 = cv2.compareHist(histS1, histD3, cv2.HISTCMP_CORREL)
    chi_sq_D3 = cv2.compareHist(histS1, histD3, cv2.HISTCMP_CHISQR)
    bhatta_D3 = cv2.compareHist(histS1, histD3, cv2.HISTCMP_BHATTACHARYYA)
    
    #Somando as distâncias ao quadrado e apicando a raiz quadrada
    S1_S2 = math.sqrt((corr_S2*corr_S2)+(chi_sq_S2*chi_sq_S2)+(bhatta_S2*bhatta_S2))
    S1_D1 = math.sqrt((corr_D1*corr_D1)+(chi_sq_D1*chi_sq_D1)+(bhatta_D1*bhatta_D1))
    S1_D2 = math.sqrt((corr_D2*corr_D2)+(chi_sq_D2*chi_sq_D2)+(bhatta_D2*bhatta_D2))
    S1_D3 = math.sqrt((corr_D3*corr_D3)+(chi_sq_D3*chi_sq_D3)+(bhatta_D3*bhatta_D3))
    
    #Comparando as distancias e retornando a menor 
    if(S1_S2 < S1_D1 and S1_S2 < S1_D2 and S1_S2 < S1_D3):
        return S2
    elif(S1_D1 < S1_S2 and S1_D1 < S1_D2 and S1_D1 < S1_D3):
        return D1
    elif(S1_D2 < S1_S2 and S1_D2 < S1_D1 and S1_D2 < S1_D3):
        return D2
    else:
        return D3

#Lendo a imagem
S1 = cv2.imread('imagensAtv3\S1.jpg', 0)

#Chamando a função para comparar e retornar a imagem mais parecida
imagem = compareHist(S1)

#Mostrando as imagens na tela
cv2.imshow('Imagem S1', S1)
cv2.imshow('Imagem mais parecida', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
