import locale
locale.setlocale(locale.LC_ALL, "en_US.UTF-8")


class ATM(object):

    # STATIC VALUES

    checking_acct = 5000
    savings_acct = 5000

    # CHECKING BALANCES

    @staticmethod
    def checking_balance():
        print(f"\nCHECKING ACCT: {locale.currency(ATM.checking_acct)}")

    @staticmethod
    def savings_balance():
        print(f"\nSAVINGS ACCT: {locale.currency(ATM.savings_acct)}")

    # ATM FUNCTIONS (CHECKING)

    @staticmethod
    def withdraw_checking():
        amt = int(input("\nEnter amount to withdraw: "))
        if amt <= ATM.savings_acct:
            print(f"\nWithdrawing {locale.currency(amt)} from your checking account")
            print("...")
            print("Done!")
            ATM.checking_acct -= amt
            print(f"CHECKING ACCT: {locale.currency(ATM.checking_acct)}")
        else:
            print("INSUFFICIENT FUNDS. PLEASE TRY AGAIN!")

    @staticmethod
    def deposit_checking():
        amt = int(input("\nEnter amount to deposit: "))
        print(f"\nDepositing {locale.currency(amt)} into your checking account")
        print("...")
        print("Done!")
        ATM.checking_acct += amt
        print(f"CHECKING ACCT: {locale.currency(ATM.checking_acct)}")

    # ATM FUNCTIONS (SAVINGS)

    @staticmethod
    def withdraw_savings():
        amt = int(input("\nEnter amount to withdraw: "))
        if amt <= ATM.savings_acct:
            print(f"\nWithdrawing {locale.currency(amt)} from your savings account")
            print("...")
            print("Done!")
            ATM.savings_acct -= amt
            print(f"SAVINGS ACCT: {locale.currency(ATM.savings_acct)}")
        else:
            print("INSUFFICIENT FUNDS. PLEASE TRY AGAIN!")

    @staticmethod
    def deposit_savings():
        amt = int(input("\nEnter amount to deposit: "))
        print(f"\nDepositing {locale.currency(amt)} into your savings account")
        print("...")
        print("Done!")
        ATM.savings_acct += amt
        print(f"SAVINGS ACCT: {locale.currency(ATM.savings_acct)}")

    # ATM FUNCTIONS (TRANSFER)

    @staticmethod
    def checking_to_savings():
        amt = int(input("\nEnter amount to transfer: "))
        if amt <= ATM.checking_acct:
            print(f"\nTransferring {locale.currency(amt)} from your checking account into your savings account")
            print("...")
            print("Done!")
            ATM.checking_acct -= amt
            ATM.savings_acct += amt
            print(f"CHECKING ACCT: {locale.currency(ATM.checking_acct)}")
            print(f"SAVINGS ACCT: {locale.currency(ATM.savings_acct)}")
        else:
            print("INSUFFICIENT FUNDS. PLEASE TRY AGAIN!")

    @staticmethod
    def savings_to_checking():
        amt = int(input("\nEnter amount to transfer: "))
        if amt <= ATM.savings_acct:
            print(f"\nTransferring {locale.currency(amt)} from your savings account into your checking account")
            print("...")
            print("Done!")
            ATM.checking_acct += amt
            ATM.savings_acct -= amt
            print(f"CHECKING ACCT: {locale.currency(ATM.checking_acct)}")
            print(f"SAVINGS ACCT: {locale.currency(ATM.savings_acct)}")
        else:
            print("INSUFFICIENT FUNDS. PLEASE TRY AGAIN!")
