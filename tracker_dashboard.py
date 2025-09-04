import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from reportlab.pdfgen import canvas

log_file = "activity_log.csv"

# Categorization rules
CATEGORIES = {
    "Work": ["VS Code", "PyCharm", "Terminal", "Notion", "Slack", "JIRA", "Cursor"],
    "Entertainment": ["YouTube", "Spotify", "Netflix"],
    "Social": ["Twitter", "Discord", "Telegram", "WhatsApp"],
    "Idle": ["Idle"]
}

def categorize(app):
    for category, keywords in CATEGORIES.items():
        for keyword in keywords:
            if keyword.lower() in app.lower():
                return category
    return "Other"

st.set_page_config(page_title="Developer Productivity Tracker", layout="wide")
st.title("🖥️ Developer Productivity Tracker")

try:
    df = pd.read_csv(log_file)
except (FileNotFoundError, pd.errors.EmptyDataError):
    df = pd.DataFrame()

if not df.empty:
    df['start'] = pd.to_datetime(df['start'])
    df['end'] = pd.to_datetime(df['end'])
    df['duration_min'] = df['duration_sec'] / 60
    df['date'] = df['start'].dt.date
    df['category'] = df['app'].apply(categorize)

    st.subheader("📊 Activity Log (Last 20 Entries)")
    st.dataframe(df.tail(20))

    st.subheader("⏳ Time Spent per App")
    time_per_app = df.groupby("app")["duration_min"].sum().sort_values(ascending=False)
    st.bar_chart(time_per_app)

    st.subheader("📂 Time Spent by Category")
    time_per_cat = df.groupby("category")["duration_min"].sum()
    st.bar_chart(time_per_cat)

    st.subheader("📅 Daily Breakdown")
    daily_summary = df.groupby(["date", "category"])["duration_min"].sum().unstack().fillna(0)
    st.line_chart(daily_summary)

    # Export to CSV
    if st.button("📥 Export CSV"):
        export_file = "activity_report.csv"
        df.to_csv(export_file, index=False)
        st.success(f"Exported to {export_file}")

    # Export to PDF
    if st.button("📄 Export PDF"):
        pdf_file = "activity_report.pdf"
        c = canvas.Canvas(pdf_file)
        c.setFont("Helvetica", 12)
        c.drawString(100, 800, "Developer Productivity Report")
        y = 760
        for app, duration in time_per_app.items():
            c.drawString(100, y, f"{app}: {duration:.2f} mins")
            y -= 20
            if y < 50:  # start new page if needed
                c.showPage()
                c.setFont("Helvetica", 12)
                y = 760
        c.save()
        st.success(f"Exported to {pdf_file}")

else:
    st.warning("No activity data found. Run tracker.py first.")
