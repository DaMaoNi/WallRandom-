import ctypes
import urllib.request
import os
import time

SPI_SETDESKWALLPAPER = 20
SPIF_UPDATEINIFILE = 0x01
SPIF_SENDWININICHANGE = 0x02

script_dir = os.path.dirname(os.path.abspath(__file__))
wallpaper_path = os.path.join(script_dir, "wallpaper.jpg")

url = "https://picsum.photos/1920/1080"
timeout = 600

while True:
    try:
        urllib.request.urlretrieve(url, wallpaper_path)

        ctypes.windll.user32.SystemParametersInfoW(
            SPI_SETDESKWALLPAPER, 0,
            wallpaper_path,
            SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE
        )
        print("Wallpaper changed successfully.")
        break
    except Exception as e:
        print(f"Error: {e}. Retrying...")
        time.sleep(5)