import time


class SelectError(BaseException):
    pass


class Mifare:
    def select(self):
        time.sleep(0.5)
        return {"id": "123456789"}
