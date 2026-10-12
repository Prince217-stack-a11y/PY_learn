# # -*- coding: utf-8 -*-
# """按“少量增加，每幅图回答一个问题”的建议生成 5 张 PNG 论文配图。
#
# 数据严格来自 k3/results/npz 下的最终空间-时间结果和附件1、附件2插值结果。
# """
# from __future__ import annotations
#
# from pathlib import Path
#
# import matplotlib
#
# matplotlib.use("Agg")
# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.patches import Circle, FancyArrowPatch
# from matplotlib.ticker import MaxNLocator
#
# ROOT = Path(r"E:\anaconda_download\2026_CUMCM_A_药材的烘干问题")
# NPZ = ROOT / "k3" / "results" / "npz"
# ATTACH = ROOT / "附件_赛题原始材料" / "附件"
# OUT = ROOT / "results" / "figures" / "配图建议_待确认"
# OUT.mkdir(parents=True, exist_ok=True)
#
# plt.rcParams.update({
#     "font.family": "sans-serif",
#     "font.sans-serif": ["SimHei", "Microsoft YaHei", "DejaVu Sans"],
#     "axes.unicode_minus": False,
#     "figure.facecolor": "white",
#     "axes.facecolor": "white",
#     "axes.labelsize": 11,
#     "axes.titlesize": 14,
#     "xtick.labelsize": 9.5,
#     "ytick.labelsize": 9.5,
#     "legend.fontsize": 9,
#     "axes.grid": True,
#     "grid.color": "#D9D9D9",
#     "grid.linestyle": "--",
#     "grid.linewidth": 0.6,
#     "grid.alpha": 0.65,
#     "axes.axisbelow": True,
#     "axes.linewidth": 0.9,
#     "savefig.dpi": 600,
#     "savefig.bbox": "tight",
#     "savefig.pad_inches": 0.08,
# })
#
# COLORS = {
#     "blue": "#3F6FB5",
#     "orange": "#E6863B",
#     "green": "#4C9A68",
#     "red": "#C44E52",
#     "purple": "#7B6BA8",
#     "cyan": "#4E9AB8",
#     "gray": "#666666",
#     "black": "#222222",
# }
# TIME_COLORS = [
#     "#4870B2",
#     "#A8C6E5",
#     "#77BFA3",
#     "#C7B85D",
#     "#E19049",
#     "#C16571",
#     "#8F6B9E",
# ]
#
#
# def style_axes(ax) -> None:
#     ax.spines["top"].set_visible(False)
#     ax.spines["right"].set_visible(False)
#     ax.tick_params(
#         direction="out",
#         colors="#444444",
#         width=0.8,
#         length=4,
#     )
#
#
# def save(fig, stem: str) -> None:
#     fig.savefig(
#         OUT / f"{stem}.png",
#         dpi=600,
#         bbox_inches="tight",
#         facecolor="white",
#     )
#     plt.close(fig)
#
#
# def interpolate_crossing(
#     time_s: np.ndarray,
#     values: np.ndarray,
#     threshold: float,
# ) -> float:
#     idx = np.flatnonzero(values < threshold)
#
#     if idx.size == 0:
#         return float("nan")
#
#     j = int(idx[0])
#
#     if j == 0:
#         return float(time_s[0])
#
#     return float(
#         time_s[j - 1]
#         + (threshold - values[j - 1])
#         * (time_s[j] - time_s[j - 1])
#         / (values[j] - values[j - 1])
#     )
#
#
# q1 = np.load(NPZ / "q1.npz")
# q2 = np.load(NPZ / "q2.npz")
# q3 = np.load(NPZ / "q3.npz")
# q4 = np.load(NPZ / "q4.npz")
#
#
# # =====================================================================
# # 图1：问题一左右两幅径向曲线，共用一个时间图例
# # =====================================================================
#
# times1 = np.asarray(
#     [100, 300, 600, 900, 1200, 1500, 1800],
#     dtype=float,
# )
#
# idx1 = np.asarray([
#     int(np.argmin(np.abs(q1["t"] - value)))
#     for value in times1
# ])
#
# r1_cm = q1["r"] * 100.0
#
# fig, axes = plt.subplots(
#     1,
#     2,
#     figsize=(11.2, 4.5),
#     sharex=True,
# )
#
# for j, (time_value, i) in enumerate(zip(times1, idx1)):
#     axes[0].plot(
#         r1_cm,
#         q1["T"][i] - 273.15,
#         color=TIME_COLORS[j],
#         lw=1.8,
#         marker="o",
#         ms=3.4,
#         markevery=20,
#         label=f"{time_value:.0f} s",
#     )
#
#     axes[1].plot(
#         r1_cm,
#         q1["C"][i],
#         color=TIME_COLORS[j],
#         lw=1.8,
#         marker="o",
#         ms=3.4,
#         markevery=20,
#         label=f"{time_value:.0f} s",
#     )
#
# axes[0].set_title(
#     "(a) 温度径向分布",
#     fontsize=12.5,
# )
#
# axes[1].set_title(
#     "(b) 水分浓度径向分布",
#     fontsize=12.5,
# )
#
# axes[0].set_ylabel("温度 / °C")
# axes[1].set_ylabel("水分浓度 / (kg/kg)")
#
# for ax in axes:
#     ax.set_xlabel("到药材中心的距离 / cm")
#     ax.set_xlim(0, 2.0)
#     style_axes(ax)
#
# handles, labels = axes[0].get_legend_handles_labels()
#
# fig.legend(
#     handles,
#     labels,
#     loc="lower center",
#     ncol=7,
#     frameon=False,
#     bbox_to_anchor=(0.5, -0.005),
# )
#
# fig.suptitle(
#     "问题1：预热阶段温度与失水的径向响应差异",
#     fontsize=14,
#     fontweight="bold",
#     y=1.02,
# )
#
# fig.subplots_adjust(
#     bottom=0.20,
#     wspace=0.28,
# )
#
# save(
#     fig,
#     "01_问题1_预热阶段径向响应",
# )
#
#
# # =====================================================================
# # 图2：问题二温度与水分过程，各取中心与表面；温度含环境曲线
# # =====================================================================
#
# t2_h = q2["t"] / 3600.0
# T2_c = q2["T"][:, 0] - 273.15
# T2_s = q2["T"][:, -1] - 273.15
# C2_c = q2["C"][:, 0]
# C2_s = q2["C"][:, -1]
#
# import pandas as pd
#
# air = pd.read_excel(ATTACH / "附件1.xlsx")
# air_t = air.iloc[:, 0].to_numpy(float)
# air_T = air.iloc[:, 1].to_numpy(float)
#
# Ta_curve = np.interp(
#     q2["t"],
#     air_t,
#     air_T,
# )
#
# fig, axes = plt.subplots(
#     1,
#     2,
#     figsize=(11.0, 4.5),
# )
#
# axes[0].plot(
#     t2_h,
#     T2_c,
#     color=COLORS["blue"],
#     lw=2.0,
#     label="中心温度",
# )
#
# axes[0].plot(
#     t2_h,
#     T2_s,
#     color=COLORS["orange"],
#     lw=2.0,
#     ls="--",
#     label="表面温度",
# )
#
# axes[0].plot(
#     t2_h,
#     Ta_curve,
#     color=COLORS["gray"],
#     lw=1.6,
#     ls=":",
#     label="环境温度",
# )
#
# axes[0].set_title(
#     "(a) 温度随时间变化",
#     fontsize=12.5,
# )
# axes[0].set_ylabel("温度 / °C")
#
# axes[1].plot(
#     t2_h,
#     C2_c,
#     color=COLORS["blue"],
#     lw=2.0,
#     label="中心水分浓度",
# )
#
# axes[1].plot(
#     t2_h,
#     C2_s,
#     color=COLORS["green"],
#     lw=2.0,
#     ls="--",
#     label="表面水分浓度",
# )
#
# axes[1].set_title(
#     "(b) 水分浓度随时间变化",
#     fontsize=12.5,
# )
# axes[1].set_ylabel("水分浓度 / (kg/kg)")
#
# for ax in axes:
#     ax.set_xlabel("时间 / h")
#     ax.set_xlim(0, 3)
#     style_axes(ax)
#     ax.legend(loc="best")
#
# dT3 = float(T2_s[-1] - T2_c[-1])
# dC3 = float(C2_c[-1] - C2_s[-1])
#
# axes[0].text(
#     0.97,
#     0.05,
#     f"3 h 径向温差 ≈ {dT3:.2f} °C",
#     transform=axes[0].transAxes,
#     ha="right",
#     va="bottom",
#     fontsize=9,
#     bbox=dict(
#         boxstyle="round,pad=0.28",
#         fc="white",
#         ec="#CCCCCC",
#     ),
# )
#
# axes[1].text(
#     0.97,
#     0.05,
#     f"3 h 径向水分差 ≈ {dC3:.2f} kg/kg",
#     transform=axes[1].transAxes,
#     ha="right",
#     va="bottom",
#     fontsize=9,
#     bbox=dict(
#         boxstyle="round,pad=0.28",
#         fc="white",
#         ec="#CCCCCC",
#     ),
# )
#
# fig.suptitle(
#     "问题2：温度趋于均匀时，水分仍存在明显径向差异",
#     fontsize=14,
#     fontweight="bold",
#     y=1.02,
# )
#
# fig.subplots_adjust(
#     wspace=0.30,
# )
#
# save(
#     fig,
#     "02_问题2_温度与水分过程",
# )
#
#
# # =====================================================================
# # 图3：问题三全域最大与表面含水率，标注两种达标时刻并局部放大
# # =====================================================================
#
# t3_h = q3["t"] / 3600.0
# Cmax = q3["C"].max(axis=1)
# Csurf = q3["C"][:, -1]
# threshold = 0.15
#
# t_surface_h = (
#     interpolate_crossing(
#         q3["t"],
#         Csurf,
#         threshold,
#     )
#     / 3600.0
# )
#
# t_global_h = (
#     interpolate_crossing(
#         q3["t"],
#         Cmax,
#         threshold,
#     )
#     / 3600.0
# )
#
# fig, ax = plt.subplots(
#     figsize=(8.4, 5.2),
# )
#
# ax.plot(
#     t3_h,
#     Cmax,
#     color=COLORS["red"],
#     lw=2.2,
#     label="全域最大含水率 Cmax(t)",
# )
#
# ax.plot(
#     t3_h,
#     Csurf,
#     color=COLORS["green"],
#     lw=1.9,
#     ls="--",
#     label="表面含水率",
# )
#
# ax.axhline(
#     threshold,
#     color=COLORS["black"],
#     lw=1.2,
#     ls=":",
#     label="阈值 C = 0.15",
# )
#
# ax.axvline(
#     t_surface_h,
#     color=COLORS["green"],
#     lw=1.0,
#     ls=":",
# )
#
# ax.axvline(
#     t_global_h,
#     color=COLORS["red"],
#     lw=1.0,
#     ls=":",
# )
#
# ax.scatter(
#     [t_surface_h, t_global_h],
#     [threshold, threshold],
#     color=[
#         COLORS["green"],
#         COLORS["red"],
#     ],
#     s=36,
#     zorder=5,
# )
#
# ax.annotate(
#     f"表面达标 ≈ {t_surface_h:.2f} h",
#     xy=(t_surface_h, threshold),
#     xytext=(t_surface_h + 1.1, 0.55),
#     color=COLORS["green"],
#     fontsize=9,
#     arrowprops=dict(
#         arrowstyle="->",
#         color=COLORS["green"],
#         lw=0.9,
#     ),
# )
#
# ax.annotate(
#     f"全域达标 ≈ {t_global_h:.2f} h",
#     xy=(t_global_h, threshold),
#     xytext=(t_global_h - 11.0, 0.29),
#     color=COLORS["red"],
#     fontsize=9,
#     arrowprops=dict(
#         arrowstyle="->",
#         color=COLORS["red"],
#         lw=0.9,
#     ),
# )
#
# ax.set_xlabel("时间 / h")
# ax.set_ylabel("水分浓度 / (kg/kg)")
# ax.set_xlim(0, 56)
# ax.set_ylim(0, 2.7)
# ax.set_title(
#     "问题3：全域最大含水率与表面含水率的达标差异",
#     fontsize=14,
#     fontweight="bold",
# )
# ax.legend(loc="upper right")
# style_axes(ax)
#
# ins = ax.inset_axes(
#     [0.58, 0.25, 0.39, 0.36],
# )
#
# ins.plot(
#     t3_h,
#     Cmax,
#     color=COLORS["red"],
#     lw=1.7,
# )
#
# ins.axhline(
#     threshold,
#     color=COLORS["black"],
#     lw=1.0,
#     ls=":",
# )
#
# ins.axvline(
#     t_global_h,
#     color=COLORS["red"],
#     lw=0.9,
#     ls=":",
# )
#
# ins.scatter(
#     [t_global_h],
#     [threshold],
#     color=COLORS["red"],
#     s=30,
#     zorder=5,
# )
#
# ins.set_xlim(
#     t_global_h - 2.2,
#     t_global_h + 0.35,
# )
#
# ins.set_ylim(
#     0.1488,
#     0.1508,
# )
#
# ins.set_xlabel(
#     "时间 / h",
#     fontsize=8,
# )
#
# ins.set_ylabel(
#     "Cmax",
#     fontsize=8,
# )
#
# ins.tick_params(
#     labelsize=7.5,
# )
#
# ins.set_title(
#     "后期局部放大",
#     fontsize=9,
# )
#
# ins.grid(
#     True,
#     ls=":",
#     lw=0.5,
#     alpha=0.55,
# )
#
# ins.spines["top"].set_visible(False)
# ins.spines["right"].set_visible(False)
#
# save(
#     fig,
#     "03_问题3_达标曲线与局部放大",
# )
#
#
# # =====================================================================
# # 图4：问题四材料坐标示意，同一材料点保持相同 xi
# # =====================================================================
#
# t4_h = q4["t"] / 3600.0
#
# show_hours = [
#     0.0,
#     12.0,
# ]
#
# idx_show = [
#     int(np.argmin(np.abs(t4_h - value)))
#     for value in show_hours
# ]
#
# R_show = q4["R_t"][idx_show]
# xi_point = 0.65
# scale = 2.0
#
# centers = np.asarray([
#     0.0,
#     12.0,
# ])
#
# radii = R_show * 100.0 * scale
#
# fig, axes = plt.subplots(
#     1,
#     2,
#     figsize=(10.2, 4.9),
# )
#
# limit = float(np.max(radii)) + 0.55
#
# for ax, radius, hour, R_value in zip(
#     axes,
#     radii,
#     show_hours,
#     R_show,
# ):
#     ax.add_patch(
#         Circle(
#             (0.0, 0.0),
#             radius,
#             facecolor="#F4F7FB",
#             edgecolor=COLORS["blue"],
#             lw=1.9,
#         )
#     )
#
#     ax.plot(
#         [0.0, xi_point * radius],
#         [0.0, 0.0],
#         color=COLORS["gray"],
#         lw=1.2,
#         ls="--",
#     )
#
#     ax.scatter(
#         [xi_point * radius],
#         [0.0],
#         color=COLORS["red"],
#         s=58,
#         zorder=5,
#     )
#
#     ax.text(
#         xi_point * radius,
#         0.22,
#         f"ξ = {xi_point:.2f}",
#         color=COLORS["red"],
#         ha="center",
#         va="bottom",
#         fontsize=10,
#     )
#
#     ax.annotate(
#         "",
#         xy=(radius, 0.0),
#         xytext=(0.0, 0.0),
#         arrowprops=dict(
#             arrowstyle="->",
#             color=COLORS["blue"],
#             lw=1.1,
#         ),
#     )
#
#     ax.text(
#         0.0,
#         -radius - 0.50,
#         f"t = {hour:.0f} h\nR(t) = {R_value * 100:.2f} cm",
#         ha="center",
#         va="top",
#         fontsize=10.5,
#     )
#
#     ax.set_aspect("equal")
#     ax.set_xlim(-limit, limit)
#     ax.set_ylim(-limit, limit)
#     ax.axis("off")
#
# fig.suptitle(
#     "问题4：移动几何如何映射到固定材料坐标",
#     fontsize=14,
#     fontweight="bold",
#     y=0.98,
# )
#
# fig.text(
#     0.5,
#     0.035,
#     "材料坐标  ξ = r/R(t)：半径收缩，同一材料点保持相同 ξ",
#     ha="center",
#     va="bottom",
#     fontsize=11,
# )
#
# fig.subplots_adjust(
#     left=0.04,
#     right=0.96,
#     top=0.84,
#     bottom=0.17,
#     wspace=0.05,
# )
#
# save(
#     fig,
#     "04_问题4_材料坐标示意",
# )
#
#
# # =====================================================================
# # 图5：问题四实际坐标 r-t 含水率热力图，外部区域严格留白
# # =====================================================================
#
# r_out_cm = np.linspace(
#     0.0,
#     2.0,
#     241,
# )
#
# r_out_m = r_out_cm / 100.0
#
# Z = np.full(
#     (len(q4["t"]), len(r_out_m)),
#     np.nan,
#     dtype=float,
# )
#
# for i, (Rt, Ci) in enumerate(
#     zip(
#         q4["R_t"],
#         q4["C"],
#     )
# ):
#     mask = r_out_m <= Rt + 1e-12
#
#     Z[i, mask] = np.interp(
#         r_out_m[mask] / Rt,
#         q4["xi"],
#         Ci,
#     )
#
# fig, ax = plt.subplots(
#     figsize=(8.0, 5.0),
# )
#
# mesh = ax.pcolormesh(
#     t4_h,
#     r_out_cm,
#     Z.T,
#     shading="auto",
#     cmap="viridis",
#     vmin=0.05,
#     vmax=2.55,
#     rasterized=True,
# )
#
# mesh.cmap.set_bad("white")
#
# ax.plot(
#     t4_h,
#     q4["R_t"] * 100.0,
#     color=COLORS["black"],
#     lw=2.0,
#     label="边界 r = R(t)",
# )
#
# ax.text(
#     4.0,
#     1.93,
#     "药材外部区域：留白",
#     color="#666666",
#     fontsize=10,
# )
#
# ax.set_xlabel("时间 / h")
# ax.set_ylabel("实际径向位置 r / cm")
# ax.set_xlim(0, t4_h[-1])
# ax.set_ylim(0, 2.02)
#
# ax.set_title(
#     "问题4：实际坐标下失水过程与半径收缩",
#     fontsize=14,
#     fontweight="bold",
# )
#
# ax.legend(loc="upper right")
# style_axes(ax)
#
# cb = fig.colorbar(
#     mesh,
#     ax=ax,
#     pad=0.02,
# )
#
# cb.set_label("水分浓度 / (kg/kg)")
#
# save(
#     fig,
#     "05_问题4_实际坐标收缩热力图",
# )
#
#
# summary = (
#     f"输出目录: {OUT}\n"
#     f"问题3 表面达标时间: {t_surface_h:.4f} h\n"
#     f"问题3 全域达标时间: {t_global_h:.4f} h\n"
#     f"问题4 烘干结束时间: {t4_h[-1]:.4f} h\n"
#     f"问题2 3 h 径向温差: {dT3:.4f} °C\n"
#     f"问题2 3 h 径向水分差: {dC3:.4f} kg/kg\n"
# )
#
# (OUT / "配图数据摘要.txt").write_text(
#     summary,
#     encoding="utf-8",
# )
#
# print(summary)
# print("SUGGESTED_FIGURES_COMPLETE")
for i in range(3):
    for j in range(3):
        if j == i :
            break
        print(i,end=" ")
