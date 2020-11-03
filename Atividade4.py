# -*- coding: utf-8 -*-

import cv2
import time

def videoErosao(img):
    mask = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    cv2.namedWindow('Erosao')
    while True:
        #Aplica a erosão
        erode = cv2.erode(img, mask)
        cv2.imshow('Erosao', erode)
        time.sleep(0.3)
        img = erode
        #Sair do loop precionando a tecla (Esc)
        if cv2.waitKey(1) & 0xFF == 27:
            break

def videoDilatacao(img):
    mask = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
    cv2.namedWindow('Dilatacao')
    while True:
        #Aplica a dilatação
        dilate = cv2.dilate(img, mask)
        cv2.imshow('Dilatacao', dilate)
        time.sleep(0.3)
        img = dilate
        #Sair do loop precionando a tecla (Esc)
        if cv2.waitKey(1) & 0xFF == 27:
            break


img = cv2.imread('imageAtv4.png', cv2.IMREAD_GRAYSCALE)

videoDilatacao(img)
videoErosao(img)

cv2.destroyAllWindows()