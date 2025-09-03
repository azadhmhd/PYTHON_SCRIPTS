# Python Scripts Collection

A collection of helpful Python scripts for various use cases and automation tasks.

## 📁 Scripts

### Brave Tab Cleaner (`brave_tab_cleaner.py`)

An automated tool that monitors and closes inactive tabs in Brave Browser to help manage memory usage and keep your browser clean.

**Features:**
- Monitors all Brave Browser tabs continuously
- Automatically closes tabs that have been inactive for a specified duration
- Configurable timeout and check intervals
- Uses AppleScript for macOS integration

**Usage:**
```bash
python3 brave_tab_cleaner.py
```

**Configuration:**
Edit the config section at the top of the script:
- `CHECK_INTERVAL`: Seconds between tab checks (default: 15)
- `TAB_TIMEOUT`: Seconds before closing inactive tabs (default: 10)

**Requirements:**
- macOS (uses AppleScript)
- Brave Browser installed
- Python 3.6+

## 🚀 Getting Started

1. Clone this repository:
```bash
git clone https://github.com/yourusername/python_scripts.git
cd python_scripts
```

2. Install dependencies (if any):
```bash
pip install -r requirements.txt
```

3. Run any script:
```bash
python3 script_name.py
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

These scripts are provided as-is for educational and personal use. Please review and test scripts before using them in production environments.
