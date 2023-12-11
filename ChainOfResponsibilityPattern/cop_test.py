from handler import CashHandler, CreditCardHandler,DebitCardHandler

cash_handler = CashHandler()
creditcard_handler = CreditCardHandler()
debitcard_handler = DebitCardHandler()

cash_handler.setNext(creditcard_handler)
creditcard_handler.setNext(debitcard_handler)

payment = {
    'method' : 'cash',
    'amount' : 10000

}

cash_handler.handle(payment)