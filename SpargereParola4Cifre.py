import pyautogui
import itertools
import time

# 🔴 SETEAZĂ COORDONATELE pentru fiecare cifră (exemplu, trebuie ajustate!)
positions = {
    1: (1268, 517),
    2: (1355, 517),
    3: (1268, 604),
    4: (1355, 604),
    5: (1268, 700),
    6: (1355, 700),
    7: (1268, 800),
    8: (1355, 800),
}


# ⏳ Timp între apăsări (în secunde)
delay = 0.2  

# 🔄 Generează toate combinațiile posibile (4096 în total)
for combo in itertools.product(range(1, 9), repeat=4):
    for digit in combo:
        x, y = positions[digit]
        pyautogui.click(x, y)
        time.sleep(delay)  # Pauză scurtă între apăsări

    # 🔵 Dacă trebuie să apeși un buton de confirmare, adaugă aici:
    # pyautogui.press("enter")  # Sau pyautogui.click(x, y) pentru un alt buton

    print(f"Încercat combinația: {''.join(map(str, combo))}")

    # ⚠️ Poți opri scriptul apăsând CTRL+C sau închizând terminalul
