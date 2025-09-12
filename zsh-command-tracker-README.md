# Zsh Command Tracker

A powerful zsh configuration that automatically logs all terminal commands and provides safety warnings for potentially dangerous operations.

## 🚀 Features

### 📝 Command Logging
- **Automatic Logging**: Every command you run is automatically logged to a CSV file
- **Detailed Information**: Captures command, timestamp, working directory, and user
- **Alias Expansion**: Automatically expands aliases to show the actual command being executed
- **CSV Format**: Easy to import into spreadsheets or analyze with other tools

### ⚠️ Safety Warnings
- **Sensitive Command Detection**: Warns before executing potentially dangerous commands
- **Interactive Confirmation**: Asks for confirmation before proceeding with risky operations
- **Command Cancellation**: Allows you to cancel commands if you change your mind
- **Customizable List**: Easy to add or remove commands from the sensitive list

## 📋 Logged Information

Each command is logged with the following details:
- **Command**: The actual command executed (with aliases expanded)
- **Timestamp**: When the command was run (YYYY-MM-DD HH:MM:SS format)
- **Working Directory**: The directory where the command was executed
- **User**: The username who executed the command

## 🛡️ Protected Commands

The following commands trigger safety warnings by default:
- `rm` - File deletion commands
- `git push` - Pushing to remote repositories
- `git pull` - Pulling from remote repositories
- `docker system prune` - Docker cleanup commands
- `shutdown` - System shutdown
- `reboot` - System reboot

## 📁 Installation

1. **Add to your `.zshrc`**:
   ```bash
   # Copy the configuration to your .zshrc file
   cat zsh-command-tracker-README.md >> ~/.zshrc
   ```

2. **Reload your shell**:
   ```bash
   source ~/.zshrc
   ```

3. **Verify installation**:
   ```bash
   echo "Test command"  # This should be logged
   ```

## 📊 Log File Location

Commands are logged to: `~/.terminal_command_log.csv`

### CSV Format
```csv
"command","timestamp","working_directory","user"
"ls -la","2024-01-15 14:30:25","/Users/username/Documents","username"
"cd /tmp","2024-01-15 14:30:28","/Users/username/Documents","username"
```

## ⚙️ Configuration

### Customizing Sensitive Commands

Edit the `SENSITIVE_CMDS` array to add or remove commands:

```bash
export SENSITIVE_CMDS=("rm" "git push" "git pull" "docker system prune" "shutdown" "reboot" "your_custom_command")
```

### Changing Log File Location

Modify the `CMD_LOG` variable:

```bash
export CMD_LOG="/path/to/your/custom/log.csv"
```

## 🔍 Usage Examples

### Normal Command Execution
```bash
$ ls -la
# Command is logged automatically, no warning
```

### Sensitive Command Execution
```bash
$ rm -rf important_folder
⚠️  WARNING: You are about to run: rm -rf important_folder
❓ Are you sure? (y/n): n
❌ Command canceled.
```

### Alias Expansion
```bash
$ alias ll="ls -la"
$ ll
# Logs: "ls -la" (the expanded command, not "ll")
```

## 📈 Data Analysis

### View Recent Commands
```bash
tail -20 ~/.terminal_command_log.csv
```

### Search for Specific Commands
```bash
grep "git" ~/.terminal_command_log.csv
```

### Count Commands by Type
```bash
cut -d',' -f1 ~/.terminal_command_log.csv | sort | uniq -c | sort -nr
```

### Import into Python for Analysis
```python
import pandas as pd

# Load the command log
df = pd.read_csv('~/.terminal_command_log.csv')

# View recent commands
print(df.tail(10))

# Most used commands
print(df['command'].value_counts().head(10))

# Commands by hour
df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
print(df['hour'].value_counts().sort_index())
```

## 🛠️ Troubleshooting

### Commands Not Being Logged
1. Ensure the configuration is in your `.zshrc` file
2. Reload your shell: `source ~/.zshrc`
3. Check if the log file is writable: `ls -la ~/.terminal_command_log.csv`

### Warnings Not Appearing
1. Verify the command starts with one of the sensitive commands
2. Check the `SENSITIVE_CMDS` array configuration
3. Ensure the command matching logic is working correctly

### Log File Issues
1. Check file permissions: `chmod 644 ~/.terminal_command_log.csv`
2. Verify directory exists: `mkdir -p $(dirname ~/.terminal_command_log.csv)`
3. Check disk space: `df -h`

## 🔒 Privacy & Security

- **Local Storage**: All logs are stored locally on your machine
- **No Network Transmission**: Commands are never sent over the network
- **User Control**: You can delete or modify the log file at any time
- **Sensitive Data**: Be cautious with commands containing passwords or sensitive information

## 🎯 Use Cases

- **Productivity Tracking**: Monitor your terminal usage patterns
- **Command History**: Keep a detailed log of all executed commands
- **Learning Tool**: Review commands you've used to improve your terminal skills
- **Debugging**: Track down when and where specific commands were run
- **Audit Trail**: Maintain a record of system changes and operations
- **Safety Net**: Prevent accidental execution of dangerous commands

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📄 License

This configuration is provided as-is for personal and educational use.

## ⚠️ Disclaimer

This tool logs all terminal commands. Be mindful of sensitive information in your commands and consider the privacy implications of command logging in your environment.
