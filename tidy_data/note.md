# Note cho các file tidy data

## Device_Specs_Extracted_1.csv

<b>Có 8 cột gồm: 3 cột object, 5 cột float64</b>

### Display

-   DISPLAY_Type: object \_\_\_ 0 missing value, 0.000000% missing value
-   DISPLAY_Size: float64 \_\_\_ 1225 missing value, 9.789819% missing value

#### Cột DISPLAY_Resolution tách ra width với height

-   DISPLAY_Resolution_Width: float64 \_\_\_ 132 missing value, 1.054903% missing value
-   DISPLAY_Resolution_Height: float64 \_\_\_ 54 missing value, 0.431551% missing value

### Platform

Đa số là chuỗi mô tả nên không sài được

-   PLATFORM_OS: object \_\_\_ 3772 missing value, 30.144650% missing value

### Memory

-   MEMORY_Card_slot: object \_\_\_ 0 missing value, 0.000000% missing value

#### Cột MEMORY_Internal tách ra rom với ram, lấy specs cao nhất

-   MEMORY_Internal_rom: float64 \_\_\_ 1877 missing value, 15.000400% missing value
-   MEMORY_Internal_ram: float64 \_\_\_ 4152 missing value, 33.181491% missing value

---> 2 cột rom với ram cân nhắc nên fill null bằng min hay 0 sẽ tốt hơn
