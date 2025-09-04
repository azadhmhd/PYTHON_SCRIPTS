#!/usr/bin/env python3
import rumps
import pyperclip
import time
import threading
from datetime import datetime
import subprocess

MAX_HISTORY = 20
CHECK_INTERVAL = 0.5

SHORTCUTS = {
    ":sig": "Best regards,\nAzad Mohamed\nDubai, UAE",
    ":mail": "your.email@example.com",
    ":phone": "+971-50-123-4567"
}

class ClipboardManager(rumps.App):
    def __init__(self):
        super(ClipboardManager, self).__init__("📋", quit_button=None)
        self.menu = ["Show History", None, "Quit"]
        self.history = []
        self.last_clip = ""

        # background thread for clipboard watching
        t = threading.Thread(target=self.watch_clipboard, daemon=True)
        t.start()

    def watch_clipboard(self):
        while True:
            text = pyperclip.paste()
            if text and text != self.last_clip:
                expanded = SHORTCUTS.get(text.strip(), text)

                if expanded != text:
                    pyperclip.copy(expanded)

                self.history.append({
                    "time": datetime.now().strftime("%H:%M:%S"),
                    "text": expanded
                })
                if len(self.history) > MAX_HISTORY:
                    self.history.pop(0)

                self.last_clip = expanded
            time.sleep(CHECK_INTERVAL)

    @rumps.clicked("Show History")
    def show_history(self, _):
        if not self.history:
            rumps.alert("Clipboard History is empty!")
            return

        items = [h["text"][:50].replace("\n", " ") for h in self.history[::-1]]
        choice = rumps.Window(
            message="Clipboard History",
            title="📋 Choose item",
            default_text="\n".join(f"{i+1}. {txt}" for i, txt in enumerate(items)),
            dimensions=(400, 200)
        ).run()

        if choice.clicked and choice.text.strip().isdigit():
            idx = int(choice.text.strip()) - 1
            if 0 <= idx < len(items):
                selected = self.history[::-1][idx]["text"]
                pyperclip.copy(selected)
                subprocess.run([
                    "osascript", "-e",
                    'tell application "System Events" to keystroke "v" using command down'
                ])

    @rumps.clicked("Quit")
    def quit_app(self, _):
        rumps.quit_application()


if __name__ == "__main__":
    ClipboardManager().run()
