
# Handler 베이스 모델
class Handler:
    def __init__(self):
        self.next_handler = None
    def setNext(self, handler):
        # 다음 핸들러로 넘기는 것
        self.next_handler = handler

    def handle(self, req):
        # 처리하기 위한 함수
        if self.next_handler:
            # 다음함수의 handle() 호출
            return self.next_handler.handle(req)
        return None

class CashHandler(Handler):
    def handle(self, req):
        if req['method'] == 'cash':
            print(f'processing cash {req["amount"]} won')
        else:
            print(f'CashHandler cannot process')
            super().handle(req)

class CreditCardHandler(Handler):
    def handle(self, req):
        if req['method'] == 'creditCard':
            print(f'processing creditCard {req["amount"]} won')
        else:
            print(f'CreditCardHandler cannot process')
            super().handle(req)


class DebitCardHandler(Handler):
    def handle(self, req):
        if req['method'] == 'debitCard':
            print(f'processing debitCard {req["amount"]} won')
        else:
            print(f'DebitCardHandler cannot process')
            super().handle(req)

