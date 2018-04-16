from WalletAPI import Wallet

print()

wallet = Wallet("email","password",showLoginMessage=True)

print()

wallet.requestTopUp("0812345678",10)
otpString = input("OTP: ")
wallet.confirmTopUp(otpString)
print()