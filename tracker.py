import time
import csv
from datetime import datetime
from Quartz import CGWindowListCopyWindowInfo, kCGWindowListOptionOnScreenOnly, kCGNullWindowID
from pynput import mouse, keyboard
import subprocess
import os

# ---------------- CONFIG ----------------
LOG_FILE = "activity_log.csv"
CHECK_INTERVAL = 2  # seconds
IDLE_THRESHOLD = 60  # seconds

last_input_time = datetime.now()

# ---------------- INPUT MONITOR ----------------
def on_input(event=None):
    global last_input_time
    last_input_time = datetime.now()

mouse.Listener(on_move=on_input, on_click=on_input).start()
keyboard.Listener(on_press=on_input).start()

# ---------------- ACTIVE WINDOW ----------------
def get_quartz_window():
    windows = CGWindowListCopyWindowInfo(kCGWindowListOptionOnScreenOnly, kCGNullWindowID)
    for w in windows:
        if w.get("kCGWindowLayer") == 0:
            title = w.get("kCGWindowName") or ""
            app = w.get("kCGWindowOwnerName") or "Unknown"
            return app, title.strip() if title.strip() else app
    return "Unknown", ""

def get_brave_tab():
    try:
        script = 'tell application "Brave Browser" to get title of active tab of front window'
        title = subprocess.check_output(["osascript", "-e", script]).decode().strip()
        return "Brave Browser", title if title else "Brave Browser"
    except:
        return "Brave Browser", ""

def get_chrome_tab():
    try:
        script = 'tell application "Google Chrome" to get title of active tab of front window'
        title = subprocess.check_output(["osascript", "-e", script]).decode().strip()
        return "Chrome", title if title else "Chrome"
    except:
        return "Chrome", ""

def get_slack_window():
    try:
        script = 'tell application "Slack" to get title of front window'
        title = subprocess.check_output(["osascript", "-e", script]).decode().strip()
        return "Slack", title if title else "Slack"
    except:
        return "Slack", ""

def get_active_app():
    app_name, window_title = get_quartz_window()
    if "Brave" in app_name:
        return get_brave_tab()
    elif "Chrome" in app_name:
        return get_chrome_tab()
    elif "Slack" in app_name:
        return get_slack_window()
    else:
        return app_name, window_title

# ---------------- CSV LOGGER ----------------
def append_csv(entry):
    file_exists = os.path.exists(LOG_FILE)
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["app", "title", "start", "end", "duration_sec"])
        writer.writerow([entry["app"], entry["title"], entry["start"], entry["end"], entry["duration_sec"]])

# ---------------- TRACKER ----------------
def log_activity():
    current_app, current_title = get_active_app()
    current_session = {
        "app": current_app,
        "title": current_title,
        "start": datetime.now(),
        "duration_sec": 0
    }

    print("Tracking started... (Ctrl+C to stop)")

    while True:
        try:
            idle_time = (datetime.now() - last_input_time).seconds
            if idle_time > IDLE_THRESHOLD:
                active_app, active_title = "Idle", ""
            else:
                active_app, active_title = get_active_app()

            now = datetime.now()

            if active_app == current_session["app"] and active_title == current_session["title"]:
                current_session["duration_sec"] += CHECK_INTERVAL
            else:
                # Save previous session
                entry = {
                    "app": current_session["app"],
                    "title": current_session["title"],
                    "start": current_session["start"].isoformat(),
                    "end": now.isoformat(),
                    "duration_sec": int(current_session["duration_sec"])
                }
                append_csv(entry)

                # Start new session
                current_session = {
                    "app": active_app,
                    "title": active_title,
                    "start": now,
                    "duration_sec": CHECK_INTERVAL
                }

            time.sleep(CHECK_INTERVAL)

        except KeyboardInterrupt:
            # Save last session on exit
            entry = {
                "app": current_session["app"],
                "title": current_session["title"],
                "start": current_session["start"].isoformat(),
                "end": datetime.now().isoformat(),
                "duration_sec": int(current_session["duration_sec"])
            }
            append_csv(entry)
            print("\nTracking stopped by user.")
            break

        except Exception as e:
            print("Error:", e)
            time.sleep(CHECK_INTERVAL)

# ---------------- MAIN ----------------
if __name__ == "__main__":
    log_activity()
