import time

temps_tuple = (23, 59, 40)
temps_liste = list(temps_tuple)

def demander_alarme():
    reponse = input("Voulez-vous définir une alarme? (o/n): ").lower()
    if reponse == "o":
        heures = int(input("Heures: "))
        minutes = int(input("Minutes: "))
        secondes = int(input("Secondes: "))
        return heures, minutes, secondes
    else:
        return None

def afficher_heure(param):
    try:
        alarme = demander_alarme()
        while True:
            if alarme:
                heures, minutes, secondes = alarme
                if param[0] == heures and param[1] == minutes and param[2] == secondes:
                    print(f"\nAlarme atteinte! : {param[0]:02d}:{param[1]:02d}:{param[2]:02d}",)
                else:
                    print(f"Heure actuelle : {param[0]:02d}:{param[1]:02d}:{param[2]:02d}", end='\r')
            else:
                print(f"Heure actuelle : {param[0]:02d}:{param[1]:02d}:{param[2]:02d}", end='\r')
            param[2] += 1
            if param[2] == 60:
                param[2] = 0
                param[1] += 1
                if param[1] == 60:
                    param[1] = 0
                    param[0] += 1
                    if param[0] == 24:
                        param[0] = 0
            time.sleep(1)
    except KeyboardInterrupt:
        print('\nArret du programme')
        import sys
        sys.exit(0)
        
def new_hour(hour_param): 
    regler_heure = input("Voulez-vous régler l'heure ? (o/n): ").lower()
    if regler_heure == "o":
        nouvelles_heures = int(input("Heures : "))
        nouvelles_minutes = int(input("Minutes : "))
        nouvelles_secondes = int(input("Secondes :"))
        
        hour_param[0] = nouvelles_heures
        hour_param[1] = nouvelles_minutes
        hour_param[2] = nouvelles_secondes
        
        print("Temps mis à jour :", hour_param)
    else:
        print("L'heure n'a pas été modifiée.")
        
new_hour(temps_liste)
afficher_heure(temps_liste)