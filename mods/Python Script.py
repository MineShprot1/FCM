import os

current_dir = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(current_dir, "mods_list.txt")

mods = sorted(
    f for f in os.listdir(current_dir)
    if f.lower().endswith(".jar")
)

with open(output_file, "w", encoding="utf-8") as file:
    for mod in mods:
        file.write(mod + "\n")

print(f"Готово! Найдено модов: {len(mods)}")
print("Список сохранён в mods_list.txt")
