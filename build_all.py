# -*- coding: utf-8 -*-
"""
Master Build Script
Compiles all 19 HTML files for Nutura Organic Vietnam
"""

import os
from pages_home import build_home
from pages_shop import build_shop
from pages_products import build_product_stage1
from pages_products_stage2_3_4 import build_product_stage2, build_product_stage3
from pages_science import build_fresh_milk_difference, build_certified_organic, build_breast_is_best
from pages_village import build_about_us, build_village, build_subscriptions, build_faqs, build_contact, build_cart

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

PAGES = {
    "index.html": build_home,
    "shop.html": build_shop,
    "product-stage1.html": build_product_stage1,
    "product-stage2.html": build_product_stage2,
    "product-stage3.html": build_product_stage3,
    "fresh-milk-difference.html": build_fresh_milk_difference,
    "certified-organic.html": build_certified_organic,
    "about-us.html": build_about_us,
    "village.html": build_village,
    "subscriptions.html": build_subscriptions,
    "faqs.html": build_faqs,
    "contact.html": build_contact,
    "cart.html": build_cart,
    "breast-is-best.html": build_breast_is_best,
}

REMOVED_PAGES = [
    "product-stage4.html",
    "product-smoothie.html",
    "product-advance-kids.html",
    "product-advance-adults.html",
    "product-motherdaily.html",
]

def main():
    print("=" * 60)
    print("BẮT ĐẦU XUẤT BẢN WEBSITE NUTURA ORGANIC VIỆT NAM (LON STAGE 1 - 3)")
    print("=" * 60)

    # Clean up removed pages
    for rm in REMOVED_PAGES:
        rm_path = os.path.join(OUTPUT_DIR, rm)
        if os.path.exists(rm_path):
            os.remove(rm_path)
            print(f"🗑️ Đã dọn dẹp trang thừa: {rm}")

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
    print(f"HOÀN THÀNH: {len(PAGES)}/{len(PAGES)} trang web đã được tạo ({total_bytes / 1024:.1f} KB tổng cộng)")
    print("=" * 60)

if __name__ == "__main__":
    main()
