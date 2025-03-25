# MeinProjekt
Einrichten des GitHUB-Repositorys:
- Account bei GitHub erstellt
- neues Repository erstellt
- Repository benannt "MeinProjekt"
- README bei Erstellung hinzugefuegt

Erstellen eines SSH-Schluessels:
- Ueberprueft, ob Schluessel existiert: ls ~/.ssh/ -> nein
- Schluessel angelegt -> Syntaxfehler behoben
- Schluessel im Defaultverzeichnis, ohne Passwort angelegt
- privaten Schluessel zur lokalen Liste hinzugefuegt
- oeffentlichen Schluessel auf GitHub hinzugefuegt

Lokales Klonen, Konfigurieren, Erstellen Initialer Commits
- Verbindung mit Git hergestellt und "MeinProjekt" geklont
- user.name und user.email geaendert
- Python Datei in lokalen Projekt-Order geschoben
- Datei dem Main-Branch hinzugefuegt, dann committed

Erstellen des Feature Branches:
- neuen Branch 'feature' erstellt und hin gewechselt
- weitere Python Datei in lokalen Projekt-Order geschoben
- Datei dem Feature-Branch hinzugefuegt, dann committed
- urspruengliche Datei im Feature-Branch veraendert und committed
- zu Main-Branch gewechselt

Vorbereitung und Merge:
- urspruengliche Datei geandert und committed 
- feature nach main gemergt 
- Merge commit Nachricht nicht veraendert 
(Alle Aenderungen wurden uebernommen, kein Konflikt)

Anmerkungen zum Arbeitsprozess:
- MeinProjekt wurde letztlich in anderen Ordner als angedacht geklont 
(in .ssh statt Git-Teilpruefung)
-> der erste Kopierversuch ist misslungen, da ich Github noch nicht
den oeffentlichen Schluessel mitgeteilt hatte
-> im Zuge dessen war ich ins .ssh Verzeichnis gerutscht und nicht zurueck gewechselt
- waehrend der Eingabe der Befehle traten haeufig Syntaxfehler auf

