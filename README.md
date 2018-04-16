# truemoney-wallet-api

Transaction, Transfer, WeCard, TrueMoney Card and MORE!

# Requirement

Python >= 3.x

Python requests

    pip install requests

# Usage

Login to your account by using `Wallet()`

    from WalletAPI import Wallet
    wallet = Wallet("email","password")

Fetch your profile by using `self.fetchProfile()` (return type = `dict`)

    profile = wallet.fetchProfile()
    print(profile)

Fetch your profile image URL by using `self.fetchProfileImageURL()` (return type = `str`)

    profileImageURL = wallet.fetchProfileImageURL()
    print(profileImageURL)

Fetch your accessToken by using `self.fetchToken()` (return type = `str`)

    accessToken = self.fetchToken()
    print(accessToken)

Use cashcard to topup by using `self.cashcardTopUp(cashcard)` (return type = `dict`)

    wallet.cashcardTopUp("97596183625657")

Transfer your money (request) by using `self.requestTransfer(mobileNumber, amount, message="")` (return type = `dict`)

    wallet.requestTransfer("0812345678", 5, "Sent from Python 3")
    # you will receive OTP code if the detail is correct

Transfer your money (confirm) by using `self.confirmTransfer(otpString)` (return type = `dict`)

    wallet.confirmTransfer("123456")

TopUp your money (request) by using `self.requestTopUp(mobileNumber, amount)` (return type = `dict`)

    wallet.requestTopUp("0812345678", 10)
    # you will receive OTP code if the detail is correct

TopUp your money (confirm) by using `self.confirmTopUp(otpString)` (return type = `dict`)

    wallet.confirmTopUp("123456")

Buy TrueMoney card (request) by using `self.requestBuyTrueMoneyCard(mobileNumber, amount)` (return type = `dict`)

    wallet.requestBuyTrueMoneyCard("0812345678", 50)
    # you will receive OTP code if the detail is correct

Buy TrueMoney card (confirm) by using `self.confirmBuyTrueMoneyCard(otpString)` (return type = `dict`)

    wallet.confirmBuyTrueMoneyCard("123456")

Fetch WeCard list by using `self.fetchWeCardList()` (return type = `list`)

    wecardList = wallet.fetchWeCardList()
    print(wecardList)

Fetch WeCard detail (request) by using `self.requestWeCardDetail(cardId)` (return type = `dict`)

    wallet.requestWeCardDetail("111111111111111111")
    # you will receive OTP code if the detail is correct

Fetch WeCard detail (confirm) by using `self.confirmWeCardDetail(otpString)` (return type = `dict`)

    wecardDetail = wallet.confirmWeCardDetail("123456")
    print(wecardDetail)

Enable WeCard by using `self.enableWeCard(cardId)` (return type = `dict`)

    wallet.enableWeCard("111111111111111111")

Disable WeCard by using `self.disableWeCard(cardId)` (return type = `dict`)

    wallet.disableWeCard("111111111111111111")

# Transaction

Available functions

    self.fetchTransactions()
    self.fetchTransactionsByMobileNumber(mobileNumber)
    self.fetchTransactionDetailByReportID(reportID)
    self.fetchTransactionDetailByTransactionID(transactionID)
    self.fetchPreviousTransactions(limit=5)
    self.fetchPreviousReportsID(limit=5)
    self.fetchPreviousTransactionsDetail(limit=5)
    self.fetchPreviousTransactionsID(limit=5)
    self.fetchTransactionAmountByReportID(reportID)
    self.fetchTransactionAmountByTransactionID(transactionID)
    self.fetchMobileNumberByReportID(reportID)
    self.fetchMobileNumberByTransactionID(transactionID)
    self.fetchNameByReportID(reportID)
    self.fetchNameByTransactionID(transactionID)
    self.fetchDateByReportID(reportID)
    self.fetchDateByTransactionID(transactionID)
    self.fetchServiceTypeByReportID(reportID)
    self.fetchServiceTypeByTransactionID(transactionID)
    self.fetchServiceCodeByReportID(reportID)
    self.fetchServiceCodeByTransactionID(transactionID)
    self.fetchPersonalMessageByReportID(reportID):
    self.fetchPersonalMessageByTransactionID(transactionID)

# Scarping (Faster than every functions in `Transaction`)

Available functions

    self.getTransactionAmount(transactionDetail)
    self.getTransactionMobileNumber(transactionDetail)
    self.getTransactionName(transactionDetail)
    self.getTransactionDate(transactionDetail)
    self.getTransactionServiceType(transactionDetail)
    self.getTransactionServiceCode(transactionDetail)
    self.getTransactionPersonalMessage(transactionDetail)
    self.getToken(profile)

# Author

[Noxturnix](https://github.com/Noxturnix) from Noxtian team
