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

### External API interaction

The 'requests' package is used to receive temporary data like name, kda and Ids, the package is also used to download frequently used objects, like icons for spells, champions and items.

Some of the API functions requires a personal key provided by RIOT, with only it's requests limitations being removed upon formal registration of the application in the RIOT developers site.

### Build and search time

Multithreading with a 10 thread limit along with the download of frequently used files are some of the tools used to make the application runtime faster to provide a better user experience.

## Developer's philosophy

As I developed and refactored the program, i followed some personal principles:

### Simple is better than complicated, which doesn't mean it can't be complex

Simplicity is used so at first look a developer within any proficiency level can understand the code.
To make something complex look simple is a bigger task than making something easy look complicated.

### Essecial is what it's necessary to make the program run well, being it the minimal code possible

Without affecting it's quality, the code needed to work must be the minimal possible. If a solution already exists, it probably also exists a smaller and simpler way of doing it.

### Clarity above simplicity, simplicity above 'super-eficiency'

Clarity on it's structure, in each function name, variable and class is more important than excessive code miniaturization because excessive code miniaturization can make it harder to understand how the code works.
Although clarity comes first, simplicity it's more valuable than complex syntax used to gain miliseconds of efficiency;

### Efficiency and speed to give a good user experience, not for benchmarks

In programs with simple functionality like this one, efficiency and speed are only valuable as far as human perception go.

### Clarity in a code's structure removes unnecessary notations

The clearer and cleaner the code and each of it's functions is, the less notations needed. Although communicating through code is harder than plain language, it's more efficient.
