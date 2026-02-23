"""
SVG 转 PNG 批量转换工具
用法：python svg2png.py

需要安装: pip install cairosvg
或者:     pip install Pillow cairosvg

会把 素材/ 目录下所有 .svg 文件转换为同名 .png 文件
"""
import os
import glob

SVG_DIR = "素材"

def convert_with_cairosvg():
    """方式一：用 cairosvg（推荐，效果最好）"""
    import cairosvg

    svg_files = glob.glob(os.path.join(SVG_DIR, "*.svg"))
    print(f"找到 {len(svg_files)} 个 SVG 文件")

    for svg_path in svg_files:
        png_path = svg_path.replace(".svg", ".png")
        print(f"  转换: {svg_path} → {png_path}")
        cairosvg.svg2png(url=svg_path, write_to=png_path)

    print("全部完成！")


def convert_with_inkscape():
    """方式二：用 Inkscape 命令行（需要安装 Inkscape）"""
    svg_files = glob.glob(os.path.join(SVG_DIR, "*.svg"))
    print(f"找到 {len(svg_files)} 个 SVG 文件")

    for svg_path in svg_files:
        png_path = svg_path.replace(".svg", ".png")
        print(f"  转换: {svg_path} → {png_path}")
        # Inkscape 命令行转换
        os.system(f'inkscape "{svg_path}" --export-type=png --export-filename="{png_path}"')

    print("全部完成！")


def convert_with_browser():
    """方式三：纯 Python，无需额外安装（用内置 http + selenium 思路太重）
    这里提供一个用 Pillow + cairosvg 的简化版本
    """
    # 如果 cairosvg 装不上，可以试试在线转换或手动用浏览器打开 SVG 后截图
    print("请使用方式一或方式二")


if __name__ == "__main__":
    try:
        print("尝试使用 cairosvg 转换...")
        convert_with_cairosvg()
    except ImportError:
        print("cairosvg 未安装，请先运行: pip install cairosvg")
        print()
        print("或者尝试使用 Inkscape 转换...")
        try:
            convert_with_inkscape()
        except Exception as e:
            print(f"Inkscape 也不可用: {e}")
            print()
            print("=== 请选择以下任一方式安装 ===")
            print("  pip install cairosvg")
            print("  或下载安装 Inkscape: https://inkscape.org/")
