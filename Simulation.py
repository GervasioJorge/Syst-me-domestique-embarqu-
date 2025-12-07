import http.server
import socketserver
import random
import time
from urllib.parse import urlparse, parse_qs

# --- 1. Variables Globales ---

TEMP_CIBLE = 25.0
LUMI_SEUIL = 100
TEMP_HYSTERESIS = 1.0

thermo_mode_auto = True
lumiere_mode_auto = True

ventilateur_etat = 0
lumiere_etat = 0
aspirateur_etat = 0
led_froid_etat = 0
led_chaud_etat = 0


# --- 2. Simulations ---

def lire_temperature_simulee():
    return round(random.uniform(18.0, 29.0), 1)

def lire_luminosite_simulee():
    return random.randint(20, 500)


# --- 3. Logique AUTO ---

def verifier_thermoregulation(temp_actuelle):
    global ventilateur_etat, led_froid_etat, led_chaud_etat, thermo_mode_auto

    if thermo_mode_auto:
        if temp_actuelle > (TEMP_CIBLE + TEMP_HYSTERESIS / 2):
            ventilateur_etat = 1
        elif temp_actuelle < (TEMP_CIBLE - TEMP_HYSTERESIS / 2):
            ventilateur_etat = 0

    led_froid_etat = 1 if temp_actuelle < TEMP_CIBLE else 0
    led_chaud_etat = 1 if temp_actuelle > TEMP_CIBLE else 0


def verifier_eclairage(lumi_actuelle):
    global lumiere_etat, lumiere_mode_auto

    if lumiere_mode_auto:
        lumiere_etat = 1 if lumi_actuelle < LUMI_SEUIL else 0


# --- 4. HTML ---

def generate_web_page(T, L):
    global ventilateur_etat, lumiere_etat, aspirateur_etat
    global thermo_mode_auto, lumiere_mode_auto
    global led_froid_etat, led_chaud_etat

    verifier_thermoregulation(T)
    verifier_eclairage(L)

    css_style = """
    <style>
        body { font-family: sans-serif; background:#f4f4f9; padding:20px; }
        h1 { color:#007bff; }
        .card { background:white; padding:15px; border-radius:8px;
                margin-top:15px; border:1px solid #ccc; }
        .status-on { color:green; font-weight:bold; }
        .status-off { color:red; font-weight:bold; }
        .btn { padding:8px 12px; border-radius:4px; color:white;
               text-decoration:none; margin:5px; display:inline-block; }
        .btn-on { background:#28a745; }
        .btn-off { background:#dc3545; }
        .btn-toggle { background:#ffc107; }
        .btn-stop { background:#6c757d; }
    </style>
    """

    html = f"""
    <html>
    <head>
        <title>Simulateur Domotique</title>
        <meta http-equiv="refresh" content="3">
        {css_style}
    </head>
    <body>

        <h1>Simulateur Maquette Domotique</h1>

        <div class="card">
            <h2>Capteurs</h2>
            Temperature : <b>{T} C</b><br>
            Luminosite : <b>{L} Lux</b><br>
        </div>

        <div class="card">
            <h2>Thermoregulation - Ventilateur :
                <span class="{'status-on' if ventilateur_etat else 'status-off'}">
                    {'ON' if ventilateur_etat else 'OFF'}
                </span>
            </h2>
            <p>Mode : <b>{"Auto" if thermo_mode_auto else "Manuel"}</b></p>

            <p>Indicateurs temperature : Froid :
                <span class="{'status-on' if led_froid_etat else 'status-off'}">
                    {'ON' if led_froid_etat else 'OFF'}
                </span>
                - Chaud :
                <span class="{'status-on' if led_chaud_etat else 'status-off'}">
                    {'ON' if led_chaud_etat else 'OFF'}
                </span>
            </p>

            <a href="/?thermo_auto" class="btn btn-toggle">Changer Mode</a>
            <a href="/?v_on" class="btn btn-on">Ventilateur ON</a>
            <a href="/?v_off" class="btn btn-off">Ventilateur OFF</a>
        </div>

        <div class="card">
            <h2>Eclairage :
                <span class="{'status-on' if lumiere_etat else 'status-off'}">
                    {'ON' if lumiere_etat else 'OFF'}
                </span>
            </h2>
            <p>Mode : <b>{"Auto" if lumiere_mode_auto else "Manuel"}</b></p>

            <a href="/?l_auto" class="btn btn-toggle">Changer Mode</a>
            <a href="/?l_on" class="btn btn-on">Lumiere ON</a>
            <a href="/?l_off" class="btn btn-off">Lumiere OFF</a>
        </div>

        <div class="card">
            <h2>Aspirateur :
                <span class="{'status-on' if aspirateur_etat else 'status-off'}">
                    {'ON' if aspirateur_etat else 'OFF'}
                </span>
            </h2>
            <a href="/?a_on" class="btn btn-on">Aspirateur ON</a>
            <a href="/?a_off" class="btn btn-off">Aspirateur OFF</a>
        </div>

        <br>
        <a href="/?stop_sim" class="btn btn-stop">Arreter Simulation</a>

    </body>
    </html>
    """

    return html



# --- 5. Serveur ---

class SmartHomeSimulator(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        global thermo_mode_auto, lumiere_mode_auto
        global ventilateur_etat, lumiere_etat, aspirateur_etat

        parsed_url = urlparse(self.path)
        query = parse_qs(parsed_url.query)

        if 'stop_sim' in query:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Arret du serveur...")
            self.server.shutdown()
            return

        if 'thermo_auto' in query:
            thermo_mode_auto = not thermo_mode_auto

        if 'v_on' in query:
            ventilateur_etat = 1
            thermo_mode_auto = False
        if 'v_off' in query:
            ventilateur_etat = 0
            thermo_mode_auto = False

        if 'a_on' in query:
            aspirateur_etat = 1
        if 'a_off' in query:
            aspirateur_etat = 0

        if 'l_auto' in query:
            lumiere_mode_auto = not lumiere_mode_auto
        if 'l_on' in query:
            lumiere_etat = 1
            lumiere_mode_auto = False
        if 'l_off' in query:
            lumiere_etat = 0
            lumiere_mode_auto = False

        T = lire_temperature_simulee()
        L = lire_luminosite_simulee()

        html = generate_web_page(T, L)

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))


def start_simulation_server(port=8080):
    with socketserver.TCPServer(("", port), SmartHomeSimulator) as httpd:
        print(f"Serveur lancé → http://127.0.0.1:{port}")
        httpd.serve_forever()


if __name__ == "__main__":
    start_simulation_server()
