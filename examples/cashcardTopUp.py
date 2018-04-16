from WalletAPI import Wallet

print()

wallet = Wallet("email","password",showLoginMessage=True)

wallet.cashcardTopUp("97596183625657")

print()
