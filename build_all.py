# -*- coding: utf-8 -*-
"""
Master Build Script
Compiles all 19 HTML files for Nutura Organic Vietnam
"""

import os
from pages_home import build_home
from pages_shop import build_shop
from pages_products import build_product_stage1
from pages_products_stage2_3_4 import build_product_stage2, build_product_stage3, build_product_stage4
from pages_products_smoothie_collab import (
    build_product_smoothie,
    build_product_advance_kids,
    build_product_advance_adults,
    build_product_motherdaily
)
from pages_science import build_fresh_milk_difference, build_certified_organic, build_breast_is_best
from pages_village import build_about_us, build_village, build_subscriptions, build_faqs, build_contact, build_cart

OUTPUT_DIR = "C:/Users/sanon/projects/nutura-vietnam"

PAGES = {
    "index.html": build_home,
    "shop.html": build_shop,
    "product-stage1.html": build_product_stage1,
    "product-stage2.html": build_product_stage2,
    "product-stage3.html": build_product_stage3,
    "product-stage4.html": build_product_stage4,
    "product-smoothie.html": build_product_smoothie,
    "product-advance-kids.html": build_product_advance_kids,
    "product-advance-adults.html": build_product_advance_adults,
    "product-motherdaily.html": build_product_motherdaily,
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

def main():
    print("=" * 60)
    print("BẮT ĐẦU XUẤT BẢN WEBSITE NUTURA ORGANIC VIỆT NAM (19 TRANG)")
    print("=" * 60)

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
    print(f"HOÀN THÀNH: 19/19 trang web đã được tạo ({total_bytes / 1024:.1f} KB tổng cộng)")
    print("=" * 60)

if __name__ == "__main__":
    main()
