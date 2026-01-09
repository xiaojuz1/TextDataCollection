import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei', 'SimHei', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

# 图表1：官方互动策略时间线
fig1, ax1 = plt.subplots(figsize=(12, 6))
fig1.patch.set_facecolor('#f8f9fa')

# 隐藏坐标轴
ax1.axis('off')
ax1.axis('tight')

# 时间线数据
timeline_data = [
    ["2018", "客服回应“蒸蒸日上”", "被截图传播", "梗诞生"],
    ["2019", "客服配合玩家重复该句", "玩家集体“行为艺术”", "梗扩散"],
    ["2021", "Steam版上线，差评爆增", "官方未回应差评", "玩家开始'刷差评保卫第一'"],
    ["2023", "官方在营销中使用“蒸蒸日上”", "玩家继续玩梗、吐槽", "梗文化延续至今"]
]

columns = ["年份", "官方行为", "玩家反应", "传播效果"]

# 创建表格
table1 = ax1.table(cellText=timeline_data,
                   colLabels=columns,
                   cellLoc='center',
                   loc='center',
                   colColours=['#e3f2fd', '#e8f5e9', '#fff3e0', '#fce4ec'])

table1.auto_set_font_size(False)
table1.set_fontsize(10)
table1.scale(1.2, 1.8)

# 设置标题
ax1.set_title('官方互动策略时间线\n（基于《传播路径.docx》）',
              fontsize=14, fontweight='bold', pad=20, color='#2c3e50')

plt.tight_layout()
plt.savefig('官方互动时间线.png', dpi=300, bbox_inches='tight')
plt.show()

# 图表2：官方互动模式与玩家情绪对比
fig2, ax2 = plt.subplots(figsize=(14, 6))
fig2.patch.set_facecolor('#f8f9fa')
ax2.axis('off')

interaction_data = [
    ["客服乐观回应", "“睁眼说瞎话”", "愤怒", "梗诞生"],
    ["客服配合玩梗", "“官方自我嘲讽”", "戏谑", "梗扩散"],
    ["官方沉默不回应", "“冷处理、无视玩家”", "失望", "持续差评"],
    ["营销中使用梗", "“自黑、蹭热度”", "嘲讽", "梗文化延续"]
]

columns2 = ["官方行为", "玩家解读", "情绪反应", "传播效果"]

# 创建表格
table2 = ax2.table(cellText=interaction_data,
                   colLabels=columns2,
                   cellLoc='center',
                   loc='center',
                   colColours=['#e3f2fd', '#f3e5f5', '#e8f5e9', '#fff3e0'])

table2.auto_set_font_size(False)
table2.set_fontsize(11)
table2.scale(1.2, 2.0)

# 设置标题
ax2.set_title('官方互动模式与玩家情绪对比\n（适用于PPT第四页）',
              fontsize=14, fontweight='bold', pad=20, color='#2c3e50')

plt.tight_layout()
plt.savefig('官方互动模式对比.png', dpi=300, bbox_inches='tight')
plt.show()

# 图表3：官方互动策略对比图（详细表格）
fig3, ax3 = plt.subplots(figsize=(16, 6))
fig3.patch.set_facecolor('#f8f9fa')
ax3.axis('off')

detailed_data = [
    ["被动回应", "客服“蒸蒸日上”回应", "愤怒、截图传播", "梗诞生"],
    ["配合玩梗", "客服重复该句", "戏谑、行为艺术", "梗扩散"],
    ["沉默不回应", "Steam差评无官方回复", "失望、持续差评", "负面情绪累积"],
    ["自黑式营销", "活动中使用“蒸蒸日上”", "嘲讽、继续玩梗", "梗文化延续"]
]

columns3 = ["互动类型", "具体表现", "玩家反应", "传播效果"]

# 创建表格
table3 = ax3.table(cellText=detailed_data,
                   colLabels=columns3,
                   cellLoc='center',
                   loc='center',
                   colColours=['#bbdefb', '#d1c4e9', '#c8e6c9', '#ffecb3'])

table3.auto_set_font_size(False)
table3.set_fontsize(11)
table3.scale(1.2, 2.2)

# 高亮关键行
for i in range(1, len(detailed_data)+1):
    if detailed_data[i-1][0] == "沉默不回应":
        for j in range(4):
            table3[(i, j)].set_facecolor('#ffcdd2')  # 红色高亮
    elif detailed_data[i-1][0] == "自黑式营销":
        for j in range(4):
            table3[(i, j)].set_facecolor('#fff9c4')  # 黄色高亮

# 设置标题
ax3.set_title('官方互动策略对比表\n（基于《传播路径.docx》与《情感分析.docx》）',
              fontsize=14, fontweight='bold', pad=20, color='#2c3e50')

plt.tight_layout()
plt.savefig('官方互动策略对比表.png', dpi=300, bbox_inches='tight')
plt.show()

# 图表4：官方互动路径示意图（使用流程图风格的表格）
fig4, ax4 = plt.subplots(figsize=(14, 8))
fig4.patch.set_facecolor('#f8f9fa')
ax4.axis('off')

# 创建流程图风格的表格
flowchart_data = [
    ["第一阶段", "玩家质疑游戏运营问题", "客服回应“蒸蒸日上”", "玩家截图传播", "官方未澄清解释"],
    ["↓", "", "", "", ""],
    ["第二阶段", "玩家继续玩梗创作", "官方保持沉默", "差评区成“打卡地”", "负面叙事主导社区"],
    ["↓", "", "", "", ""],
    ["第三阶段", "官方在营销中玩梗", "玩家嘲讽式互动", "梗文化反哺品牌", "形成负面辨识度"]
]

columns4 = ["阶段", "玩家行为", "官方行为", "社群反应", "长期影响"]

# 创建表格
table4 = ax4.table(cellText=flowchart_data,
                   colLabels=columns4,
                   cellLoc='center',
                   loc='center',
                   colColours=['#e1f5fe', '#fce4ec', '#f3e5f5', '#e8f5e9', '#fff3e0'])

table4.auto_set_font_size(False)
table4.set_fontsize(10)
table4.scale(1.1, 2.0)

# 设置箭头行的样式
table4[(2, 0)].set_facecolor('#f5f5f5')
table4[(2, 0)].set_text_props(fontsize=16, fontweight='bold', color='#666')
table4[(4, 0)].set_facecolor('#f5f5f5')
table4[(4, 0)].set_text_props(fontsize=16, fontweight='bold', color='#666')

# 设置标题
ax4.set_title('官方互动路径示意图\n（从回应到沉默的演变过程）',
              fontsize=14, fontweight='bold', pad=20, color='#2c3e50')

# 添加说明文字
ax4.text(0.5, 0.02, '箭头表示互动路径的发展方向，展示官方从“被动回应”到“沉默”再到“自黑营销”的演变',
         fontsize=9, style='italic', ha='center', transform=ax4.transAxes, color='#666')

plt.tight_layout()
plt.savefig('官方互动路径图.png', dpi=300, bbox_inches='tight')
plt.show()

print("✅ 四张图表已生成并保存为PNG文件：")
print("1. 官方互动时间线.png")
print("2. 官方互动模式对比.png")
print("3. 官方互动策略对比表.png")
print("4. 官方互动路径图.png")