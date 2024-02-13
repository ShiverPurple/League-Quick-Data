<p align=”center”>
<a href=https://www.linkedin.com/in/wandersongasco/>
<img src=https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin&labelColor=blue>
</a>
<a href=https://github.com/WandersonKnight/League-Quick-Data/blob/main/README.en.md/>
<img src=https://img.shields.io/badge/lang-en-red>
</a>
</a>
<a href=https://github.com/WandersonKnight/League-Quick-Data/blob/main/README.md/>
<img src=https://img.shields.io/badge/lang-pt--br-success>
</a>
</p>

# League Quick Data

## What it does

The program returns a summary of the 10 last matches of a player, up to 5 players simultaneously. Along of their matches, it returns a summary of their profile displaying: rank, winrate and the recent played champions' kda.

To lower the search time, every time it's used the application will download the missing icons and images from RIOT Datadragon API to the user's PC.

### Elements displayed

Profile summary:

* Player name
* Player rank
* Winrate from the last 10 matches
* Average KDA from the last 10 matches
* Most played champions recently
* Winrate of the most played champions recently
* Average KDA of the most played champions recently

Match summary:

* Champion played
* Gamemode
* Spells
* Level
* Items purchased
* KDA
* Total gold earned
* Map
* Game time length
* Game date

## How it works

### GUI

The user interface consists of: Python' standard interface package 'Tkinter', icons and borders made specifically for the program and image files returned from RIOT Datadragon API.

#### Before search

<img src="https://user-images.githubusercontent.com/39245594/147681869-c59ad6be-af8b-4488-a0de-de9c3dd6fcfa.png" alt="Default window" width="600"/>

#### After search

<img src="https://user-images.githubusercontent.com/39245594/147681961-d7c06b38-addf-4c80-a9b2-a74a59aa5854.png" alt="Information window" width="600"/>

### External API interaction

The 'requests' package is used to receive temporary data like name, kda and Ids, the package is also used to download frequently used objects, like icons for spells, champions and items.

Some of the API functions requires a personal key provided by RIOT, with only it's requests limitations being removed upon formal registration of the application in the RIOT developers site.


# Final Thoughts

Any changes made by RIOT after 11/08/21 won't be covered by this program.

Riot Developer key needed. The non-commercial key will allow a maximum of 3 simultaneous searches due to Riot's request limit.
