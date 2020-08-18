def search_string_array(src, key):
    return bool([name for name in src if key in name])

src = ["minecraftgame", "intelligent", "innercrafttalent", "knife", "scissor", "stonecrafter"]
key = "craft"

print(search_string_array(src, key))
