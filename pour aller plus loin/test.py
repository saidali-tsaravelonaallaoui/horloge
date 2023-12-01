import time

temps_tuple = (23, 59, 50)
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

def format_heure(param, mode_12h=False):
    heures, minutes, secondes = param
    if mode_12h:
        suffixe = "AM" if heures < 12 else "PM"
        heures = heures % 12 or 12
        return f"{heures:02d}:{minutes:02d}:{secondes:02d} {suffixe}"
    else:
        return f"{heures:02d}:{minutes:02d}:{secondes:02d}"

def afficher_heure(param, mode_12h=False):
    try:
        alarme = demander_alarme()
        while True:
            if alarme:
                heures, minutes, secondes = alarme
                if param[0] == heures and param[1] == minutes and param[2] == secondes:
                    print("\nAlarme atteinte!")
                else:
                    heure_formattee = format_heure(param, mode_12h)
                    print(f"Heure actuelle : {heure_formattee}", end='\r')
            else:
                heure_formattee = format_heure(param, mode_12h)
                print(f"Heure actuelle : {heure_formattee}", end='\r')

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
        print('\nArrêt du programme')
        import sys
        sys.exit(0)

def new_hour(hour_param):
    regler_heure = input("Voulez-vous régler l'heure ? (o/n): ").lower()
    if regler_heure == "o":
        try:
            nouvelles_heures = int(input("Heures : "))
            nouvelles_minutes = int(input("Minutes : "))
            nouvelles_secondes = int(input("Secondes :"))

            heure_ampm = input("AM ou PM ? : ").upper()
            if heure_ampm == "PM" and nouvelles_heures != 12:
                nouvelles_heures += 12
            elif heure_ampm == "AM" and nouvelles_heures == 12:
                nouvelles_heures = 0

            hour_param[0] = nouvelles_heures
            hour_param[1] = nouvelles_minutes
            hour_param[2] = nouvelles_secondes

            print("Temps mis à jour :", hour_param)
        except ValueError:
            print("Veuillez entrer des valeurs valides.")
    else:
        print("L'heure n'a pas été modifiée.")

mode_12h = input("Choisissez le mode d'affichage (12/24): ").lower() == "12"
new_hour(temps_liste)
afficher_heure(temps_liste, mode_12h)
