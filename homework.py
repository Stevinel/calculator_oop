import datetime as dt
DATE_FORMAT = '%d.%m.%Y'


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, new_record):
        self.records.append(new_record)

    def get_today_stats(self):
        today_stats_count = 0
        today_date = dt.date.today()
        for record in self.records:
            if record.date == today_date:
                today_stats_count += record.amount
        return today_stats_count

    def get_week_stats(self):
        week_stats = 0
        today = dt.date.today()
        date_week_ago = (today - dt.timedelta(days=7))
        for record in self.records:
            if date_week_ago <= record.date <= today:
                week_stats += record.amount
        return week_stats

    def get_remained(self):
        return self.limit - self.get_today_stats()
  

class CashCalculator(Calculator):
    USD_RATE = 77.12
    EURO_RATE = 90.95

    def get_today_cash_remained(self, currency):
        CUR_LIB = {
            'rub': (1, 'руб'),
            'usd': (self.USD_RATE, 'USD'),
            'eur': (self.EURO_RATE, 'Euro')
        }

        if currency not in CUR_LIB.keys():
            return 'Валюта не поддерживается'

        if self.get_remained() == 0:
            return 'Денег нет, держись'

        cur = CUR_LIB[currency]
        remains = round(abs(self.get_remained()) / cur[0], 2)
        if self.get_remained() > 0:
            return (f'На сегодня осталось {remains} {cur[1]}')
        else:
            return (f'Денег нет, держись: твой долг - {remains} {cur[1]}')


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        if self.get_remained() > 0:
            return (
                'Сегодня можно съесть что-нибудь ещё, '
                f'но с общей калорийностью не более {self.get_remained()} кКал'
            )
        else:
            return 'Хватит есть!'


class Record():
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date =  dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, DATE_FORMAT).date()
