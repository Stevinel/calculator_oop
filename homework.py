import datetime as dt
date_format = '%d.%m.%Y'

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, new_record):
        self.records.append(new_record)

    def get_today_stats(self):
        today_stats_count = 0
        today_date = dt.datetime.now().date()
        for i in self.records:
            if i.date == today_date:
                today_stats_count += i.amount
        return today_stats_count
    
    def get_week_stats(self):
        week_stats = 0
        today = dt.datetime.now().date()
        date_week_ago = (today - dt.timedelta(days=7))
        for i in self.records:
            if date_week_ago <= i.date <= today:
                week_stats += i.amount
        return week_stats

class CashCalculator(Calculator):
    USD_RATE = 77.48
    EURO_RATE = 91.06

    def get_today_cash_remained(self, currency):
        remains = self.limit - self.get_today_stats()
      
        if currency == 'usd':
            cur = (f'{round(abs(remains/self.USD_RATE), 2)} USD')
        elif currency == 'eur':
            cur = (f'{round(abs(remains/self.EURO_RATE), 2)} Euro')
        else:
            cur = (f'{abs(remains)} руб')

        if remains > 0:
            return (f'На сегодня осталось {cur}')
        elif remains < 0:
            return (f'Денег нет, держись: твой долг - {cur}')
        else:
            return 'Денег нет, держись'
            
class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        remains = self.limit - self.get_today_stats()
        print(self.get_today_stats())
        if remains > 0:
            return (f'Сегодня можно съесть что-нибудь ещё,\
 но с общей калорийностью не более {remains} кКал')
        else:
            return 'Хватит есть!'
    
class Record():
    def __init__(self, amount, comment, date = None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, date_format).date()
