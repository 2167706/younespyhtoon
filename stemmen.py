
stemmen_younes = 0
stemmen_lucas = 0

print("Welkom bij de verkiezingen van Florijnia!")
print("Je kunt stemmen op younes of lucas.")
print("Type 'UITSLAG' om de stemmen te stoppen en de winnaar te zien.\n")

stem = input("Op wie wil je stemmen? ")

while stem != 'UITSLAG':

    if stem.lower() == 'younes':
        stemmen_omer += 1
    elif stem.lower() == 'lucas':
        stemmen_mehmet += 1
    else:
        print("Ongeldige keuze. Probeer opnieuw.")

    stem = input("Op wie wil je stemmen? ")

# Bepalen van de winnaar op basis van het aantal stemmen
if stemmen_younes > stemmen_lucas:
    print("Omer heeft gewonnen!")
elif stemmen_lucas > stemmen_younes:
    print("Mehmet heeft gewonnen!")
else:
    print("Het is een gelijkspel!")

input('Press ENTER to exit')

