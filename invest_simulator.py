import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import os

# フォント設定：Streamlit Cloudでも文字化けしないようにフォントを明示指定
font_path = os.path.join("fonts", "ipaexg.ttf")  # ← フォントファイルを fonts フォルダに入れておく
if os.path.exists(font_path):
    font_prop = fm.FontProperties(fname=font_path)
    plt.rcParams["font.family"] = font_prop.get_name()
else:
    st.warning("⚠ フォントファイルが見つかりません。日本語が文字化けする可能性があります。")

# Streamlit UI
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
        values = [monthly * 12 * ((1 + r) ** y - 1) / r for y in x]
    else:
        values = [monthly * 12 * y for y in x]
    # 万円単位で表示する
    results.append([v / 10000 for v in values])

fig, ax = plt.subplots()
for i, yvals in enumerate(results):
    ax.plot(x, yvals, label=labels[i], linewidth=2)
ax.set_title("年利の違いによる将来資産の比較（万円）")
ax.set_xlabel("運用年数")
ax.set_ylabel("資産総額（万円）")
ax.legend()
ax.grid(True)
st.pyplot(fig)
