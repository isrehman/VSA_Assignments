# Find Maximum Element

Verilmiş ədəd massivində maksimum elementi tapan funksiya.

## İstifadə

```python
from find_max import find_max

find_max([3, 1, 9, 2])   # → 9
find_max([-5, -1, -3])   # → -1
find_max([42])            # → 42
find_max([])              # → Warning + None
```

## Suallar

### 1. Seçilmiş alqoritmin zaman mürəkkəbliyi nədir?

**O(n)** — xətti mürəkkəblik.  
Funksiya massivin hər elementinə tam olaraq bir dəfə baxır.  
`n` elementli massiv üçün dəqiq `n − 1` müqayisə aparılır.

### 2. Eyni problemi həll edən alternativ yanaşma varmı?

| Yanaşma | Zaman | Qeyd |
|---|---|---|
| **Xətti axtarış** (bu həll) | O(n) | Ən optimal |
| `max()` built-in | O(n) | Python daxili, eyni məntiq |
| Sıralama + son element | O(n log n) | Lazımsız əlavə iş |
| Rekursiv bölmə | O(n) | Əlavə stack yükü var |

### 3. Niyə bu həll daha uyğundur?

- **Minimal mürəkkəblik:** massivi yalnız bir dəfə gəzir, əlavə yaddaş istifadə etmir — yəni O(1) space complexity.  
- **Sadəlik:** şərt aydın, oxunuşu asandır, debug etmək rahatdır.  
- **Sıralama yoxdur:** sıralama O(n log n) vaxt tələb edir; maksimum tapmaq üçün buna ehtiyac yoxdur.  
- **Sərhəd hallar idarə olunur:** boş massiv üçün xəbərdarlıq verir, tək elementli massiv üçün düzgün işləyir, mənfi ədədlər üçün də problem yoxdur.
