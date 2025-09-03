#!/usr/bin/env python3
import subprocess
import time

# ========== CONFIG ==========
CHECK_INTERVAL = 15   # seconds between checks
TAB_TIMEOUT = 300     # seconds before closing inactive tab
# ============================

inactive_tabs = {}  # store {url: last_seen_time}


def get_tabs():
    """Return list of (url, title) for all Brave tabs"""
    script = '''
    tell application "Brave Browser"
        set window_list to every window
        set tab_list to {}
        repeat with w in window_list
            repeat with t in every tab of w
                set end of tab_list to {URL of t, title of t}
            end repeat
        end repeat
        return tab_list
    end tell
    '''
    result = subprocess.run(
        ["osascript", "-e", script],
        capture_output=True,
        text=True
    )

    # Parse AppleScript output
    raw = result.stdout.strip()
    if not raw:
        return []
    parts = [x.strip() for x in raw.split(", ")]
    # Pairs of (url, title)
    return list(zip(parts[0::2], parts[1::2]))


def close_tab(url):
    """Close a Brave tab by URL"""
    script = f'''
    tell application "Brave Browser"
        repeat with w in every window
            repeat with t in every tab of w
                if URL of t is "{url}" then
                    close t
                    return
                end if
            end repeat
        end repeat
    end tell
    '''
    subprocess.run(["osascript", "-e", script])


def main():
    print(f"🔍 Brave Tab Cleaner started (timeout={TAB_TIMEOUT}s)...")
    global inactive_tabs
    while True:
        now = time.time()
        tabs = get_tabs()

        current_urls = [url for url, _ in tabs]

        for url in current_urls:
            if url not in inactive_tabs:
                inactive_tabs[url] = now  # first seen
            else:
                # already seen, check inactivity
                if now - inactive_tabs[url] > TAB_TIMEOUT:
                    print(f"🗑️ Closing inactive tab: {url}")
                    close_tab(url)
                    del inactive_tabs[url]

        # Remove tabs that are no longer open
        inactive_tabs = {u: t for u, t in inactive_tabs.items() if u in current_urls}

        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()

