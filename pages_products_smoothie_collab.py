# -*- coding: utf-8 -*-
"""
Product Detail Generators: The Good Smoothie, Smart Grow Kids, Active Adults, MotherDaily
"""

from build_site import render_head, render_topbar, render_navbar, render_footer

def build_product_smoothie():
    content = render_head(
        title="Sữa Bột The Good Smoothie Nutura | Dinh Dưỡng Hướng Đích Trí Não, Giấc Ngủ & Đề Kháng",
        description="Dòng sữa bột Smoothie The Good Smoothie của Nutura Organic: Cognitive (Trí Não), Calm (Thư Giãn Giấc Ngủ), Immunity (Tăng Đề Kháng). 100% sữa bò ăn cỏ Úc.",
        canonical_url="product-smoothie.html"
    )
    content += render_topbar()
    content += render_navbar(active_page="shop")
    content += """
  <div class="bg-[#FAF7F2] py-4 border-b border-stone-200/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-xs text-stone-500 flex items-center gap-2">
      <a href="index.html" class="hover:text-[#FF6F78]">Trang Chủ</a>
      <span>/</span>
      <a href="shop.html" class="hover:text-[#FF6F78]">Sản Phẩm</a>
      <span>/</span>
      <span class="text-stone-800 font-bold">The Good Smoothie</span>
    </div>
  </div>

  <section class="py-12 lg:py-16 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-3xl mx-auto mb-12 space-y-3">
        <span class="stage-badge stage-badge-smoothie">Đột Phá Dinh Dưỡng 2026</span>
        <h1 class="text-3xl sm:text-4xl font-bold text-stone-900">Dòng Sữa Bột The Good Smoothie</h1>
        <p class="text-stone-600 text-sm leading-relaxed">
          Được làm từ sữa bò ăn cỏ tự nhiên của Úc và bổ sung các vi chất chuyên sâu theo từng mục tiêu sức khỏe của bé. Giá khuyến mãi đặc biệt: <strong>410.000 đ/hộp 300g</strong> (Giá gốc 590.000 đ).
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <!-- Cognitive -->
        <div class="nutura-card p-6 flex flex-col bg-white">
          <span class="stage-badge stage-badge-smoothie self-start mb-2">Trí Não & Tập Trung</span>
          <h3 class="text-xl font-bold text-stone-900 mb-1">Smoothie Cognitive</h3>
          <p class="text-xs text-stone-500 mb-4">Hỗ trợ nhận thức, trí nhớ và sự tập trung</p>
          <img src="assets/images/smoothie-cognitive.png" alt="Cognitive" class="h-56 mx-auto object-contain my-3">
          <ul class="text-xs text-stone-600 space-y-1.5 my-3 bg-purple-50/50 p-3 rounded-xl">
            <li>• <strong>Phospholipids:</strong> Phát triển màng tế bào não</li>
            <li>• <strong>Tyrosine:</strong> Dẫn truyền thần kinh nhanh nhạy</li>
            <li>• <strong>DHA & B-Vitamins:</strong> Não bộ và thị lực</li>
          </ul>
          <div class="mt-auto pt-3 border-t border-stone-100 flex items-center justify-between">
            <div>
              <span class="text-lg font-bold text-[#FF6F78]">410.000 đ</span>
              <span class="text-xs text-stone-400 line-through block">590.000 đ</span>
            </div>
            <button onclick="window.nuturaCart.addItem('smoothie-cognitive', 1);" class="px-4 py-2 bg-[#FF6F78] hover:bg-[#E65A63] text-white font-bold text-xs rounded-full">
              + Giỏ Hàng
            </button>
          </div>
        </div>

        <!-- Calm -->
        <div class="nutura-card p-6 flex flex-col bg-white">
          <span class="stage-badge bg-amber-50 text-amber-700 self-start mb-2">Giấc Ngủ & Thư Giãn</span>
          <h3 class="text-xl font-bold text-stone-900 mb-1">Smoothie Calm</h3>
          <p class="text-xs text-stone-500 mb-4">Giúp bé dễ đi vào giấc ngủ, ngủ ngon giấc</p>
          <img src="assets/images/smoothie-calm.png" alt="Calm" class="h-56 mx-auto object-contain my-3">
          <ul class="text-xs text-stone-600 space-y-1.5 my-3 bg-amber-50/50 p-3 rounded-xl">
            <li>• <strong>Hoa cúc Chamomile:</strong> Thảo mộc êm dịu</li>
            <li>• <strong>Yến mạch Avena Sativa:</strong> Xoa dịu căng thẳng</li>
            <li>• <strong>Magie & Chuối:</strong> Hỗ trợ thư giãn cơ bắp</li>
          </ul>
          <div class="mt-auto pt-3 border-t border-stone-100 flex items-center justify-between">
            <div>
              <span class="text-lg font-bold text-[#FF6F78]">410.000 đ</span>
              <span class="text-xs text-stone-400 line-through block">590.000 đ</span>
            </div>
            <button onclick="window.nuturaCart.addItem('smoothie-calm', 1);" class="px-4 py-2 bg-[#FF6F78] hover:bg-[#E65A63] text-white font-bold text-xs rounded-full">
              + Giỏ Hàng
            </button>
          </div>
        </div>

        <!-- Immunity -->
        <div class="nutura-card p-6 flex flex-col bg-white">
          <span class="stage-badge bg-rose-50 text-rose-700 self-start mb-2">Tăng Đề Kháng</span>
          <h3 class="text-xl font-bold text-stone-900 mb-1">Smoothie Immunity</h3>
          <p class="text-xs text-stone-500 mb-4">Lá chắn miễn dịch vững vàng chống ốm vặt</p>
          <img src="assets/images/smoothie-immunity.png" alt="Immunity" class="h-56 mx-auto object-contain my-3">
          <ul class="text-xs text-stone-600 space-y-1.5 my-3 bg-rose-50/50 p-3 rounded-xl">
            <li>• <strong>Lactoferrin:</strong> Kháng thể sinh học tự nhiên</li>
            <li>• <strong>Quả cơm cháy Elderberry:</strong> Chống virus tự nhiên</li>
            <li>• <strong>Kẽm sinh học & Vitamin C:</strong> Miễn dịch toàn diện</li>
          </ul>
          <div class="mt-auto pt-3 border-t border-stone-100 flex items-center justify-between">
            <div>
              <span class="text-lg font-bold text-[#FF6F78]">410.000 đ</span>
              <span class="text-xs text-stone-400 line-through block">590.000 đ</span>
            </div>
            <button onclick="window.nuturaCart.addItem('smoothie-immunity', 1);" class="px-4 py-2 bg-[#FF6F78] hover:bg-[#E65A63] text-white font-bold text-xs rounded-full">
              + Giỏ Hàng
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>
"""
    content += render_footer()
    return content

def build_product_advance_kids():
    content = render_head(
        title="Nutura Advance Smart Grow for Kids 800g | Sữa Dinh Dưỡng Phát Triển Thể Chất",
        description="Sữa Nutura Advance Smart Grow for Kids - Dinh dưỡng cao cấp phát triển chiều cao, thể lực và trí tuệ cho trẻ em từ 3 tuổi trở lên.",
        canonical_url="product-advance-kids.html"
    )
    content += render_topbar()
    content += render_navbar(active_page="shop")
    content += """
  <div class="bg-[#FAF7F2] py-4 border-b border-stone-200/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-xs text-stone-500 flex items-center gap-2">
      <a href="index.html" class="hover:text-[#FF6F78]">Trang Chủ</a>
      <span>/</span>
      <a href="shop.html" class="hover:text-[#FF6F78]">Sản Phẩm</a>
      <span>/</span>
      <span class="text-stone-800 font-bold">Nutura Advance Smart Grow</span>
    </div>
  </div>

  <section class="py-12 lg:py-16 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-start">
        <div class="lg:col-span-6 space-y-4">
          <div class="bg-[#FAF7F2] rounded-3xl p-8 border border-stone-200/80 text-center">
            <img src="assets/images/smart-grow-kids.jpg" alt="Nutura Advance Smart Grow" class="h-96 mx-auto object-contain">
          </div>
        </div>
        <div class="lg:col-span-6 space-y-6">
          <h1 class="text-3xl sm:text-4xl font-bold text-stone-900 leading-tight">Nutura Advance Smart Grow for Kids</h1>
          <p class="text-sm font-semibold text-[#FF6F78]">Premium Nutritional Milk Drink • 800g</p>
          <p class="text-stone-600 text-sm leading-relaxed">
            Dòng sữa công thức bổ sung vi chất dinh dưỡng năng lượng cao, thiết kế đặc biệt cho trẻ biếng ăn, nhẹ cân hoặc cần bứt phá thể lực và chiều cao trong giai đoạn phát triển vàng.
          </p>
          <div class="p-5 bg-[#FAF7F2] rounded-2xl border border-stone-200/80">
            <span class="text-3xl font-bold text-[#FF6F78]">780.000 đ</span>
            <button onclick="window.nuturaCart.addItem('smart-grow-kids', 1);" class="mt-4 w-full py-3 bg-[#FF6F78] hover:bg-[#E65A63] text-white font-bold rounded-full transition text-sm">
              Thêm Vào Giỏ Hàng
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>
"""
    content += render_footer()
    return content

def build_product_advance_adults():
    content = render_head(
        title="Nutura Advance Active Adults 800g | Sữa Dinh Dưỡng Phục Hồi Cho Người Lớn",
        description="Sữa dinh dưỡng Nutura Advance Active Adults dành cho người lớn tuổi, người hoạt động thể thao hoặc cần phục hồi sức khỏe nhanh chóng.",
        canonical_url="product-advance-adults.html"
    )
    content += render_topbar()
    content += render_navbar(active_page="shop")
    content += """
  <div class="bg-[#FAF7F2] py-4 border-b border-stone-200/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-xs text-stone-500 flex items-center gap-2">
      <a href="index.html" class="hover:text-[#FF6F78]">Trang Chủ</a>
      <span>/</span>
      <a href="shop.html" class="hover:text-[#FF6F78]">Sản Phẩm</a>
      <span>/</span>
      <span class="text-stone-800 font-bold">Nutura Advance Active Adults</span>
    </div>
  </div>

  <section class="py-12 lg:py-16 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-start">
        <div class="lg:col-span-6 space-y-4">
          <div class="bg-[#FAF7F2] rounded-3xl p-8 border border-stone-200/80 text-center">
            <img src="assets/images/active-adults.jpg" alt="Nutura Active Adults" class="h-96 mx-auto object-contain">
          </div>
        </div>
        <div class="lg:col-span-6 space-y-6">
          <h1 class="text-3xl sm:text-4xl font-bold text-stone-900 leading-tight">Nutura Advance Active Adults</h1>
          <p class="text-sm font-semibold text-[#FF6F78]">Dinh Dưỡng Phục Hồi Năng Lượng Cho Người Lớn • 800g</p>
          <p class="text-stone-600 text-sm leading-relaxed">
            Giàu Canxi, Đạm tươi sinh học, Magie và hệ 28 vitamin khoáng chất thiết yếu giúp bảo vệ mật độ xương, giảm mệt mỏi cơ bắp và duy trì lối sống tích cực.
          </p>
          <div class="p-5 bg-[#FAF7F2] rounded-2xl border border-stone-200/80">
            <span class="text-3xl font-bold text-[#FF6F78]">780.000 đ</span>
            <button onclick="window.nuturaCart.addItem('active-adults', 1);" class="mt-4 w-full py-3 bg-[#FF6F78] hover:bg-[#E65A63] text-white font-bold rounded-full transition text-sm">
              Thêm Vào Giỏ Hàng
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>
"""
    content += render_footer()
    return content

def build_product_motherdaily():
    content = render_head(
        title="Combo Nutura x MotherDaily | Bộ Đôi Chăm Sóc Hoàn Hảo Cho Mẹ & Bé (Giảm 40%)",
        description="Ưu đãi độc quyền Nutura x MotherDaily giảm ngay 40%: Combo lon sữa hữu cơ Nutura cùng trọn bộ sản phẩm phục hồi sau sinh MotherDaily.",
        canonical_url="product-motherdaily.html"
    )
    content += render_topbar()
    content += render_navbar(active_page="shop")
    content += """
  <div class="bg-[#FAF7F2] py-4 border-b border-stone-200/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-xs text-stone-500 flex items-center gap-2">
      <a href="index.html" class="hover:text-[#FF6F78]">Trang Chủ</a>
      <span>/</span>
      <a href="shop.html" class="hover:text-[#FF6F78]">Sản Phẩm</a>
      <span>/</span>
      <span class="text-stone-800 font-bold">Combo Nutura x MotherDaily</span>
    </div>
  </div>

  <section class="py-12 lg:py-16 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        <div class="lg:col-span-6 space-y-4">
          <div class="bg-gradient-to-br from-rose-50 to-amber-50 rounded-3xl p-8 border border-rose-200 text-center">
            <span class="inline-block px-3 py-1 rounded-full bg-rose-500 text-white text-xs font-bold mb-4">Ưu Đãi Đặc Quyền -40%</span>
            <img src="assets/images/motherdaily-pack.png" alt="Nutura x MotherDaily" class="max-h-96 mx-auto object-contain">
          </div>
        </div>
        <div class="lg:col-span-6 space-y-6">
          <h1 class="text-3xl sm:text-4xl font-bold text-stone-900 leading-tight">
            Combo Hoàn Hảo Cho Mẹ & Bé: Nutura x MotherDaily
          </h1>
          <p class="text-stone-600 text-sm leading-relaxed">
            Sự kết hợp hoàn hảo giữa <strong>sữa hữu cơ tinh khiết Nutura</strong> nuôi dưỡng con và <strong>bộ sản phẩm phục hồi chuyên sâu MotherDaily</strong> dành riêng cho mẹ sau sinh. Tiết kiệm ngay 890.000 đ khi mua theo combo.
          </p>
          <div class="p-5 bg-rose-50/50 rounded-2xl border border-rose-200 space-y-4">
            <div class="flex items-baseline gap-3">
              <span class="text-3xl font-bold text-[#FF6F78]">1.330.000 đ</span>
              <span class="text-stone-400 line-through text-base">2.220.000 đ</span>
              <span class="text-xs bg-rose-100 text-rose-700 font-bold px-2.5 py-1 rounded-full">Tiết kiệm 40%</span>
            </div>
            <button onclick="window.nuturaCart.addItem('collab-stage1', 1);" class="w-full py-3.5 bg-[#FF6F78] hover:bg-[#E65A63] text-white font-bold rounded-full transition text-sm shadow-md shadow-[#FF6F78]/30">
              Đặt Mua Combo Nutura x MotherDaily Ngay
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>
"""
    content += render_footer()
    return content

print("Product smoothie & collab builders ready.")
