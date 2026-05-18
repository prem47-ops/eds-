
# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import SpanSelector

# -----------------------------
# STEP 1: Create Sample Dataset
# -----------------------------
dates = pd.date_range(start='2024-01-01', periods=30, freq='D')
sales = np.random.randint(100, 500, size=30)

df = pd.DataFrame({
    'Date': dates,
    'Sales': sales
})

df.set_index('Date', inplace=True)

# -----------------------------
# GRAPH 1: SpanSelector (Interactive)
# -----------------------------
fig, ax = plt.subplots()
ax.plot(df.index, df['Sales'])
ax.set_title("Span Selector - Select Region of Sales Data")
ax.set_xlabel("Date")
ax.set_ylabel("Sales")

def onselect(xmin, xmax):
    print(f"Selected range: {xmin} to {xmax}")

span = SpanSelector(ax, onselect, 'horizontal', useblit=True,
                    props=dict(alpha=0.5))

plt.show()

# -----------------------------
# GRAPH 2: Broken Horizontal Bar Plot
# -----------------------------
fig, ax = plt.subplots()

# Example: machine working intervals (start, duration)
xranges = [(0, 5), (7, 3), (12, 6)]

ax.broken_barh(xranges, [(10, 5)])
ax.set_xlabel("Time")
ax.set_ylabel("Task")
ax.set_title("Broken Horizontal Bar Plot (Task Scheduling)")

plt.show()

# -----------------------------
# GRAPH 3: Watermarked Sales Chart
# -----------------------------
fig, ax = plt.subplots()
ax.plot(df.index, df['Sales'])

ax.set_title("Sales Trend with Watermark")
ax.set_xlabel("Date")
ax.set_ylabel("Sales")

# Add watermark text
plt.text(0.5, 0.5, 'CONFIDENTIAL',
         transform=ax.transAxes,
         fontsize=40,
         alpha=0.3,
         ha='center',
         va='center')

plt.show()

# -----------------------------
# GRAPH 4: Area Plot (Extra Advanced)
# -----------------------------
df['Sales'].plot.area()
plt.title("Area Plot of Sales")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.show()

# -----------------------------
# GRAPH 5: Rolling Mean (Trend Analysis)
# -----------------------------
rolling = df['Sales'].rolling(window=5).mean()

plt.plot(df.index, df['Sales'], label='Original')
plt.plot(df.index, rolling, label='Rolling Mean (5 days)')

plt.title("Sales with Rolling Mean")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.show()

print("\n===== ADVANCED VISUALIZATION COMPLETED =====")
