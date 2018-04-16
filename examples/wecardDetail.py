from WalletAPI import Wallet

print()

wallet = Wallet("email","password",showLoginMessage=True)

print()

wecardList = wallet.fetchWeCardList()

if wecardList != []:
    text = "WeCard list:\n"
    count = 1
    for wecard in wecardList:
        text += "%s. %s (created at %s)\n" % (count,wecard["cardIdentifier"],wecard["createdDate"])
        count += 1
    numberOfCard = count-1
    text += "Choose a card [1-%s]: " % (numberOfCard)
    while True:
        try:
            choose = input(text)
            choose = int(choose)
            if choose > 0 and choose <= numberOfCard:
                break
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except:
            pass
        print()
    print()
    choose -= 1
    cardIdentifier = wecardList[choose]["cardIdentifier"]
    wallet.requestWeCardDetail(cardIdentifier)
    otpString = input("OTP: ")
    cardDetail = wallet.confirmWeCardDetail(otpString)
    if cardDetail["cardStatus"] == 4:
        cardStatus = "Disable"
    elif cardDetail["cardStatus"] == 3:
        cardStatus = "Enable"
    else:
        cardStatus = "Unknown"
    print()
    print("""Card detail

Card Status: %s
Card Number: %s
Expiry Date: %s
CVV: %s

Card Holder Name: %s %s

Card Identifier: %s
""" % (cardStatus,cardDetail["cardNumber"],cardDetail["expiryDate"],cardDetail["cvv"],cardDetail["firstName"],cardDetail["lastName"],cardDetail["cardIdentifier"]))
else:
    print("No WeCard found\n")