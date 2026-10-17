# -*- coding: utf-8 -*-
"""
Master Build Script
Compiles all compliant HTML pages for Nutura Việt Nam (Trang thương hiệu & tra cứu nhãn)
Tuân thủ Nghị định 100/2014/NĐ-CP & tiêu chuẩn WHO
"""

import os
from pages_home import build_home
from pages_products import build_product_stage1
from pages_products_stage2_3_4 import build_product_stage2, build_product_stage3
from pages_science import build_fresh_milk_difference, build_certified_organic, build_breast_is_best
from pages_village import build_about_us, build_village, build_faqs, build_contact

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

PAGES = {
    "index.html": build_home,
    "about-us.html": build_about_us,
    "fresh-milk-difference.html": build_fresh_milk_difference,
    "certified-organic.html": build_certified_organic,
    "product-stage1.html": build_product_stage1,
    "product-stage2.html": build_product_stage2,
    "product-stage3.html": build_product_stage3,
    "village.html": build_village,
    "breast-is-best.html": build_breast_is_best,
    "contact.html": build_contact,
    "faqs.html": build_faqs,
}

# Các trang thương mại, bán hàng, checkout, gói định kỳ cần xoá bỏ triệt để
REMOVED_PAGES = [
    "shop.html",
    "subscriptions.html",
    "cart.html",
    "product-stage4.html",
    "product-smoothie.html",
    "product-advance-kids.html",
    "product-advance-adults.html",
    "product-motherdaily.html",
]

def main():
    print("=" * 60)
    print("XUẤT BẢN WEBSITE NUTURA VIỆT NAM (PHIÊN BẢN TUÂN THỦ NĐ100/2014/NĐ-CP)")
    print("=" * 60)

    # 1. Dọn dẹp các trang bán hàng và trang không thuộc phạm vi
    for rm in REMOVED_PAGES:
        rm_path = os.path.join(OUTPUT_DIR, rm)
        if os.path.exists(rm_path):
            os.remove(rm_path)
            print(f"🗑️ Đã xoá trang thừa: {rm}")

    # 2. Xuất bản các trang hợp lệ
    total_bytes = 0
    for filename, builder in PAGES.items():
        html = builder()
        filepath = os.path.join(OUTPUT_DIR, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        file_size = len(html.encode("utf-8"))
        total_bytes += file_size
        print(f"✓ Đã tạo thành công: {filename:<30} ({file_size:>6} bytes)")

    print("-" * 60)
    print(f"HOÀN THÀNH: {len(PAGES)} trang web đã được xuất bản ({total_bytes / 1024:.1f} KB tổng cộng)")
    print("=" * 60)

if __name__ == "__main__":
    main()
