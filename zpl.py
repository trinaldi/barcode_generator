#!/usr/bin/env python3

from io import BytesIO
from PIL import Image
import requests

def main():
    print("Olá, vamos criar uma etiqueta?")
    print("Maravilha!")
    density = check_density()
    width = input("Qual a largura? (em polegadas) ")
    width = check_empty(width)
    height = input("Qual a altura? (em polegadas) ")
    height = check_empty(height)
    zpl = input("Digite o código ZPL: ")
    zpl = check_empty(zpl)
    print("Show, vou gerar um PNG, perae")
    api_url = "http://api.labelary.com/v1/printers/{}dpmm/labels/{}x{}/0/{}"
    r = requests.get(api_url.format(density, width, height, zpl))
    barcode_img = Image.open(BytesIO(r.content))
    barcode_img.save("barcode.png")

def check_density():
    density = input("Primeiro, qual a densidade em dpmm [6, 8, 12 ou 24]? ")
    while density not in ["6", "8", "12", "24"]:
        print("Veja as opções, coleguinha!")
        density = input("Qual a densidade em dpmm [6, 8, 12 ou 24]? ")

    return density

def check_empty(value):
    while value is "":
        value = input("De novo, vai: ")

    return value

if __name__ == "__main__":
    main()
