from WalletAPI import Wallet

print()

wallet = Wallet("email","password",showLoginMessage=True)

latestTransaction = wallet.fetchPreviousTransactions(limit=1)[0]
transDetail = wallet.fetchTransactionDetailByReportID(latestTransaction["reportID"])

serviceType = wallet.getTransactionServiceType(transDetail)
serviceCode = wallet.getTransactionServiceCode(transDetail)
date = wallet.getTransactionDate(transDetail)
name = wallet.getTransactionName(transDetail)
mobileNumber = wallet.getTransactionMobileNumber(transDetail)
amount = wallet.getTransactionAmount(transDetail)
try:
    personalMessage = wallet.getTransactionPersonalMessage(transDetail)
except:
    personalMessage = ""

print("""
Latest transaction

Service Type: %s
Service Code: %s

Date: %s

Name: %s
Mobile Number: %s
Amount: %s

Personal Message: %s
""" % (serviceType, serviceCode, date, name, mobileNumber, amount, personalMessage))