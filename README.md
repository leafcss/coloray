# coloray

[![PyPI version](https://img.shields.io/pypi/v/coloray?color=blue&label=PyPI)](https://pypi.org/project/coloray/)
[![PyPI downloads](https://img.shields.io/pypi/dm/coloray?color=green&label=downloads)](https://pypistats.org/packages/coloray)
[![License](https://img.shields.io/badge/license-AGPLv3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0.en.html)
[![GitHub stars](https://img.shields.io/github/stars/leafcss/coloray?style=social)](https://github.com/leafcss/coloray/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/leafcss/coloray)](https://github.com/leafcss/coloray/issues)

A minimal, high-performance Python library for colorful terminal output. Support for 24-bit TrueColor, 8-bit fallback, and easy-to-use gradients.

---

## 🚀 Features

* **24-bit support** for modern terminals.
* **8-bit fallback** automatically handles older environments.
* **Gradients** for both foreground and background text.
* **Background colors** with easy foreground nesting.
* **Full Text Styling**: Bold, italic, underline, strike, and reverse.
* **Lightweight**: Zero heavy dependencies.

---

## 📦 Install

```bash
pip install coloray

```

---

## 🛠 How to Use

### 1. Switching Modes

Choose between high-fidelity 24-bit TrueColor or standard 8-bit colors.

```python
from coloray import truecolor, ansi8bit

truecolor()  # Enable 24-bit mode (Default)
ansi8bit()   # Enable 8-bit mode for compatibility

```

### 2. Basic Colors

Use named constants for quick coloring, or define specific colors using Hex/RGB.

```python
from coloray import color

# Standard named colors
print(color.RED + "This is red" + color.RESET)
print(color.LIME + "This is lime" + color.RESET)

# Hex and RGB support
print(color.hex("#058aff") + "Beautiful Hex Color" + color.RESET)
print(color.rgb(255, 0, 255) + "Vibrant RGB Color" + color.RESET)

```

### 3. Text Styles

Styles can be used individually or combined for emphasis.

```python
from coloray import style

print(style.BOLD + "Bolded text" + style.RESET)
print(style.ITALIC + "Italicized text" + style.RESET)
print(style.UNDERLINE + style.BOLD + "Combined Styles" + style.RESET)

```

### 4. Backgrounds

Apply colors to the text background. You can also layer foreground colors on top.

```python
from coloray import color, style

# Basic Background
print(color.bg.RED + "Red Background" + color.RESET)

# Background + Foreground Mix
print(color.bg.WHITE + color.BLACK + "Black text on White BG" + color.RESET)

```

### 5. Gradients

Smooth transitions between two colors for that extra polish.

```python
from coloray import color

# Foreground gradient
print(color.gradient("#FF0000", "#FF8800", "Red to Orange Gradient") + color.RESET)

# Background gradient with a fixed foreground color
print(color.bg.gradient("#FF0000", "#FF8800", "Gradient BG", fg=color.BLACK) + color.RESET)

```

---

## 📝 Important Notes

* **Always Reset**: Use `color.RESET` and `style.RESET` at the end of your strings to avoid "leaking" styles into the rest of the terminal.
* **Auto-Adapt**: Gradients, Hex, and RGB functions automatically adjust their output based on whether `truecolor()` or `ansi8bit()` is active.
* **Hierarchy**: All named colors are available for both foreground (`color.RED`) and background (`color.bg.RED`).

```
