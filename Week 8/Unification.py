from unification import *
@unifiable
class Account(object):
    def _init_(self, id, name, balance):
        self.id = id
        self.name = name
        self.balance = balance

data = [Account(1, 'Alice', 100),
        Account(2, 'Bob', 0),
        Account(2, 'Charlie', 0),
        Account(2, 'Denis', 400),
        Account(2, 'Edith', 500)]

id, name, balance = var('id'), var('name'), var('balance')
[unify(Account(id, name, balance), acct) for acct in data]
[unify(Account(id, name, 0), acct) for acct in data]