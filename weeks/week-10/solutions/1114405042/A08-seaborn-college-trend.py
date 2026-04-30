# A08. 使用 seaborn 繪製 109~114 學年各學院生源分析圖
# Bloom：Apply — 把 A07 的統計成果接到視覺化流程中，完成資料呈現
#
# 執行前需要安裝：pip install seaborn matplotlib pandas
#
# 這支範例延續 A07 的 I/O 技巧，重點如下：
#   5.7  zipfile：直接從壓縮檔讀 CSV，不必先解壓到資料夾
#   5.1  utf-8-sig：正確處理 BOM，避免第一個欄名出現怪字元
#   5.6  io.StringIO + csv：把字串包成檔案樣式，讓 csv 模組能直接解析
#   5.11 pathlib：用 Path 管理檔案與輸出路徑，讓程式更容易維護
#   5.5  open('x')：用「只允許新建」的方式輸出圖片，避免覆蓋原檔

import csv
import io
import platform
import zipfile
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# ── 中文字型設定：依作業系統挑選較可能存在的字型 ───────────
# matplotlib 在不同平台預設可用字型不同；若沒有設定中文字型，圖表標題與標籤
# 很可能會出現方塊或亂碼。這裡先依平台建立候選清單，再交給 matplotlib 嘗試。
_CJK_FONTS = {
    "Darwin":  ["Heiti TC", "Arial Unicode MS", "PingFang TC"],
    "Windows": ["Microsoft JhengHei", "Microsoft YaHei"],
    "Linux":   ["Noto Sans CJK TC", "WenQuanYi Zen Hei"],
}.get(platform.system(), ["sans-serif"])


def _apply_cjk_font():
    """將中文字型與顯示設定套回 matplotlib。

    seaborn 的 set_theme 會重設部分 matplotlib rcParams，因此如果先設定字型，
    後面再呼叫 seaborn 時設定可能會被蓋掉。這個小函式的用途，就是在需要時
    把中文字型、負號顯示等設定重新補回去，確保圖上的中文可以正常顯示。
    """
    plt.rcParams["font.sans-serif"] = _CJK_FONTS + plt.rcParams["font.sans-serif"]
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["axes.unicode_minus"] = False


_apply_cjk_font()

# ── 系所 → 學院 對照表：把每個系所歸類到對應學院 ─────────────
# 這份映射表是後續統計的核心之一。原始資料通常只提供系所名稱，
# 但視覺化時我們更想看「學院」層級的趨勢，因此先將系所對應到學院。
DEPT_TO_COLLEGE = {
    # 人文暨管理學院
    "應用外語系":       "人文暨管理學院",
    "航運管理系":       "人文暨管理學院",
    "行銷與物流管理系": "人文暨管理學院",
    "觀光休閒系":       "人文暨管理學院",
    "資訊管理系":       "人文暨管理學院",
    "餐旅管理系":       "人文暨管理學院",
    # 海洋資源暨工程學院
    "水產養殖系":       "海洋資源暨工程學院",
    "海洋遊憩系":       "海洋資源暨工程學院",
    "食品科學系":       "海洋資源暨工程學院",
    # 電資工程學院
    "資訊工程系":       "電資工程學院",
    "電信工程系":       "電資工程學院",
    "電機工程系":       "電資工程學院",
}

# ── 5.11：定位資料檔案 ───────────────────────────────
HERE = Path(__file__).resolve().parent
ZIP_PATH = HERE.parent.parent.parent / "assets" / "npu-stu-109-114-anon.zip"
assert ZIP_PATH.exists(), f"找不到：{ZIP_PATH}"


# ── 5.7 + 5.6 + 5.1：把 zip 裡所有 CSV 讀成長表格式資料 ───
def load_long_frame(zip_path: Path) -> pd.DataFrame:
    """將壓縮檔中的所有 CSV 讀入，並整理成適合繪圖的長表格式。

    回傳的 DataFrame 每一列代表一位學生的「學年、學院、系所」三個欄位，
    這樣後續就能直接交給 pandas 分組統計，再讓 seaborn 畫趨勢圖。
    """
    records = []
    with zipfile.ZipFile(zip_path) as z:
        for info in z.infolist():
            if not info.filename.endswith(".csv"):
                continue
            year = info.filename[:3]                     # 檔名前三碼即學年，例如 109、110
            text = z.read(info).decode("utf-8-sig")      # 用 utf-8-sig 去除 BOM，避免欄位名稱異常
            reader = csv.DictReader(io.StringIO(text))    # 讓 csv.DictReader 把文字內容當成檔案讀取
            for row in reader:
                # 系所名稱是這份視覺化的分類基礎；若該列沒有系所名稱，就直接略過。
                dept = row.get("系所名稱", "").strip()
                if not dept:
                    continue
                records.append({
                    "學年": int(year),
                    "學院": DEPT_TO_COLLEGE.get(dept, "其他"),
                    "系所": dept,
                })
    return pd.DataFrame.from_records(records)


df = load_long_frame(ZIP_PATH)
print("總筆數:", len(df))
print(df.head())

# 先做一個學年 × 學院 的彙總表，後面兩張圖都會用到這份統計結果。
pivot = (df.groupby(["學年", "學院"])
           .size()
           .reset_index(name="人數"))
print("\n各學年各學院:")
print(pivot.pivot(index="學年", columns="學院", values="人數"))


# ── seaborn 繪圖：設定視覺風格並產生兩張子圖 ───────────────
sns.set_theme(style="whitegrid", context="talk", palette="Set2")
_apply_cjk_font()  # 蓋回中文字型

fig, axes = plt.subplots(1, 2, figsize=(15, 6),
                         gridspec_kw={"width_ratios": [1.3, 1]})

# 圖 A：折線加散點，呈現各學院在不同學年的新生人數走勢
# 這張圖適合看趨勢與轉折點：哪個學院成長、哪個學院下滑，一眼就能看出來。
sns.lineplot(data=pivot, x="學年", y="人數", hue="學院",
             marker="o", markersize=10, linewidth=2.5, ax=axes[0])
axes[0].set_title("109–114 各學院新生人數趨勢", fontsize=16, pad=12)
axes[0].set_xticks(sorted(pivot["學年"].unique()))
axes[0].legend(title="學院", loc="upper right", frameon=True)

# 在每個資料點上直接標示人數，方便讀者不用反覆對照座標軸
for _, r in pivot.iterrows():
    axes[0].annotate(int(r["人數"]),
                     (r["學年"], r["人數"]),
                     textcoords="offset points", xytext=(0, 8),
                     ha="center", fontsize=9, alpha=0.8)

# 圖 B：堆疊長條圖，呈現每一學年內各學院的結構比例
# 這張圖適合觀察「組成」而不是單純總量，也就是每年各學院在總新生中所占的份額。
pivot_wide = pivot.pivot(index="學年", columns="學院", values="人數").fillna(0)
pivot_wide.plot(kind="bar", stacked=True,
                ax=axes[1], colormap="Set2", width=0.75, edgecolor="white")
axes[1].set_title("各學年學院結構（堆疊）", fontsize=16, pad=12)
axes[1].set_ylabel("人數")
axes[1].tick_params(axis="x", rotation=0)
axes[1].legend(title="學院", loc="upper right", fontsize=9)

# 整體標題用來交代分析主題與時間範圍，讓兩張子圖合起來有一致脈絡。
fig.suptitle("國立澎湖科技大學  109–114 學年新生生源分析",
             fontsize=18, fontweight="bold", y=1.02)
fig.tight_layout()

# ── 5.5：用 'x' 模式輸出圖片，避免不小心覆蓋既有成果 ───────
OUT = HERE / "A08-college-trend.png"
try:
    with open(OUT, "xb") as f:
        fig.savefig(f, dpi=150, bbox_inches="tight")
    print(f"\n圖檔已寫入：{OUT.name}")
except FileExistsError:
    print(f"\n{OUT.name} 已存在，保留舊檔（要重畫請先刪除）")

plt.show()

# ── 延伸挑戰：如果要再往下做，可以試試這幾個方向 ─────────
# 1) 改畫「各系所」熱力圖：例如用 sns.heatmap(pivot_by_dept, annot=True, fmt='d') 直接看系所分布。
# 2) 再加一張圓餅圖：專門呈現 114 學年各學院的占比結構。
# 3) 把年度 x 軸改成 '109學年' ~ '114學年' 的字串標籤：需要先轉型，再用 set_xticklabels 調整顯示。
