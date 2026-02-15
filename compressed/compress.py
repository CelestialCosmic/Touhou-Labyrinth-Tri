from PIL import Image
import os

def compress_image_jpeg(input_path, output_path, quality=60):
    """
    压缩 JPEG 图片并输出压缩后大小
    input_path: 原始图片路径
    output_path: 压缩后保存路径
    quality: 压缩质量 (1-95，数值越低压缩越狠)
    """
    img = Image.open(input_path)
    img = img.convert("RGB")  # 确保格式正确
    img.save(output_path, "JPEG", optimize=True, quality=quality)
    
    size_bytes = os.path.getsize(output_path)
    size_kb = size_bytes / 1024
    print(f"{output_path} 压缩后大小: {size_kb:.2f} KB")

def batch_compress_jpeg(input_folder, output_folder, quality=60):
    os.makedirs(output_folder, exist_ok=True)
    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            input_path = os.path.join(input_folder, filename)
            # 输出文件统一为 .jpg
            output_filename = os.path.splitext(filename)[0] + ".jpg"
            output_path = os.path.join(output_folder, output_filename)
            
            # 如果目标文件已存在则跳过
            if os.path.exists(output_path):
                print(f"跳过已存在文件: {output_path}")
                continue
            
            compress_image_jpeg(input_path, output_path, quality)

# 示例调用
batch_compress_jpeg("E:\\themeblog\\Touhou-Labyrinth-Tri\\images", 
                    "E:\\themeblog\\Touhou-Labyrinth-Tri\\compressed",
                    quality=60)
