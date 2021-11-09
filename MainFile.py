import tkinter
import requests
import ujson
import datetime
from PIL import ImageTk,Image 
from tkinter import ttk
from concurrent import futures

# pip install: requests, pillow, ujson

#region Static Requests

key = "RGAPI-7cc920a9-e9c7-4924-9b90-188594617e9b"

# ----------- Request Session -----------

sessionSummoner = requests.Session()
sessionRank = requests.Session()
sessionMatch = requests.Session()
sessionMatchList = requests.Session()

# ----------- Current Patch -----------

patchesJson = requests.get("https://ddragon.leagueoflegends.com/api/versions.json")
patches = ujson.loads(patchesJson.text)

currentPatch = patches[0]

# ----------- Static League Data -----------

summonerSpellJsonData = requests.get(f"http://ddragon.leagueoflegends.com/cdn/{currentPatch}/data/en_US/summoner.json")
summonerSpellRawData = ujson.loads(summonerSpellJsonData.text)["data"]

mapListJsonData = requests.get("https://static.developer.riotgames.com/docs/lol/maps.json")
mapListRawData = ujson.loads(mapListJsonData.text)

#endregion

root = tkinter.Tk()
root.title("Quick League Data")
root.iconbitmap("LQ.ico")
root.configure(background = "black")
root.resizable(False, False)

#region Languages

class ChangeRegion:

    def __init__(self, languageDict = None, buttonSearchLang = None, sessionRegionLang = None, matchResultLang = None):
        
        self.languageDict = languageDict

        self.buttonSearchLang = buttonSearchLang
        self.sessionRegionLang = sessionRegionLang
        self.matchResultLang = matchResultLang

    def CreateDict(self):

        self.languageDict = {"searchButton":["BUSCAR", "SEARCH"], "sessionRegion":["BR", "NA"], "gameResult":[["VITORIA", "DERROTA"], ["VICTORY", "DEFEAT"]]}

        self.buttonSearchLang = self.languageDict["searchButton"][0]
        self.sessionRegionLang = self.languageDict["sessionRegion"][0]
        self.matchResultLang = self.languageDict["gameResult"][0]

    def RegionNA(self, buttonSearch, buttonBR, buttonNA):

        self.buttonSearchLang = self.languageDict["searchButton"][1]
        self.sessionRegionLang = self.languageDict["sessionRegion"][1]
        self.matchResultLang = self.languageDict["gameResult"][1]

        buttonSearch.configure(text = self.buttonSearchLang)

        buttonBR.configure(background = "black")
        buttonNA.configure(background = "#10293f")

    def RegionBR(self, buttonSearch, buttonBR, buttonNA):

        self.buttonSearchLang = self.languageDict["searchButton"][0]
        self.sessionRegionLang = self.languageDict["sessionRegion"][0]
        self.matchResultLang = self.languageDict["gameResult"][0] 

        buttonSearch.configure(text = self.buttonSearchLang)
        
        buttonBR.configure(background = "#10293f")
        buttonNA.configure(background = "black")

regionMethods = ChangeRegion()
regionMethods.CreateDict()

#endregion

# ----------- Search Button -----------

searchButtonBorder = tkinter.Frame(root, background = "#048195")
searchButtonBorder.grid(row = 0, column = 2, sticky = "nswe")
searchButtonBorder.grid_columnconfigure(0, weight = 1)

searchButton = tkinter.Label(searchButtonBorder, text = "BUSCAR", font = ("", 8, "bold"), background = "black", foreground = "white", borderwidth = 3)
searchButton.grid(row = 0, column = 0, sticky = "nswe", padx = 2, pady = 2)

# ----------- Region Buttons -----------

languageFrame = tkinter.Frame(root, width = 10, background = "#024e64")
languageFrame.grid(row = 0, column = 4, sticky = "e")

brButton = tkinter.Button(languageFrame,
                            width = 3, 
                            text = "BR",
                            font = ("Arial", 9, "bold"),
                            activebackground = "#07141f", 
                            activeforeground = "white",
                            foreground = "white", 
                            background = "black", 
                            relief = "ridge", 
                            borderwidth = 0,
                            command = lambda: regionMethods.RegionBR(searchButton, brButton, naButton))
brButton.grid(row = 0, column = 0, padx = 1, pady = 1)

naButton = tkinter.Button(languageFrame,
                            width = 3, 
                            text = "NA",
                            font = ("Arial", 9, "bold"),
                            activebackground = "#07141f", 
                            activeforeground = "white",
                            foreground = "white", 
                            background = "black", 
                            relief = "ridge", 
                            borderwidth = 0,
                            command = lambda: regionMethods.RegionNA(searchButton, brButton, naButton))
naButton.grid(row = 0, column = 1, padx = 1, pady = 1)

regionMethods.RegionBR(searchButton, brButton, naButton)

# ----------- Scrollbar Style -----------

style = ttk.Style()

style.theme_use("classic")
style.map("TScrollbar", background=[('pressed', '!focus', '#ae914b')],  relief=[('pressed', 'flat')])
style.configure("TScrollbar", troughcolor = "black", relief = "flat",  background = "#775829", arrowsize = 0, width = 5, borderwidth = 0)

#region Entries

player1 = tkinter.Entry(root, width = 22, 
                        background = "black", 
                        foreground = "white", 
                        borderwidth = 0, 
                        highlightthickness = 2, 
                        highlightcolor = "#775829", 
                        highlightbackground = "#775829", 
                        insertbackground = "light grey", 
                        insertborderwidth = 1, 
                        relief= "ridge")
player1.grid(row = 1, column = 0, sticky = "we")

player2 = tkinter.Entry(root, width = 22, 
                        background = "black", 
                        foreground = "white", 
                        borderwidth = 0, 
                        highlightthickness = 2, 
                        highlightcolor = "#775829", 
                        highlightbackground = "#775829", 
                        insertbackground = "light grey", 
                        insertborderwidth = 1, 
                        relief= "ridge")
player2.grid(row = 1, column = 1, sticky = "we")

player3 = tkinter.Entry(root, width = 22, 
                        background = "black", 
                        foreground = "white", 
                        borderwidth = 0, 
                        highlightthickness = 2, 
                        highlightcolor = "#775829", 
                        highlightbackground = "#775829", 
                        insertbackground = "light grey", 
                        insertborderwidth = 1, 
                        relief= "ridge")
player3.grid(row = 1, column = 2, sticky = "we")

player4 = tkinter.Entry(root, width = 22, 
                        background = "black", 
                        foreground = "white", 
                        borderwidth = 0, 
                        highlightthickness = 2, 
                        highlightcolor = "#775829", 
                        highlightbackground = "#775829", 
                        insertbackground = "light grey", 
                        insertborderwidth = 1, 
                        relief= "ridge")
player4.grid(row = 1, column = 3, sticky = "we")

player5 = tkinter.Entry(root, width = 22, 
                        background = "black", 
                        foreground = "white", 
                        borderwidth = 0, 
                        highlightthickness = 2, 
                        highlightcolor = "#775829", 
                        highlightbackground = "#775829", 
                        insertbackground = "light grey", 
                        insertborderwidth = 1, 
                        relief= "ridge")
player5.grid(row = 1, column = 4, sticky = "we")

playerArray = [player1, player2, player3, player4, player5]

#endregion

#region Gui creation methods

scrollBarArray = [0, 0, 0, 0, 0]

# ----------- Frame Buttons -----------

playerHistoryButtonArray = [0, 0, 0, 0, 0]

def CreateButtonBG():

    for i in range(5):

        if playerArray[i].get():

            buttonBackground = tkinter.Label(root, background = "black", foreground = "white")
            buttonBackground.grid(row = 2, columnspan = 5, sticky = "nswe")

            break

        if i == 4:
            buttonBackground = tkinter.Label(root, background = "black", foreground = "white", text = "Null")
            buttonBackground.grid(row = 2, columnspan = 5, sticky = "nswe")

def CreateHistoryButton(playerNumber):

    historyButtonBorder = tkinter.Frame(root, background = "#ae914b")
    historyButtonBorder.grid(row = 2, column = playerNumber, sticky = "we")
    historyButtonBorder.grid_columnconfigure(0, weight = 1)

    playerHistoryButton = tkinter.Label(historyButtonBorder, text = playerArray[playerNumber].get(), font = ("", 9, "bold"), background = "#0e191d", 
    foreground = "#fff6d6", borderwidth = 2)
    playerHistoryButton.grid(row = 0, column = 0, sticky = "we", padx = 1, pady = 1)

    playerHistoryButtonArray[playerNumber] = playerHistoryButton

# ----------- Frames -----------

scrollableMainFrameArray = [0, 0, 0, 0, 0]
historyFrameArray = [0, 0, 0, 0, 0]

def CreateHistoryFrame(playerNumber):

    scrollableFrame = tkinter.Frame(root, height = 450, width = 680, background = "black")
    scrollableFrame.grid(row = 4, columnspan = 5, sticky = "nsew")
    scrollableFrame.grid_columnconfigure((0, 1), weight = 1)

    canvasLayout = tkinter.Canvas(scrollableFrame, height = 450, width = 680, background = "black", highlightthickness = 0, scrollregion = (0, 0, 0, 980))
    canvasLayout.grid(row=0, column = 0, sticky = "nsew")
    
    historyFrame = tkinter.Frame(canvasLayout, height = 450, width = 680, background = "black")
    canvasLayout.create_window((0, 0), window = historyFrame, anchor = "nw")

    scrollbar = ttk.Scrollbar(scrollableFrame, orient = "vertical", command = canvasLayout.yview)
    scrollbar.grid(row = 0, column = 1, sticky = "nse", padx = (4, 3), pady = (0, 3))

    canvasLayout.configure(yscrollcommand = scrollbar.set)

    # ----------- Scroll Function -----------

    def MouseWheelMove(event):
        canvasLayout.yview_scroll(-1 * (event.delta // 120), "units")

    scrollbar.bind_all("<MouseWheel>", MouseWheelMove)

    scrollableMainFrameArray[playerNumber] = scrollableFrame
    historyFrameArray[playerNumber] = historyFrame

# ----------- Match Previews -----------

playerMatchArray = [0, 0, 0, 0, 0]

def CreateMatchPreview(playerNumber):

    matchArray = []

    for i in range(11):

        if i == 0:
            ProfileSummary.CreateProfileFrame(playerNumber)

        else:
            match = tkinter.Frame(historyFrameArray[playerNumber], height = 85, width = 680, background = "black")
            match.grid(pady = (6, 0), columnspan = 5)
            match.grid_rowconfigure((0,1) ,  weight = 1)
            match.grid_columnconfigure((0,1,2,3) ,  weight = 1)
            match.grid_propagate(False)

            matchArray.append(match)

    playerMatchArray[playerNumber] = matchArray

#endregion

#region Classes

championCircleFrame = ImageTk.PhotoImage(Image.open("circlebig.png").resize((75, 75)))
levelCircleFrame = ImageTk.PhotoImage(Image.open("circlesma.png").resize((23, 23)))
minionIcon = ImageTk.PhotoImage(Image.open("minion.png").resize((11, 13)))
goldIcon = ImageTk.PhotoImage(Image.open("gold.png").resize((15, 12)))

itemList1 = [[],[],[],[],[],[],[],[],[],[]]
itemList2 = [[],[],[],[],[],[],[],[],[],[]]
itemList3 = [[],[],[],[],[],[],[],[],[],[]]
itemList4 = [[],[],[],[],[],[],[],[],[],[]]
itemList5 = [[],[],[],[],[],[],[],[],[],[]]

spellList1 = [[],[],[],[],[],[],[],[],[],[]]
spellList2 = [[],[],[],[],[],[],[],[],[],[]]
spellList3 = [[],[],[],[],[],[],[],[],[],[]]
spellList4 = [[],[],[],[],[],[],[],[],[],[]]
spellList5 = [[],[],[],[],[],[],[],[],[],[]]

championList = [[],[],[],[],[],[],[],[],[],[]]

summaryChampionIconArray = [[],[],[],[],[]]

profileSummaryArray = [0, 0, 0, 0, 0]

# ----------- Get Data -----------

class SummaryStats:

    def __init__(self, matchesWon = None, matchesLost = None, averageKill = None, averageDeath = None, averageAssist = None, championDictOrder = None):

        self.matchesWon = matchesWon
        self.matchesLost = matchesLost

        self.averageKill = averageKill
        self.averageDeath = averageDeath
        self.averageAssist = averageAssist

        self.championDictOrder = championDictOrder

    def GetSummaryWins(self, matchRawDataArray, playerPuuid): #Recent win/lose/winrate

        self.matchesWon = 0
        self.matchesLost = 0

        for i in range(10):
            
            if len(matchRawDataArray) >= i + 1:

                participants = matchRawDataArray[i]["metadata"]["participants"]
                if matchRawDataArray[i]["info"]["participants"][participants.index(playerPuuid)]["win"]:

                    self.matchesWon += 1

                else:

                    self.matchesLost += 1

    def GetSummaryKda(self, matchRawDataArray, playerPuuid): #Player kda

        self.averageKill = 0
        self.averageDeath = 0
        self.averageAssist = 0

        for i in range(10):
            if len(matchRawDataArray) >= i + 1:
                participants = matchRawDataArray[i]["metadata"]["participants"]

                self.averageKill += matchRawDataArray[i]["info"]["participants"][participants.index(playerPuuid)]["kills"]
                self.averageDeath += matchRawDataArray[i]["info"]["participants"][participants.index(playerPuuid)]["deaths"]
                self.averageAssist += matchRawDataArray[i]["info"]["participants"][participants.index(playerPuuid)]["assists"]

    def GetSummaryChampions(self, matchRawDataArray, playerPuuid, player):

        championDict = {}

        participantsArray = []
        championPlayedArray = []

        # ----------- Recent Champion Names -----------

        for i in range(10):
            if len(matchRawDataArray) >= i + 1:
                participants = matchRawDataArray[i]["metadata"]["participants"]
                participantsArray.append(participants)

                championPlayedArray.append(matchRawDataArray[i]["info"]["participants"][participants.index(playerPuuid)]["championName"])

        # ----------- Match Result -----------

        championIndex = 0

        for i in championPlayedArray:

            if i in championDict:

                if matchRawDataArray[championIndex]["info"]["participants"][participantsArray[championIndex].index(playerPuuid)]["win"]:
                    championDict[i][1] += 1

                else:
                    championDict[i][2] += 1

            else:

                if matchRawDataArray[championIndex]["info"]["participants"][participantsArray[championIndex].index(playerPuuid)]["win"]:
                    championDict[i] = [[0, 0, 0], 1, 0]

                else:
                    championDict[i] = [[0, 0, 0], 0, 1]

            championIndex += 1

        # ----------- Recent Champion Names -----------

        for i in range(10):

            if len(matchRawDataArray) >= i + 1:            
                championName = matchRawDataArray[i]["info"]["participants"][participantsArray[i].index(playerPuuid)]["championName"]

                championDict[championName][0][0] += matchRawDataArray[i]["info"]["participants"][participantsArray[i].index(playerPuuid)]["kills"]
                championDict[championName][0][1] += matchRawDataArray[i]["info"]["participants"][participantsArray[i].index(playerPuuid)]["deaths"]
                championDict[championName][0][2] += matchRawDataArray[i]["info"]["participants"][participantsArray[i].index(playerPuuid)]["assists"]
        
        # ----------- Sort Dictionary -----------

        self.championDictOrder = [[key, value] for (key, value) in championDict.items()]

        for i in range(len(championDict)):
            
            aux = 0

            for j in range(len(championDict) - 1):

                if (self.championDictOrder[j][1][1] + self.championDictOrder[j][1][2]) < (self.championDictOrder[j + 1][1][1] + self.championDictOrder[j + 1][1][2]):

                    aux = self.championDictOrder[j + 1]
                    self.championDictOrder[j + 1] = self.championDictOrder[j]
                    self.championDictOrder[j] = aux

        # ----------- Champion Icon -----------

        for i in range(3):

            if len(self.championDictOrder) >= i + 1:
                try:
                    image = ImageTk.PhotoImage(Image.open(f"datadragon/{self.championDictOrder[i][0]}.png").resize((32,32)))

                except:
                    response = requests.get(f"http://ddragon.leagueoflegends.com/cdn/{currentPatch}/img/champion/{self.championDictOrder[i][0]}.png")
                    if response.status_code == 200:
                        open(f"datadragon/{self.championDictOrder[i][0]}.png", 'wb').write(response.content)
                        
                    image = ImageTk.PhotoImage(Image.open(f"datadragon/{self.championDictOrder[i][0]}.png").resize((32, 32)))

                summaryChampionIconArray[player].append(image)

class PlayerStats:

    def __init__(self, playerPuuid = None, encryptedSummonerId = None, playerRank = None):

        self.playerPuuid = playerPuuid #"puuid" - summoner api
        self.encryptedSummonerId = encryptedSummonerId #"id" - summoner api
        
        self.playerRank = playerRank #"tier + rank" - leagueV4 api

    def PlayerDataRequest(self, name):
        
        if regionMethods.sessionRegionLang == "BR":
            playerJsonData = sessionSummoner.get(f"https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}?api_key={key}")
            playerRawData = ujson.loads(playerJsonData.text)

        else:
            playerJsonData = sessionSummoner.get(f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}?api_key={key}")
            playerRawData = ujson.loads(playerJsonData.text)

        try:
            self.playerPuuid = playerRawData["puuid"]
            self.encryptedSummonerId = playerRawData["id"]
            print(self.playerPuuid)

        except:
            return 0

        else:
            return 1

    def PlayerRankRequest(self):
        
        if regionMethods.sessionRegionLang == "BR":
            playerRankJsonData = sessionRank.get(f"https://br1.api.riotgames.com/lol/league/v4/entries/by-summoner/{self.encryptedSummonerId}?api_key={key}")
            playerRankRawData = ujson.loads(playerRankJsonData.text)

        else:
            playerRankJsonData = sessionRank.get(f"https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/{self.encryptedSummonerId}?api_key={key}")
            playerRankRawData = ujson.loads(playerRankJsonData.text)

        try:
            self.playerRank = playerRankRawData[0]["tier"] + " " + playerRankRawData[0]["rank"]
            if playerRankRawData[0]["tier"] == "MASTER" or "GRANDMASTER" or "CHALLANGER":
                self.playerRank = playerRankRawData[0]["tier"]

        except:
            self.playerRank = "Unranked"

class MatchStatsChampion:

    def __init__(self, championId = None, championLevel = None):

        self.championId = championId #"championId" - match api
        self.championLevel = championLevel #"champLevel" - #match api

    def MatchStatsChampionRequest(self, matchRawData, playerKey, player):

        participants = matchRawData["metadata"]["participants"]

        self.championId = matchRawData["info"]["participants"][participants.index(playerKey)]["championName"]
        self.championLevel = matchRawData["info"]["participants"][participants.index(playerKey)]["champLevel"]

        try:
            image = ImageTk.PhotoImage(Image.open(f"datadragon/{self.championId}.png").resize((60,60)))

        except:
            response = requests.get(f"http://ddragon.leagueoflegends.com/cdn/{currentPatch}/img/champion/{self.championId}.png")
            if response.status_code == 200:
                open(f"datadragon/{self.championId}.png", 'wb').write(response.content)

            image = ImageTk.PhotoImage(Image.open(f"datadragon/{self.championId}.png").resize((60,60)))
            
        championList[player].append(image)

class MatchStatsSpells:

    def __init__(self, spellArrayIds = None, spellSpriteName = None):

        self.spellArrayIds = spellArrayIds #["Summoner1Id", "Summoner2Id"] - #match api
        self.spellSpriteName = spellSpriteName #[spells[0], spells[1]] - #key in http://ddragon.leagueoflegends.com/cdn/11.19.1/data/en_US/summoner.json

    def MatchStatsSpellsRequest(self, matchRawData, playerKey):

        participants = matchRawData["metadata"]["participants"]

        self.spellArrayIds = [0, 0]
        self.spellSpriteName = [0, 0]

        self.spellArrayIds[0] = matchRawData["info"]["participants"][participants.index(playerKey)]["summoner1Id"]
        self.spellArrayIds[1] = matchRawData["info"]["participants"][participants.index(playerKey)]["summoner2Id"]

        for spellDict in summonerSpellRawData.values():
            if spellDict["key"] == f"{self.spellArrayIds[0]}":
                self.spellSpriteName[0] = (spellDict["id"])

            elif spellDict["key"] == f"{self.spellArrayIds[1]}":
                self.spellSpriteName[1] = (spellDict["id"])

    def GetSpellSprites(self, player, preview):

        for i in range(2):

            if self.spellSpriteName[i] != 0:
                try:
                    image = ImageTk.PhotoImage(Image.open(f"datadragon/{self.spellSpriteName[i]}.png").resize((18, 18)))

                except:
                    response = requests.get(f"http://ddragon.leagueoflegends.com/cdn/{currentPatch}/img/spell/{self.spellSpriteName[i]}.png")
                    if response.status_code == 200:
                        open(f"datadragon/{self.spellSpriteName[i]}.png", 'wb').write(response.content)

                    image = ImageTk.PhotoImage(Image.open(f"datadragon/{self.spellSpriteName[i]}.png").resize((18, 18)))

                if player == 0:
                    spellList1[preview].append(image)

                elif player == 1:
                    spellList2[preview].append(image)

                elif player == 2:
                    spellList3[preview].append(image)

                elif player == 3:
                    spellList4[preview].append(image)

                elif player == 4:
                    spellList5[preview].append(image)

        if player == 0:
            return spellList1

        elif player == 1:
            return spellList2

        elif player == 2:
            return spellList3

        elif player == 3:
            return spellList4

        elif player == 4:
            return spellList5

class MatchStatsItems:

    def __init__(self, itemArray = None):

        self.itemArray = itemArray #["num", "num", "num", "num", "num", "num", "num"] - #match api

    def MatchStatsItemsRequests(self, matchRawData, playerKey):

        participants = matchRawData["metadata"]["participants"]

        self.itemArray = []

        for i in range(7):
            self.itemArray.append(matchRawData["info"]["participants"][participants.index(playerKey)][f"item{i}"])

    def GetItemSprites(self, player, preview):

        for i in range(7):

            if self.itemArray[i] != 0:
                try:
                    image = ImageTk.PhotoImage(Image.open(f"datadragon/{self.itemArray[i]}.png").resize((32, 32)))

                except:
                    response = requests.get(f"http://ddragon.leagueoflegends.com/cdn/{currentPatch}/img/item/{self.itemArray[i]}.png")
                    if response.status_code == 200:
                        open(f"datadragon/{self.itemArray[i]}.png", 'wb').write(response.content)

                    image = ImageTk.PhotoImage(Image.open(f"datadragon/{self.itemArray[i]}.png").resize((32, 32)))

                if player == 0:
                    itemList1[preview].append(image)

                elif player == 1:
                    itemList2[preview].append(image)

                elif player == 2:
                    itemList3[preview].append(image)

                elif player == 3:
                    itemList4[preview].append(image)

                elif player == 4:
                    itemList5[preview].append(image)

        if player == 0:
            return itemList1

        elif player == 1:
            return itemList2

        elif player == 2:
            return itemList3

        elif player == 3:
            return itemList4

        elif player == 4:
            return itemList5

class MatchStatsPlayer:

    def __init__(self, playerKills = None, playerDeaths = None, playerAssists = None, playerMinions = None, playerGold = None):

        self.playerKills = playerKills #"kill" - match api
        self.playerDeaths = playerDeaths #"death" - match api
        self.playerAssists = playerAssists #"assist" - match api

        self.playerMinions = playerMinions #"totalMinionsKilled" - match api

        self.playerGold = playerGold #"goldEarned" - match api

    def MatchStatsPlayerRequest(self, matchRawData, playerKey):

        participants = matchRawData["metadata"]["participants"]

        self.playerKills = matchRawData["info"]["participants"][participants.index(playerKey)]["kills"]
        self.playerDeaths = matchRawData["info"]["participants"][participants.index(playerKey)]["deaths"]
        self.playerAssists = matchRawData["info"]["participants"][participants.index(playerKey)]["assists"]

        self.playerMinions = matchRawData["info"]["participants"][participants.index(playerKey)]["totalMinionsKilled"]
        self.playerGold = matchRawData["info"]["participants"][participants.index(playerKey)]["goldEarned"]

        self.playerGold = '{:,}'.format(self.playerGold).replace(",", ".")

    def ScoreConstructor(self):
        
        return f"{self.playerKills} / {self.playerDeaths} / {self.playerAssists}"

class MatchStatsGame:

    def __init__(self, mapId = None, mapName = None, gameMode = None, gameCreation = None, gameDuration = None, matchResult = None):

        self.mapId = mapId #"mapId" - match api
        self.mapName = mapName #mapId > mapName https://static.developer.riotgames.com/docs/lol/maps.json

        self.gameMode = gameMode #"gameMode" - match api
        self.gameCreation = gameCreation #"gameCreation" - match api - unix to date
        self.gameDuration = gameDuration #"gameDuration" - match api - milisegundos
        self.matchResult = matchResult #"win" - match api

    def MatchModeRequest(self, matchRawData):

        self.mapId = matchRawData["info"]["mapId"]
        self.mapName = [mapValues["mapName"] for mapValues in mapListRawData if mapValues["mapId"] == self.mapId]
        self.mapName = self.mapName[0]

        self.gameMode = matchRawData["info"]["gameMode"]
        
    def MatchTimeRequest(self, matchRawData):

        gameCreationTimestamp = matchRawData["info"]["gameCreation"]
        gameCreationDatetime = datetime.datetime.fromtimestamp(gameCreationTimestamp/1000)
        
        if regionMethods.sessionRegionLang == "BR":
            self.gameCreation = gameCreationDatetime.strftime('%d / %m / %Y')
        else:
            self.gameCreation = gameCreationDatetime.strftime('%m / %d / %Y')

        if "gameEndTimestamp" in matchRawData["info"]:
            
            datatimeRaw = str(datetime.timedelta(seconds = matchRawData["info"]["gameDuration"]))

            if datatimeRaw[0] == "0":
                self.gameDuration = datatimeRaw[2:]
            else:
                self.gameDuration = datatimeRaw

        else:
            datatimeRaw = str(datetime.timedelta(seconds = (matchRawData["info"]["gameDuration"] // 1000)))

            if datatimeRaw[0] == "0":
                self.gameDuration = datatimeRaw[2:]
            else:
                self.gameDuration = datatimeRaw

    def GetMatchResult(self, matchRawData, playerKey):

        participants = matchRawData["metadata"]["participants"]

        self.matchResult = regionMethods.matchResultLang[0] if matchRawData["info"]["participants"][participants.index(playerKey)]["win"] else regionMethods.matchResultLang[1]

# ----------- Create Assets -----------

class ProfileSummary:

    def CreateProfileFrame(playerNumber):

        profileSummaryFrame = tkinter.Frame(historyFrameArray[playerNumber], height = 60, width = 680, background = "black")
        profileSummaryFrame.grid(columnspan = 5)
        profileSummaryFrame.grid_propagate(False)
        profileSummaryFrame.grid_rowconfigure(0, weight = 1)
        profileSummaryFrame.grid_columnconfigure((0, 1), weight = 1)

        profileSummaryArray[playerNumber] = profileSummaryFrame

    def CreateNameRank(profileSummaryArray, name, rank):

        nameRankFrame = tkinter.Frame(profileSummaryArray, height = 38, width = 135, background = "black")
        nameRankFrame.grid(row = 0, column = 0, sticky = "w")
        nameRankFrame.grid_propagate(False)
        nameRankFrame.grid_rowconfigure((0, 1), weight = 1)
        nameRankFrame.grid_columnconfigure(0, weight = 1)

        nameLabel = tkinter.Label(nameRankFrame, text = name, font = ("", 10, "bold"), background = "black", foreground = "white", borderwidth = 0, highlightthickness = 0)
        nameLabel.grid(row = 0, column = 0, sticky = "swe", pady = (0, 0))

        rankLabel = tkinter.Label(nameRankFrame, text = rank, font = ("", 10, "bold"), background = "black", foreground = "white", borderwidth = 0, highlightthickness = 0)
        rankLabel.grid(row = 1, column = 0, sticky = "nwe", pady = (0, 0))

        frameLine = tkinter.Frame(nameRankFrame, height = 1, width = 120, background = "#775829")
        frameLine.grid(row = 2, column = 0, pady = (5, 0))

    def CreateRecentMatches(profileSummaryArray, recentWinValue, recentLossValue, averageKill, averageDeath, averageAssist):

        # ----------- Recent Matches Stats -----------

        recentMatchesStats = tkinter.Frame(profileSummaryArray, height = 110, width = 152, background = "black")
        recentMatchesStats.grid(row = 0, column = 1, sticky = "w", pady = (7, 0))
        recentMatchesStats.grid_propagate(False)
        recentMatchesStats.grid_rowconfigure((0, 1), weight = 1)
        recentMatchesStats.grid_columnconfigure((0, 1), weight = 1)

        # ----------- Player Performance (Recent Matches Stats) -----------

        recentPerformance = tkinter.Frame(recentMatchesStats, height = 30, width = 150)
        recentPerformance.grid(row = 0, column = 0)
        recentPerformance.grid_propagate(False)
        recentPerformance.grid_rowconfigure((0, 1), weight = 1)
        recentPerformance.grid_columnconfigure((0), weight = 1)

        winrate = f"{recentWinValue} / {recentLossValue}"
        kda = f"{averageKill / 10} / {averageDeath / 10} / {averageAssist / 10}"

        recentWinrateLabel = tkinter.Label(recentPerformance, text = winrate, font = ("", 11, "bold"), background = "black", foreground = "white")
        recentWinrateLabel.grid(row = 0, column = 0, sticky = "we")

        averageKdaLabel = tkinter.Label(recentPerformance, text = kda, font = ("", 8, "bold"), background = "black", foreground = "white")
        averageKdaLabel.grid(row = 1, column = 0, sticky = "we")    
        
        # ----------- Winrate Stats (Recent Matches Stats) -----------

        winrateGraph = tkinter.Frame(recentMatchesStats, height = 22, width = 150, background = "black", highlightthickness = 0, borderwidth = 0)
        winrateGraph.grid(row = 1, column = 0, pady = (0, 4))
        winrateGraph.grid_propagate(False)
        winrateGraph.grid_columnconfigure((0, 1, 2), weight = 1)
        winrateGraph.grid_rowconfigure(0, weight = 1)

        recentWinsLabel = tkinter.Label(winrateGraph, text = f"{recentWinValue} V", font = ("", 10, "bold"), background = "black", foreground = "deep sky blue", borderwidth = 0, 
        highlightthickness = 0)
        recentWinsLabel.grid(row = 0, column = 0, sticky = "e")

        kdaBar = tkinter.Frame(winrateGraph, height = 15, width = 80, highlightthickness = 0, borderwidth = 0)
        kdaBar.grid(row = 0, column = 1)

        recentLossesLabel = tkinter.Label(winrateGraph, text = f"{recentLossValue} D", font = ("", 10, "bold"), background = "black", foreground = "red", borderwidth = 0, 
        highlightthickness = 0)
        recentLossesLabel.grid(row = 0, column = 2, sticky = "w")

        for i in range(recentWinValue):
            
            filledColor = tkinter.Canvas(kdaBar, height = 15, width = 8, background = "deep sky blue", highlightthickness = 0, borderwidth = 0)
            filledColor.grid(row = 0, column = i)

        for i in range(recentLossValue):
            
            filledColor = tkinter.Canvas(kdaBar, height = 15, width = 8, background = "red", highlightthickness = 0, borderwidth = 0)
            filledColor.grid(row = 0, column = recentWinValue + i)

        # ----------- Vertical Line (Recent Matches Stats) -----------

        frameLine = tkinter.Frame(recentMatchesStats, height = 110, width = 1, background = "#775829")
        frameLine.grid(row = 0,rowspan = 2, column = 1,sticky = "ns")
        
    def CreateRecentChampion(profileSummaryArray, championDict, championIconArray):

        recentChampionsFrame = tkinter.Frame(profileSummaryArray, height = 34, width = 381, background = "black")
        recentChampionsFrame.grid(row = 0, column = 2)
        recentChampionsFrame.grid_propagate(False)
        recentChampionsFrame.grid_columnconfigure((0, 1, 2), weight = 1)
        recentChampionsFrame.grid_rowconfigure(0, weight = 1)

        for i in range(3): 
            
            if len(championDict) >= i + 1:

                # ----------- Champion Data -----------

                championWinrate = f"{championDict[i][1][1]} / {championDict[i][1][2]}"
                championWinrate = championWinrate + "  (" + str("{:.0f}".format((championDict[i][1][1] / (championDict[i][1][1] + championDict[i][1][2])) * 100)) + "%)"

                championAverageKill = "{:.1f}".format(championDict[i][1][0][0] / (championDict[i][1][1] + championDict[i][1][2]))
                championAverageDeath = "{:.1f}".format(championDict[i][1][0][1] / (championDict[i][1][1] + championDict[i][1][2]))
                championAverageAssist = "{:.1f}".format(championDict[i][1][0][2] / (championDict[i][1][1] + championDict[i][1][2]))

                championKda = f"{championAverageKill} / {championAverageDeath} / {championAverageAssist}"

                # ----------- Recent Played Champion -----------

                mostPlayedChampion = tkinter.Frame(recentChampionsFrame, height = 34, width = 127, background = "black")
                mostPlayedChampion.grid(row = 0, column = i)
                mostPlayedChampion.grid_propagate(False)
                mostPlayedChampion.grid_columnconfigure((0, 1), weight = 1)
                mostPlayedChampion.grid_rowconfigure(0, weight = 1)

                # ----------- Champion Icon (Recent Played Champion) -----------

                championBorder = tkinter.Frame(mostPlayedChampion, height = 34, width = 34, background = "#775829", borderwidth = 0, highlightthickness = 0)
                championBorder.grid(row = 0, column = 0, sticky = "w")

                championIcon = tkinter.Canvas(championBorder, height = 32, width = 32, background = "black", borderwidth = 0, highlightthickness = 0)
                championIcon.grid(row = 0, column = 0, padx = 1, pady = 1)

                championIcon.create_image((16, 16), image = championIconArray[i])

                # ----------- Champion Stats Label (Recent Played Champion) -----------

                championStats = tkinter.Frame(mostPlayedChampion, height = 34, width = 84, background = "black", borderwidth = 0)
                championStats.grid(row = 0, column = 1, padx = (0, 6), sticky = "w")
                championStats.grid_propagate(False)
                championStats.grid_columnconfigure(0, weight = 1)
                championStats.grid_rowconfigure((0, 1), weight = 1)

                championWinrateLabel = tkinter.Label(championStats, text = championWinrate, font = ("Arial Narrow", 10, "bold"), background = "black", foreground = "white")
                championWinrateLabel.grid(row = 0, column = 0, sticky = "w" )

                championKdaLabel = tkinter.Label(championStats, text = championKda, font = ("Arial Narrow", 10, "bold"), background = "black", foreground = "white")
                championKdaLabel.grid(row = 1, column = 0, sticky = "w")

class MatchPreview:
    
    def ChampionCircle(frameNumber, championImage, playerLevel):

        circle = tkinter.Canvas(frameNumber, height = 85, width = 85, background = "black", highlightthickness = 0)
        circle.grid(row = 0, column = 0) 

        circle.create_image((42, 42), image = championImage)

        circle.create_image((42, 42), image = championCircleFrame)
        circle.create_image((65, 62), image = levelCircleFrame)

        circle.create_text((65, 63), text = playerLevel, fill = "#918c83", font = ("", 8, "bold"))

    def GamemodeResult(frameNumber, matchResult, gameMode, spellArray, preview):
       
        gamemodeResultFrame = tkinter.Frame(frameNumber, height = 63, width = 110, background = "black")
        gamemodeResultFrame.grid(row = 0, column = 1, pady = (14, 0), sticky= "nwe")
        gamemodeResultFrame.grid_rowconfigure((0 , 1, 2), weight = 1)
        gamemodeResultFrame.grid_propagate(False)

        # ----------- Match Result -----------     

        matchResultLabel = tkinter.Label(gamemodeResultFrame, text = matchResult, background = "black", 
        foreground = "red" if matchResult == regionMethods.matchResultLang[1] else "deep sky blue", borderwidth = 0, font = ("", 10, "bold")) #text = matchResult/gameMode
        
        matchResultLabel.grid(row = 0, column = 0, sticky = "nw")

        # ----------- Gamemode -----------

        matchGamemodeLabel = tkinter.Label(gamemodeResultFrame, text = gameMode, background = "black", foreground = "#918c83", borderwidth = 0, 
        font = ("", 9, "bold")) #text = matchResult/gameMode

        matchGamemodeLabel.grid(row = 1, column = 0, sticky= "nw", pady = (0,3))

        # ----------- Spell Sprites -----------

        spellFrame = tkinter.Frame(gamemodeResultFrame, height = 18, width = 36, background = "#775829",  borderwidth = 0)
        spellFrame.grid(row = 2, column = 0, sticky = "nw", pady = (0, 3)) 

        for i in range(2):

            if len(spellArray[preview]) >= i + 1:

                if i == 1:
                    spellSprite = tkinter.Canvas(spellFrame, height = 18, width = 18 , highlightthickness = 0,  borderwidth = 0)
                    spellSprite.grid(row = 0, column = i, padx = 1, pady = 1)

                else:
                    spellSprite = tkinter.Canvas(spellFrame, height = 18, width = 18 , highlightthickness = 0,  borderwidth = 0)
                    spellSprite.grid(row = 0, column = i, padx = (1,0), pady = 1)

                spellSprite.create_image((9, 9), image = spellArray[preview][i])
    
    def PlayerResult(frameNumber, gold, totalMinion, score, itemArray, preview):

        playerResultFrame = tkinter.Frame(frameNumber, height = 64, width = 192, background = "black",  borderwidth = 0)
        playerResultFrame.grid(row = 0, column = 2, pady = (16, 0), padx = (20, 20), sticky = "n")
        
        # ----------- Items -----------  
         
        itemFrame = tkinter.Frame(playerResultFrame, height = 32, width = 192, background = "#775829", borderwidth = 0)
        itemFrame.grid(row = 0, column = 0)

        for i in range(7):

            if i == 6:
                itemSprite = tkinter.Canvas(itemFrame, height = 32, width = 32 , background = "black", highlightthickness = 0,  borderwidth = 0)
                itemSprite.grid(row = 0, column = i, padx = 1, pady = 1)

            else:
                itemSprite = tkinter.Canvas(itemFrame, height = 32, width = 32 , background = "black", highlightthickness = 0,  borderwidth = 0)
                itemSprite.grid(row = 0, column = i, padx = (1,0), pady = 1)

            if i < len(itemArray[preview]):
                itemSprite.create_image((16,16), image = itemArray[preview][i])

        # ----------- Score -----------   

        scoreFrame = tkinter.Frame(playerResultFrame, height = 11, width = 192, background = "black", borderwidth = 0)
        scoreFrame.grid(row = 1, column = 0, pady = (9, 0), sticky = "swe")
        scoreFrame.grid_columnconfigure((0, 1, 2), weight = 1)

        kdaLabel = tkinter.Label(scoreFrame, text = score, background = "black", foreground = "#918c83", font = ("Heuristica", 11,"bold"), borderwidth = 0)
        kdaLabel.grid(row = 0, column = 0, sticky = "w")

        # ----------- Minions -----------   

        minionFrame = tkinter.Frame(scoreFrame, background = "black")
        minionFrame.grid(row = 0, column = 1)

        minionLabel = tkinter.Label(minionFrame, text = totalMinion, background = "black", foreground = "#918c83", font = ("", 11,"bold"), borderwidth = 0)
        minionLabel.grid(row = 0, column = 0, padx = (0, 2))

        minionCanvas = tkinter.Canvas(minionFrame, background = "black", highlightthickness = 0, height = 16, width = 16)
        minionCanvas.grid(row = 0, column = 1)

        minionCanvas.create_image((8, 7), image = minionIcon)

        # ----------- Gold -----------   

        goldFrame = tkinter.Frame(scoreFrame, background = "black")
        goldFrame.grid(row = 0, column = 2, sticky = "e")

        goldLabel = tkinter.Label(goldFrame, text = gold, background = "black", foreground = "#918c83",font = ("", 11,"bold"),  borderwidth = 0)
        goldLabel.grid(row = 0, column = 0, padx = (0, 4))

        goldCanvas = tkinter.Canvas(goldFrame, background = "black", highlightthickness = 0, height = 17, width = 17)
        goldCanvas.grid(row = 0, column = 1)

        goldCanvas.create_image((8, 8), image = goldIcon)

    def TimeData(frameNumber, mapName, gameDuration, gameCreation):

        dataFrame = tkinter.Frame(frameNumber, height = 85, width = 100, background = "black", borderwidth = 0)
        dataFrame.grid(row = 0, column = 3, pady = 5, sticky = "nswe")
        dataFrame.grid_rowconfigure((0, 1), weight=1)
        dataFrame.grid_columnconfigure((0), weight=1)
        dataFrame.grid_propagate(False)

        mapLabel = tkinter.Label(dataFrame, text = mapName, background = "black", font = ("", 9, "bold"), foreground = "#918c83")
        mapLabel.grid(row = 0, column = 0, sticky = "w")

        dateTimeLabel = tkinter.Label(dataFrame, text = f"{gameDuration} · {gameCreation}", font = ("", 9, "bold"), background = "black", foreground = "#918c83")
        dateTimeLabel.grid(row = 1, column = 0, pady = (0, 20), sticky = "w")

    def PreviewLine(frameNumber):

        line = tkinter.Frame(frameNumber, height = 1,  width = 800, background = "#7d6f4b", borderwidth = 0)
        line.grid(row = 0, columnspan = 6, sticky = "swe")

#endregion

#region Match Data

matchDataArray = [[], [], [], [], []]

def MatchDataRequest(match):

    matchJsonData = sessionMatch.get(match)
    matchRawData = ujson.loads(matchJsonData.text)

    return matchRawData

def MatchListDataRequest(playerPuuid, player):

    matchListJsonData = sessionMatchList.get(f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{playerPuuid}/ids?start=0&count=10&api_key={key}")
    matchListRawData = ujson.loads(matchListJsonData.text) 
    multithreadMatchList = []

    for i in range(10):
        if len(matchListRawData) >= i + 1:
            multithreadMatchList.append(f"https://americas.api.riotgames.com/lol/match/v5/matches/{matchListRawData[i]}?api_key={key}")

        if len(matchListRawData) == 0:
            return 0

    with futures.ThreadPoolExecutor(max_workers = 10) as executor:
       for request in executor.map(MatchDataRequest, multithreadMatchList):
           matchDataArray[player].append(request)
 
def ChangeFrame(player):

    if player == "player1":

        scrollableMainFrameArray[0].tkraise()

    elif player == "player2":

        scrollableMainFrameArray[1].tkraise()

    elif player == "player3":

        scrollableMainFrameArray[2].tkraise()

    elif player == "player4":
    
        scrollableMainFrameArray[3].tkraise()

    elif player == "player5":

        scrollableMainFrameArray[4].tkraise()

#endregion

#region Instantiation

playerSummaryStats1 = SummaryStats()
playerStats1 = PlayerStats()
matchStatsChampion1 = MatchStatsChampion()
matchStatsSpells1 = MatchStatsSpells()
matchStatsItems1 = MatchStatsItems()
matchStatsPlayer1 = MatchStatsPlayer()
matchStatsGame1 = MatchStatsGame()

playerSummaryStats2 = SummaryStats()
playerStats2 = PlayerStats()
matchStatsChampion2 = MatchStatsChampion()
matchStatsSpells2 = MatchStatsSpells()
matchStatsItems2 = MatchStatsItems()
matchStatsPlayer2 = MatchStatsPlayer()
matchStatsGame2 = MatchStatsGame()

playerSummaryStats3 = SummaryStats()
playerStats3 = PlayerStats()
matchStatsChampion3 = MatchStatsChampion()
matchStatsSpells3 = MatchStatsSpells()
matchStatsItems3 = MatchStatsItems()
matchStatsPlayer3 = MatchStatsPlayer()
matchStatsGame3 = MatchStatsGame()

playerSummaryStats4 = SummaryStats()
playerStats4 = PlayerStats()
matchStatsChampion4 = MatchStatsChampion()
matchStatsSpells4 = MatchStatsSpells()
matchStatsItems4 = MatchStatsItems()
matchStatsPlayer4 = MatchStatsPlayer()
matchStatsGame4 = MatchStatsGame()

playerSummaryStats5 = SummaryStats()
playerStats5 = PlayerStats()
matchStatsChampion5 = MatchStatsChampion()
matchStatsSpells5 = MatchStatsSpells()
matchStatsItems5 = MatchStatsItems()
matchStatsPlayer5 = MatchStatsPlayer()
matchStatsGame5 = MatchStatsGame()

#endregion

playerSummaryStatsArray = [playerSummaryStats1, playerSummaryStats2, playerSummaryStats3, playerSummaryStats4, playerSummaryStats5]
playerStatsArray = [playerStats1, playerStats2, playerStats3, playerStats4, playerStats5]
statsChampionArray = [matchStatsChampion1, matchStatsChampion2, matchStatsChampion3, matchStatsChampion4, matchStatsChampion5]
statsSpellsArray = [matchStatsSpells1, matchStatsSpells2, matchStatsSpells3, matchStatsSpells4, matchStatsSpells5]
statsItemsArray = [matchStatsItems1, matchStatsItems2, matchStatsItems3, matchStatsItems4, matchStatsItems5]
matchStatsPlayerArray = [matchStatsPlayer1, matchStatsPlayer2, matchStatsPlayer3, matchStatsPlayer4, matchStatsPlayer5]
statsGameArray = [matchStatsGame1, matchStatsGame2, matchStatsGame3, matchStatsGame4, matchStatsGame5]

def AssignHistoryButton(player):

    if player == 0:
        playerHistoryButtonArray[player].bind("<Button-1>", lambda event: ChangeFrame("player1"))
        playerHistoryButtonArray[player].bind("<Button-1>", lambda event: ChangeEntry(event, 0), add = "+")
    
    if player == 1:
        playerHistoryButtonArray[player].bind("<Button-1>", lambda event: ChangeFrame("player2"))
        playerHistoryButtonArray[player].bind("<Button-1>", lambda event: ChangeEntry(event, 1), add = "+")

    if player == 2:
        playerHistoryButtonArray[player].bind("<Button-1>", lambda event: ChangeFrame("player3"))
        playerHistoryButtonArray[player].bind("<Button-1>", lambda event: ChangeEntry(event, 2), add = "+")

    if player == 3:
        playerHistoryButtonArray[player].bind("<Button-1>", lambda event: ChangeFrame("player4"))
        playerHistoryButtonArray[player].bind("<Button-1>", lambda event: ChangeEntry(event, 3), add = "+")

    if player == 4:
        playerHistoryButtonArray[player].bind("<Button-1>", lambda event: ChangeFrame("player5"))
        playerHistoryButtonArray[player].bind("<Button-1>", lambda event: ChangeEntry(event, 4), add = "+")

def DestroyOldApp():

    for i in range(5):
        
        summaryChampionIconArray[i].clear()

        if playerHistoryButtonArray[i] != 0:
            
            scrollableMainFrameArray[i].destroy()
            matchDataArray[i].clear()
            profileSummaryArray[i].destroy()

    for i in range(10):

        itemList1[i].clear()
        itemList2[i].clear()
        itemList3[i].clear()
        itemList4[i].clear()
        itemList5[i].clear()
        
        spellList1[i].clear()
        spellList2[i].clear()
        spellList3[i].clear()
        spellList4[i].clear()
        spellList5[i].clear()

        championList[i].clear() 

def AppBuilder(event):
    
    lastColor = []
    DestroyOldApp()

    # ----------- UI Creation -----------

    CreateButtonBG()

    for i in range(5):

        if playerArray[i].get() != "" and " ":

            if playerStatsArray[i].PlayerDataRequest(playerArray[i].get()) == 0:
                pass
            
            elif MatchListDataRequest(playerStatsArray[i].playerPuuid, i) == 0:
                pass

            else:

                CreateHistoryButton(i)
                CreateHistoryFrame(i)
                CreateMatchPreview(i)
                AssignHistoryButton(i)

                playerStatsArray[i].PlayerRankRequest()
                playerSummaryStatsArray[i].GetSummaryWins(matchDataArray[i], playerStatsArray[i].playerPuuid)
                playerSummaryStatsArray[i].GetSummaryKda(matchDataArray[i], playerStatsArray[i].playerPuuid)
                playerSummaryStatsArray[i].GetSummaryChampions(matchDataArray[i], playerStatsArray[i].playerPuuid, i)

                ProfileSummary.CreateNameRank(profileSummaryArray[i], playerArray[i].get(), playerStatsArray[i].playerRank)
                ProfileSummary.CreateRecentMatches(profileSummaryArray[i], playerSummaryStatsArray[i].matchesWon, playerSummaryStatsArray[i].matchesLost, 
                playerSummaryStatsArray[i].averageKill, playerSummaryStatsArray[i].averageDeath, playerSummaryStatsArray[i].averageAssist)
                ProfileSummary.CreateRecentChampion(profileSummaryArray[i], playerSummaryStatsArray[i].championDictOrder, summaryChampionIconArray[i])
                
                lastColor.append(playerHistoryButtonArray[i])
    
        elif i == 4:
            lastColor[len(lastColor) - 1].configure(background = "#042937")

    for player in range(5):

        if playerHistoryButtonArray[player] != 0:
            for preview in range(10):  
                
                # ----------- Data Requests -----------

                statsChampionArray[player].MatchStatsChampionRequest(matchDataArray[player][preview], playerStatsArray[player].playerPuuid, player)
                statsSpellsArray[player].MatchStatsSpellsRequest(matchDataArray[player][preview], playerStatsArray[player].playerPuuid)
                statsItemsArray[player].MatchStatsItemsRequests(matchDataArray[player][preview], playerStatsArray[player].playerPuuid)
                matchStatsPlayerArray[player].MatchStatsPlayerRequest(matchDataArray[player][preview], playerStatsArray[player].playerPuuid)
                statsGameArray[player].GetMatchResult(matchDataArray[player][preview], playerStatsArray[player].playerPuuid)
                statsGameArray[player].MatchModeRequest(matchDataArray[player][preview])
                statsGameArray[player].MatchTimeRequest(matchDataArray[player][preview])
                
                # ----------- UI Elements -----------

                MatchPreview.ChampionCircle(playerMatchArray[player][preview], championList[player][preview], statsChampionArray[player].championLevel)
                MatchPreview.GamemodeResult(playerMatchArray[player][preview], statsGameArray[player].matchResult, statsGameArray[player].gameMode, 
                statsSpellsArray[player].GetSpellSprites(player, preview), preview)

                MatchPreview.PlayerResult(playerMatchArray[player][preview], matchStatsPlayerArray[player].playerGold, matchStatsPlayerArray[player].playerMinions, 
                matchStatsPlayerArray[player].ScoreConstructor(), statsItemsArray[player].GetItemSprites(player, preview), preview)

                MatchPreview.TimeData(playerMatchArray[player][preview], statsGameArray[player].mapName, statsGameArray[player].gameDuration, statsGameArray[player].gameCreation)
                MatchPreview.PreviewLine(playerMatchArray[player][preview])
       
def ChangeSearch(event):
    if str(event.type) == "ButtonPress":
        searchButton.config(background = "#07141f")
    elif str(event.type) == "ButtonRelease":
        searchButton.config(background = "black")

def ChangeEntry(event, player):

    for i in range(5):

        if i == player:
            playerHistoryButtonArray[i].configure(background = "#042937")

        elif playerHistoryButtonArray[i] != 0:
            playerHistoryButtonArray[i].configure(background = "black")

searchButton.bind("<Button-1>", ChangeSearch)
searchButton.bind("<Button-1>", AppBuilder, add = "+")
searchButton.bind("<ButtonRelease>", ChangeSearch)

player1.bind("<Return>", AppBuilder)
player2.bind("<Return>", AppBuilder)
player3.bind("<Return>", AppBuilder)
player4.bind("<Return>", AppBuilder)
player5.bind("<Return>", AppBuilder)

root.mainloop()

#pyinstaller --onefile --noconsole MainFile.py
