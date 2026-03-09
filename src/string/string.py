# datetime.py - Date & Time Library untuk JPX
import time
import datetime as dt

class DateTime:
    def now(self):
        """Tanggal dan waktu sekarang"""
        now = dt.datetime.now()
        return {
            'year': now.year,
            'month': now.month,
            'day': now.day,
            'hour': now.hour,
            'minute': now.minute,
            'second': now.second,
            'iso': now.isoformat()
        }
    
    def today(self):
        """Tanggal hari ini"""
        today = dt.date.today()
        return {
            'year': today.year,
            'month': today.month,
            'day': today.day,
            'iso': today.isoformat()
        }
    
    def format(self, date_obj, format_str="%Y-%m-%d %H:%M:%S"):
        """Format tanggal ke string"""
        try:
            if isinstance(date_obj, dict):
                # Dari output now()/today()
                d = dt.datetime(
                    date_obj.get('year', 2000),
                    date_obj.get('month', 1),
                    date_obj.get('day', 1),
                    date_obj.get('hour', 0),
                    date_obj.get('minute', 0),
                    date_obj.get('second', 0)
                )
                return d.strftime(format_str)
            return str(date_obj)
        except:
            return ""
    
    def parse(self, date_str, format_str="%Y-%m-%d"):
        """Parse string ke tanggal"""
        try:
            d = dt.datetime.strptime(date_str, format_str)
            return {
                'year': d.year,
                'month': d.month,
                'day': d.day,
                'hour': d.hour,
                'minute': d.minute,
                'second': d.second
            }
        except:
            return None
    
    def add_days(self, date_obj, days):
        """Tambah hari ke tanggal"""
        try:
            if isinstance(date_obj, dict):
                d = dt.datetime(
                    date_obj.get('year', 2000),
                    date_obj.get('month', 1),
                    date_obj.get('day', 1)
                )
                result = d + dt.timedelta(days=int(days))
                return {
                    'year': result.year,
                    'month': result.month,
                    'day': result.day
                }
            return date_obj
        except:
            return date_obj
    
    def diff_days(self, date1, date2):
        """Selisih hari antara dua tanggal"""
        try:
            if isinstance(date1, dict) and isinstance(date2, dict):
                d1 = dt.date(date1['year'], date1['month'], date1['day'])
                d2 = dt.date(date2['year'], date2['month'], date2['day'])
                return abs((d2 - d1).days)
            return 0
        except:
            return 0
    
    def timestamp(self):
        """Unix timestamp sekarang"""
        return int(time.time())
    
    def sleep(self, seconds):
        """Delay program"""
        time.sleep(float(seconds))

exports = {'datetime': DateTime()}
