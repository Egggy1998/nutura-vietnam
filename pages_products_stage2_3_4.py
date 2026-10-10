# -*- coding: utf-8 -*-
"""
Product Detail Generators: Stage 2, Stage 3, Stage 4
"""

from build_site import render_head, render_topbar, render_navbar, render_footer

def build_product_stage2():
    content = render_head(
        title="Sữa Hữu Cơ Nutura Stage 2 (6 - 12 tháng) 800g | Giàu DHA, Sắt & Kẽm Ăn Dặm",
        description="Sữa công thức hữu cơ Nutura Stage 2 dành cho bé từ 6 đến 12 tháng tuổi. Đạm Casein cân bằng, tăng cường Sắt, Kẽm, DHA và hệ chất xơ GOS/FOS hỗ trợ hệ tiêu hóa giai đoạn ăn dặm.",
        canonical_url="product-stage2.html"
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
      <span class="text-stone-800 font-bold">Sữa Hữu Cơ Nutura Stage 2</span>
    </div>
  </div>

  <section class="py-12 lg:py-16 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-start">
        <div class="lg:col-span-6 space-y-4">
          <div class="bg-[#FAF7F2] rounded-3xl p-8 border border-stone-200/80 text-center relative overflow-hidden">
            <span class="absolute top-4 left-4 stage-badge stage-badge-s2">6 - 12 Tháng</span>
            <span class="absolute top-4 right-4 bg-emerald-100 text-emerald-800 px-3 py-1 rounded-full text-xs font-bold">ACO Hữu Cơ</span>
            <img src="assets/images/stage2.png" alt="Sữa Nutura Stage 2" class="h-96 mx-auto object-contain hover:scale-105 transition duration-300">
          </div>
        </div>

        <div class="lg:col-span-6 space-y-6">
          <div class="space-y-2">
            <div class="flex items-center gap-2">
              <div class="flex text-amber-400 text-sm">★★★★★</div>
              <span class="text-xs text-stone-500 font-semibold">(112 đánh giá)</span>
            </div>
            <h1 class="text-3xl sm:text-4xl font-bold text-stone-900 leading-tight">
              Sữa Công Thức Hữu Cơ Nutura Stage 2
            </h1>
            <p class="text-sm font-semibold text-[#FF6F78]">Follow-on Formula cho bé từ 6 đến 12 tháng tuổi • Khối lượng tịnh: 800g</p>
          </div>

          <p class="text-stone-600 text-sm leading-relaxed">
            Từ 6 tháng tuổi, khi bé bắt đầu hành trình ăn dặm, nhu cầu về <strong>Sắt, Canxi và Kẽm</strong> tăng cao rõ rệt. Nutura Stage 2 được điều chỉnh tỷ lệ <strong>Casein cân bằng (50:50)</strong> giúp bé no lâu, ngủ sâu giấc hơn vào ban đêm, kết hợp cùng hệ chất xơ GOS & FOS giúp hệ tiêu hóa luôn êm mượt, không táo bón.
          </p>

          <div class="p-5 bg-[#FAF7F2] rounded-2xl border border-stone-200/80 space-y-4">
            <div class="flex items-baseline justify-between">
              <div>
                <span class="text-3xl font-bold text-[#FF6F78]">780.000 đ</span>
                <span class="text-xs text-stone-400 ml-2">≈ $46.00 AUD</span>
              </div>
              <span class="text-xs bg-emerald-100 text-emerald-800 font-bold px-2.5 py-1 rounded-full">Còn hàng</span>
            </div>

            <div class="flex items-center gap-4 pt-2">
              <button onclick="window.nuturaCart.addItem('stage-2', 1);" class="flex-1 py-3 px-6 bg-[#FF6F78] hover:bg-[#E65A63] text-white font-bold rounded-full transition shadow-lg shadow-[#FF6F78]/30 text-sm flex items-center justify-center gap-2">
                <span>Thêm Vào Giỏ Hàng</span>
              </button>
              <a href="subscriptions.html" class="py-3 px-5 rounded-full border border-stone-300 font-semibold text-xs text-stone-700 hover:bg-stone-50">
                Giao Định Kỳ -15%
              </a>
            </div>
          </div>

          <div class="grid grid-cols-2 gap-3 pt-2 text-xs text-stone-700">
            <div class="flex items-center gap-2"><span class="text-emerald-500 font-bold">✓</span> Đạm A2 từ bò ăn cỏ Úc</div>
            <div class="flex items-center gap-2"><span class="text-emerald-500 font-bold">✓</span> Tăng cường Sắt & Kẽm ăn dặm</div>
            <div class="flex items-center gap-2"><span class="text-emerald-500 font-bold">✓</span> Prebiotics kép GOS + FOS</div>
            <div class="flex items-center gap-2"><span class="text-emerald-500 font-bold">✓</span> Chuẩn hữu cơ kép ACO & NASAA</div>
          </div>
        </div>
      </div>
    </div>
  </section>
"""
    content += render_footer()
    return content

def build_product_stage3():
    content = render_head(
        title="Sữa Hữu Cơ Nutura Stage 3 (12 - 36 tháng) 800g | Giải Thưởng Số 1 Nước Úc",
        description="Sữa dinh dưỡng hữu cơ Nutura Stage 3 cho trẻ từ 1 đến 3 tuổi. Đạt giải thưởng Product Review Awards Số 1 nước Úc. 16 vitamin & khoáng chất, FOS/GOS, DHA giúp phát triển chiều cao và trí tuệ vượt trội.",
        canonical_url="product-stage3.html"
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
      <span class="text-stone-800 font-bold">Sữa Hữu Cơ Nutura Stage 3</span>
    </div>
  </div>

  <section class="py-12 lg:py-16 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-start">
        <div class="lg:col-span-6 space-y-4">
          <div class="bg-[#FAF7F2] rounded-3xl p-8 border border-stone-200/80 text-center relative overflow-hidden">
            <span class="absolute top-4 left-4 stage-badge stage-badge-s3">12 - 36 Tháng</span>
            <span class="absolute top-4 right-4 bg-amber-100 text-amber-900 px-3 py-1 rounded-full text-xs font-bold">Số 1 Nước Úc</span>
            <img src="assets/images/stage3.png" alt="Sữa Nutura Stage 3" class="h-96 mx-auto object-contain hover:scale-105 transition duration-300">
          </div>
        </div>

        <div class="lg:col-span-6 space-y-6">
          <div class="space-y-2">
            <div class="flex items-center gap-2">
              <div class="flex text-amber-400 text-sm">★★★★★</div>
              <span class="text-xs text-stone-500 font-semibold">(204 đánh giá - ProductReview No.1)</span>
            </div>
            <h1 class="text-3xl sm:text-4xl font-bold text-stone-900 leading-tight">
              Sữa Dinh Dưỡng Hữu Cơ Nutura Stage 3
            </h1>
            <p class="text-sm font-semibold text-[#FF6F78]">Toddler Milk Drink cho bé 1 - 3 tuổi • Khối lượng tịnh: 800g</p>
          </div>

          <p class="text-stone-600 text-sm leading-relaxed">
            Sản phẩm đạt giải thưởng danh giá <strong>Product Review Awards 2022 & 2023</strong> tại Úc. Cung cấp đến <strong>50% nhu cầu khuyến nghị hàng ngày (RDI)</strong> của 16 loại vitamin và khoáng chất quan trọng chỉ với 1-2 khẩu phần mỗi ngày. Bổ sung Canxi, Vitamin D3 tăng trưởng chiều cao, DHA và ARA cho trí não nhạy bén.
          </p>

          <div class="p-5 bg-[#FAF7F2] rounded-2xl border border-stone-200/80 space-y-4">
            <div class="flex items-baseline justify-between">
              <div>
                <span class="text-3xl font-bold text-[#FF6F78]">780.000 đ</span>
                <span class="text-xs text-stone-400 ml-2">≈ $46.00 AUD</span>
              </div>
              <span class="text-xs bg-emerald-100 text-emerald-800 font-bold px-2.5 py-1 rounded-full">Bán chạy nhất</span>
            </div>

            <div class="flex items-center gap-4 pt-2">
              <button onclick="window.nuturaCart.addItem('stage-3', 1);" class="flex-1 py-3 px-6 bg-[#FF6F78] hover:bg-[#E65A63] text-white font-bold rounded-full transition shadow-lg shadow-[#FF6F78]/30 text-sm flex items-center justify-center gap-2">
                <span>Thêm Vào Giỏ Hàng</span>
              </button>
              <a href="subscriptions.html" class="py-3 px-5 rounded-full border border-stone-300 font-semibold text-xs text-stone-700 hover:bg-stone-50">
                Giao Định Kỳ -15%
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
"""
    content += render_footer()
    return content

def build_product_stage4():
    content = render_head(
        title="Sữa Dinh Dưỡng Nutura Stage 4 (3 tuổi trở lên) 800g | Chuẩn Úc Cho Bé Lớn",
        description="Sữa dinh dưỡng Nutura Stage 4 Junior Milk Drink dành cho trẻ từ 3 tuổi trở lên. Nguồn dưỡng chất toàn diện cho giai đoạn mầm non và chuẩn bị bước vào tiểu học.",
        canonical_url="product-stage4.html"
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
      <span class="text-stone-800 font-bold">Sữa Nutura Stage 4</span>
    </div>
  </div>

  <section class="py-12 lg:py-16 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-start">
        <div class="lg:col-span-6 space-y-4">
          <div class="bg-[#FAF7F2] rounded-3xl p-8 border border-stone-200/80 text-center relative overflow-hidden">
            <span class="absolute top-4 left-4 stage-badge bg-indigo-50 text-indigo-700">3+ Tuổi</span>
            <img src="assets/images/stage4.jpg" alt="Sữa Nutura Stage 4" class="h-96 mx-auto object-contain hover:scale-105 transition duration-300">
          </div>
        </div>

        <div class="lg:col-span-6 space-y-6">
          <div class="space-y-2">
            <h1 class="text-3xl sm:text-4xl font-bold text-stone-900 leading-tight">
              Sữa Dinh Dưỡng Nutura Stage 4 (Junior Milk)
            </h1>
            <p class="text-sm font-semibold text-[#FF6F78]">Dành cho trẻ từ 3 tuổi trở lên • Khối lượng tịnh: 800g</p>
          </div>

          <p class="text-stone-600 text-sm leading-relaxed">
            Thiết kế dành riêng cho giai đoạn trẻ hoạt động thể chất và tư duy học hỏi không ngừng tại trường mầm non và tiểu học. Bổ sung Canxi, Kẽm, Vitamin A, C, D giúp hệ xương răng chắc khỏe và nâng cao đề kháng.
          </p>

          <div class="p-5 bg-[#FAF7F2] rounded-2xl border border-stone-200/80 space-y-4">
            <div class="flex items-baseline justify-between">
              <div>
                <span class="text-3xl font-bold text-[#FF6F78]">560.000 đ</span>
                <span class="text-xs text-stone-400 ml-2">≈ $33.00 AUD</span>
              </div>
              <span class="text-xs bg-emerald-100 text-emerald-800 font-bold px-2.5 py-1 rounded-full">Còn hàng</span>
            </div>

            <div class="flex items-center gap-4 pt-2">
              <button onclick="window.nuturaCart.addItem('stage-4', 1);" class="flex-1 py-3 px-6 bg-[#FF6F78] hover:bg-[#E65A63] text-white font-bold rounded-full transition shadow-lg shadow-[#FF6F78]/30 text-sm flex items-center justify-center gap-2">
                <span>Thêm Vào Giỏ Hàng</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
"""
    content += render_footer()
    return content

print("Stage 2, 3, 4 builders ready.")
