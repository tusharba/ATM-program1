class Atm:
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.Menu()

    def Menu(self):
       user_input = input('''
       1).press 1 to create pin
       2).press 2 to change pin
       3).check 3 to balance
       4).check 4 to withdraw
       5).exit
      ''')
       if   user_input == '1':
         self.create_pin()
       elif user_input == '2':
         self.change_pin()
       elif user_input == '3':
         self.chack_balance()
       elif user_input == '4':
         self.withdraw()
       elif user_input == '5':
         pass

    def create_pin(self):
         new_pin = input("Enter your pin")
         self.pin = new_pin

         user_balance = int(input("enter your balance"))
         self.balance = user_balance

         print('pin created successfully')
         self.Menu()

    def change_pin(self):
        old_pin = input("Enter your old pin")

        if old_pin == self.pin:
            new_pin = input("Enter new pin")
            self.pin = new_pin
            print('pin change successfully')
            self.Menu()
        else:
            print('nai karne de sakta re baba')

    def chack_balance(self):
        user_pin = input("Enter you pin")
        if user_pin == self.pin:
            print('your balance is: ', self.balance)
            self.Menu()
        else:
            print('sal nikal yaha se')

    def withdraw(self):
        user_pin = input("Enter you pin")
        if user_pin == self.pin:
            amount = int(input('Enter your amount'))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print('withdraw successful balance is: ', self.balance)
            else:
                print('abe grib')
        else:
            print('sale chor')
            self.Menu()





obj = Atm()