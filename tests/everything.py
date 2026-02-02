from coloray import color, style, truecolor, ansi8bit

truecolor()  # ts 24 bit colors

# foreground named colors
print(color.RED + "red" + color.RESET)
print(color.ORANGE + "orange" + color.RESET)
print(color.YELLOW + "yellow" + color.RESET)
print(color.LIME + "lime" + color.RESET)
print(color.GREEN + "green" + color.RESET)
print(color.CYAN + "cyan" + color.RESET)
print(color.LIGHTBLUE + "lightblue" + color.RESET)
print(color.BLUE + "blue" + color.RESET)
print(color.MAGENTA + "magenta" + color.RESET)
print(color.BLACK + "black" + color.RESET)
print(color.RESET + "wowowo" + color.RESET)

# foreground hex/rgb
print(color.hex("#058aff") + "hex color" + color.RESET)
print(color.rgb(255,0,255) + "rgb color" + color.RESET)

# background colors
print(color.bg.WHITE + color.BLACK + "bg white color w black txt" + color.RESET + style.RESET)
print(color.bg.rgb(128,0,128) + color.YELLOW + "bg purple color w yellow txt" + color.RESET + style.RESET)
print(color.bg.hex("#00FFFF") + color.MAGENTA + "bg cyan color w magenta txt" + color.RESET + style.RESET)

# gradient
print(color.gradient("#FF0000", "#ff8800", "txt gradient red and orange") + color.RESET)

# styles
print(style.BOLD + style.UNDERLINE + style.ITALIC + "wowo" + style.RESET)
print(style.STRIKE + "strike" + color.RESET)
ansi8bit() # ts 8bit

print(color.RED + "red (8-bit)" + color.RESET)
print(color.ORANGE + "orange (8-bit)" + color.RESET)
print(color.LIME + "lime (8-bit)" + color.RESET)
print(color.bg.rgb(128,0,128) + color.YELLOW + "bg purple with yellow text (8-bit)" + color.RESET + style.RESET)
print(color.gradient("#FF0000","#FF8800","gradient red->orange (8-bit)") + color.RESET)
print(style.BOLD + style.UNDERLINE + style.ITALIC + "wowo (8-bit)" + style.RESET)
