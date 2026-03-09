# json.py - JSON Library untuk JPX (FIXED)
# Pola: panggil langsung, tanpa $, akses property dengan titik

import json as py_json

class JSON:
    def encode(self, obj):
        """Convert object ke JSON string"""
        try:
            return py_json.dumps(obj)
        except:
            return "{}"
    
    def decode(self, json_str):
        """Parse JSON string ke object"""
        if json_str is None:
            return {}
        try:
            # Parse JSON dan return object
            result = py_json.loads(str(json_str))
            return result
        except:
            return {}
    
    def pretty(self, obj, indent=2):
        """JSON dengan format bagus"""
        try:
            return py_json.dumps(obj, indent=int(indent))
        except:
            return "{}"
    
    def read(self, filepath):
        """Baca JSON dari file"""
        try:
            with open(str(filepath), 'r', encoding='utf-8') as f:
                return py_json.load(f)
        except:
            return {}
    
    def write(self, filepath, obj):
        """Tulis JSON ke file"""
        try:
            with open(str(filepath), 'w', encoding='utf-8') as f:
                py_json.dump(obj, f, indent=2)
            return True
        except:
            return False
    
    def validate(self, json_str):
        """Cek valid JSON"""
        try:
            py_json.loads(str(json_str))
            return True
        except:
            return False
    
    def keys(self, obj):
        """Ambil semua keys"""
        if isinstance(obj, dict):
            return list(obj.keys())
        return []
    
    def values(self, obj):
        """Ambil semua values"""
        if isinstance(obj, dict):
            return list(obj.values())
        return []
    
    def get(self, obj, key, default=None):
        """Ambil value dengan key"""
        if isinstance(obj, dict):
            return obj.get(key, default)
        return default
    
    def merge(self, obj1, obj2):
        """Gabungkan dua object"""
        if not isinstance(obj1, dict) or not isinstance(obj2, dict):
            return obj1
        result = obj1.copy()
        result.update(obj2)
        return result

exports = {'json': JSON()}

if __name__ != "__main__":
    print("[json.py] Library JSON siap!")
