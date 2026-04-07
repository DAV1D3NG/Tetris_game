# Tetris in Python

## 🇬🇧 English

### Description

A simple Tetris game built in Python using the **Pygame** library.

The project is organized in a modular way and includes several typical game features:

* Ghost piece (shows where the piece will land)
* Next piece preview
* Increasing speed with score
* Pause, restart, and exit
* Audio system (music and sound effects)

---

### Requirements

* Python 3.x
* Pygame

Installation:

```bash
pip install pygame
```

---


### Running the game

Open the terminal in the main project folder (where `main.py` is located) and run:

```bash
python main.py
```

**Note**: do not run files inside `src/`, otherwise imports may not work correctly.

---

### Project structure

```
tetris/
│
├── main.py              # Game entry point
│
├── src/                 # Game logic
│   ├── __init__.py
│   ├── game.py
│   ├── config.py
│   ├── grid.py
│   ├── piece.py
│   ├── render.py
│   ├── audio.py
│   ├── input_handler.py
│   └── utils.py
│
├── assets/              # Resources (images, sounds, music)
│   ├── sounds/
│   ├── music/
│   └── images/
│
├── data/                # Saved data (High Score)
│   └── highscore.txt
```

---

### Controls

* ⬅️ / ➡️ → Move the piece horizontally
* ⬇️ → Soft drop
* ⬆️ → Rotate the piece (clockwise)
* Space → Hard drop (piece falls instantly)
* P → Pause
* R → Restart
* M → Toggle Music
* K → Toggle Sound Effects (SFX)
* ESC → Exit the game (close window)

---

### Game objective

Complete horizontal lines without leaving gaps.
Each completed line is removed and increases the score.
More lines cleared simultaneously give higher points.
The game ends when blocks reach the top of the grid.

---

### Main features

* Score system with local high score saving
* Increasing falling speed and music tempo as the game progresses
* Next piece preview
* Ghost piece (landing preview)
* Audio controls (Music and SFX adjustable and toggleable separately)

---

### Important files

* `main.py` → game entry point
* `game.py` → main logic (coordinates all other files)
* `piece.py` → piece management (Piece class)
* `grid.py` → game grid management
* `render.py` → graphical rendering

---

### License

This project is distributed under the GNU GPL license; for more details, see the [LICENSE.md](LICENSE) file.

---

### Author

Davide D'Angelo (DAVIDENG): creator of the entire project.

---------------------------------------------------------------------------------------------------------------------------------------------------------------

# Tetris in Python

## 🇮🇹 Italiano

### Descrizione

Un semplice gioco Tetris realizzato in Python utilizzando la libreria **Pygame**.

Il progetto è organizzato in modo modulare e include diverse funzionalità tipiche del gioco:

* Ghost piece (mostra dove cadrà il pezzo)
* Anteprima del prossimo pezzo
* Aumento della velocità con il punteggio
* Pausa, riavvio e uscita
* Sistema audio (musica ed effetti sonori)

---

### Requisiti

* Python 3.x
* Pygame

Installazione:

```bash
pip install pygame
```

---

### Avvio del gioco

Apri il terminale nella cartella principale del progetto (dove si trova `main.py`) ed esegui:

```bash
python main.py
```

**Nota:** non avviare i file dentro `src/`, altrimenti gli import potrebbero non funzionare correttamente.

---

### Struttura del progetto

```
tetris/
│
├── main.py              # Avvio del gioco
│
├── src/                 # Logica del gioco
│   ├── __init__.py
│   ├── game.py
│   ├── config.py
│   ├── grid.py
│   ├── piece.py
│   ├── render.py
│   ├── audio.py
│   ├── input_handler.py
│   └── utils.py
│
├── assets/              # Risorse (immagini, suoni, musica)
│   ├── sounds/
│   ├── music/
│   └── images/
│
├── data/                # Dati salvati (Record)
│   └── highscore.txt
```

---

### Controlli

* ⬅️ / ➡️ → Muovere il pezzo orizzontalmente
* ⬇️ → Accelerare la discesa (Soft Drop)
* ⬆️ → Ruotare il pezzo (Senso Orario)
* Spazio → Cadere il pezzo fino a terra (Hard Drop)
* P → Pausa
* R → Riavvia
* M → Muta/Smuta la Musica
* K → Muta/Smuta gli Effetti Sonori (SFX)
* ESC → Esce dal Gioco (Chiude la Finestra)

---

### Obiettivo del gioco

Completare righe orizzontali senza lasciare spazi vuoti.
Ogni riga completata viene eliminata e aumenta il punteggio.
Più righe completate in contemporanea danno più punti.
Il gioco termina quando i blocchi raggiungono la parte superiore della griglia.

---

### Funzionalità principali

* Sistema di punteggio con salvataggio del record in file locale
* Velocità crescente della caduta dei pezzi e anche della musica durante la partita
* Anteprima del prossimo pezzo
* Ghost piece (anteprima di dove cadrà)
* Controlli audio (Musica e SFX regolabili e mutabili separatamente)

---

### File principali

* `main.py` → avvio del gioco
* `game.py` → logica principale (raggruppa tutti file.py)
* `piece.py` → gestione dei pezzi (classe Piece)
* `grid.py` → gestione della griglia di gioco
* `render.py` → rendering grafico

---

### Licenza

Questo progetto è distribuito sotto licenza GNU GPL; per ulteriori dettagli, consultare il file [LICENSE.md](LICENSE)

---

### Autore

Davide D'Angelo (DAVIDENG): realizzatore dell'intero progetto.
