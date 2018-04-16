from WalletAPI import Wallet

print()

wallet = Wallet("email","password",showLoginMessage=True)

print()

wallet.requestTransfer("0812345678",5,"")
otpString = input("OTP: ")
wallet.confirmTransfer(otpString)
print()