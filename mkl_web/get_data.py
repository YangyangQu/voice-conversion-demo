import pandas as pd
import shutil
import os

# 1. 设置 csv 路径
csv_file = "/medias/speech/projects/quy/VC_baseline/mkl_best_wavs/best_sim_K32_cd32_min40_sd256_lam1.0.csv"  # 确保这个文件也在当前目录下

# 2. 读取并排序
df = pd.read_csv(csv_file)
top_20 = df.sort_values(by='sim', ascending=False).head(20)

# 3. 创建输出目录
output_dir = "demo_audio"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 4. 复制文件
print(f"开始复制 Top 20 的音频文件到 {output_dir}...")
count = 0
for index, row in top_20.iterrows():
    for col in ['src', 'ref', 'out']:
        src_path = row[col]
        filename = os.path.basename(src_path)
        dst_path = os.path.join(output_dir, filename)

        try:
            shutil.copyfile(src_path, dst_path)
            print(f"已复制: {filename}")
            count += 1
        except FileNotFoundError:
            print(f"文件未找到 (跳过): {src_path}")

print(f"完成！共复制了 {count} 个文件。请把 demo_audio 文件夹改名为 audio 并上传到你的网站。")