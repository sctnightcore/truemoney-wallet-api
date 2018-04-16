import requests, json, hashlib, time

class Wallet:

    HOST = "https://wallet.truemoney.com"

    LOGIN_PATH = "/user/login"
    WEB_API_PATH = "/v1web"

    TRANSACTION_PATH = WEB_API_PATH + "/api/transaction_history"
    TRANSACTION_DETAIL_PATH = WEB_API_PATH + "/api/transaction_history_detail"

    PROFILE_DETAIL_PATH = WEB_API_PATH + "/api/profile"
    PROFILE_IMAGE_DETAIL_PATH = WEB_API_PATH + "/api/profile_image"

    TRANSFER_PATH = WEB_API_PATH + "/transfer"
    TRANSFER_REQUEST_PATH = TRANSFER_PATH + "/draft"
    TRANSFER_CONFIRM_PATH = TRANSFER_PATH + "/confirm"

    TOPUP_PATH = "/topup"
    TOPUP_REQUEST_PATH = TOPUP_PATH + "/draft"
    TOPUP_CONFIRM_PATH = TOPUP_PATH + "/confirm"

    ECASH_CARD_PATH = "/ecashcard"
    ECASH_CARD_REQUEST_PATH = ECASH_CARD_PATH + "/draft"
    ECASH_CARD_CONFIRM_PATH = ECASH_CARD_PATH + "/confirm"

    WECARD_PATH = WEB_API_PATH + "/wecard"
    WECARD_LIST_PATH = WECARD_PATH + "/list"
    WECARD_REQUEST_DETAIL_PATH = WECARD_PATH + "/view_detail"
    WECARD_CONFIRM_DETAIL_PATH = WECARD_PATH + "/confirm_view_detail"
    WECARD_ENABLE_PATH = WECARD_PATH + "/enable"
    WECARD_DISABLE_PATH = WECARD_PATH + "/disable"

    def __init__(self, email, password, showLoginMessage=False):
        if showLoginMessage:
            print("Logging in..")
        self.session = requests.session()
        resp = self.session.post(self.HOST + self.LOGIN_PATH, data={"email": email, "password": password})
        self.username = email
        self.password = hashlib.sha1((email+password).encode("utf-8")).hexdigest()
        self.accessToken = self.fetchToken()
        if resp.status_code != 200:
            raise Exception("Wrong email or password")
        if showLoginMessage:
            print("Login success!")

    """SERVER"""

    def fetchProfile(self):
        return json.loads(self.session.post("https://api-ewm.truemoney.com/api/v1/signin?device_os=android&device_id=d520d0d12d0d48cb89394905168c6ed5&device_type=CPH1611&device_version=6.0.1&app_name=wallet&app_version=4.0.1", headers={"Contant-Type": "application/json"}, json={"username": self.username, "password": self.password, "type": "email", "deviceToken": "fUUbZJ9nwBk:APA91bHHgBBHhP9rqBEon_BtUNz3rLHQ-sYXnezA10PRSWQTwFpMvC9QiFzh-CqPsbWEd6x409ATC5RVsHAfk_-14cSqVdGzhn8iX2K_DiNHvpYfMMIzvFx_YWpYj5OaEzMyIPh3mgtx", "mobileTracking": "dJyFzn\/GIq7lrjv2RCsZbphpp0L\/W2+PsOTtOpg352mgWrt4XAEAAA=="}).text)

    def fetchProfileImageURL(self):
        return self.session.get(self.HOST + self.PROFILE_IMAGE_DETAIL_PATH).text

    def fetchToken(self):
        return json.loads(self.session.post("https://api-ewm.truemoney.com/api/v1/signin?device_os=android&device_id=d520d0d12d0d48cb89394905168c6ed5&device_type=CPH1611&device_version=6.0.1&app_name=wallet&app_version=4.0.1", headers={"Contant-Type": "application/json"}, json={"username": self.username, "password": self.password, "type": "email", "deviceToken": "fUUbZJ9nwBk:APA91bHHgBBHhP9rqBEon_BtUNz3rLHQ-sYXnezA10PRSWQTwFpMvC9QiFzh-CqPsbWEd6x409ATC5RVsHAfk_-14cSqVdGzhn8iX2K_DiNHvpYfMMIzvFx_YWpYj5OaEzMyIPh3mgtx", "mobileTracking": "dJyFzn\/GIq7lrjv2RCsZbphpp0L\/W2+PsOTtOpg352mgWrt4XAEAAA=="}).text)["data"]["accessToken"]

    def cashcardTopUp(self, cashcard):
        return json.loads(self.session.post("https://api-ewm.truemoney.com/api/api/v1/topup/mobile/%s/%s/cashcard/%s" % (str(int(time.time())), self.accessToken, cashcard)).text)

    def requestTransfer(self, mobileNumber, amount, message=""):
        return json.loads(self.session.post(self.HOST + self.TRANSFER_REQUEST_PATH, data={"mobileNumber": mobileNumber, "amount": str(amount), "message": message}).text)

    def confirmTransfer(self, otpString):
        return json.loads(self.session.post(self.HOST + self.TRANSFER_CONFIRM_PATH, data={"otpString": otpString}).text)

    def requestTopUp(self, mobileNumber, amount):
        return json.loads(self.session.post(self.HOST + self.TOPUP_REQUEST_PATH, data={"mobileNumber": mobileNumber, "amount": str(amount)}).text)

    def confirmTopUp(self, otpString):
        return json.loads(self.session.post(self.HOST + self.TOPUP_CONFIRM_PATH, data={"otpString": otpString}).text)

    def requestBuyTrueMoneyCard(self, mobileNumber, amount):
        return json.loads(self.session.post(self.HOST + self.ECASH_CARD_REQUEST_PATH, data={"mobileNumber": mobileNumber, "amount": str(amount)}).text)

    def confirmBuyTrueMoneyCard(self, otpString):
        return json.loads(self.session.post(self.HOST + self.ECASH_CARD_CONFIRM_PATH, data={"otpString": otpString}).text)

    def fetchWeCardList(self):
        return json.loads(self.session.get(self.HOST + self.WECARD_LIST_PATH).text)

    def requestWeCardDetail(self, cardId):
        return json.loads(self.session.post(self.HOST + self.WECARD_REQUEST_DETAIL_PATH, data={"cardId": cardId}).text)

    def confirmWeCardDetail(self, otpString):
        return json.loads(self.session.post(self.HOST + self.WECARD_CONFIRM_DETAIL_PATH, data={"otpString": otpString}).text)

    def enableWeCard(self, cardId):
        return json.loads(self.session.post(self.HOST + self.WECARD_ENABLE_PATH, data={"cardId": cardId}).text)

    def disableWeCard(self, cardId):
        return json.loads(self.session.post(self.HOST + self.WECARD_DISABLE_PATH, data={"cardId": cardId}).text)

    def fetchTransactions(self):
        return json.loads(self.session.get(self.HOST + self.TRANSACTION_PATH).text)

    def fetchTransactionsByMobileNumber(self, mobileNumber):
        transactions = self.fetchTransactions()["data"]["activities"]
        while "-" in mobileNumber:
            mobileNumber = mobileNumber.replace("-","")
        if mobileNumber.startswith("+66"):
            mobileNumber = "0%s" % (mobileNumber[len("+66"):])
        mobileNumber = "%s-%s-%s" % (mobileNumber[:3],mobileNumber[3:6],mobileNumber[6:])
        tsacs = []
        for trans in transactions:
            if trans["text5En"] == mobileNumber:
                tsacs.append(trans)
        return tsacs

    def fetchTransactionDetailByReportID(self, reportID):
        return json.loads(self.session.get(self.HOST + self.TRANSACTION_DETAIL_PATH, params={"reportID": reportID}).text)

    def fetchTransactionDetailByTransactionID(self, transactionID):
        transactions = self.fetchTransactions()["data"]["activities"]
        for trans in transactions:
            transDetail = self.fetchTransactionDetailByReportID(trans["reportID"])
            if transDetail["data"]["section4"]["column2"]["cell1"]["value"] == transactionID:
                return transDetail

    def fetchPreviousTransactions(self, limit=5):
        transactions = self.fetchTransactions()["data"]["activities"]
        tsacs = []
        count = 0
        for trans in transactions:
            if count < limit:
                tsacs.append(trans)
            else:
                break
            count += 1
        return tsacs

    def fetchPreviousReportsID(self, limit=5):
        transactions = self.fetchTransactions()["data"]["activities"]
        tsacs = []
        count = 0
        for trans in transactions:
            if count < limit:
                tsacs.append(trans["reportID"])
            else:
                break
            count += 1
        return tsacs

    def fetchPreviousTransactionsDetail(self, limit=5):
        transactions = self.fetchTransactions()["data"]["activities"]
        tsacs = []
        count = 0
        for trans in transactions:
            if count < limit:
                tsacs.append(self.fetchTransactionDetailByReportID(trans["reportID"]))
            else:
                break
            count += 1
        return tsacs

    def fetchPreviousTransactionsID(self, limit=5):
        transactions = self.fetchTransactions()["data"]["activities"]
        tsacs = []
        count = 0
        for trans in transactions:
            if count < limit:
                tsacs.append(self.fetchTransactionDetailByReportID(trans["reportID"])["data"]["section4"]["column2"]["cell1"]["value"])
            else:
                break
            count += 1
        return tsacs

    def fetchTransactionAmountByReportID(self, reportID):
        return self.fetchTransactionDetailByReportID(reportID)["data"]["amount"]

    def fetchTransactionAmountByTransactionID(self, transactionID):
        return self.fetchTransactionDetailByTransactionID(transactionID)["data"]["amount"]

    def fetchMobileNumberByReportID(self, reportID):
        return self.fetchTransactionDetailByReportID(reportID)["data"]["ref1"]

    def fetchMobileNumberByTransactionID(self, transactionID):
        return self.fetchTransactionDetailByTransactionID(transactionID)["data"]["ref1"]

    def fetchNameByReportID(self, reportID):
        return self.fetchTransactionDetailByReportID(reportID)["data"]["section2"]["column1"]["cell2"]["value"]

    def fetchNameByTransactionID(self, transactionID):
        return self.fetchTransactionDetailByTransactionID(transactionID)["data"]["section2"]["column1"]["cell2"]["value"]

    def fetchDateByReportID(self, reportID):
        return self.fetchTransactionDetailByReportID(reportID)["data"]["section4"]["column1"]["cell1"]["value"]

    def fetchDateByTransactionID(self, transactionID):
        return self.fetchTransactionDetailByTransactionID(transactionID)["data"]["section4"]["column1"]["cell1"]["value"]

    def fetchServiceTypeByReportID(self, reportID):
        return self.fetchTransactionDetailByReportID(reportID)["data"]["serviceType"]

    def fetchServiceTypeByTransactionID(self, transactionID):
        return self.fetchTransactionDetailByTransactionID(transactionID)["data"]["serviceType"]

    def fetchServiceCodeByReportID(self, reportID):
        return self.fetchTransactionDetailByReportID(reportID)["data"]["serviceCode"]

    def fetchServiceCodeByTransactionID(self, transactionID):
        return self.fetchTransactionDetailByTransactionID(transactionID)["data"]["serviceCode"]

    def fetchPersonalMessageByReportID(self, reportID):
        return self.fetchTransactionDetailByReportID(reportID)["data"]["personalMessage"]["value"]

    def fetchPersonalMessageByTransactionID(self, transactionID):
        return self.fetchTransactionDetailByTransactionID(transactionID)["data"]["personalMessage"]["value"]

    """CLIENT"""

    def getTransactionAmount(self, transactionDetail):
        return transactionDetail["data"]["amount"]

    def getTransactionMobileNumber(self, transactionDetail):
        return transactionDetail["data"]["ref1"]

    def getTransactionName(self, transactionDetail):
        return transactionDetail["data"]["section2"]["column1"]["cell2"]["value"]

    def getTransactionDate(self, transactionDetail):
        return transactionDetail["data"]["section4"]["column1"]["cell1"]["value"]

    def getTransactionServiceType(self, transactionDetail):
        return transactionDetail["data"]["serviceType"]

    def getTransactionServiceCode(self, transactionDetail):
        return transactionDetail["data"]["serviceCode"]

    def getTransactionPersonalMessage(self, transactionDetail):
        return transactionDetail["data"]["personalMessage"]["value"]

    def getToken(self, profile):
        return profile["data"]["accessToken"]