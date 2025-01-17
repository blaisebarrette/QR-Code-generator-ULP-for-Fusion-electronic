# Version History

## Version 1.1.2 (January 17 2025)
### New Feature
- Added unit selection in the dialog box
    - Inches
    - Mils
    - mm

### Improvements
- Fixed QR code size accuracy issue when grid unit is set to mm

## Version 1.1.1 (January 1 2025)
### New Features
- New language support
    - Turkish
    - Polish
    - Portuguese
    - Chinese (Simplified)
- #usage updated to support all languages
- Added help dialog

## Version 1.1.0 (December 31 2024)
### New Features
- There is now only one version of ULP for both Windows and MacOS

### Improvements
- Less System calls
- Use native ULP language for most file operations
- Improved Windows compatibility using VBScript for network operations
- Better UTF-8 handling for localization files
- Eliminated command window flashing on Windows
- More reliable network operations across both platforms

## Version 1.0.4 (December 29 2024)
### New Features
- Added support for Symbol and footprint in Electronics Library

### Improvements
- Enhanced compatibility with Fusion Electronics Library Symbol and Footprint editor
- Improved user interface for Symbol and Footprint QR code generation
- Modified layer naming to be more consistent with Fusion Electronics interface

## Version 1.0.3 (December 23 2024)
### New Features
- Added support for Schematic environment

### Improvements
- Enhanced compatibility with Fusion Electronics Schematic editor
- Improved user interface for Schematic QR code generation

### Bug Fixes
- Fixed version checking

### Technical Details
- Updated ULP to detect and operate within the Schematic environment
- Ensured QR code generation works seamlessly on Schematic sheets
- Maintained all previous functionalities for PCB layers

## Version 1.0.2 (December 22 2024)
### Improvements
- Fixed QR code size accuracy issue
- Removed QR code border for precise sizing
- QR codes now match exactly the requested dimensions
- Improved size consistency across all QR versions

### Technical Details
- Modified server to generate borderless QR codes
- Maintained exact sizing for both short and long URLs
- Consistent results for all requested sizes (250-5000 mils)

### Bug Fixes
- Fixed version checking

## Version 1.0.1 (December 20 2024)
### New Features
- Added multi-language support (8 languages)
- Automatic language detection based on system settings
- Improved error handling and user feedback

### Improvements
- Simplified user interface
- Automatic QR code placement
- Removed manual position controls
- Better file handling with unique temporary files
- Updated documentation and README

### Bug Fixes
- Fixed layer mirroring for bottom layers
- Fixed file cleanup issues
- Improved network error handling

## Version 1.0.0 (December 19 2024)
### Features
- Cloud-based QR code generation
- Support for multiple PCB layers
- Automatic version checking
- Customizable QR code size
- Manual position controls
- Windows and MacOS support

### Technical
- Integration with PythonAnywhere service
- Version control through versions.csv
- Comprehensive error handling
- Support for Eagle/Fusion360 Electronics

## Version 0.2 (December 18 2024)
### Features
- Initial public release
- Basic QR code generation

### Known Limitations
- No version checking
- Basic error handling
- Local file operations only 