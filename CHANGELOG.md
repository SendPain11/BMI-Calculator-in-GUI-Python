# Changelog - BMI Calculator

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [3.0.0] - 2026-02-01 - CustomTkinter Version

### Added
- 🎨 **Dark Mode Interface** - Professional dark theme using CustomTkinter
- ✨ **Modern Components** - Sleek buttons, entries, and frames
- 🌈 **Theme System** - Customizable color themes
- 📝 **Placeholder Text** - Input hints in entry fields
- 🎭 **Hover Effects** - Smooth transitions on button hover
- 🎯 **Better Layout** - Improved spacing and visual hierarchy

### Changed
- Migrated from standard Tkinter to CustomTkinter
- Enhanced visual design with modern aesthetics
- Improved color scheme for dark mode
- Updated button styling with rounded corners

### Dependencies
- Added: `customtkinter==5.2.1`

### Notes
- Requires installation: `pip install customtkinter`
- All features from v2.0 are preserved
- Best for production-ready applications

---

## [2.0.0] - 2026-02-01 - Enhanced Version

### 🐛 Fixed
- **CRITICAL BUG:** Fixed height input reading from wrong entry field
  ```python
  # Before (v1): height = float(weigh_ent.get())  ❌
  # After (v2):  height = float(height_ent.get())  ✅
  ```
- Fixed incorrect BMI calculations caused by the above bug
- Fixed potential crashes from invalid inputs

### Added
- ✅ **Error Handling** - Try-catch blocks for all user inputs
- ✅ **Input Validation** - Checks for positive numbers and realistic values
- ✅ **Clear Button** - Reset all fields with one click
- ✅ **Keyboard Support** - Press Enter key to calculate
- ✅ **Height Warning** - Alert when height > 3 meters
- ✅ **Info Panel** - Built-in BMI category reference guide
- ✅ **Focus Management** - Auto-focus on weight input on start
- ✅ **Error Popups** - User-friendly error messages with messagebox

### Changed
- Improved UI layout with better spacing
- Added background colors for better visual appeal
- Enhanced button styling with raised relief
- Optimized if-else logic (changed to if-elif for efficiency)
- Improved result display with better formatting
- Added window size restrictions (non-resizable)
- Better font choices and sizes

### Improved
- Code organization with better comments
- Function documentation with docstrings
- Variable naming for clarity
- Color-coded results now actually work (were commented in v1)

### Technical
- Added `on_enter()` function for keyboard handling
- Added `clear_fields()` function for reset functionality
- Improved `calculate()` with comprehensive error handling
- Better exception handling (ValueError, ZeroDivisionError)

---

## [1.0.0] - 2026-01-XX - Initial Release

### Features
- Basic BMI calculation
- Simple Tkinter GUI interface
- 5 BMI categories (Underweight to Extremely Obese)
- Category-based health advice
- Color-coded results (commented out)

### Known Issues
- ❌ **Critical Bug:** Height reads from weight entry field
- ❌ No error handling for invalid inputs
- ❌ No input validation
- ❌ Color coding not implemented (only commented)
- ❌ No clear/reset functionality
- ❌ Limited user feedback
- ❌ Can crash with non-numeric input

### Code Stats
- Lines of Code: ~80
- Functions: 1 (calculate)
- Error Handling: None
- Input Validation: None

---

## Version Comparison Summary

| Feature | v1.0 | v2.0 | v3.0 |
|---------|------|------|------|
| **Bug Status** | 🔴 Broken | 🟢 Fixed | 🟢 Fixed |
| **Error Handling** | ❌ | ✅ | ✅ |
| **Input Validation** | ❌ | ✅ | ✅ |
| **Clear Function** | ❌ | ✅ | ✅ |
| **Keyboard Support** | ❌ | ✅ | ✅ |
| **Color Coding** | ⚠️ | ✅ | ✅ Enhanced |
| **UI Quality** | Basic | Good | Excellent |
| **Dark Mode** | ❌ | ❌ | ✅ |
| **Dependencies** | None | None | CustomTkinter |
| **Lines of Code** | ~80 | ~170 | ~180 |
| **Recommended** | ❌ | ✅ | ✅ Premium |

---

## Migration Guide

### From v1.0 to v2.0

**Breaking Changes:** None (fully backward compatible in terms of functionality)

**What You Need to Do:**
1. Replace v1 file with v2 file
2. No code changes needed
3. Enjoy bug-free calculations!

**Benefits:**
- Immediate bug fix
- Better user experience
- No additional dependencies

### From v2.0 to v3.0

**Breaking Changes:** Requires CustomTkinter installation

**What You Need to Do:**
1. Install CustomTkinter: `pip install customtkinter`
2. Replace v2 file with v3 file
3. Run and enjoy modern UI!

**Benefits:**
- Professional dark mode interface
- Modern, sleek design
- Better visual appeal
- Same functionality, better looks

### From v1.0 to v3.0 (Direct)

**What You Need to Do:**
1. Install CustomTkinter: `pip install customtkinter`
2. Replace v1 file with v3 file
3. Get bug fixes + modern UI in one upgrade!

**Benefits:**
- All bug fixes from v2
- All visual improvements from v3
- Best overall experience

---

## Detailed Bug Analysis

### The Critical Height Input Bug (v1.0)

**Location:** Line 5-6 in `calculate()` function

**Original Code (v1.0):**
```python
def calculate():
    weight = float(weigh_ent.get())
    height = float(weigh_ent.get())  # ❌ BUG HERE!
    bmi = weight / (height ** 2)
```

**Problem:**
- Both `weight` and `height` variables read from `weigh_ent`
- This is a classic copy-paste error
- `height_ent` is never used for input

**Impact:**
```python
# Example with bug:
User Input: weight=70kg, height=1.75m
Actual Calculation: bmi = 70 / (70²) = 0.014
Expected: bmi = 70 / (1.75²) = 22.86

# Result: Completely wrong BMI!
```

**Fixed Code (v2.0+):**
```python
def calculate():
    weight = float(weigh_ent.get())
    height = float(height_ent.get())  # ✅ FIXED!
    bmi = weight / (height ** 2)
```

**How It Was Missed:**
- No syntax error (valid Python code)
- No runtime error (both are Entry widgets)
- Only produces wrong results
- Needs manual testing to discover

---

## Upgrade Recommendations

### For Beginners
- ✅ **Start with v2.0** - Bug-free, no extra installations
- 📚 Learn standard Tkinter first
- 🎓 Understand the bug and its fix

### For Intermediate Users
- ✅ **Use v2.0 for learning** - Clean, well-commented code
- 🚀 **Try v3.0 for projects** - Impressive portfolio piece
- 🎨 Experiment with CustomTkinter features

### For Production
- ✅ **Deploy v3.0** - Professional appearance
- 💼 Best for client-facing applications
- 🌟 Impressive demo material

---

## Future Roadmap

### Version 4.0 (Planned)
- [ ] BMI history tracking with database
- [ ] Weight goal calculator
- [ ] Progress charts and graphs
- [ ] Export results to PDF
- [ ] Multi-language support (ID/EN)

### Version 5.0 (Concept)
- [ ] Web version (Flask/Django)
- [ ] Mobile app (Kivy/BeeWare)
- [ ] API integration
- [ ] Cloud sync

---

## Contributors

### Version 1.0
- Initial development by SEND

### Version 2.0
- Bug fixes and enhancements by [Your Name]
- Testing and validation by community

### Version 3.0
- CustomTkinter implementation by [Your Name]
- UI/UX improvements

---

## Support

For questions about specific versions:
- **v1.0 issues:** Check v2.0 (bug fixed)
- **v2.0 issues:** Open GitHub issue
- **v3.0 issues:** Check CustomTkinter docs

---

**Last Updated:** February 1, 2026
