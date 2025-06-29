import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

import matplotlib
matplotlib.rcParams['font.family'] = 'MS Gothic'  # 'Meiryo' や 'Yu Gothic' も可

st.set_page_config(page_title="資産運用シミュレーター", layout="centered")
st.title("📊 年利の違いでここまで差が出る！資産運用シミュレーター")

monthly = st.slider("💰 毎月の積立額（円）", 1000, 100000, 10000, step=1000)
years = st.slider("🕒 積立年数", 1, 40, 20)

rates = [0.001, 0.02, 0.05, 0.07]
labels = ["銀行預金（0.001%）", "債券型（2%）", "株式型（5%）", "高成長型（7%）"]

x = np.arange(1, years + 1)
results = []
for r in rates:
    if r > 0:
        # 1万円単位に変換（値を10000で割る）
        values = [monthly * 12 * ((1 + r) ** y - 1) / r / 10000 for y in x]
    else:
        values = [monthly * 12 * y / 10000 for y in x]
    results.append(values)

fig, ax = plt.subplots()
for i, yvals in enumerate(results):
    ax.plot(x, yvals, label=labels[i], linewidth=2)
ax.set_title("年利の違いによる将来資産の比較")
ax.set_xlabel("運用年数")
ax.set_ylabel("資産総額（万円）")
ax.legend()
ax.grid(True)
st.pyplot(fig)
