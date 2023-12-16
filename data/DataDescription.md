# Tên bộ dữ liệu

Gmsarena Device Spec Dataset

# Nguồn dữ liệu

Bộ dữ liệu được thu thập từ trang web [Gsmarena](https://www.gsmarena.com/).

# Mô tả dữ liệu

Bộ dữ liệu gồm 3 file csv:
* Brand_data.csv: chứa thông tin về các hãng điện thoại và đường dẫn đến trang thông tin của hãng đó.
* Devices_url.csv: chứng thông tin về hãng và đường dẫn đến trang thông tin của điện thoại.
* Devices_Specs.csv: là file dữ liệu chính của bộ dữ liệu, chứa thông tin về các thông số kỹ thuật của điện thoại.

# Các trường dữ liệu

Các trường dữ liệu chính của bộ dữ liệu:

* Brand_data.csv: gồm 3 thuộc tính:
    * BrandName: tên hãng điện thoại.
    * NumberOfPhone: số lượng điện thoại của hãng.
    * BrandUrl: đường dẫn đến trang thông tin của hãng điện thoại.

* Devices_url.csv: gồm 2 thuộc tính:
    * BrandName: tên hãng điện thoại.
    * DeviceUrl: đường dẫn đến trang thông tin của điện thoại.

* Devices_Specs.csv: gồm 52 thuộc tính:
    * Brand: tên hãng điện thoại.
    * url: đường dẫn đến trang thông tin của điện thoại.
    * imgUrl: đường dẫn đến ảnh của điện thoại.
    * Name: tên điện thoại.

    * NETWORK_Technology: mạng di động.
    * NETWORK_2G_bands: mạng 2G.
    * NETWORK_3G_bands: mạng 3G.
    * NETWORK_4G_bands: mạng 4G.
    * NETWORK_5G_bands: mạng 5G.
    * NETWORK_GPRS: có hỗ trợ GPRS hay không.
    * NETWORK_EDGE: có hỗ trợ EDGE hay không.
    * NETWORK_Speed: tốc độ mạng.

    * LAUNCH_Announced: ngày ra mắt.
    * LAUNCH_Status: tình trạng ra mắt.

    * BODY_Dimensions: kích thước.
    * BODY_Weight: trọng lượng.
    * BODY_Build: chất liệu.
    * BODY_SIM: số lượng sim.

    * DISPLAY_Type: loại màn hình.
    * DISPLAY_Size: kích thước màn hình.
    * DISPLAY_Resolution: độ phân giải màn hình.
    * DISPLAY_Protection: chất liệu bảo vệ màn hình.

    * PLATFORM_OS: hệ điều hành.
    * PLATFORM_Chipset: chip xử lý.
    * PLATFORM_CPU: tốc độ chip xử lý.
    * PLATFORM_GPU: chip đồ họa.

    * MEMORY_Card_slot: có hỗ trợ thẻ nhớ hay không.
    * MEMORY_Internal: bộ nhớ trong.

    * MAIN_CAM_1_Module: số lượng camera sau.
    * MAIN_CAM_1_Features: tính năng camera sau.
    * MAIN_CAM_1_Video: chất lượng quay video của camera sau.

    * SELFIE_CAM_2_Module: số lượng camera trước.
    * SELFIE_CAM_2_Features: tính năng camera trước.
    * SELFIE_CAM_2_Video: chất lượng quay video của camera trước.

    * SOUND_Loudspeaker: có loa ngoài hay không.
    * SOUND_35mm_jack: có jack cắm tai nghe 3.5mm hay không.

    * COMMS_WLAN: có hỗ trợ wifi hay không.
    * COMMS_Bluetooth: có hỗ trợ bluetooth hay không.
    * COMMS_GPS: có hỗ trợ GPS hay không.
    * COMMS_NFC: có hỗ trợ NFC hay không.
    * COMMS_Radio: có hỗ trợ radio hay không.
    * COMMS_USB: có hỗ trợ cổng USB hay không.

    * FEATURES_Sensors: các cảm biến.

    * BATTERY_Type: loại pin.
    * BATTERY_Stand_by: thời gian chờ.
    * BATTERY_Talk_time: thời gian đàm thoại.
    * BATTERY_Music_play: thời gian nghe nhạc.

    * MISC_Colors: màu sắc.
    * MISC_SAR: mức độ phát ra của sóng điện từ ở mỹ.
    * MISC_SAR_EU: mức độ phát ra của sóng điện từ ở châu âu.
    * MISC_Models: các model khác.
    * MISC_Price: giá bán.

# Quy trình thu thập dữ liệu

## Các bước thu thập dữ liệu

* Bước 1: Thu thập thông tin về các hãng điện thoại
* Bước 2: Truy cập vào từng hãng và thu thập đường dẫn đến các điện thoại của các hãng
* Bước 3: Truy cập vào từng điện thoại và thu thập thông tin về các thông số kỹ thuật của điện thoại

## Các công cụ sử dụng

* Python 3.10.5
* BeautifulSoup 4.12.0
* Requests 2.28.2
* Selenium 4.8.3
* Webdriver for Edge 119.0.2151.44

# Trích xuất dữ liệu

Chưa thực hiện

Bộ dữ liệu hiện đang là dữ liệu thô, chưa thực hiện các bước trích xuất dữ liệu và tiền xử lý. Do đó đại đa số các trường dữ liệu đều là dạng chuỗi.

Kế hoặch trích xuất dữ liệu: thực hiện tách chuỗi và chuyển đổi dữ liệu về dạng số hoặc thực hiện mã hoá dữ liệu.

# Thống kê mô tả

Đang được thực hiện trong file [inspectData.ipynb](data/inspectData.ipynb) và sẽ được cập nhật sau khi thực hiện trích xuất dữ liệu.

# Tiền xử lý dữ liệu

Chưa thực hiện