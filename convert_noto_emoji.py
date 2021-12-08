from custom_fonttools.merge import Merger

fonts = [
    "./src/NotoColorEmoji_WindowsCompatible.ttf",
    "./src/Hack Regular Nerd Font Complete Mono Windows Compatible.ttf",
#     "./src/DejaVuSansMono.ttf",
#     "./src/iconsfordevs.ttf",
#     "./src/Noto Mono for Powerline.ttf",
#     "./src/NotoSansCJKjp-Regular.ttf",
]
merged_font = Merger().merge(fonts)
merged_font.save('./NotoColorEmojiNerd.ttf')
