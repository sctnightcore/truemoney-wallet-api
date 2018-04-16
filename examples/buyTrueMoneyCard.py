from WalletAPI import Wallet

print()

wallet = Wallet("email","password",showLoginMessage=True)

print()

wallet.requestBuyTrueMoneyCard("0812345678",50)
otpString = input("OTP: ")
resp = wallet.confirmBuyTrueMoneyCard(otpString)
print()