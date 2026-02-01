# 🏋️ BMI Calculator - Python GUI Application

A comprehensive Body Mass Index (BMI) calculator built with Python and Tkinter, featuring three versions from basic to advanced with modern UI design.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-purple)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📊 What is BMI?

Body Mass Index (BMI) is a measure of body fat based on height and weight. It's calculated using:

```
BMI = weight (kg) / height² (m²)
```

### BMI Categories:
- **Below 18.5** = Underweight 🔵
- **18.5 - 24.9** = Normal (Healthy) 🟢
- **25.0 - 29.9** = Overweight 🟠
- **30.0 - 34.9** = Obese 🔴
- **Above 35.0** = Extremely Obese ⚫

## 🌟 Features

### Core Features (All Versions)
✅ **Accurate BMI Calculation** - WHO standard formula  
✅ **Category Classification** - 5 BMI categories with health advice  
✅ **Color-Coded Results** - Visual feedback based on BMI category  
✅ **Input Validation** - Prevents invalid data entry  
✅ **Error Handling** - User-friendly error messages  

### Enhanced Features (v2 & v3)
✅ **Clear Function** - Reset all fields with one click  
✅ **Keyboard Support** - Press Enter to calculate  
✅ **Modern UI** - Improved design and user experience  
✅ **Info Panel** - Built-in BMI reference guide  

### Premium Features (v3 - CustomTkinter)
✅ **Dark Mode** - Eye-friendly dark theme  
✅ **Modern Components** - Sleek, contemporary interface  
✅ **Smooth Animations** - Enhanced visual effects  
✅ **Placeholder Text** - Better input guidance  

## 📦 Available Versions

### Version 1 - Basic (Original)
The original simple implementation with basic functionality.

**Features:**
- Basic BMI calculation
- Simple Tkinter interface
- Color-coded results (commented)
- Minimal error handling

**Status:** ⚠️ Contains bugs (fixed in v2)

**Bug Found:**
```python
# ❌ Critical Bug in calculate() function
height = float(weigh_ent.get())  # Wrong! Should be height_ent
```

---

### Version 2 - Enhanced (Recommended)
Improved version with bug fixes and enhanced features.

**File:** `new-code.py`

**What's New:**
- ✅ **Bug Fixed:** Height input now correctly reads from height_ent
- ✅ **Error Handling:** Try-catch blocks for invalid inputs
- ✅ **Input Validation:** Check for positive numbers and reasonable values
- ✅ **Clear Button:** Reset functionality
- ✅ **Better UI:** Improved layout and styling
- ✅ **Keyboard Support:** Enter key triggers calculation
- ✅ **Info Panel:** BMI category reference built-in
- ✅ **Color Coding:** Dynamic result colors based on BMI

**Dependencies:**
```bash
# Built-in libraries only (no installation needed)
tkinter (included with Python)
```

---

### Version 3 - Modern (CustomTkinter)
Premium version with modern dark-mode UI.

**File:** `custom-tkinter-GUI.py`

**What's New (vs v2):**
- 🎨 **Dark Mode:** Professional dark theme
- 🎯 **Modern Components:** CustomTkinter widgets
- ✨ **Smooth Animations:** Hover effects and transitions
- 📝 **Placeholder Text:** Input hints in entry fields
- 🎭 **Better Aesthetics:** Rounded corners, modern fonts
- 🌈 **Theme System:** Customizable color themes

**Dependencies:**
```bash
pip install customtkinter
```

---

## 🚀 Installation & Usage

### Prerequisites
- Python 3.8 or higher
- tkinter (usually comes with Python)

### Quick Start

#### For Version 2 (Standard - Recommended)
```bash
# 1. Clone or download the repository
git clone https://github.com/yourusername/bmi-calculator.git
cd bmi-calculator

# 2. Run directly (no installation needed)
python bmi_calculator_v2.py
```

#### For Version 3 (CustomTkinter - Modern UI)
```bash
# 1. Install CustomTkinter
pip install customtkinter

# 2. Run the application
custom-tkinter-GUI.py
```

## 📖 How to Use

1. **Enter Your Weight** - Input in kilograms (e.g., 70)
2. **Enter Your Height** - Input in meters (e.g., 1.75)
3. **Click Calculate** or press **Enter**
4. **View Results** - See your BMI, category, and health advice
5. **Click Clear** to reset and start over

### Example Inputs:
| Weight (kg) | Height (m) | BMI | Category |
|-------------|-----------|-----|----------|
| 70 | 1.75 | 22.9 | Normal ✅ |
| 55 | 1.65 | 20.2 | Normal ✅ |
| 85 | 1.70 | 29.4 | Overweight ⚠️ |
| 95 | 1.75 | 31.0 | Obese 🔴 |

## 🔄 Version Comparison

| Feature | Version 1 | Version 2 | Version 3 (CTK) |
|---------|-----------|-----------|-----------------|
| **BMI Calculation** | ✅ (Buggy) | ✅ Fixed | ✅ Fixed |
| **Error Handling** | ❌ Basic | ✅ Complete | ✅ Complete |
| **Input Validation** | ❌ | ✅ | ✅ |
| **Color Coding** | ⚠️ Commented | ✅ Working | ✅ Enhanced |
| **Clear Function** | ❌ | ✅ | ✅ |
| **Keyboard Support** | ❌ | ✅ | ✅ |
| **Modern UI** | ❌ | ⚠️ Improved | ✅ Professional |
| **Dark Mode** | ❌ | ❌ | ✅ |
| **Dependencies** | Built-in | Built-in | CustomTkinter |
| **Setup Difficulty** | Easy | Easy | Medium |
| **Recommended For** | Learning | Daily Use | Production |

## 🎯 Which Version Should You Choose?

### Choose **Version 2** if:
- ✅ You want a reliable, bug-free calculator
- ✅ You prefer standard Python (no extra installations)
- ✅ You need a clean, simple interface
- ✅ You're learning Python GUI development
- ✅ **Best for beginners and general use**

### Choose **Version 3** if:
- ✅ You want a modern, professional look
- ✅ You prefer dark mode interfaces
- ✅ You don't mind installing dependencies
- ✅ You're building a portfolio project
- ✅ **Best for impressive demos and presentations**

## 🏗️ Project Structure

```
BMI-calculator-GUI/
│
├── code.py          # Original version (with bug)
├── new-code.py          # Enhanced version (recommended)
├── custom-tkinter-GUI.py      # CustomTkinter version
├── README.md                      # This file
├── requirements.txt               # Python dependencies (for v3)
├── .gitignore                     # Git ignore file
```

## 🐛 Bug Fixes from v1 to v2

### Critical Bug Fix
**Problem in v1:**
```python
def calculate():
    weight = float(weigh_ent.get())
    height = float(weigh_ent.get())  # ❌ BUG: Reading weight twice!
    bmi = weight / (height ** 2)     # Wrong calculation
```

**Fixed in v2:**
```python
def calculate():
    weight = float(weigh_ent.get())
    height = float(height_ent.get())  # ✅ FIXED: Reading height correctly
    bmi = weight / (height ** 2)      # Correct calculation
```

### Additional Improvements in v2:
1. **Input Validation** - Checks for positive numbers
2. **Error Messages** - User-friendly popups instead of crashes
3. **Height Warning** - Alerts if height seems unrealistic (>3m)
4. **Code Optimization** - Changed multiple `if` statements to `if-elif`

## 📝 Code Examples

### Basic Usage (All Versions)
```python
# User inputs
Weight: 70 kg
Height: 1.75 m

# Calculation
BMI = 70 / (1.75)² = 22.86

# Result
Your BMI: 22.9
Category: Normal
You're doing great!
```

### Adding Custom Categories (Advanced)
```python
# In calculate() function, you can add custom ranges:
elif 20 <= bmi <= 22:
    category = "Optimal"
    advice = "Perfect weight for athletes!"
    color = "#00ff00"
```

## 🔮 Future Enhancements

### Planned Features
- [ ] **BMI History Tracking** - Save and view past calculations
- [ ] **Weight Goal Calculator** - Calculate target weight
- [ ] **Imperial Units** - Support for pounds and inches
- [ ] **BMI Chart Visualization** - Graphical representation
- [ ] **Multi-language Support** - Indonesian, English, etc.
- [ ] **Export Results** - Save as PDF or image
- [ ] **Age & Gender Factors** - More accurate health assessment
- [ ] **Mobile Version** - Android/iOS app

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. Create a **feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. Open a **Pull Request**

### Development Guidelines
- Follow PEP 8 style guide
- Add comments for complex logic
- Test thoroughly before submitting
- Update README if adding new features


### Test Cases
```python
# Test Case 1: Normal BMI
Input: weight=70, height=1.75
Expected: BMI=22.9, Category="Normal", Color=Green

# Test Case 2: Underweight
Input: weight=45, height=1.70
Expected: BMI=15.6, Category="UnderWeight", Color=Blue

# Test Case 3: Invalid Input
Input: weight="abc", height=1.75
Expected: Error message popup
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Your Name**
- GitHub: [@SendPain11](https://github.com/SendPain11)
- LinkedIn: [Sendy Prismana Nurferian](https://linkedin.com/in/sendy-prismana-nurferian)
- Email: semdyprisma02@gmail.com

## 🙏 Acknowledgments

- **Tkinter Documentation** - Python's standard GUI library
- **CustomTkinter** by Tom Schimansky - Modern UI framework
- **WHO Guidelines** - BMI classification standards
- **Python Community** - Inspiration and support

## 📧 Support

Having issues? Here's how to get help:

1. **Check the README** - Most questions are answered here
2. **Search existing issues** - Someone might have the same problem
3. **Open a new issue** - Describe your problem in detail
4. **Email support** - sendyprisma02@gmail.com


## 📚 Learn More

### Resources
- [BMI Information - WHO](https://www.who.int/news-room/fact-sheets/detail/obesity-and-overweight)
- [Tkinter Tutorial](https://docs.python.org/3/library/tkinter.html)
- [CustomTkinter Documentation](https://github.com/TomSchimansky/CustomTkinter)
- [Python GUI Programming](https://realpython.com/python-gui-tkinter/)

---

## ⭐ Star This Project!

If you found this BMI Calculator helpful, please give it a ⭐ on GitHub!

**Made with ❤️ using Python**

---

**Last Updated:** February 2026  
**Version:** 3.0  
**Status:** ✅ Active Development
