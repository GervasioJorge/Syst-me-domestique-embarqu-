"""
Interface: esp32
Nom du projet: SYstème Domestique embarqué
Description: 
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><variables><variable id="YX:0o$6!:C|ow=IN=1%)">temp_actuelle</variable><variable id="3tDB#mFO1zRXyj(31ris">lumi_actuelle</variable><variable id="N~Ppf]9W?d-v%Lc}e9uB">T</variable><variable id="0o`:Iwr8TC_aB;2?!bO;">L</variable><variable id="f:l,4MQ0{~;*[oqpGA-D">V_etat</variable><variable id=".M}PQ}bMYnX~#a~s(:#)">L_etat</variable><variable id="[RDU3,XJM^R:A^[g8**U">A_etat</variable><variable id="io1Qs6TQF[1|z9LwYc.b">T_cible</variable><variable id="WUD5yG;CKb2_EE4%PG%K">html</variable><variable id="^sus}S}d~Ck44|{iVA1{">wlan</variable><variable id="7(Y/PY9tW`]:fu`ZFKd]">lumiere_mode_auto</variable><variable id="M[dC:2wm75{=fCt`,NPF">request</variable><variable id="u_Osm_cFQA{J4TqE2,UH">TEMP_CIBLE</variable><variable id="yRskH/,!^B*mx$r{@^4h">ip</variable><variable id=";J-}^-MBpFI6-5]X}kFh">SSID</variable><variable id="FEp;7r691}pqA4$gakbd">s</variable><variable id="GEQh5Dv)LVRTWPS2*E]3">PASSWORD</variable><variable id="P0u/O.]-JbsK.~f^vjDH">PIN_VENTILATEUR</variable><variable id="Z(Eluh[xdVZEZl~Yu!^B">LUMI_SEUIL</variable><variable id="9)o5CjpN2i1HE80_mI|U">PIN_LUMIERE</variable><variable id="vjL*87{?.,]7anu)Z|)]">TEMP_HYSTERESIS</variable><variable id="TCjhWEL[_J1|jO5D4b9@">timeout</variable><variable id="KNJAdwfOS1ZypQPfX7o}">PIN_ASPIRATEUR</variable><variable id="*_znvQ*.}KfC^/U0ERYz">conn, addr</variable><variable id="Q?C)PL4p/jO(?yyZ_.7N">PIN_LED_FROID</variable><variable id="3pEy:SD9oZW1X2+OjkU7">e</variable><variable id="]lDpnbKY!vD7DwNDPnuc">PIN_LED_CHAUD</variable><variable id="[F1.mi#cGL:)sm)`cbyq">PIN_DHT_DATA</variable><variable id="nLQjRj!$)!c953AZdpW$">ventilateur</variable><variable id="j.wB|o[$usE@a`@#OZt9">lumiere</variable><variable id="^Mpm}Om.vJ8_t#V!{mCl">aspirateur</variable><variable id="|A8m1YGV%(mdtyw[`!uk">led_froid</variable><variable id="T?l]]uswech9)BW:`Mkn">led_chaud</variable><variable id="JNU71{:*x3.0F@qGq#Lg">response</variable><variable id="Q$bmarS.?~FY9~$vOU-m">__name__</variable></variables><block type="procedures_callreturn" id="BYfo/j0+ydE6^=N-#6)o" x="0" y="0"><mutation name="start_server"></mutation></block><block type="call_expression" id="htV8HNGYHBm$d]f?+t1:" x="0" y="0"><field name="NAME">wlan</field><value name="chain"><block type="call_expression_editable_return" id="de%|66|Ravn)nEGf_W9e"><mutation items="1"></mutation><field name="NAME">ifconfig</field><value name="items0"><block type="math_number" id="|}f)##A=)zKb|5*@f?Vn"><field name="NUM">0</field></block></value></block></value></block><block type="text" id="bri9Pn+,-WCRz.x)%!1{" x="0" y="0"><field name="TEXT">Serveur web démarré sur http://%s</field></block><block type="math_arithmetic" id="9vR$bz:%GLu.MiYVy;J)" x="0" y="0"><field name="OP">ADD</field><value name="B"><block type="variables_get" id="=GaBRb}d?%4veBhCnwtm"><field name="VAR" id="M[dC:2wm75{=fCt`,NPF">request</field></block></value></block><block type="text" id="]Z^*id?6ae(da)?VP+n:" x="0" y="0"><field name="TEXT">?v_on</field></block><block type="math_arithmetic" id="$%2F9XTA~fo1no=Y-!fR" x="0" y="0"><field name="OP">ADD</field><value name="B"><block type="variables_get" id="bdR2D?C@I1ju$V#4E~sS"><field name="VAR" id="M[dC:2wm75{=fCt`,NPF">request</field></block></value></block><block type="text" id="o#f/GQf_|p7@+-]@t4yC" x="0" y="0"><field name="TEXT">?v_off</field></block><block type="math_arithmetic" id="#E#bL+P4f}Z.NoV@3^%~" x="0" y="0"><field name="OP">ADD</field><value name="B"><block type="variables_get" id="*]ETU~{S]xnY,~uB$^gl"><field name="VAR" id="M[dC:2wm75{=fCt`,NPF">request</field></block></value></block><block type="text" id="QNyw|O%R_r2z!je25m]y" x="0" y="0"><field name="TEXT">?a_on</field></block><block type="math_arithmetic" id="KPrOeM%BGi(~}*C`%[lA" x="0" y="0"><field name="OP">ADD</field><value name="B"><block type="variables_get" id="Z%LH5fo(j`|},fQ,C9r7"><field name="VAR" id="M[dC:2wm75{=fCt`,NPF">request</field></block></value></block><block type="text" id="PVpP{iEU@.`EHn.PoYNS" x="0" y="0"><field name="TEXT">?a_off</field></block><block type="math_arithmetic" id="o]9l8XG!v|Q@3Wad}|+w" x="0" y="0"><field name="OP">ADD</field><value name="B"><block type="variables_get" id="iCN,/dA*aGaWOF3$l~IB"><field name="VAR" id="M[dC:2wm75{=fCt`,NPF">request</field></block></value></block><block type="text" id="9Vht?5HDtn;4X7NM940[" x="0" y="0"><field name="TEXT">?l_on</field></block><block type="math_arithmetic" id="uh@(fIG{FSmQi~fjndsp" x="0" y="0"><field name="OP">ADD</field><value name="B"><block type="variables_get" id="2OypQ:6KT9BsW(:QwoO."><field name="VAR" id="M[dC:2wm75{=fCt`,NPF">request</field></block></value></block><block type="text" id="M!hnk6c{RbU+:54Z7;aP" x="0" y="0"><field name="TEXT">?l_off</field></block><block type="math_arithmetic" id="W5{HnzJ+7qI3lfEqc1xn" x="0" y="0"><field name="OP">ADD</field><value name="B"><block type="variables_get" id="*x`ZxHk}eKXdj};O.exb"><field name="VAR" id="M[dC:2wm75{=fCt`,NPF">request</field></block></value></block><block type="text" id=":PJ/Q6[|J56qZ[S0Qc,Z" x="0" y="0"><field name="TEXT">?l_auto</field></block><block type="math_arithmetic" id="!4BC;r26miAv=QZy:bkB" x="0" y="0"><field name="OP">ADD</field></block><block type="text" id="IT}Rr%p#zW#l}vXgw7y~" x="0" y="0"><field name="TEXT">ETIMEDOUT</field></block><block type="on_start" id="1G`TsiI8ATGR39`Q=yW`" x="20" y="20"><statement name="DO"><block type="text_comment" id="qWaOHc-S.ye}QU+:)S(}"><field name="TEXT"> Importez ici les librairies réelles pour vos capteurs
</field><next><block type="text_comment" id="zJV4}T#3I!y^]8p%FzTa"><field name="TEXT"> Exemple : import dht # Pour le DHT11
</field><next><block type="text_comment" id="xN4s`r=tN|iuF?Ozu]2`"><field name="TEXT"> Exemple : from bh1750 import BH1750 # Pour le BH1750
</field><next><block type="text_comment" id="u?9WY.B]]u*wZ=:J$l!V"><field name="TEXT"> --- 1. Configuration des Broches GPIO (À ADAPTER) ---
</field><next><block type="text_comment" id="|fCv{|P)F-bZ:}gO;Qq~"><field name="TEXT"> Actionneurs (LEDs/Moteur)
</field><next><block type="variables_set" id="z/f2D4BAFi*q-q(dk:H7"><field name="VAR" id="P0u/O.]-JbsK.~f^vjDH">PIN_VENTILATEUR</field><value name="VALUE"><block type="math_number" id="GJ~+OgtT,_U:*/$MKY}@"><field name="NUM">14</field></block></value><next><block type="text_comment" id=",ZMOV1*do`Z^wOR4f~|!"><field name="TEXT"> Broche pour le moteur/ventilateur (Thermorégulation)
</field><next><block type="variables_set" id="Xeyxin##*}iOWT~5G1g$"><field name="VAR" id="9)o5CjpN2i1HE80_mI|U">PIN_LUMIERE</field><value name="VALUE"><block type="math_number" id="-:g`~L59e1f|n^fns?=j"><field name="NUM">15</field></block></value><next><block type="text_comment" id="x,cbyz!y2@u1hRWIRzVL"><field name="TEXT"> Broche pour la LED de la lumière
</field><next><block type="variables_set" id="bh-%UqjcXcdQ2F{*R{~`"><field name="VAR" id="KNJAdwfOS1ZypQPfX7o}">PIN_ASPIRATEUR</field><value name="VALUE"><block type="math_number" id="oZw{KNBz]DL!ZneE3302"><field name="NUM">16</field></block></value><next><block type="text_comment" id="K?rsv{}iyvqs%^ar}jg,"><field name="TEXT"> Broche pour le moteur/LED de l'aspirateur (Électroménager)
</field><next><block type="variables_set" id="R6fo.AcJ*RY/fBt#VlYS"><field name="VAR" id="Q?C)PL4p/jO(?yyZ_.7N">PIN_LED_FROID</field><value name="VALUE"><block type="math_number" id=":3PDNbNt}O[aMcDO,%7a"><field name="NUM">26</field></block></value><next><block type="text_comment" id="FnY3Q)N_leIWl#1E+|zV"><field name="TEXT"> LED pour indiquer que la T° est trop BASSE
</field><next><block type="variables_set" id="%2zJzd@_ocz?]4j`V:L!"><field name="VAR" id="]lDpnbKY!vD7DwNDPnuc">PIN_LED_CHAUD</field><value name="VALUE"><block type="math_number" id="M6kpj;97m.xr)1dzv,|m"><field name="NUM">27</field></block></value><next><block type="text_comment" id="fk@@+)9Zg]=GN%(,hq{."><field name="TEXT"> LED pour indiquer que la T° est trop HAUTE
</field><next><block type="text_comment" id="9[N=S)|=mMy]3Hn7iSHk"><field name="TEXT"> Capteurs
</field><next><block type="variables_set" id="/xzE%EfTAv$/NWrKUK#5"><field name="VAR" id="[F1.mi#cGL:)sm)`cbyq">PIN_DHT_DATA</field><value name="VALUE"><block type="math_number" id="|3`,t{``SDGVrU}+G8xX"><field name="NUM">4</field></block></value><next><block type="text_comment" id="%2rSw?Z-}5QF=q7.gWL|"><field name="TEXT"> Broche pour le capteur de température/humidité (DHT11/DHT22)
</field><next><block type="text_comment" id="jpo{1zS:!?3^6+la-e8K"><field name="TEXT"> NOTE: Le BH1750 (luminosité) utilise I2C (SCL/SDA) qui sont généralement sur les broches 22/21 de l'ESP32.
</field><next><block type="text_comment" id="0AyIZN47V-wf$D}8vysB"><field name="TEXT"> Initialisation des actionneurs
</field><next><block type="variables_set" id="uV7R]ut+VE7p3[+4|8}v"><field name="VAR" id="nLQjRj!$)!c953AZdpW$">ventilateur</field><value name="VALUE"><block type="call_expression_return" id="ZdC5_zBUNWhsoGWCCYxt"><field name="NAME">machine</field><value name="chain"><block type="call_expression_editable_return" id="?R]GxQOvB1SUzuD@^Rr:"><mutation items="2"></mutation><field name="NAME">Pin</field><value name="items0"><block type="variables_get" id="N##/~SZ!jW.*%#E3^)Ot"><field name="VAR" id="P0u/O.]-JbsK.~f^vjDH">PIN_VENTILATEUR</field></block></value></block></value></block></value><next><block type="variables_set" id="y9),NEW-6v:lw;+pGlcU"><field name="VAR" id="j.wB|o[$usE@a`@#OZt9">lumiere</field><value name="VALUE"><block type="call_expression_return" id="f{9`}+fQERY$tAVSR+As"><field name="NAME">machine</field><value name="chain"><block type="call_expression_editable_return" id="-9B}{hTXqOIeGMtfmdpS"><mutation items="2"></mutation><field name="NAME">Pin</field><value name="items0"><block type="variables_get" id="H4Sa;|FQp~:mMwn$h)~^"><field name="VAR" id="9)o5CjpN2i1HE80_mI|U">PIN_LUMIERE</field></block></value></block></value></block></value><next><block type="variables_set" id="l~)$CIE4VPz:mV}8:pc*"><field name="VAR" id="^Mpm}Om.vJ8_t#V!{mCl">aspirateur</field><value name="VALUE"><block type="call_expression_return" id="z]|aga.y|w-:risWBtIi"><field name="NAME">machine</field><value name="chain"><block type="call_expression_editable_return" id="#}K~xf7JcWU*eu.2lE9W"><mutation items="2"></mutation><field name="NAME">Pin</field><value name="items0"><block type="variables_get" id="w8v:#w?yR`@`aG.a[Emi"><field name="VAR" id="KNJAdwfOS1ZypQPfX7o}">PIN_ASPIRATEUR</field></block></value></block></value></block></value><next><block type="variables_set" id="H#^yvCth;`(7uy^*x63d"><field name="VAR" id="|A8m1YGV%(mdtyw[`!uk">led_froid</field><value name="VALUE"><block type="call_expression_return" id="=n34W%#[.|/#[/CH`[Ab"><field name="NAME">machine</field><value name="chain"><block type="call_expression_editable_return" id="2r/Il5IHswxrYFR|,fLe"><mutation items="2"></mutation><field name="NAME">Pin</field><value name="items0"><block type="variables_get" id="m^*Zo|NczcHnY6uC8WL|"><field name="VAR" id="Q?C)PL4p/jO(?yyZ_.7N">PIN_LED_FROID</field></block></value></block></value></block></value><next><block type="variables_set" id="Rr^wcxGC*#g?^}ICOMX5"><field name="VAR" id="T?l]]uswech9)BW:`Mkn">led_chaud</field><value name="VALUE"><block type="call_expression_return" id="6D^l]0.TsOO4?2pwdyF;"><field name="NAME">machine</field><value name="chain"><block type="call_expression_editable_return" id="`e5fk$wVN6svV!2Sk$.P"><mutation items="2"></mutation><field name="NAME">Pin</field><value name="items0"><block type="variables_get" id="pNslS7U}%9mLE/,.!:bZ"><field name="VAR" id="]lDpnbKY!vD7DwNDPnuc">PIN_LED_CHAUD</field></block></value></block></value></block></value><next><block type="text_comment" id="eMeIG-Au8]86bn5!EjH9"><field name="TEXT"> Initialisation des capteurs (placeholders pour le code réel)
</field><next><block type="text_comment" id="PY1BLnnbR^,QF,X;`p.`"><field name="TEXT"> d = dht.DHT11(machine.Pin(PIN_DHT_DATA)) # Exemple de décommenter si DHT11
</field><next><block type="text_comment" id=":W?iA`T+$22)XF.p]ufX"><field name="TEXT"> i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(21)) # Exemple I2C pour BH1750
</field><next><block type="text_comment" id="$dy(Hq`*1C^.T!Ec.l$h"><field name="TEXT"> light_sensor = BH1750(i2c)
</field><next><block type="text_comment" id=":qEynuB/OD@hm0sGOt3E"><field name="TEXT"> --- 2. Variables d'État Globales ---
</field><next><block type="variables_set" id="@b%#K}-1-^n][=#lo{L~"><field name="VAR" id="u_Osm_cFQA{J4TqE2,UH">TEMP_CIBLE</field><value name="VALUE"><block type="math_number" id="D@8g)/$;GnbZTX(%pK{m"><field name="NUM">25</field></block></value><next><block type="text_comment" id="MKcyShE7Jgg*=r}(e2Mz"><field name="TEXT"> Température cible par défaut (°C)
</field><next><block type="variables_set" id="Msg*9q1JaX^@/.[oRh{V"><field name="VAR" id="vjL*87{?.,]7anu)Z|)]">TEMP_HYSTERESIS</field><value name="VALUE"><block type="math_number" id="f.RJ}t@{uxX^$gOg-jFc"><field name="NUM">1</field></block></value><next><block type="text_comment" id="Zg+c4k.z6D@GFjIBqX7S"><field name="TEXT"> Marge pour éviter l'activation/désactivation constante
</field><next><block type="variables_set" id="TCEinSiwJ#lRn2uAO~8h"><field name="VAR" id="Z(Eluh[xdVZEZl~Yu!^B">LUMI_SEUIL</field><value name="VALUE"><block type="math_number" id="]eny2a%=h[(31f:5|?M="><field name="NUM">100</field></block></value><next><block type="text_comment" id="+J~osr@6slJ7yt=c(=~x"><field name="TEXT"> Seuil de luminosité (en Lux) pour l'allumage automatique
</field><next><block type="variables_set" id="Mg;zt~*lA84fVJ#,3tX#"><field name="VAR" id="7(Y/PY9tW`]:fu`ZFKd]">lumiere_mode_auto</field><value name="VALUE"><block type="logic_boolean" id="gz;mM4[Ih1U}ZpyFvWun"><field name="BOOL">TRUE</field></block></value><next><block type="text_comment" id="NQ?GrxTwg5/?RnT%pu!x"><field name="TEXT"> Mode d'éclairage automatique activé par défaut
</field><next><block type="text_comment" id="{fMA~w/MB:#}Z^`wKkA/"><field name="TEXT"> --- 3. Fonctions de Lecture (SIMULATION - À REMPLACER) ---
</field><next><block type="text_comment" id="f+b$H@.hl5QU90Q6|Sn1"><field name="TEXT"> --- 4. Logique d'Automatisation (F01 et F02) ---
</field><next><block type="text_comment" id="6GTm(n;:j$`j8i{5MZuz"><field name="TEXT"> --- 5. Serveur Web et Interface HTML ---
</field><next><block type="text_comment" id="AqHlIM@WI[6APfX2a~/x"><field name="TEXT"> --- 6. Fonction de Connexion Wi-Fi (Doit être exécutée au démarrage) ---
</field><next><block type="text_comment" id="A%NxTW1?2DDHq81+8A4!"><field name="TEXT"> --- 7. Boucle Principale ---
</field><next><block type="controls_if" id="CBMHZXL?S8[^Pd-+{JK*"><value name="IF0"><block type="logic_compare" id="^WMuo)m4k~QN=ekly9Vz"><field name="OP">EQ</field><value name="A"><block type="variables_get" id="r-U$XDfA]UTjf2*m#ldP"><field name="VAR" id="Q$bmarS.?~FY9~$vOU-m">__name__</field></block></value><value name="B"><block type="text" id="H:[Y#hHGVDztn`ue4Gov"><field name="TEXT">__main__</field></block></value></block></value></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></statement></block><block type="procedures_defreturn" id="26!COJOm^Zpl8[nZ_V(|" x="360" y="10"><mutation name="lire_temperature"></mutation><field name="NAME">lire_temperature</field><statement name="STACK"><block type="comment_docstrings" id="35pLpZ]-Gztjq$0Hw*+Y"><field name="COMMENT"> Simule ou lit la température réelle du capteur (ex: DHT11). </field><next><block type="text_comment" id="[W?{h4$3/H5AWq7S$k(="><field name="TEXT"> Décommenter et adapter pour le DHT11 réel:
</field><next><block type="text_comment" id="(.;=PFv7)4-[Tdai:I=b"><field name="TEXT"> try:
</field><next><block type="text_comment" id="xGO1botFIjJ#wX9`wa-l"><field name="TEXT"> d.measure()
</field><next><block type="text_comment" id="0V6lK{Vlb#Xy:REwY$wU"><field name="TEXT"> return d.temperature()
</field><next><block type="text_comment" id="Rg{+9(T{TGb%I=,G_rEc"><field name="TEXT"> except Exception:
</field><next><block type="text_comment" id="iDXbwRiDAdKsnjjHbJ%D"><field name="TEXT"> return 0.0 # Valeur par défaut en cas d'erreur
</field><next><block type="text_comment" id="U}RYU#IJ=Ynk~JaI(Z-J"><field name="TEXT"> SIMULATION
</field></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></statement><value name="RETURN"><block type="math_number" id="B(4s+su.pfP03xI9rP0("><field name="NUM">22.5</field></block></value></block><block type="procedures_defreturn" id="{(3^qJ5J}1DaRT:y$umB" x="360" y="543"><mutation name="lire_luminosite"></mutation><field name="NAME">lire_luminosite</field><statement name="STACK"><block type="comment_docstrings" id="X,WyXV%$Se:4zDEU8aV?"><field name="COMMENT"> Simule ou lit la luminosité réelle du capteur (ex: BH1750). </field><next><block type="text_comment" id="MuEOh+,d%e,zfSv)]Rf5"><field name="TEXT"> Décommenter et adapter pour le BH1750 réel:
</field><next><block type="text_comment" id="%.@mA[);04U;$hsBkSpO"><field name="TEXT"> try:
</field><next><block type="text_comment" id="Y1eZa2$bd+[Yr+LmG78L"><field name="TEXT"> return light_sensor.read_light()
</field><next><block type="text_comment" id="E@t!`Ab#=tA5FA7usqG@"><field name="TEXT"> except Exception:
</field><next><block type="text_comment" id="r$?(q(Kz^AmV;%[G`_6P"><field name="TEXT"> return 0
</field><next><block type="text_comment" id="/G$ZVrMBt4of#O$K?{e7"><field name="TEXT"> SIMULATION
</field><next><block type="text_comment" id="cpepqD.uf.fcIcn1znWu"><field name="TEXT"> Simuler une faible luminosité
</field></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></statement><value name="RETURN"><block type="math_number" id="b2qikwJ?qAV=Z]P$~5*h"><field name="NUM">80</field></block></value></block><block type="procedures_defnoreturn" id="9E2P8L})Oq{)1,^3}NNI" x="360" y="1076"><mutation name="verifier_thermoregulation"><arg name="temp_actuelle" varid="YX:0o$6!:C|ow=IN=1%)" paramId="q82oo|2^#-G+3L4F1$[h"></arg></mutation><field name="NAME">verifier_thermoregulation</field><field name="q82oo|2^#-G+3L4F1$[h">temp_actuelle</field><statement name="STACK"><block type="comment_docstrings" id="FIW2hugmKtj{mu.rpzp!"><field name="COMMENT"> F01 : Gère le ventilateur et les LEDs d'indication de température. </field><next><block type="variables_global" id="]tVe4NDr9w]v*IvfZH8L"><field name="VAR" id="u_Osm_cFQA{J4TqE2,UH">TEMP_CIBLE</field><next><block type="text_comment" id="#-t4C0~6vCWzGA36q0yV"><field name="TEXT"> Gérer le ventilateur (Refroidissement / Chauffage simulé)
</field><next><block type="controls_if" id="KbVaO~OtAS@gm~{cP+.d"><mutation elseif="1"></mutation><value name="IF0"><block type="logic_compare" id="1,pR6|QwDd3$d6?lTQp-"><field name="OP">GT</field><value name="A"><block type="variables_get" id="z%.*E_gJLfY1DMgMa@A+"><field name="VAR" id="YX:0o$6!:C|ow=IN=1%)">temp_actuelle</field></block></value><value name="B"><block type="math_arithmetic" id="B!#L4q7`$`d8iZ(`i0Rf"><field name="OP">ADD</field><value name="A"><block type="variables_get" id="{Bsq^:N{vo*/^86EK{`Q"><field name="VAR" id="u_Osm_cFQA{J4TqE2,UH">TEMP_CIBLE</field></block></value><value name="B"><block type="math_arithmetic" id="RYN/y?[P6O8KH:Sj(yZx"><field name="OP">DIVIDE</field><value name="A"><block type="variables_get" id="XJ9lNoi34h+qwom~C?8N"><field name="VAR" id="vjL*87{?.,]7anu)Z|)]">TEMP_HYSTERESIS</field></block></value><value name="B"><block type="math_number" id="G;#oDM~LHwLOLTztfC-b"><field name="NUM">2</field></block></value></block></value></block></value></block></value><statement name="DO0"><block type="call_expression" id="V2+J{D@rkI*n5/HK00!7"><field name="NAME">ventilateur</field><value name="chain"><block type="call_expression_editable_return" id="x~Kk^NT,9`8bL5Ca{RS0"><mutation items="1"></mutation><field name="NAME">value</field><value name="items0"><block type="math_number" id="i8Pgxu_?_3w9Sdv7SxNf"><field name="NUM">1</field></block></value></block></value><next><block type="text_comment" id="%)Pa$$yM1$)CV1P.V*ZY"><field name="TEXT"> Allumer
</field></block></next></block></statement><value name="IF1"><block type="logic_compare" id="|Uy:*SJHLQ6,N!DeVKdh"><field name="OP">LT</field><value name="A"><block type="variables_get" id="%9_$Ufo@19.a82jTT,8g"><field name="VAR" id="YX:0o$6!:C|ow=IN=1%)">temp_actuelle</field></block></value><value name="B"><block type="math_arithmetic" id="J|QXmJ^UHG6wdK;hbj`^"><field name="OP">MINUS</field><value name="A"><block type="variables_get" id="Rt9,/L-=6]Wp=Wi)E-+9"><field name="VAR" id="u_Osm_cFQA{J4TqE2,UH">TEMP_CIBLE</field></block></value><value name="B"><block type="math_arithmetic" id="[r^RV=4Sjb0^t179J;#@"><field name="OP">DIVIDE</field><value name="A"><block type="variables_get" id="[A+S~(5/zwP:If%5c@(!"><field name="VAR" id="vjL*87{?.,]7anu)Z|)]">TEMP_HYSTERESIS</field></block></value><value name="B"><block type="math_number" id="9u(+5=2=1X8S*g^/^74L"><field name="NUM">2</field></block></value></block></value></block></value></block></value><statement name="DO1"><block type="call_expression" id="*itK~R;bQIp-$J]$o9b1"><field name="NAME">ventilateur</field><value name="chain"><block type="call_expression_editable_return" id="cSE6x26N~G_uStEXgW)#"><mutation items="1"></mutation><field name="NAME">value</field><value name="items0"><block type="math_number" id="ROy^,2TUu]Qx3xI4km:j"><field name="NUM">0</field></block></value></block></value><next><block type="text_comment" id="x)D@DleKlrP!HO~{J0Oc"><field name="TEXT"> Éteindre
</field></block></next></block></statement><next><block type="text_comment" id="pBZJ6/{XRK[GF3tHURX0"><field name="TEXT"> else: L'état reste le même (hystérésis)
</field><next><block type="text_comment" id=".m^3;JPh7|^2S;m)kD0u"><field name="TEXT"> Gérer les LEDs d'indication
</field></block></next></block></next></block></next></block></next></block></next></block></statement></block><block type="procedures_defnoreturn" id="EbXgAje9O5RE#?L:uvDn" x="360" y="1901"><mutation name="verifier_eclairage"><arg name="lumi_actuelle" varid="3tDB#mFO1zRXyj(31ris" paramId="Y~2H-kdnzS`)DLlfyFb)"></arg></mutation><field name="NAME">verifier_eclairage</field><field name="Y~2H-kdnzS`)DLlfyFb)">lumi_actuelle</field><statement name="STACK"><block type="comment_docstrings" id="Q~bclt6+ySswP~+-)PP{"><field name="COMMENT"> F02 : Gère la lumière en mode automatique. </field><next><block type="variables_global" id="g`IFfPkWm]|YWUugG0Z("><field name="VAR" id="7(Y/PY9tW`]:fu`ZFKd]">lumiere_mode_auto</field><next><block type="controls_if" id="-5}g4lOWK,cDr~oe~hYS"><value name="IF0"><block type="variables_get" id="X8imefz3v|}W0B4`/e4o"><field name="VAR" id="7(Y/PY9tW`]:fu`ZFKd]">lumiere_mode_auto</field></block></value><statement name="DO0"><block type="controls_if" id="*JQ.Ows9^]m8@f%}a6Ln"><mutation else="1"></mutation><value name="IF0"><block type="logic_compare" id="lm+WdG6/Lf[=uP#-X.4I"><field name="OP">LT</field><value name="A"><block type="variables_get" id="mY{ZE{fh=I+xo(SF$KcJ"><field name="VAR" id="3tDB#mFO1zRXyj(31ris">lumi_actuelle</field></block></value><value name="B"><block type="variables_get" id="?Ek.RN_ED.XC_64efT+."><field name="VAR" id="Z(Eluh[xdVZEZl~Yu!^B">LUMI_SEUIL</field></block></value></block></value><statement name="DO0"><block type="call_expression" id="|yxu_-S/m.E(lOcoO_Y0"><field name="NAME">lumiere</field><value name="chain"><block type="call_expression_editable_return" id="mok2OyU%(VjI0LAAoQiJ"><mutation items="1"></mutation><field name="NAME">value</field><value name="items0"><block type="math_number" id="@JI10r0+U1@Ad80Ih/}w"><field name="NUM">1</field></block></value></block></value><next><block type="text_comment" id=".56u`*swykSp=?WFSk=-"><field name="TEXT"> Allumer la lumière
</field></block></next></block></statement><statement name="ELSE"><block type="call_expression" id="f#.a+XTYhY(aT#6[/G;F"><field name="NAME">lumiere</field><value name="chain"><block type="call_expression_editable_return" id="FsUN}|bv[c0/5@*0opv,"><mutation items="1"></mutation><field name="NAME">value</field><value name="items0"><block type="math_number" id="3RMdnJ-51:2;C58^3PUA"><field name="NUM">0</field></block></value></block></value><next><block type="text_comment" id="h^k2!%|A=Any,aY/*?V~"><field name="TEXT"> Éteindre la lumière
</field></block></next></block></statement></block></statement></block></next></block></next></block></statement></block><block type="procedures_defreturn" id="4sD2[7Yy2{5AOiBf/zt]" x="360" y="2619"><mutation name="web_page"><arg name="T" varid="N~Ppf]9W?d-v%Lc}e9uB" paramId="_Z:Utl/R~Ye,hB$3MN-P"></arg><arg name="L" varid="0o`:Iwr8TC_aB;2?!bO;" paramId="bnYZ/xcI*Euwl5:B#4KW"></arg><arg name="V_etat" varid="f:l,4MQ0{~;*[oqpGA-D" paramId="_.@1`ke*EW,qIlC8exe0"></arg><arg name="L_etat" varid=".M}PQ}bMYnX~#a~s(:#)" paramId="Q%kKyCKTPj8dFxO/7oZY"></arg><arg name="A_etat" varid="[RDU3,XJM^R:A^[g8**U" paramId=":xXae!^Nr^!;M.tgmsr)"></arg><arg name="T_cible" varid="io1Qs6TQF[1|z9LwYc.b" paramId="WGaqb,M@UTL?6w!~Yi.m"></arg></mutation><field name="NAME">web_page</field><field name="_Z:Utl/R~Ye,hB$3MN-P">T</field><field name="bnYZ/xcI*Euwl5:B#4KW">L</field><field name="_.@1`ke*EW,qIlC8exe0">V_etat</field><field name="Q%kKyCKTPj8dFxO/7oZY">L_etat</field><field name=":xXae!^Nr^!;M.tgmsr)">A_etat</field><field name="WGaqb,M@UTL?6w!~Yi.m">T_cible</field><statement name="STACK"><block type="comment_docstrings" id="h{;CY;60`hp*JL[kCzd!"><field name="COMMENT"> Génère la page HTML avec les données et les boutons de contrôle. </field><next><block type="text_comment" id="S2gSCR)3,LU#gk0jR]?V"><field name="TEXT"> États des actionneurs pour l'affichage
</field><next><block type="variables_set" id="KC_Q/L[u^YHBxL$T5/Pc"><field name="VAR" id="WUD5yG;CKb2_EE4%PG%K">html</field><value name="VALUE"><block type="text" id="BeV-YI!yRx#|`0OZEH}E"><field name="TEXT">f
    &lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Maquette Domotique ESP32&lt;/title&gt;
        &lt;meta name=viewport content=width=device-width, initial-scale=1&gt;
        &lt;style&gt;
            body {{ font-family: sans-serif; margin: 20px; }}
            h1 {{ color: #007bff; }} .data {{ font-size: 1.2em; font-weight: bold; }}
            .btn {{ display: inline-block; padding: 10px 15px; margin: 5px; text-decoration: none; color: white; background-color: #28a745; border-radius: 5px; }}
            .btn-off {{ background-color: #dc3545; }} .card {{ border: 1px solid #ccc; padding: 15px; margin-top: 10px; border-radius: 8px; }}
        &lt;/style&gt;
    &lt;/head&gt;
    &lt;body&gt;
        &lt;h1&gt;💡 Contrôle de la Maquette&lt;/h1&gt;
        
        &lt;div class=card&gt;
            &lt;h2&gt;Capteurs &amp; Cible&lt;/h2&gt;
            &lt;p&gt;Température Actuelle : &lt;span class=data&gt;{T}°C&lt;/span&gt; (Cible: {T_cible}°C)&lt;/p&gt;
            &lt;p&gt;Luminosité Actuelle : &lt;span class=data&gt;{L} Lux&lt;/span&gt;&lt;/p&gt;
            &lt;p&gt;T° Indicateurs : &lt;span class=data&gt;Froid {🟢 if led_froid.value() else 🔴} | Chaud {🟢 if led_chaud.value() else 🔴}&lt;/span&gt;&lt;/p&gt;
        &lt;/div&gt;
        
        &lt;div class=card&gt;
            &lt;h2&gt;F01 : Thermorégulation (Ventilateur : {V_txt})&lt;/h2&gt;
            &lt;p&gt;Mode : **Automatique** (Activé si T &gt; {T_cible}°C)&lt;/p&gt;
            &lt;p&gt;&lt;a href=/?v_on class=btn&gt;Ventilateur ON&lt;/a&gt; &lt;a href=/?v_off class=btn btn-off&gt;Ventilateur OFF&lt;/a&gt;&lt;/p&gt;
        &lt;/div&gt;
        
        &lt;div class=card&gt;
            &lt;h2&gt;F02 : Éclairage (Lumière : {L_txt})&lt;/h2&gt;
            &lt;p&gt;Mode : **{Mode_Auto_txt}** (Seuil: {LUMI_SEUIL} Lux)&lt;/p&gt;
            &lt;p&gt;
                &lt;a href=/?l_on class=btn&gt;Lumière ON&lt;/a&gt; 
                &lt;a href=/?l_off class=btn btn-off&gt;Lumière OFF&lt;/a&gt; 
                &lt;a href=/?l_auto class=btn style=background-color: #ffc107;&gt;Mode Auto&lt;/a&gt;
            &lt;/p&gt;
        &lt;/div&gt;
        
        &lt;div class=card&gt;
            &lt;h2&gt;F03 : Appareil Domestique (Aspirateur : {A_txt})&lt;/h2&gt;
            &lt;p&gt;(Simulé par LED/Moteur)&lt;/p&gt;
            &lt;p&gt;
                &lt;a href=/?a_on class=btn&gt;Aspirateur ON&lt;/a&gt; 
                &lt;a href=/?a_off class=btn btn-off&gt;Aspirateur OFF&lt;/a&gt;
            &lt;/p&gt;
        &lt;/div&gt;
        
    &lt;/body&gt;
    &lt;/html&gt;
    </field></block></value></block></next></block></next></block></statement><value name="RETURN"><block type="variables_get" id="Q``h~jVuvJkrK:M?Unl7"><field name="VAR" id="WUD5yG;CKb2_EE4%PG%K">html</field></block></value></block><block type="procedures_defreturn" id="2?0@p;oX%20~TlEdZ}h[" x="360" y="3193"><mutation name="do_connect"></mutation><field name="NAME">do_connect</field><statement name="STACK"><block type="variables_set" id="?E)BZwhbuKg,h+T,EN;3"><field name="VAR" id="^sus}S}d~Ck44|{iVA1{">wlan</field><value name="VALUE"><block type="call_expression_return" id="-x}#PGB?f9TZ/ZV5y$t0"><field name="NAME">network</field><value name="chain"><block type="call_expression_editable_return" id="$y0]+,H+K|b3~TaHw28p"><mutation items="1"></mutation><field name="NAME">WLAN</field></block></value></block></value><next><block type="call_expression" id="J$W}J7Th=w!}|Uz.2GGM"><field name="NAME">wlan</field><value name="chain"><block type="call_expression_editable_return" id="`xlyOfCUw#-P=9{za=/C"><mutation items="1"></mutation><field name="NAME">active</field><value name="items0"><block type="logic_boolean" id="M);;-G[Y;/FJQ}M]+qI*"><field name="BOOL">TRUE</field></block></value></block></value><next><block type="text_comment" id="jo+pCgM`m-IR{:9Xk3h4"><field name="TEXT"> Remplacer par vos identifiants Wi-Fi
</field><next><block type="variables_set" id="uaB^1j?1{~Wf}77$:,ns"><field name="VAR" id=";J-}^-MBpFI6-5]X}kFh">SSID</field><value name="VALUE"><block type="text" id="iZ8K5KhIefz~/ZkJ!T~t"><field name="TEXT">NOM_DE_VOTRE_RESEAU</field></block></value><next><block type="variables_set" id="WPS]I1#ly`jw]?^8dq[N"><field name="VAR" id="GEQh5Dv)LVRTWPS2*E]3">PASSWORD</field><value name="VALUE"><block type="text" id="WN/X:1DN,_;Tp|^,|)_9"><field name="TEXT">VOTRE_MOT_DE_PASSE</field></block></value><next><block type="controls_if" id="6|d%iB/`sdev(R)([P*8"><value name="IF0"><block type="logic_negate" id="Kor$Ildj4+-;=Q;M5NrV"><value name="BOOL"><block type="call_expression_return" id="MG}Tf9b27[$oi84{Shs;"><field name="NAME">wlan</field><value name="chain"><block type="call_expression_editable_return" id="iVY)|26KSVfe$_!1iQ(Q"><field name="NAME">isconnected</field></block></value></block></value></block></value><statement name="DO0"><block type="communication_serialWrite" id="B6F0S@Rg#`8^fj[*OUSI"><mutation newlines="false"></mutation><value name="TEXT"><block type="text" id="YlZJAJO}i)_q5EIM5ufr"><field name="TEXT">Connexion au réseau...</field></block></value><next><block type="call_expression" id="aZyuY+?-?)k*$aerj2#~"><field name="NAME">wlan</field><value name="chain"><block type="call_expression_editable_return" id=")G:7;ky5TZA:{3l=SCMI"><mutation items="2"></mutation><field name="NAME">connect</field><value name="items0"><block type="variables_get" id="2q,zMY=)wa@45fn=h14N"><field name="VAR" id=";J-}^-MBpFI6-5]X}kFh">SSID</field></block></value><value name="items1"><block type="variables_get" id="FB6W%qVX/Eg5I|A-@{#w"><field name="VAR" id="GEQh5Dv)LVRTWPS2*E]3">PASSWORD</field></block></value></block></value><next><block type="variables_set" id="k|Mn:v:qpPm6T?Hu[LYf"><field name="VAR" id="TCjhWEL[_J1|jO5D4b9@">timeout</field><value name="VALUE"><block type="math_number" id="HHgY9Udosm.m/Ejm8_1u"><field name="NUM">10</field></block></value><next><block type="controls_whileUntil" id="]*p|NA%t9D^.wQkMC65l"><field name="MODE">WHILE</field><statement name="DO"><block type="call_expression" id="@Q1vJ}TFdah2:QIF`E]g"><field name="NAME">time</field><value name="chain"><block type="call_expression_editable_return" id="xeIZrnr?e}6Hi_%Qsg_c"><mutation items="1"></mutation><field name="NAME">sleep</field><value name="items0"><block type="math_number" id="v|s7/X#87ROqt3PYm{6:"><field name="NUM">1</field></block></value></block></value></block></statement></block></next></block></next></block></next></block></statement><next><block type="controls_if" id="(aKVEOTe1j5W1R(V4f-T"><mutation else="1"></mutation><value name="IF0"><block type="call_expression_return" id="~.5^C+F2R|:a4W`U{!Kk"><field name="NAME">wlan</field><value name="chain"><block type="call_expression_editable_return" id="izt;.Y%yhnF(2Nf}y*H2"><field name="NAME">isconnected</field></block></value></block></value><statement name="DO0"><block type="print_with_separator" id="vkRvOYPLf9ksZY2Ho~%]"><mutation items="2"></mutation><value name="items0"><block type="text" id="I8{[@Lti[m4eNxR%2UkO"><field name="TEXT">Connexion réussie! IP:</field></block></value><next><block type="procedures_simple_return" id="D4~2HDmqHP-PzN(@:/~6"></block></next></block></statement><statement name="ELSE"><block type="communication_serialWrite" id="0CR|LVB~ssqA:;xVGd-W"><mutation newlines="false"></mutation><value name="TEXT"><block type="text" id="s9`zNu)u..Hc1B7~jQu8"><field name="TEXT">Échec de la connexion Wi-Fi.</field></block></value><next><block type="procedures_simple_return" id=";|8.pSTgw~QrascHz#FX"></block></next></block></statement></block></next></block></next></block></next></block></next></block></next></block></next></block></statement><value name="RETURN"><block type="text" id="9SBpdPP2;T6I7U,ie833"><field name="TEXT"></field></block></value></block><block type="procedures_defreturn" id="[wiftW1`7lWH{w@ZaytU" x="360" y="4314"><mutation name="start_server"></mutation><field name="NAME">start_server</field><statement name="STACK"><block type="variables_global" id="494046D=o:[DRX`^cMOO"><field name="VAR" id="7(Y/PY9tW`]:fu`ZFKd]">lumiere_mode_auto</field><next><block type="variables_set" id="pTZ;bJ7Mc!+FsGr9FU=A"><field name="VAR" id="yRskH/,!^B*mx$r{@^4h">ip</field><value name="VALUE"><block type="procedures_callreturn" id=";2WLHD9V]n~[NTlI}3=*"><mutation name="do_connect"></mutation></block></value><next><block type="controls_if" id="%`piZ1$dzAQDsORvzRd-"><value name="IF0"><block type="logic_negate" id="DC*]]x2JL6L+pR3e5F%q"><value name="BOOL"><block type="variables_get" id="*HbQPZQPH0U+C,N=PD|n"><field name="VAR" id="yRskH/,!^B*mx$r{@^4h">ip</field></block></value></block></value><statement name="DO0"><block type="communication_serialWrite" id="_1Ee/dMGwv||5#vZf{,{"><mutation newlines="false"></mutation><value name="TEXT"><block type="text" id="VMbM;JL+To`5!wRNC5+i"><field name="TEXT">Impossible de démarrer le serveur sans connexion IP.</field></block></value><next><block type="procedures_simple_return" id="i0+acjhf}TWsD_[Vhc8E"></block></next></block></statement><next><block type="variables_set" id="N,);L-,!RvPb0ra2pLQ%"><field name="VAR" id="FEp;7r691}pqA4$gakbd">s</field><value name="VALUE"><block type="call_expression_return" id="GeCKgRlL)LOUg`Ro#=0!"><field name="NAME">socket</field><value name="chain"><block type="call_expression_editable_return" id="#1S;$|HlD3K6Zw)ZFLOn"><mutation items="2"></mutation><field name="NAME">socket</field></block></value></block></value><next><block type="call_expression" id="ioX$sm:1Pnv~Ad7O+).S"><field name="NAME">s</field><value name="chain"><block type="call_expression_editable_return" id="/JzKis:02:fUme4(Nt0^"><mutation items="1"></mutation><field name="NAME">bind</field></block></value><next><block type="call_expression" id="?5FVuW~]AwPTx/i4EGxU"><field name="NAME">s</field><value name="chain"><block type="call_expression_editable_return" id=":[JQHE6iTg6w^#DsMy^8"><mutation items="1"></mutation><field name="NAME">listen</field><value name="items0"><block type="math_number" id="zZVc3:eNPGi2}b0+z0d!"><field name="NUM">5</field></block></value></block></value><next><block type="communication_serialWrite" id="eKwQ#YYq859$_u6L)v}q"><mutation newlines="false"></mutation><value name="TEXT"><block type="math_modulo" id="c#+L_R:kM6(1(15(kwEr"><value name="DIVISOR"><block type="variables_get" id="2,F1?(qqM$OA3%Zx0UnW"><field name="VAR" id="yRskH/,!^B*mx$r{@^4h">ip</field></block></value></block></value><next><block type="controls_whileUntil" id="bh,ugPb1zAzlcg![*8Qs"><field name="MODE">WHILE</field><statement name="DO"><block type="exception_try" id=",F-%;?**Mc;ZamXydh#}"><mutation except="1" exceptarg="1"></mutation><statement name="EXC"><block type="variables_set" id=".G2mIClx6X8?8_wCgtHn"><field name="VAR" id="*_znvQ*.}KfC^/U0ERYz">conn, addr</field><value name="VALUE"><block type="call_expression_return" id="jUH4hmBNwMH2gOg%/ws|"><field name="NAME">s</field><value name="chain"><block type="call_expression_editable_return" id="Id$m*W-F%WM|RP=f9(!6"><field name="NAME">accept</field></block></value></block></value><next><block type="text_comment" id="29H$/`)qxp!V4xPh,Q^U"><field name="TEXT"> Lecture de la requête HTTP
</field><next><block type="variables_set" id="q1Ez/HIrB/fec%=;p=wI"><field name="VAR" id="M[dC:2wm75{=fCt`,NPF">request</field><value name="VALUE"><block type="call_expression_return" id="uK89SP5)+1ox#r.|yAH^"><field name="NAME">conn</field><value name="chain"><block type="call_expression_editable_return" id="sr{l2Wa)N_G6f+UI]i_W"><mutation items="1"></mutation><field name="NAME">recv</field><value name="items0"><block type="math_number" id=";qLiiU,%Z9qAKH=0bwZ;"><field name="NUM">1024</field></block></value></block></value></block></value><next><block type="variables_set" id="es_INry=tT_8{UQQ!4z%"><field name="VAR" id="M[dC:2wm75{=fCt`,NPF">request</field><value name="VALUE"><block type="variables_force_type" id="p9+-EPoNz?T~n!T_o[G?"><field name="TYPE">str</field><value name="VALUE"><block type="variables_get" id="J21~(;7bdUAeReg*yYvL"><field name="VAR" id="M[dC:2wm75{=fCt`,NPF">request</field></block></value></block></value><next><block type="print_with_separator" id="PTQq|9?q3sUrN3b88q8:"><mutation items="2"></mutation><value name="items0"><block type="text" id="L/Ki4,g$..Qq;Ai!7^sI"><field name="TEXT">Requête:</field></block></value><value name="items1"><block type="variables_get" id="tw@T6ahOeE)O5uNn_uy!"><field name="VAR" id="M[dC:2wm75{=fCt`,NPF">request</field></block></value><next><block type="text_comment" id="Wv+[J|,yDMkZ5F2;RfRy"><field name="TEXT"> --- Analyse des Commandes de l'Interface Web ---
</field><next><block type="text_comment" id="dSK-Ds@/~I988#lh;]2I"><field name="TEXT"> F01 Ventilateur (Contrôle manuel)
</field><next><block type="controls_if" id="#$z#@6(R?WdBtc:OLP-r"><statement name="DO0"><block type="call_expression" id="#*WNJ?jtT|H1C%y`lTEQ"><field name="NAME">ventilateur</field><value name="chain"><block type="call_expression_editable_return" id="wX|:X(.R;~wCjC$Q2@}%"><mutation items="1"></mutation><field name="NAME">value</field><value name="items0"><block type="math_number" id="k8BDIzA@mM*}m2V%Eq8d"><field name="NUM">1</field></block></value></block></value></block></statement><next><block type="controls_if" id="F#$[pqcK_N{oYbH/^!EO"><statement name="DO0"><block type="call_expression" id="tqQqoH4vfNYmrRny-Tsc"><field name="NAME">ventilateur</field><value name="chain"><block type="call_expression_editable_return" id="tMeN(XP;]g^N!([Bloc|"><mutation items="1"></mutation><field name="NAME">value</field><value name="items0"><block type="math_number" id="iuM{8l]4]bJpw5gDfKUe"><field name="NUM">0</field></block></value></block></value></block></statement><next><block type="text_comment" id="9FQwJ-MZUAhD_Zxq,2=G"><field name="TEXT"> F03 Aspirateur
</field><next><block type="controls_if" id="wZ_7%rvg@t^Ij%(_g?W;"><statement name="DO0"><block type="call_expression" id="9e(fh*zIxk3WJJ3+ZlT:"><field name="NAME">aspirateur</field><value name="chain"><block type="call_expression_editable_return" id="$AXvt~P|az%4SbzV)Trz"><mutation items="1"></mutation><field name="NAME">value</field><value name="items0"><block type="math_number" id="]}oYNMrCb6?Kijo}#9`U"><field name="NUM">1</field></block></value></block></value></block></statement><next><block type="controls_if" id="c;*6ctpOJ#1/ugv+baJ1"><statement name="DO0"><block type="call_expression" id="b2kuCnNRYQ!o`@LtasY1"><field name="NAME">aspirateur</field><value name="chain"><block type="call_expression_editable_return" id="hqVwboi@Tpfj@w/4m:]N"><mutation items="1"></mutation><field name="NAME">value</field><value name="items0"><block type="math_number" id=":vpNP2niTpq{7od8KKm?"><field name="NUM">0</field></block></value></block></value></block></statement><next><block type="text_comment" id="C_Q-mfm4j}ZUG0!d@.QA"><field name="TEXT"> F02 Lumière (Contrôle manuel)
</field><next><block type="controls_if" id="TIUp867FM3#K!N.4geCI"><statement name="DO0"><block type="call_expression" id="h0$^[h{$~S%30i`{?O03"><field name="NAME">lumiere</field><value name="chain"><block type="call_expression_editable_return" id="[LaKiS(^nj8DRM*p?cs7"><mutation items="1"></mutation><field name="NAME">value</field><value name="items0"><block type="math_number" id="G{teqVrdHD/2.p1-x@:k"><field name="NUM">1</field></block></value></block></value><next><block type="variables_set" id="0X4U~X%KWt8Wpo/X6*MT"><field name="VAR" id="7(Y/PY9tW`]:fu`ZFKd]">lumiere_mode_auto</field><value name="VALUE"><block type="logic_boolean" id=",7?.}1i:eS`Jt=X2EEy1"><field name="BOOL">FALSE</field></block></value></block></next></block></statement><next><block type="controls_if" id="Nv#wYWMDMo}(|rUaZYnE"><statement name="DO0"><block type="call_expression" id="RIwLlqB:RT#77RKD+XK|"><field name="NAME">lumiere</field><value name="chain"><block type="call_expression_editable_return" id="%w.WrfW~F^Rp=[ZKC5O+"><mutation items="1"></mutation><field name="NAME">value</field><value name="items0"><block type="math_number" id="1?L^HTRF%gE;^EUN*B(Z"><field name="NUM">0</field></block></value></block></value><next><block type="variables_set" id="@@W#/Mcz77hbMm}F?E9S"><field name="VAR" id="7(Y/PY9tW`]:fu`ZFKd]">lumiere_mode_auto</field><value name="VALUE"><block type="logic_boolean" id="~@^k49PLu:nUR(L6KRCf"><field name="BOOL">FALSE</field></block></value></block></next></block></statement><next><block type="text_comment" id="():w7e~vtd,-M1|4*{_#"><field name="TEXT"> F02 Lumière (Toggle Mode Auto)
</field><next><block type="controls_if" id="4.Cr@,!yqE4,o}m3j=3G"><statement name="DO0"><block type="variables_set" id="L{N.ZJ|s5?hahZ$q~[oO"><field name="VAR" id="7(Y/PY9tW`]:fu`ZFKd]">lumiere_mode_auto</field><value name="VALUE"><block type="logic_negate" id="!{%VODu.16M86EoqhE.W"><value name="BOOL"><block type="variables_get" id="68Gr}F~G!g=tlju6|vwr"><field name="VAR" id="7(Y/PY9tW`]:fu`ZFKd]">lumiere_mode_auto</field></block></value></block></value></block></statement><next><block type="text_comment" id="7?i%h!UY?G;X|t=T4}.r"><field name="TEXT"> Lecture des capteurs
</field><next><block type="variables_set" id="?F9w-T0*^OKhMY+d_%N?"><field name="VAR" id="N~Ppf]9W?d-v%Lc}e9uB">T</field><value name="VALUE"><block type="procedures_callreturn" id="q~n54ObKi|AM}8`NmPm{"><mutation name="lire_temperature"></mutation></block></value><next><block type="variables_set" id="-^Jrr^^aQ5yBVs_3u273"><field name="VAR" id="0o`:Iwr8TC_aB;2?!bO;">L</field><value name="VALUE"><block type="procedures_callreturn" id="*+NSqU{%oGHJp^C(4+7z"><mutation name="lire_luminosite"></mutation></block></value><next><block type="text_comment" id="52On2G|NuYAg1QB)Tr]C"><field name="TEXT"> Exécution de la logique automatique
</field><next><block type="procedures_callnoreturn" id="eC`JJ~YcX1/f;sY]MiQ3"><mutation name="verifier_thermoregulation"><arg name="temp_actuelle"></arg></mutation><value name="ARG0"><block type="variables_get" id="?}gW6(lt26rlWAYewoWV"><field name="VAR" id="N~Ppf]9W?d-v%Lc}e9uB">T</field></block></value><next><block type="procedures_callnoreturn" id="Y3ORxA.6w7rPz~Uy(-;#"><mutation name="verifier_eclairage"><arg name="lumi_actuelle"></arg></mutation><value name="ARG0"><block type="variables_get" id="{BpBE8%=X8WI33]F:^ET"><field name="VAR" id="0o`:Iwr8TC_aB;2?!bO;">L</field></block></value><next><block type="text_comment" id=")ZT~-:z6N(z_dlBLf0*1"><field name="TEXT"> Envoi de la page HTML
</field><next><block type="variables_set" id="i,7Yg6vj=x|e5;1%3e)D"><field name="VAR" id="JNU71{:*x3.0F@qGq#Lg">response</field><value name="VALUE"><block type="procedures_callreturn" id="5B`LE?X?azEkz3$6a(^4"><mutation name="web_page"><arg name="T"></arg><arg name="L"></arg><arg name="V_etat"></arg><arg name="L_etat"></arg><arg name="A_etat"></arg><arg name="T_cible"></arg></mutation><value name="ARG0"><block type="variables_get" id="iJTGoN7qI:Ew;;7[9[EH"><field name="VAR" id="N~Ppf]9W?d-v%Lc}e9uB">T</field></block></value><value name="ARG1"><block type="variables_get" id="t_zYtVK2{eUK6FVEk4IM"><field name="VAR" id="0o`:Iwr8TC_aB;2?!bO;">L</field></block></value><value name="ARG2"><block type="call_expression_return" id="~t^/Vb.aOdyFt#PpaMOS"><field name="NAME">ventilateur</field><value name="chain"><block type="call_expression_editable_return" id="M)ihiz5zQW~j2MsQCPfv"><field name="NAME">value</field></block></value></block></value><value name="ARG3"><block type="call_expression_return" id="u8(t#`Nc/vFBk$eODWR?"><field name="NAME">lumiere</field><value name="chain"><block type="call_expression_editable_return" id="{WAEHLpe+S4z()whKt8T"><field name="NAME">value</field></block></value></block></value><value name="ARG4"><block type="call_expression_return" id="{OYLxl8#`=9#`=xKaj/D"><field name="NAME">aspirateur</field><value name="chain"><block type="call_expression_editable_return" id="p;,U2+spZH23r!hfXTIB"><field name="NAME">value</field></block></value></block></value><value name="ARG5"><block type="variables_get" id="a*OO%{IS^(f.zLp@Vf~0"><field name="VAR" id="u_Osm_cFQA{J4TqE2,UH">TEMP_CIBLE</field></block></value></block></value><next><block type="call_expression" id="Sk9;[AQVcKq[H|6F2}|="><field name="NAME">conn</field><value name="chain"><block type="call_expression_editable_return" id="jti}^39`u3R[^RBku}(9"><mutation items="1"></mutation><field name="NAME">send</field><value name="items0"><block type="text" id="Co1zr@e9$lI]bKcD%4u="><field name="TEXT">HTTP/1.1 200 OK\n</field></block></value></block></value><next><block type="call_expression" id="SuOsWLE6.57%#Lg!c@MX"><field name="NAME">conn</field><value name="chain"><block type="call_expression_editable_return" id="ph,`UnSXim+BBd*=^Y@t"><mutation items="1"></mutation><field name="NAME">send</field><value name="items0"><block type="text" id="caM#:|9kdZJ]Jm1FKSk_"><field name="TEXT">Content-Type: text/html\n</field></block></value></block></value><next><block type="call_expression" id="spqADtc|;.upK9+tU:xq"><field name="NAME">conn</field><value name="chain"><block type="call_expression_editable_return" id="XjJQX98f^x!Y6O:ypwcg"><mutation items="1"></mutation><field name="NAME">send</field><value name="items0"><block type="text" id="AAEz3swnq=tDHaLEtArB"><field name="TEXT">Connection: close\n\n</field></block></value></block></value><next><block type="call_expression" id="4|2bfiL1]j;%zdY91ZOB"><field name="NAME">conn</field><value name="chain"><block type="call_expression_editable_return" id="H!x@P8pNnYDx~;R)HO_4"><mutation items="1"></mutation><field name="NAME">sendall</field><value name="items0"><block type="variables_get" id="N;w|Cy|J0zmVuCTpDV9Y"><field name="VAR" id="JNU71{:*x3.0F@qGq#Lg">response</field></block></value></block></value><next><block type="call_expression" id="`bq;UiXM$+2px|3xPlNN"><field name="NAME">conn</field><value name="chain"><block type="call_expression_editable_return" id="n;%?$_/6jtrZ)I%KUkMQ"><field name="NAME">close</field></block></value></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></statement><statement name="DO1"><block type="controls_if" id="OJi+nKc38~lInU$A.b;z"><statement name="DO0"><block type="print_with_separator" id="%C)u%wGj;UiZtJ3~KN0x"><mutation items="2"></mutation><value name="items0"><block type="text" id=".T$ij.hs5+R#Xf8j|f:C"><field name="TEXT">Erreur de connexion:</field></block></value><value name="items1"><block type="variables_get" id="4FgXVs)Z_wk[%rq@nlMS"><field name="VAR" id="3pEy:SD9oZW1X2+OjkU7">e</field></block></value></block></statement><next><block type="exception_try" id="2.R}{|z;r8}C_U}o0(ld"><mutation except="1" exceptarg="1"></mutation><statement name="EXC"><block type="call_expression" id="{_Wu_]r/Me-?[?VMNGQ("><field name="NAME">conn</field><value name="chain"><block type="call_expression_editable_return" id="+lcrl3:t;CVyoNrn,FRm"><field name="NAME">close</field></block></value></block></statement></block></next></block></statement></block></statement></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></statement><value name="RETURN"><block type="text" id="Asj5dX.F~|R}SE3=3N2@"><field name="TEXT"></field></block></value></block></xml>

Projet généré par Vittascience.
Ce fichier contient le code textuel ainsi que le code blocs. Il peut être importé de nouveau
sur l'interface http://vittascience.com/esp32

"""

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
