
# Zkrácený výpis: pouze funkce výběru kvality + místo pro logiku přehrávání z Webshare
import xbmcgui

def select_quality_filter():
    options = ["1080p", "720p", "Vše (bez filtru)"]
    choice = xbmcgui.Dialog().select("Vyber požadovanou kvalitu", options)
    if choice == 0:
        return "1080p"
    elif choice == 1:
        return "720p"
    else:
        return None

# Dummy funkce pro demonstraci
def main_menu():
    xbmcgui.Dialog().ok("CinemaKitty", "Doplněk je připraven. (Testovací verze)")

if __name__ == '__main__':
    main_menu()
