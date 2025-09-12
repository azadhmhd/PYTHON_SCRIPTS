# Tracks/logs every command you run in the terminal.
# For some sensitive commands (like rm -rf, git push origin main, docker prune), it should warn and ask for confirmation before executing.

# Path to command log
export CMD_LOG="$HOME/.terminal_command_log.csv"

# Sensitive commands
export SENSITIVE_CMDS=("rm" "git push" "git pull" "docker system prune" "shutdown" "reboot")

preexec() {
    local timestamp=$(date +"%Y-%m-%d %H:%M:%S")
    local user=$USER
    local cmd="$1"
    local cwd=$(pwd)

    # Expand alias if it exists
    local expanded_cmd=$(alias "$cmd" 2>/dev/null | sed -E "s/^$cmd='(.*)'/\1/")
    if [[ -n "$expanded_cmd" ]]; then
        cmd="$expanded_cmd"
    fi

    # Log to CSV
    echo "\"$cmd\",\"$timestamp\",\"$cwd\",\"$user\"" >> "$CMD_LOG"

    # Check sensitive list
    for scmd in "${SENSITIVE_CMDS[@]}"; do
        if [[ "$cmd" == "$scmd"* ]]; then
            echo "⚠️  WARNING: You are about to run: $cmd"
            read "answer?❓ Are you sure? (y/n): "
            if [[ ! "$answer" =~ ^[Yy]$ ]]; then
                echo "❌ Command canceled."
                kill -INT $$
            fi
        fi
    done
}
