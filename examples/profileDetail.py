from WalletAPI import Wallet

print()

wallet = Wallet("email","password",showLoginMessage=True)

profile = wallet.fetchProfile()

fullname = "%s %s" % (profile["data"]["title"],profile["data"]["fullname"])
email = profile["data"]["email"]
thaiID = profile["data"]["thaiId"]
mobileNumber = profile["data"]["mobileNumber"]
balance = round(float(profile["data"]["currentBalance"]),2)
dateOfBirth = "%s/%s/%s" % (profile["data"]["birthdate"][-2:],profile["data"]["birthdate"][4:6],profile["data"]["birthdate"][:4])

profileImage = wallet.fetchProfileImageURL()

print("""
Profile

Balance: %s

Fullname: %s
Email: %s
Mobile Number: %s

Thai Citizen ID: %s
Date Of Birth: %s

Profile Image URL: %s
""" % (balance,fullname,email,mobileNumber,thaiID,dateOfBirth,profileImage))