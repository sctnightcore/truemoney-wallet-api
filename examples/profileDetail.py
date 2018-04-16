from WalletAPI import Wallet

print()

wallet = Wallet("email","password",showLoginMessage=True)

profile = wallet.fetchProfile()

fullname = "%s %s" % (profile["title"],profile["fullname"])
email = profile["email"]
thaiID = profile["thaiID"]
mobileNumber = profile["mobileNumber"]
balance = profile["balance"]
dateOfBirth = "%s/%s/%s" % (profile["dateOfBirth"][-2:],profile["dateOfBirth"][4:6],profile["dateOfBirth"][:4])

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