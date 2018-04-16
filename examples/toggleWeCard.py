from WalletAPI import Wallet

print()

wallet = Wallet("email","password",showLoginMessage=True)

print()

wecardList = wallet.fetchWeCardList()

if wecardList != []:
    while True:
        text = "WeCard list:\n"
        count = 1
        for wecard in wecardList:
            if wecard["status"] == "4":
                cardStatus = "Disable"
            elif wecard["status"] == "3":
                cardStatus = "Enable"
            else:
                cardStatus = "Unknown"
            text += "%s. %s (created at %s) [%s]\n" % (count,wecard["cardIdentifier"],wecard["createdDate"],cardStatus)
            count += 1
        numberOfCard = count-1
        text += "Choose a card [1-%s]: " % (numberOfCard)
        try:
            choose = input(text)
            choose = int(choose)
            if choose > 0 and choose <= numberOfCard:
                choose -= 1
                cardIdentifier = wecardList[choose]["cardIdentifier"]
                cardStatus = wecardList[choose]["status"]
                if cardStatus == "4":
                    wallet.enableWeCard(cardIdentifier)
                elif cardStatus == "3":
                    wallet.disableWeCard(cardIdentifier)
                else:
                    raise Exception("Unknown card status")
                wecardList = wallet.fetchWeCardList()
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except:
            pass
        print()
else:
    print("No WeCard found\n")