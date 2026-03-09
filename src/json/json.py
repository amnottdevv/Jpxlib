# json.py - JSON Manipulation Library untuk JPX
# Mengikuti pola dari color.py (exports = {'nama': Class()})

import json as py_json
import os

# ============================================================
# FUNGSI-FUNGSI JSON
# ============================================================

class JSON:
    def encode(self, obj):
        """
        Convert JPX object/list ke JSON string
        
        Contoh:
            json.encode({name: "John", age: 30})
            -> '{"name": "John", "age": 30}'
        """
        try:
            return py_json.dumps(obj)
        except TypeError as e:
            return f"<JSON encode error: {e}>"
        except:
            return "{}"
    
    def decode(self, json_str):
        """
        Parse JSON string ke JPX object/list
        
        Contoh:
            json.decode('{"name": "John", "age": 30}')
            -> {name: "John", age: 30}
        """
        if json_str is None:
            return {}
        try:
            return py_json.loads(str(json_str))
        except py_json.JSONDecodeError as e:
            return f"<JSON decode error: {e}>"
        except:
            return {}
    
    def pretty(self, obj, indent=2):
        """
        JSON dengan format bagus (indentasi)
        
        Contoh:
            json.pretty({name: "John", age: 30}, 4)
        """
        try:
            return py_json.dumps(obj, indent=int(indent))
        except:
            return "{}"
    
    def read(self, filepath):
        """
        Baca JSON dari file
        
        Contoh:
            json.read("data.json")
        """
        try:
            with open(str(filepath), 'r', encoding='utf-8') as f:
                return py_json.load(f)
        except FileNotFoundError:
            return f"<File not found: {filepath}>"
        except py_json.JSONDecodeError as e:
            return f"<Invalid JSON in file: {e}>"
        except Exception as e:
            return f"<Error reading file: {e}>"
    
    def write(self, filepath, obj, pretty=True):
        """
        Tulis JSON ke file
        
        Contoh:
            json.write("data.json", {name: "John", age: 30})
            -> true
        """
        try:
            with open(str(filepath), 'w', encoding='utf-8') as f:
                if pretty:
                    py_json.dump(obj, f, indent=2)
                else:
                    py_json.dump(obj, f)
            return True
        except Exception as e:
            return f"<Error writing file: {e}>"
    
    def validate(self, json_str):
        """
        Cek apakah string valid JSON
        
        Contoh:
            json.validate('{"name": "John"}') -> true
            json.validate('{name: John}') -> false
        """
        if json_str is None:
            return False
        try:
            py_json.loads(str(json_str))
            return True
        except:
            return False
    
    def minify(self, json_str):
        """
        Hapus whitespace dari JSON string (minify)
        
        Contoh:
            json.minify('{"name": "John", "age": 30}')
            -> '{"name":"John","age":30}'
        """
        try:
            obj = py_json.loads(str(json_str))
            return py_json.dumps(obj, separators=(',', ':'))
        except:
            return json_str
    
    def load(self, filepath):
        """
        Alias untuk read() - baca JSON dari file
        """
        return self.read(filepath)
    
    def save(self, filepath, obj):
        """
        Alias untuk write() - simpan JSON ke file
        """
        return self.write(filepath, obj)
    
    def merge(self, obj1, obj2):
        """
        Gabungkan dua JSON object
        
        Contoh:
            json.merge({a: 1}, {b: 2}) -> {a: 1, b: 2}
        """
        if not isinstance(obj1, dict) or not isinstance(obj2, dict):
            return obj1
        result = obj1.copy()
        result.update(obj2)
        return result
    
    def keys(self, obj):
        """
        Ambil semua keys dari JSON object
        
        Contoh:
            json.keys({name: "John", age: 30}) -> ["name", "age"]
        """
        if isinstance(obj, dict):
            return list(obj.keys())
        return []
    
    def values(self, obj):
        """
        Ambil semua values dari JSON object
        
        Contoh:
            json.values({name: "John", age: 30}) -> ["John", 30]
        """
        if isinstance(obj, dict):
            return list(obj.values())
        return []
    
    def items(self, obj):
        """
        Ambil pasangan [key, value] dari JSON object
        
        Contoh:
            json.items({name: "John", age: 30})
            -> [["name", "John"], ["age", 30]]
        """
        if isinstance(obj, dict):
            return [[k, v] for k, v in obj.items()]
        return []
    
    def has_key(self, obj, key):
        """
        Cek apakah object memiliki key tertentu
        
        Contoh:
            json.has_key({name: "John"}, "name") -> true
        """
        if isinstance(obj, dict):
            return key in obj
        return False
    
    def get(self, obj, key, default=None):
        """
        Ambil value dengan key, jika tidak ada return default
        
        Contoh:
            json.get({name: "John"}, "age", 0) -> 0
        """
        if isinstance(obj, dict):
            return obj.get(key, default)
        return default
    
    def to_string(self, obj):
        """
        Alias untuk encode() - convert ke JSON string
        """
        return self.encode(obj)
    
    def from_string(self, json_str):
        """
        Alias untuk decode() - parse dari JSON string
        """
        return self.decode(json_str)
    
    def pretty_print(self, obj):
        """
        Langsung print JSON dengan format bagus
        
        Contoh:
            json.pretty_print({name: "John", age: 30})
        """
        print(self.pretty(obj))
    
    def is_empty(self, obj):
        """
        Cek apakah JSON object/list kosong
        
        Contoh:
            json.is_empty({}) -> true
            json.is_empty([]) -> true
        """
        if obj is None:
            return True
        if isinstance(obj, (dict, list)):
            return len(obj) == 0
        return False
    
    def size(self, obj):
        """
        Hitung jumlah item dalam object/list
        
        Contoh:
            json.size({name: "John", age: 30}) -> 2
            json.size([1,2,3]) -> 3
        """
        if isinstance(obj, (dict, list)):
            return len(obj)
        return 0
    
    def copy(self, obj):
        """
        Buat salinan JSON object/list
        
        Contoh:
            json.copy({name: "John"})
        """
        try:
            return py_json.loads(py_json.dumps(obj))
        except:
            return obj
    
    def update(self, target, source):
        """
        Update target object dengan source
        
        Contoh:
            json.update({a: 1}, {b: 2}) -> {a: 1, b: 2}
        """
        if isinstance(target, dict) and isinstance(source, dict):
            target.update(source)
        return target
    
    def clear(self, obj):
        """
        Kosongkan object/list
        
        Contoh:
            json.clear({name: "John"}) -> {}
            json.clear([1,2,3]) -> []
        """
        if isinstance(obj, dict):
            obj.clear()
        elif isinstance(obj, list):
            obj.clear()
        return obj
    
    def type(self, obj):
        """
        Cek tipe JSON (object/array/string/number/boolean/null)
        
        Contoh:
            json.type({}) -> "object"
            json.type([]) -> "array"
            json.type("hello") -> "string"
        """
        if obj is None:
            return "null"
        if isinstance(obj, dict):
            return "object"
        if isinstance(obj, list):
            return "array"
        if isinstance(obj, str):
            return "string"
        if isinstance(obj, bool):
            return "boolean"
        if isinstance(obj, (int, float)):
            return "number"
        return "unknown"

# ============================================================
# EXPORT - INI YANG DICARI JPX (SAMA PERSIS DENGAN COLOR.PY)
# ============================================================
exports = {'json': JSON()}

# Debug message biar tau library berhasil dimuat
if __name__ != "__main__":
    print("[json.py] Library JSON siap digunakan!")
