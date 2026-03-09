# string.py - Complete String Manipulation Library for JPX
# Author: Generated for JPX Interpreter
# License: MIT (sesuai dengan lisensi JPX)

import re
import html
import urllib.parse
import base64
import hashlib
import random
import string as py_string

# ============================================================
# CORE STRING OPERATIONS
# ============================================================

def length(s):
    """
    Mengembalikan panjang string.
    
    Contoh:
        string.length("hello")  -> 5
    """
    if s is None:
        return 0
    if not isinstance(s, str):
        s = str(s)
    return len(s)

def upper(s):
    """
    Mengubah string menjadi huruf besar (uppercase).
    
    Contoh:
        string.upper("hello")  -> "HELLO"
    """
    if s is None:
        return ""
    if not isinstance(s, str):
        s = str(s)
    return s.upper()

def lower(s):
    """
    Mengubah string menjadi huruf kecil (lowercase).
    
    Contoh:
        string.lower("HELLO")  -> "hello"
    """
    if s is None:
        return ""
    if not isinstance(s, str):
        s = str(s)
    return s.lower()

def capitalize(s):
    """
    Mengubah huruf pertama menjadi kapital, sisanya kecil.
    
    Contoh:
        string.capitalize("hello WORLD")  -> "Hello world"
    """
    if s is None:
        return ""
    if not isinstance(s, str):
        s = str(s)
    return s.capitalize()

def title(s):
    """
    Mengubah huruf pertama setiap kata menjadi kapital.
    
    Contoh:
        string.title("hello world")  -> "Hello World"
    """
    if s is None:
        return ""
    if not isinstance(s, str):
        s = str(s)
    return s.title()

def swapcase(s):
    """
    Membalikkan huruf besar menjadi kecil dan sebaliknya.
    
    Contoh:
        string.swapcase("Hello World")  -> "hELLO wORLD"
    """
    if s is None:
        return ""
    if not isinstance(s, str):
        s = str(s)
    return s.swapcase()

# ============================================================
# STRING MANIPULATION
# ============================================================

def strip(s, chars=None):
    """
    Menghapus whitespace atau karakter tertentu dari awal dan akhir string.
    
    Contoh:
        string.strip("  hello  ")          -> "hello"
        string.strip("...hello...", ".")   -> "hello"
    """
    if s is None:
        return ""
    if not isinstance(s, str):
        s = str(s)
    if chars is None:
        return s.strip()
    return s.strip(chars)

def lstrip(s, chars=None):
    """
    Menghapus whitespace atau karakter tertentu dari awal string.
    
    Contoh:
        string.lstrip("  hello")  -> "hello"
    """
    if s is None:
        return ""
    if not isinstance(s, str):
        s = str(s)
    if chars is None:
        return s.lstrip()
    return s.lstrip(chars)

def rstrip(s, chars=None):
    """
    Menghapus whitespace atau karakter tertentu dari akhir string.
    
    Contoh:
        string.rstrip("hello  ")  -> "hello"
    """
    if s is None:
        return ""
    if not isinstance(s, str):
        s = str(s)
    if chars is None:
        return s.rstrip()
    return s.rstrip(chars)

def trim(s):
    """
    Alias untuk strip() - menghapus spasi di awal dan akhir.
    
    Contoh:
        string.trim("  hello  ")  -> "hello"
    """
    return strip(s)

def pad_left(s, width, char=" "):
    """
    Menambahkan karakter di sebelah kiri hingga mencapai lebar tertentu.
    
    Contoh:
        string.pad_left("42", 5, "0")  -> "00042"
    """
    if s is None:
        s = ""
    if not isinstance(s, str):
        s = str(s)
    if len(char) != 1:
        char = " "
    return char * max(0, width - len(s)) + s

def pad_right(s, width, char=" "):
    """
    Menambahkan karakter di sebelah kanan hingga mencapai lebar tertentu.
    
    Contoh:
        string.pad_right("42", 5, "0")  -> "42000"
    """
    if s is None:
        s = ""
    if not isinstance(s, str):
        s = str(s)
    if len(char) != 1:
        char = " "
    return s + char * max(0, width - len(s))

def center(s, width, char=" "):
    """
    Menengahkan string dengan karakter pengisi.
    
    Contoh:
        string.center("hello", 11, "-")  -> "---hello---"
    """
    if s is None:
        s = ""
    if not isinstance(s, str):
        s = str(s)
    if len(char) != 1:
        char = " "
    return s.center(width, char)

def reverse(s):
    """
    Membalikkan urutan karakter dalam string.
    
    Contoh:
        string.reverse("hello")  -> "olleh"
    """
    if s is None:
        return ""
    if not isinstance(s, str):
        s = str(s)
    return s[::-1]

def repeat(s, count):
    """
    Mengulang string sebanyak count kali.
    
    Contoh:
        string.repeat("ha", 3)  -> "hahaha"
    """
    if s is None:
        return ""
    if not isinstance(s, str):
        s = str(s)
    try:
        count = int(count)
        if count <= 0:
            return ""
        return s * count
    except:
        return s

# ============================================================
# STRING SEARCHING & VALIDATION
# ============================================================

def contains(s, substring):
    """
    Mengecek apakah string mengandung substring.
    
    Contoh:
        string.contains("hello world", "world")  -> true
    """
    if s is None or substring is None:
        return False
    if not isinstance(s, str):
        s = str(s)
    if not isinstance(substring, str):
        substring = str(substring)
    return substring in s

def index_of(s, substring, start=0):
    """
    Mengembalikan posisi pertama substring, atau -1 jika tidak ditemukan.
    
    Contoh:
        string.index_of("hello world", "world")  -> 6
    """
    if s is None or substring is None:
        return -1
    if not isinstance(s, str):
        s = str(s)
    if not isinstance(substring, str):
        substring = str(substring)
    try:
        start = int(start)
        return s.find(substring, start)
    except:
        return -1

def last_index_of(s, substring):
    """
    Mengembalikan posisi terakhir substring, atau -1 jika tidak ditemukan.
    
    Contoh:
        string.last_index_of("hello hello", "hello")  -> 6
    """
    if s is None or substring is None:
        return -1
    if not isinstance(s, str):
        s = str(s)
    if not isinstance(substring, str):
        substring = str(substring)
    try:
        return s.rfind(substring)
    except:
        return -1

def starts_with(s, prefix):
    """
    Cek apakah string diawali dengan prefix.
    
    Contoh:
        string.starts_with("hello", "he")  -> true
    """
    if s is None or prefix is None:
        return False
    if not isinstance(s, str):
        s = str(s)
    if not isinstance(prefix, str):
        prefix = str(prefix)
    return s.startswith(prefix)

def ends_with(s, suffix):
    """
    Cek apakah string diakhiri dengan suffix.
    
    Contoh:
        string.ends_with("hello", "lo")  -> true
    """
    if s is None or suffix is None:
        return False
    if not isinstance(s, str):
        s = str(s)
    if not isinstance(suffix, str):
        suffix = str(suffix)
    return s.endswith(suffix)

def count_occurrences(s, substring):
    """
    Menghitung berapa kali substring muncul dalam string.
    
    Contoh:
        string.count_occurrences("hello hello", "hello")  -> 2
    """
    if s is None or substring is None:
        return 0
    if not isinstance(s, str):
        s = str(s)
    if not isinstance(substring, str):
        substring = str(substring)
    if not substring:
        return 0
    return s.count(substring)

# ============================================================
# STRING EXTRACTION
# ============================================================

def char_at(s, index):
    """
    Mengambil karakter pada posisi index.
    
    Contoh:
        string.char_at("hello", 1)  -> "e"
    """
    if s is None:
        return ""
    if not isinstance(s, str):
        s = str(s)
    try:
        index = int(index)
        if 0 <= index < len(s):
            return s[index]
        return ""
    except:
        return ""

def substring(s, start, end=None):
    """
    Mengambil substring dari start ke end.
    Jika end tidak diberikan, ambil sampai akhir.
    
    Contoh:
        string.substring("hello", 1, 3)    -> "el"
        string.substring("hello", 2)        -> "llo"
    """
    if s is None:
        return ""
    if not isinstance(s, str):
        s = str(s)
    try:
        start = int(start)
        if end is not None:
            end = int(end)
            return s[start:end]
        return s[start:]
    except:
        return ""

def first(s, n):
    """
    Mengambil n karakter pertama.
    
    Contoh:
        string.first("hello", 2)  -> "he"
    """
    return substring(s, 0, n)

def last(s, n):
    """
    Mengambil n karakter terakhir.
    
    Contoh:
        string.last("hello", 2)  -> "lo"
    """
    if s is None:
        return ""
    if not isinstance(s, str):
        s = str(s)
    try:
        n = int(n)
        if n <= 0:
            return ""
        return s[-n:]
    except:
        return ""

def before(s, delimiter):
    """
    Mengambil bagian string sebelum delimiter pertama.
    
    Contoh:
        string.before("nama:john:doe", ":")  -> "nama"
    """
    pos = index_of(s, delimiter)
    if pos == -1:
        return s or ""
    return substring(s, 0, pos)

def after(s, delimiter):
    """
    Mengambil bagian string setelah delimiter pertama.
    
    Contoh:
        string.after("nama:john:doe", ":")  -> "john:doe"
    """
    pos = index_of(s, delimiter)
    if pos == -1:
        return ""
    return substring(s, pos + length(delimiter))

def between(s, left, right):
    """
    Mengambil string di antara left dan right.
    
    Contoh:
        string.between("[hello]", "[", "]")  -> "hello"
    """
    pos_left = index_of(s, left)
    if pos_left == -1:
        return ""
    pos_right = index_of(s, right, pos_left + length(left))
    if pos_right == -1:
        return ""
    return substring(s, pos_left + length(left), pos_right)

# ============================================================
# STRING TRANSFORMATION
# ============================================================

def replace(s, old, new):
    """
    Mengganti semua substring old dengan new.
    
    Contoh:
        string.replace("hello world", "world", "JPX")  -> "hello JPX"
    """
    if s is None:
        return ""
    if not isinstance(s, str):
        s = str(s)
    if old is None:
        return s
    if not isinstance(old, str):
        old = str(old)
    if new is None:
        new = ""
    if not isinstance(new, str):
        new = str(new)
    return s.replace(old, new)

def replace_first(s, old, new):
    """
    Mengganti hanya kemunculan pertama old dengan new.
    
    Contoh:
        string.replace_first("a b a", "a", "x")  -> "x b a"
    """
    if s is None:
        return ""
    if not isinstance(s, str):
        s = str(s)
    if old is None:
        return s
    pos = index_of(s, old)
    if pos == -1:
        return s
    return s[:pos] + new + s[pos + length(old):]

def remove(s, substring):
    """
    Menghapus semua kemunculan substring.
    
    Contoh:
        string.remove("hello hello", "llo")  -> "he he"
    """
    return replace(s, substring, "")

def insert(s, position, text):
    """
    Menyisipkan teks pada posisi tertentu.
    
    Contoh:
        string.insert("hello", 2, "LP")  -> "heLPllo"
    """
    if s is None:
        s = ""
    if not isinstance(s, str):
        s = str(s)
    if text is None:
        text = ""
    try:
        position = int(position)
        if position < 0:
            position = 0
        if position > len(s):
            position = len(s)
        return s[:position] + text + s[position:]
    except:
        return s + text

# ============================================================
# SPLIT & JOIN
# ============================================================

def split(s, delimiter=" ", limit=-1):
    """
    Memisahkan string berdasarkan delimiter, mengembalikan list.
    
    Contoh:
        string.split("a,b,c", ",")  -> ["a", "b", "c"]
    """
    if s is None:
        return []
    if not isinstance(s, str):
        s = str(s)
    if delimiter is None:
        delimiter = " "
    if not isinstance(delimiter, str):
        delimiter = str(delimiter)
    try:
        limit = int(limit)
        if limit <= 0:
            return s.split(delimiter)
        parts = s.split(delimiter, limit)
        return parts
    except:
        return [s]

def split_lines(s):
    """
    Memisahkan string per baris.
    
    Contoh:
        string.split_lines("a\nb\nc")  -> ["a", "b", "c"]
    """
    if s is None:
        return []
    if not isinstance(s, str):
        s = str(s)
    return s.splitlines()

def join(list_obj, glue=""):
    """
    Menggabungkan list menjadi string dengan perekat (glue).
    
    Contoh:
        string.join(["a", "b", "c"], ",")  -> "a,b,c"
    """
    if list_obj is None:
        return ""
    if not isinstance(list_obj, list):
        # Coba konversi ke list jika bukan list
        try:
            list_obj = list(list_obj)
        except:
            return str(list_obj)
    if glue is None:
        glue = ""
    return glue.join(str(item) for item in list_obj)

def join_path(parts):
    """
    Menggabungkan bagian-bagian path dengan separator yang sesuai.
    
    Contoh:
        string.join_path(["folder", "sub", "file.txt"])  -> "folder/sub/file.txt"
    """
    if parts is None:
        return ""
    if not isinstance(parts, list):
        return str(parts)
    # Gunakan forward slash untuk kompatibilitas
    return "/".join(str(p).strip("/") for p in parts)

def explode(s, delimiter=" "):
    """
    Alias untuk split() - memisahkan string.
    """
    return split(s, delimiter)

def implode(list_obj, glue=""):
    """
    Alias untuk join() - menggabungkan list.
    """
    return join(list_obj, glue)

# ============================================================
# CASE CONVERSIONS
# ============================================================

def camel_case(s):
    """
    Mengubah ke camelCase (huruf pertama kecil).
    
    Contoh:
        string.camel_case("hello world")  -> "helloWorld"
    """
    if s is None:
        return ""
    if not isinstance(s, str):
        s = str(s)
    # Hapus karakter non-alfanumerik, jadikan spasi
    words = re.sub(r'[^a-zA-Z0-9]+', ' ', s).strip().split()
    if not words:
        return ""
    # Kata pertama lowercase, sisanya capitalize
    return words[0].lower() + ''.join(w.capitalize() for w in words[1:])

def pascal_case(s):
    """
    Mengubah ke PascalCase (huruf pertama besar).
    
    Contoh:
        string.pascal_case("hello world")  -> "HelloWorld"
    """
    if s is None:
        return ""
    if not isinstance(s, str):
        s = str(s)
    words = re.sub(r'[^a-zA-Z0-9]+', ' ', s).strip().split()
    return ''.join(w.capitalize() for w in words)

def snake_case(s):
    """
    Mengubah ke snake_case (dengan underscore).
    
    Contoh:
        string.snake_case("hello world")  -> "hello_world"
    """
    if s is None:
        return ""
    if not isinstance(s, str):
        s = str(s)
    # Ganti non-alfanumerik dengan underscore
    s = re.sub(r'[^a-zA-Z0-9]+', '_', s)
    # Hapus underscore ganda
    s = re.sub(r'_+', '_', s)
    # Hapus underscore di awal/akhir
    return s.strip('_').lower()

def kebab_case(s):
    """
    Mengubah ke kebab-case (dengan dash).
    
    Contoh:
        string.kebab_case("hello world")  -> "hello-world"
    """
    if s is None:
        return ""
    if not isinstance(s, str):
        s = str(s)
    # Ganti non-alfanumerik dengan dash
    s = re.sub(r'[^a-zA-Z0-9]+', '-', s)
    # Hapus dash ganda
    s = re.sub(r'-+', '-', s)
    # Hapus dash di awal/akhir
    return s.strip('-').lower()

# ============================================================
# ENCODING / DECODING
# ============================================================

def url_encode(s):
    """
    Encode string untuk URL.
    
    Contoh:
        string.url_encode("hello world")  -> "hello%20world"
    """
    if s is None:
        return ""
    if not isinstance(s, str):
        s = str(s)
    return urllib.parse.quote(s)

def url_decode(s):
    """
    Decode string dari URL encoding.
    
    Contoh:
        string.url_decode("hello%20world")  -> "hello world"
    """
    if s is None:
        return ""
    if not isinstance(s, str):
        s = str(s)
    return urllib.parse.unquote(s)

def html_encode(s):
    """
    Encode karakter HTML ke entity.
    
    Contoh:
        string.html_encode("<tag>")  -> "&lt;tag&gt;"
    """
    if s is None:
        return ""
    if not isinstance(s, str):
        s = str(s)
    return html.escape(s)

def html_decode(s):
    """
    Decode entity HTML ke karakter asli.
    
    Contoh:
        string.html_decode("&lt;tag&gt;")  -> "<tag>"
    """
    if s is None:
        return ""
    if not isinstance(s, str):
        s = str(s)
    return html.unescape(s)

def base64_encode(s):
    """
    Encode string ke base64.
    
    Contoh:
        string.base64_encode("hello")  -> "aGVsbG8="
    """
    if s is None:
        return ""
    if not isinstance(s, str):
        s = str(s)
    return base64.b64encode(s.encode('utf-8')).decode('utf-8')

def base64_decode(s):
    """
    Decode string dari base64.
    
    Contoh:
        string.base64_decode("aGVsbG8=")  -> "hello"
    """
    if s is None:
        return ""
    if not isinstance(s, str):
        s = str(s)
    try:
        return base64.b64decode(s.encode('utf-8')).decode('utf-8')
    except:
        return ""

def md5(s):
    """
    Menghitung hash MD5 dari string.
    
    Contoh:
        string.md5("hello")  -> "5d41402abc4b2a76b9719d911017c592"
    """
    if s is None:
        return ""
    if not isinstance(s, str):
        s = str(s)
    return hashlib.md5(s.encode('utf-8')).hexdigest()

def sha1(s):
    """
    Menghitung hash SHA1 dari string.
    
    Contoh:
        string.sha1("hello")  -> "aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d"
    """
    if s is None:
        return ""
    if not isinstance(s, str):
        s = str(s)
    return hashlib.sha1(s.encode('utf-8')).hexdigest()

def sha256(s):
    """
    Menghitung hash SHA256 dari string.
    
    Contoh:
        string.sha256("hello")  -> "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
    """
    if s is None:
        return ""
    if not isinstance(s, str):
        s = str(s)
    return hashlib.sha256(s.encode('utf-8')).hexdigest()

# ============================================================
# VALIDATION
# ============================================================

def is_alpha(s):
    """
    Cek apakah string hanya berisi huruf.
    
    Contoh:
        string.is_alpha("hello")  -> true
        string.is_alpha("hello123")  -> false
    """
    if s is None:
        return False
    if not isinstance(s, str):
        s = str(s)
    return s.isalpha()

def is_digit(s):
    """
    Cek apakah string hanya berisi angka.
    
    Contoh:
        string.is_digit("123")  -> true
        string.is_digit("123a")  -> false
    """
    if s is None:
        return False
    if not isinstance(s, str):
        s = str(s)
    return s.isdigit()

def is_alnum(s):
    """
    Cek apakah string hanya berisi huruf dan angka.
    
    Contoh:
        string.is_alnum("hello123")  -> true
    """
    if s is None:
        return False
    if not isinstance(s, str):
        s = str(s)
    return s.isalnum()

def is_lower(s):
    """
    Cek apakah string semua huruf kecil.
    
    Contoh:
        string.is_lower("hello")  -> true
        string.is_lower("Hello")  -> false
    """
    if s is None:
        return False
    if not isinstance(s, str):
        s = str(s)
    return s.islower()

def is_upper(s):
    """
    Cek apakah string semua huruf besar.
    
    Contoh:
        string.is_upper("HELLO")  -> true
    """
    if s is None:
        return False
    if not isinstance(s, str):
        s = str(s)
    return s.isupper()

def is_space(s):
    """
    Cek apakah string hanya berisi whitespace.
    
    Contoh:
        string.is_space("   ")  -> true
    """
    if s is None:
        return False
    if not isinstance(s, str):
        s = str(s)
    return s.isspace()

def is_empty(s):
    """
    Cek apakah string kosong atau None.
    
    Contoh:
        string.is_empty("")  -> true
        string.is_empty(null)  -> true
        string.is_empty("hello")  -> false
    """
    return s is None or (isinstance(s, str) and s == "")

def is_not_empty(s):
    """
    Cek apakah string tidak kosong.
    
    Contoh:
        string.is_not_empty("hello")  -> true
    """
    return not is_empty(s)

def is_email(s):
    """
    Validasi format email sederhana.
    
    Contoh:
        string.is_email("user@example.com")  -> true
    """
    if s is None or not isinstance(s, str):
        return False
    # Regex sederhana untuk email
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, s) is not None

def is_url(s):
    """
    Validasi format URL sederhana.
    
    Contoh:
        string.is_url("https://example.com")  -> true
    """
    if s is None or not isinstance(s, str):
        return False
    pattern = r'^(https?|ftp)://[^\s/$.?#].[^\s]*$'
    return re.match(pattern, s) is not None

# ============================================================
# GENERATION
# ============================================================

def random(length=10, chars=None):
    """
    Menghasilkan string acak dengan panjang tertentu.
    
    Contoh:
        string.random(8)  -> "aB3dE5fG"
    """
    try:
        length = int(length)
        if length <= 0:
            return ""
        if chars is None:
            chars = py_string.ascii_letters + py_string.digits
        return ''.join(random.choice(chars) for _ in range(length))
    except:
        return ""

def random_letters(length=10):
    """
    Menghasilkan string acak berisi huruf.
    
    Contoh:
        string.random_letters(5)  -> "aBcDe"
    """
    return random(length, py_string.ascii_letters)

def random_digits(length=10):
    """
    Menghasilkan string acak berisi angka.
    
    Contoh:
        string.random_digits(5)  -> "12345"
    """
    return random(length, py_string.digits)

def random_hex(length=8):
    """
    Menghasilkan string heksadesimal acak.
    
    Contoh:
        string.random_hex(6)  -> "a1b2c3"
    """
    return random(length, "0123456789abcdef")

def uuid():
    """
    Menghasilkan UUID versi 4.
    
    Contoh:
        string.uuid()  -> "550e8400-e29b-41d4-a716-446655440000"
    """
    import uuid as uuid_lib
    return str(uuid_lib.uuid4())

# ============================================================
# SLUG & FORMATTING
# ============================================================

def slugify(s):
    """
    Mengubah string menjadi slug untuk URL.
    
    Contoh:
        string.slugify("Hello World! 2024")  -> "hello-world-2024"
    """
    if s is None:
        return ""
    if not isinstance(s, str):
        s = str(s)
    # Lowercase, ganti non-alfanumerik dengan dash
    s = s.lower()
    s = re.sub(r'[^a-z0-9]+', '-', s)
    return s.strip('-')

def truncate(s, length, suffix="..."):
    """
    Memotong string hingga panjang tertentu, tambahkan suffix.
    
    Contoh:
        string.truncate("Hello world", 5)  -> "Hello..."
    """
    if s is None:
        return ""
    if not isinstance(s, str):
        s = str(s)
    try:
        length = int(length)
        if len(s) <= length:
            return s
        return s[:length].rstrip() + suffix
    except:
        return s

def word_wrap(s, width=80):
    """
    Membungkus teks agar tidak melebihi lebar tertentu.
    
    Contoh:
        string.word_wrap("long text...", 20)
    """
    if s is None:
        return ""
    if not isinstance(s, str):
        s = str(s)
    try:
        width = int(width)
        words = s.split()
        lines = []
        current_line = []
        current_length = 0
        
        for word in words:
            if current_length + len(word) + 1 <= width:
                current_line.append(word)
                current_length += len(word) + 1
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
                current_length = len(word)
        
        if current_line:
            lines.append(' '.join(current_line))
        
        return '\n'.join(lines)
    except:
        return s

# ============================================================
# COMPARISON
# ============================================================

def compare(s1, s2):
    """
    Membandingkan dua string secara case-sensitive.
    Mengembalikan:
        0 jika sama
        <0 jika s1 < s2
        >0 jika s1 > s2
    
    Contoh:
        string.compare("a", "b")  -> -1
    """
    if s1 is None and s2 is None:
        return 0
    if s1 is None:
        return -1
    if s2 is None:
        return 1
    if not isinstance(s1, str):
        s1 = str(s1)
    if not isinstance(s2, str):
        s2 = str(s2)
    if s1 == s2:
        return 0
    return -1 if s1 < s2 else 1

def compare_ignore_case(s1, s2):
    """
    Membandingkan dua string secara case-insensitive.
    
    Contoh:
        string.compare_ignore_case("Hello", "hello")  -> 0
    """
    if s1 is None and s2 is None:
        return 0
    if s1 is None:
        return -1
    if s2 is None:
        return 1
    if not isinstance(s1, str):
        s1 = str(s1)
    if not isinstance(s2, str):
        s2 = str(s2)
    return compare(lower(s1), lower(s2))

def equals(s1, s2):
    """
    Cek apakah dua string sama persis.
    
    Contoh:
        string.equals("hello", "hello")  -> true
    """
    return compare(s1, s2) == 0

def equals_ignore_case(s1, s2):
    """
    Cek apakah dua string sama (abaikan huruf besar/kecil).
    
    Contoh:
        string.equals_ignore_case("Hello", "hello")  -> true
    """
    return compare_ignore_case(s1, s2) == 0

# ============================================================
# CONSTANTS
# ============================================================

def get_constants():
    """
    Mengembalikan konstanta string yang berguna.
    """
    return {
        "digits": "0123456789",
        "letters": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "lowercase": "abcdefghijklmnopqrstuvwxyz",
        "uppercase": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "punctuation": "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~",
        "whitespace": " \t\n\r\x0b\x0c",
        "hexdigits": "0123456789abcdefABCDEF",
        "octdigits": "01234567"
    }

# ============================================================
# EXPORTS - Semua fungsi yang akan diregistrasi ke JPX
# ============================================================

# Ini adalah dictionary yang berisi semua fungsi yang bisa dipanggil dari JPX
string_functions = {
    # Core operations
    "length": length,
    "len": length,  # Alias
    "upper": upper,
    "lower": lower,
    "capitalize": capitalize,
    "title": title,
    "swapcase": swapcase,
    
    # Manipulation
    "strip": strip,
    "lstrip": lstrip,
    "rstrip": rstrip,
    "trim": trim,
    "pad_left": pad_left,
    "pad_right": pad_right,
    "center": center,
    "reverse": reverse,
    "repeat": repeat,
    
    # Searching
    "contains": contains,
    "index_of": index_of,
    "last_index_of": last_index_of,
    "starts_with": starts_with,
    "ends_with": ends_with,
    "count": count_occurrences,
    
    # Extraction
    "char_at": char_at,
    "substring": substring,
    "substr": substring,  # Alias
    "first": first,
    "last": last,
    "before": before,
    "after": after,
    "between": between,
    
    # Transformation
    "replace": replace,
    "replace_first": replace_first,
    "remove": remove,
    "insert": insert,
    
    # Split & Join
    "split": split,
    "split_lines": split_lines,
    "join": join,
    "join_path": join_path,
    "explode": explode,
    "implode": implode,
    
    # Case conversions
    "camel_case": camel_case,
    "pascal_case": pascal_case,
    "snake_case": snake_case,
    "kebab_case": kebab_case,
    
    # Encoding
    "url_encode": url_encode,
    "url_decode": url_decode,
    "html_encode": html_encode,
    "html_decode": html_decode,
    "base64_encode": base64_encode,
    "base64_decode": base64_decode,
    "md5": md5,
    "sha1": sha1,
    "sha256": sha256,
    
    # Validation
    "is_alpha": is_alpha,
    "is_digit": is_digit,
    "is_alnum": is_alnum,
    "is_lower": is_lower,
    "is_upper": is_upper,
    "is_space": is_space,
    "is_empty": is_empty,
    "is_not_empty": is_not_empty,
    "is_email": is_email,
    "is_url": is_url,
    
    # Generation
    "random": random,
    "random_letters": random_letters,
    "random_digits": random_digits,
    "random_hex": random_hex,
    "uuid": uuid,
    
    # Slug & Formatting
    "slugify": slugify,
    "truncate": truncate,
    "word_wrap": word_wrap,
    
    # Comparison
    "compare": compare,
    "compare_ignore_case": compare_ignore_case,
    "equals": equals,
    "equals_ignore_case": equals_ignore_case,
    
    # Constants (fungsi khusus yang mengembalikan objek)
    "constants": get_constants,
}

# Untuk memudahkan registrasi, export juga daftar nama fungsi
__all__ = ["string_functions"]
