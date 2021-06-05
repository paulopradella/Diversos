# Retirado do instagram @python.hub
import pywhatkit

print("***Convesor para letra cursiva***")
texto = input("Insira o texto que deseja converter:")
pywhatkit.text_to_handwriting(texto, rgb=( 0, 0, 255))