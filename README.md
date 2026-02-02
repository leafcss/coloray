# coloray

A minimal Python library for colorful terminal output with support for 24-bit TrueColor, 8-bit fallback, and beautiful gradients.

---

## Features

* **24-bit TrueColor** support.
* **8-bit fallback** for older terminal emulators.
* **Gradients** for both foreground and background.
* **Text Styles**: Bold, italic, underline, strike, and reverse.
* **Simple API**: Lightweight and easy to integrate into any CLI project.

---

## Install

```bash
pip install coloray

```

---

## How to Use

### Switching Modes

By default, `coloray` uses 24-bit mode. You can manually toggle modes based on your terminal's capabilities:

```python
from coloray import truecolor, ansi8bit

truecolor()  # Enable 24-bit TrueColor mode
ansi8bit()   # Fallback to 8-bit mode

```

### Foreground Colors

```python
from coloray import color

# Standard named colors
print(color.RED + "Red Text" + color.RESET)
print(color.LIME + "Lime Text" + color.RESET)
print(color.CYAN + "Cyan Text" + color.RESET)

# Hex and RGB colors
print(color.hex("#058aff") + "Hex Color" + color.RESET)
print(color.rgb(255, 0, 255) + "RGB Color" + color.RESET)

```

### Text Styles

```python
from coloray import style

print(style.BOLD + "Bold Text" + style.RESET)
print(style.ITALIC + "Italic Text" + style.RESET)
print(style.UNDERLINE + "Underline Text" + style.RESET)
print(style.STRIKE + "Strikethrough" + style.RESET)

# Combine styles and colors
print(style.BOLD + style.UNDERLINE + color.RED + "Bold Red Underline" + style.RESET)

```

### Background Colors

```python
from coloray import color, style

# Named backgrounds
print(color.bg.RED + "Red Background" + color.RESET)

# Background + Foreground combinations
print(color.bg.WHITE + color.BLACK + "Black text on White" + color.RESET)

# RGB / Hex backgrounds
print(color.bg.hex("#00ffff") + color.MAGENTA + "Magenta on Cyan" + color.RESET)

```

### Gradients

Gradients automatically interpolate between two colors.

```python
from coloray import color

# Foreground gradient
print(color.gradient("#ff0000", "#ff8800", "Red to Orange Gradient") + color.RESET)

# Background gradient with a fixed foreground color
print(color.bg.gradient("#ff0000", "#ff8800", "Gradient BG", fg=color.BLACK) + color.RESET)

```
---

## Notes

* **Resetting**: Always use `color.RESET` or `style.RESET` to prevent color bleeding into your next terminal line.
* **Compatibility**: Gradients, Hex, and RGB inputs automatically adjust their output based on whether you have `truecolor()` or `ansi8bit()` enabled.
* **Naming**: All named colors are available for both foreground (`color.RED`) and background (`color.bg.RED`).
