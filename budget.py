class Category:
    def __init__(self, category):
        self.name = category
        self.ledger = []
        self.balance = 0
        self.spending = 0

    def deposit(self, amount, description =""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += float(amount)

    def withdraw(self,amount, description =""):
        if not self.check_funds(amount): return False
        self.ledger.append({"amount": -1*amount, "description": description})
        self.balance -= amount
        self.spending += amount
        return True

    def get_balance(self):
        return self.balance

    def check_funds(self, amount):
        return self.balance >= amount

    def transfer(self, amount, category):
        if not self.check_funds(amount): return False
        self.withdraw(amount, f'Transfer to {category.name}')
        category.deposit(amount, f'Transfer from {self.name}')
        return True
    def __repr__(self):
       return self.__str__()   
  
    def __str__(self):
        ast_len = (30 - len(self.name)) // 2
        str_rep = f"{ast_len*'*'}{self.name}{ast_len*'*'}\n"
        for trans in self.ledger:
            amount = "{:.2f}".format(trans["amount"])
            description,amount_len = trans["description"],len(amount)
            des_len = 23 if len(description) >= 23 else len(description)
            spaces = (30-amount_len-des_len) * " "
            str_rep += f'{description[:des_len]}{spaces}{amount}\n'
        str_rep += f'Total: {self.balance}'
        return str_rep   



def create_spend_chart(categories):
    chart = 'Percentage spent by category\n'
    withdrawls, total = {}, 0
    for cat in categories:
        withdrawls[cat.name] = 0
        for movement in cat.ledger:
            if movement['amount'] < 0:withdrawls[cat.name] += movement['amount']
        withdrawls[cat.name] = -withdrawls[cat.name]
        total += withdrawls[cat.name]
    for name in withdrawls:
        withdrawls[name] = int(withdrawls[name]*100/total)
    for i in range (100, -10, -10):
        chart+= str(i).rjust(3) + '| '
        for name in withdrawls:
            chart += 'o  ' if withdrawls[name] >= i else '   '
        chart += '\n'
    chart += " " * 4 + "-" * (len(withdrawls) * 3 + 1) + '\n'
    max_len = 0
    for cat in categories:
        if len(cat.name) > max_len:max_len = len(cat.name)
    for i in range(max_len):
        chart += ' ' * 5
        for cat in categories:
            chart += cat.name[i] + '  ' if len(cat.name) > i else '   '
        chart += '\n'
    return chart[0:-1]

