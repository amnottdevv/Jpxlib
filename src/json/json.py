# json.py - JSON Manipulation Library untuk JPX (FIXED VERSION)

import json as py_json

# ============================================================
# FUNGSI-FUNGSI JSON
# ============================================================

def _ensure_dict(obj):
    """Pastikan return value selalu dict/list, bukan string"""
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, list):
        return obj
    return {}

def _ensure_string(obj):
    """Pastikan return value selalu string"""
    if obj is None:
        return ""
    return str(obj)

class JSON:
    def encode(self, obj):
        """Convert JPX object/list ke JSON string"""
        try:
            return py_json.dumps(obj)
        except:
            return "{}"
    
    def decode(self, json_str):
        """
        Parse JSON string ke JPX object/list
        PASTIKAN return dict/list, BUKAN string!
        """
        if json_str is None:
            return {}
        try:
            # Parse JSON
            result = py_json.loads(str(json_str))
            # Pastikan return dict/list, bukan string
            return result
        except py_json.JSONDecodeError:
            return {}
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
    
    def write(self, filepath, obj, pretty=True):
        """Tulis JSON ke file"""
        try:
            with open(str(filepath), 'w', encoding='utf-8') as f:
                if pretty:
                    py_json.dump(obj, f, indent=2)
                else:
                    py_json.dump(obj, f)
            return True
        except:
            return False
    
    def validate(self, json_str):
        """Cek apakah string valid JSON"""
        if json_str is None:
            return False
        try:
            py_json.loads(str(json_str))
            return True
        except:
            return False
    
    def keys(self, obj):
        """Ambil semua keys dari JSON object"""
        if isinstance(obj, dict):
            return list(obj.keys())
        return []
    
    def values(self, obj):
        """Ambil semua values dari JSON object"""
        if isinstance(obj, dict):
            return list(obj.values())
        return []
    
    def get(self, obj, key, default=None):
        """Ambil value dengan key"""
        if isinstance(obj, dict):
            return obj.get(key, default)
        return default
    
    def has_key(self, obj, key):
        """Cek apakah object memiliki key"""
        if isinstance(obj, dict):
            return key in obj
        return False
    
    def merge(self, obj1, obj2):
        """Gabungkan dua JSON object"""
        if not isinstance(obj1, dict) or not isinstance(obj2, dict):
            return obj1
        result = obj1.copy()
        result.update(obj2)
        return result
    
    def to_string(self, obj):
        """Alias untuk encode()"""
        return self.encode(obj)
    
    def from_string(self, json_str):
        """Alias untuk decode() - PASTIKAN return object"""
        return self.decode(json_str)

# ============================================================
# EXPORT
# ============================================================
exports = {'json': JSON()}

if __name__ != "__main__":
    print("[json.py] Library JSON siap digunakan!")
