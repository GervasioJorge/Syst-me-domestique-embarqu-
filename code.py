import machine
import socket
import time
# Importez ici les librairies réelles pour vos capteurs
# Exemple : import dht # Pour le DHT11
# Exemple : from bh1750 import BH1750 # Pour le BH1750

# --- 1. Configuration des Broches GPIO (À ADAPTER) ---

# Actionneurs (LEDs/Moteur)
PIN_VENTILATEUR = 14 # Broche pour le moteur/ventilateur (Thermorégulation)
PIN_LUMIERE = 15 # Broche pour la LED de la lumière
PIN_ASPIRATEUR = 16 # Broche pour le moteur/LED de l'aspirateur (Électroménager)
PIN_LED_FROID = 26 # LED pour indiquer que la T° est trop BASSE
PIN_LED_CHAUD = 27 # LED pour indiquer que la T° est trop HAUTE

# Capteurs
PIN_DHT_DATA = 4 # Broche pour le capteur de température/humidité (DHT11/DHT22)
# NOTE: Le BH1750 (luminosité) utilise I2C (SCL/SDA) qui sont généralement sur les broches 22/21 de l'ESP32.

# Initialisation des actionneurs
ventilateur = machine.Pin(PIN_VENTILATEUR, machine.Pin.OUT)
lumiere = machine.Pin(PIN_LUMIERE, machine.Pin.OUT)
aspirateur = machine.Pin(PIN_ASPIRATEUR, machine.Pin.OUT)
led_froid = machine.Pin(PIN_LED_FROID, machine.Pin.OUT)
led_chaud = machine.Pin(PIN_LED_CHAUD, machine.Pin.OUT)

# Initialisation des capteurs (placeholders pour le code réel)
# d = dht.DHT11(machine.Pin(PIN_DHT_DATA)) # Exemple de décommenter si DHT11
# i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(21)) # Exemple I2C pour BH1750
# light_sensor = BH1750(i2c)

# --- 2. Variables d'État Globales ---

TEMP_CIBLE = 25.0 # Température cible par défaut (°C)
TEMP_HYSTERESIS = 1.0 # Marge pour éviter l'activation/désactivation constante
LUMI_SEUIL = 100 # Seuil de luminosité (en Lux) pour l'allumage automatique
lumiere_mode_auto = True # Mode d'éclairage automatique activé par défaut

# --- 3. Fonctions de Lecture (SIMULATION - À REMPLACER) ---

def lire_temperature():
    """ Simule ou lit la température réelle du capteur (ex: DHT11). """
    # Décommenter et adapter pour le DHT11 réel:
    # try:
    # d.measure()
    # return d.temperature()
    # except Exception:
    # return 0.0 # Valeur par défaut en cas d'erreur
    
    # SIMULATION
    return 22.5 

def lire_luminosite():
    """ Simule ou lit la luminosité réelle du capteur (ex: BH1750). """
    # Décommenter et adapter pour le BH1750 réel:
    # try:
    # return light_sensor.read_light()
    # except Exception:
    # return 0
        
    # SIMULATION
    return 80 # Simuler une faible luminosité

# --- 4. Logique d'Automatisation (F01 et F02) ---

def verifier_thermoregulation(temp_actuelle):
    """ F01 : Gère le ventilateur et les LEDs d'indication de température. """
    global TEMP_CIBLE

    # Gérer le ventilateur (Refroidissement / Chauffage simulé)
    if temp_actuelle > (TEMP_CIBLE + TEMP_HYSTERESIS / 2):
        ventilateur.value(1) # Allumer
    elif temp_actuelle < (TEMP_CIBLE - TEMP_HYSTERESIS / 2):
        ventilateur.value(0) # Éteindre
    # else: L'état reste le même (hystérésis)
    
    # Gérer les LEDs d'indication
    led_froid.value(1) if temp_actuelle < TEMP_CIBLE else led_froid.value(0)
    led_chaud.value(1) if temp_actuelle > TEMP_CIBLE else led_chaud.value(0)


def verifier_eclairage(lumi_actuelle):
    """ F02 : Gère la lumière en mode automatique. """
    global lumiere_mode_auto

    if lumiere_mode_auto:
        if lumi_actuelle < LUMI_SEUIL:
            lumiere.value(1) # Allumer la lumière
        else:
            lumiere.value(0) # Éteindre la lumière

# --- 5. Serveur Web et Interface HTML ---

def web_page(T, L, V_etat, L_etat, A_etat, T_cible):
    """ Génère la page HTML avec les données et les boutons de contrôle. """
    
    # États des actionneurs pour l'affichage
    V_txt = "ON" if V_etat else "OFF"
    L_txt = "ON" if L_etat else "OFF"
    A_txt = "ON" if A_etat else "OFF"
    Mode_Auto_txt = "Automatique (Actif)" if lumiere_mode_auto else "Manuel (Inactif)"
    
    html = f"""
    <html>
    <head>
        <title>Maquette Domotique ESP32</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {{ font-family: sans-serif; margin: 20px; }}
            h1 {{ color: #007bff; }} .data {{ font-size: 1.2em; font-weight: bold; }}
            .btn {{ display: inline-block; padding: 10px 15px; margin: 5px; text-decoration: none; color: white; background-color: #28a745; border-radius: 5px; }}
            .btn-off {{ background-color: #dc3545; }} .card {{ border: 1px solid #ccc; padding: 15px; margin-top: 10px; border-radius: 8px; }}
        </style>
    </head>
    <body>
        <h1>💡 Contrôle de la Maquette</h1>
        
        <div class="card">
            <h2>Capteurs & Cible</h2>
            <p>Température Actuelle : <span class="data">{T}°C</span> (Cible: {T_cible}°C)</p>
            <p>Luminosité Actuelle : <span class="data">{L} Lux</span></p>
            <p>T° Indicateurs : <span class="data">Froid {'🟢' if led_froid.value() else '🔴'} | Chaud {'🟢' if led_chaud.value() else '🔴'}</span></p>
        </div>
        
        <div class="card">
            <h2>F01 : Thermorégulation (Ventilateur : {V_txt})</h2>
            <p>Mode : **Automatique** (Activé si T > {T_cible}°C)</p>
            <p><a href="/?v_on" class="btn">Ventilateur ON</a> <a href="/?v_off" class="btn btn-off">Ventilateur OFF</a></p>
        </div>
        
        <div class="card">
            <h2>F02 : Éclairage (Lumière : {L_txt})</h2>
            <p>Mode : **{Mode_Auto_txt}** (Seuil: {LUMI_SEUIL} Lux)</p>
            <p>
                <a href="/?l_on" class="btn">Lumière ON</a> 
                <a href="/?l_off" class="btn btn-off">Lumière OFF</a> 
                <a href="/?l_auto" class="btn" style="background-color: #ffc107;">Mode Auto</a>
            </p>
        </div>
        
        <div class="card">
            <h2>F03 : Appareil Domestique (Aspirateur : {A_txt})</h2>
            <p>(Simulé par LED/Moteur)</p>
            <p>
                <a href="/?a_on" class="btn">Aspirateur ON</a> 
                <a href="/?a_off" class="btn btn-off">Aspirateur OFF</a>
            </p>
        </div>
        
    </body>
    </html>
    """
    return html

# --- 6. Fonction de Connexion Wi-Fi (Doit être exécutée au démarrage) ---

def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    # Remplacer par vos identifiants Wi-Fi
    SSID = "NOM_DE_VOTRE_RESEAU"
    PASSWORD = "VOTRE_MOT_DE_PASSE"
    
    if not wlan.isconnected():
        print('Connexion au réseau...')
        wlan.connect(SSID, PASSWORD)
        timeout = 10
        while not wlan.isconnected() and timeout > 0:
            time.sleep(1)
            timeout -= 1
        
    if wlan.isconnected():
        print('Connexion réussie! IP:', wlan.ifconfig()[0])
        return wlan.ifconfig()[0]
    else:
        print("Échec de la connexion Wi-Fi.")
        return None

# --- 7. Boucle Principale ---

def start_server():
    global lumiere_mode_auto
    
    ip = do_connect()
    if not ip:
        print("Impossible de démarrer le serveur sans connexion IP.")
        return
        
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)
    
    print("Serveur web démarré sur http://%s" % ip)

    while True:
        try:
            conn, addr = s.accept()
            # Lecture de la requête HTTP
            request = conn.recv(1024)
            request = str(request)
            print('Requête:', request)
            
            # --- Analyse des Commandes de l'Interface Web ---
            
            # F01 Ventilateur (Contrôle manuel)
            if '?v_on' in request: ventilateur.value(1)
            if '?v_off' in request: ventilateur.value(0)
            
            # F03 Aspirateur
            if '?a_on' in request: aspirateur.value(1)
            if '?a_off' in request: aspirateur.value(0)
            
            # F02 Lumière (Contrôle manuel)
            if '?l_on' in request: 
                lumiere.value(1)
                lumiere_mode_auto = False
            if '?l_off' in request: 
                lumiere.value(0)
                lumiere_mode_auto = False
            
            # F02 Lumière (Toggle Mode Auto)
            if '?l_auto' in request:
                lumiere_mode_auto = not lumiere_mode_auto
                
            # Lecture des capteurs
            T = lire_temperature()
            L = lire_luminosite()

            # Exécution de la logique automatique
            verifier_thermoregulation(T)
            verifier_eclairage(L)

            # Envoi de la page HTML
            response = web_page(T, L, ventilateur.value(), lumiere.value(), aspirateur.value(), TEMP_CIBLE)
            
            conn.send('HTTP/1.1 200 OK\n')
            conn.send('Content-Type: text/html\n')
            conn.send('Connection: close\n\n')
            conn.sendall(response)
            conn.close()

        except OSError as e:
            if 'ETIMEDOUT' not in str(e): # Ignorer les erreurs de timeout courantes
                print('Erreur de connexion:', e)
            try:
                conn.close()
            except:
                pass

if __name__ == '__main__':
    start_server()
