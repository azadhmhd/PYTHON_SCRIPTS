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

### Clipboard Manager (`clipboard_manager.py`)

A macOS menu bar application that provides clipboard history management and text shortcuts for improved productivity.

**Features:**
- Runs as a menu bar app with a clipboard icon (📋)
- Automatically monitors clipboard changes in the background
- Maintains a history of the last 20 clipboard items
- Text shortcuts for common phrases (e.g., `:sig` for signature)
- Quick access to clipboard history through menu
- Auto-paste functionality for selected history items

**Usage:**
```bash
python3 clipboard_manager.py
```

**Text Shortcuts:**
- `:sig` → "Best regards,\nAzad Mohamed\nDubai, UAE"
- `:mail` → "your.email@example.com"
- `:phone` → "+971-50-123-4567"

**Features:**
- Click "Show History" to view and select from clipboard history
- Selected items are automatically copied and pasted
- Configurable history size and check intervals
- Clean, minimal interface

**Requirements:**
- macOS (uses rumps for menu bar integration)
- Python 3.6+
- Dependencies: `rumps`, `pyperclip`

### Activity Tracker (`tracker.py`)

A comprehensive productivity tracking system that monitors your computer usage and provides detailed analytics through a web dashboard.

**Features:**
- **Real-time Activity Monitoring**: Tracks active applications and window titles
- **Smart Browser Detection**: Special handling for Brave Browser, Chrome, and Slack tabs
- **Idle Detection**: Automatically detects when you're away from the computer
- **JSON Logging**: Stores detailed activity logs with timestamps and durations
- **Background Monitoring**: Runs continuously with minimal system impact
- **Keyboard/Mouse Input Tracking**: Uses Quartz framework for accurate activity detection

**Usage:**
```bash
python3 tracker.py
```

**Configuration:**
Edit the config section at the top of the script:
- `LOG_FILE`: Output file for activity logs (default: "activity_log.json")
- `CHECK_INTERVAL`: Seconds between activity checks (default: 2)
- `IDLE_THRESHOLD`: Seconds of inactivity before marking as idle (default: 60)

**Supported Applications:**
- **Browsers**: Brave Browser, Chrome (with tab titles)
- **Communication**: Slack (with window titles)
- **Development**: VS Code, PyCharm, Terminal, Cursor
- **General**: All other macOS applications

### Activity Dashboard (`tracker_dashboard.py`)

A Streamlit web application that provides comprehensive analytics and visualization of your tracked activity data.

**Features:**
- **Interactive Dashboard**: Clean, modern web interface
- **Activity Categorization**: Automatically categorizes apps into Work, Entertainment, Social, Idle, and Other
- **Time Analytics**: 
  - Time spent per application
  - Time spent by category
  - Daily breakdown charts
- **Data Export**: Export data to CSV or PDF formats
- **Real-time Updates**: Refresh to see latest activity data

**Usage:**
```bash
streamlit run tracker_dashboard.py
```

**Categories:**
- **Work**: VS Code, PyCharm, Terminal, Notion, Slack, JIRA, Cursor
- **Entertainment**: YouTube, Spotify, Netflix
- **Social**: Twitter, Discord, Telegram, WhatsApp
- **Idle**: System idle time
- **Other**: Unclassified applications

**Dashboard Sections:**
1. **Activity Log**: Last 20 entries with detailed timestamps
2. **Time per App**: Bar chart showing total time spent in each application
3. **Time by Category**: Bar chart showing time distribution across categories
4. **Daily Breakdown**: Line chart showing daily activity patterns
5. **Export Options**: Download data as CSV or PDF reports

**Requirements:**
- Python 3.6+
- Dependencies: `streamlit`, `pandas`, `matplotlib`, `reportlab`
- Activity data from `tracker.py`

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
