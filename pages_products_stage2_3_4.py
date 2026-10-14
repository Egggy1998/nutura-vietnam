# -*- coding: utf-8 -*-
"""
Product Detail Generators: Stage 2, Stage 3, Stage 4
"""

from build_site import render_head, render_topbar, render_navbar, render_footer

def build_product_stage2():
    content = render_head(
        title="Sữa Hữu Cơ Nutura Stage 2 (6 - 12 tháng) 800g | Giàu DHA, Sắt & Kẽm Ăn Dặm",
        description="Sữa công thức hữu cơ Nutura Stage 2 dành cho bé từ 6 đến 12 tháng tuổi. Tỷ lệ Whey : Casein 40 : 60, có DHA và chất xơ GOS/FOS theo nhãn sản phẩm.",
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
              <span class="text-xs text-stone-500 font-semibold">Thông tin sản phẩm theo nhãn Stage 2</span>
            </div>
            <h1 class="text-3xl sm:text-4xl font-bold text-stone-900 leading-tight">
              Sữa Công Thức Hữu Cơ Nutura Stage 2
            </h1>
            <p class="text-sm font-semibold text-[#FF6F78]">Follow-on Formula cho bé từ 6 đến 12 tháng tuổi • Khối lượng tịnh: 800g</p>
          </div>

          <p class="text-stone-600 text-sm leading-relaxed">
            Nutura Stage 2 là sữa công thức tiếp nối dành cho trẻ từ 6 đến 12 tháng tuổi. Nhãn sản phẩm ghi tỷ lệ <strong>Whey : Casein 40 : 60</strong>, có DHA, GOS và FOS. Sản phẩm không thay thế chế độ ăn dặm đa dạng.
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
            <div class="flex items-center gap-2"><span class="text-emerald-500 font-bold">✓</span> Chứng nhận hữu cơ ACO theo nhãn</div>
          </div>
        </div>
      </div>
      <div class="mt-10 rounded-2xl border border-amber-200 bg-amber-50 p-6 text-sm text-stone-800 space-y-2">
        <h2 class="font-bold text-base">Pha sữa theo nhãn Stage 2</h2>
        <p>Chỉ dùng cho trẻ từ 6 tháng tuổi. Dùng muỗng trong lon: 1 muỗng gạt ngang (4,6 g) cho 30 ml nước đun sôi để nguội. Trẻ 6–9 tháng: 180 ml nước + 6 muỗng, khoảng 4 cữ/ngày; trẻ 9–12 tháng: 240 ml nước + 8 muỗng, khoảng 3 cữ/ngày. Không tự thay đổi tỷ lệ trừ khi có chỉ định y tế.</p>
        <p>Sữa mẹ là thức ăn tốt nhất cho trẻ sơ sinh và trẻ nhỏ. Hỏi ý kiến chuyên gia y tế trước khi dùng sữa công thức; trẻ từ 6 tháng cần ăn dặm phù hợp.</p>
      </div>
    </div>
  </section>
"""
    content += render_footer()
    return content

def build_product_stage3():
    content = render_head(
        title="Sữa Hữu Cơ Nutura Stage 3 (12 - 36 tháng) 800g | Thông Tin Theo Nhãn Sản Phẩm",
        description="Sữa dinh dưỡng hữu cơ Nutura Stage 3 cho trẻ từ 1 đến 3 tuổi; mỗi khẩu phần 230 ml cung cấp 216 mg canxi, 2,5 µg vitamin D và 33 mg DHA theo nhãn sản phẩm.",
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
            <span class="absolute top-4 right-4 bg-amber-100 text-amber-900 px-3 py-1 rounded-full text-xs font-bold">Từ 12 tháng tuổi</span>
            <img src="assets/images/stage3.png" alt="Sữa Nutura Stage 3" class="h-96 mx-auto object-contain hover:scale-105 transition duration-300">
          </div>
        </div>

        <div class="lg:col-span-6 space-y-6">
          <div class="space-y-2">
            <div class="flex items-center gap-2">
              <span class="text-xs text-stone-500 font-semibold">Thông tin sản phẩm theo nhãn Stage 3</span>
            </div>
            <h1 class="text-3xl sm:text-4xl font-bold text-stone-900 leading-tight">
              Sữa Dinh Dưỡng Hữu Cơ Nutura Stage 3
            </h1>
            <p class="text-sm font-semibold text-[#FF6F78]">Toddler Milk Drink cho bé 1 - 3 tuổi • Khối lượng tịnh: 800g</p>
          </div>

          <p class="text-stone-600 text-sm leading-relaxed">
            Nutura Stage 3 dành cho trẻ từ 1 đến 3 tuổi. Theo nhãn, mỗi khẩu phần 230 ml cung cấp <strong>216 mg canxi</strong>, <strong>2,5 µg vitamin D</strong> và <strong>33 mg DHA</strong>; tỷ lệ đáp ứng nhu cầu khuyến nghị khác nhau tùy dưỡng chất.
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
      <div class="mt-10 rounded-2xl border border-amber-200 bg-amber-50 p-6 text-sm text-stone-800 space-y-2">
        <h2 class="font-bold text-base">Pha sữa theo nhãn Stage 3</h2>
        <p>Chỉ dùng cho trẻ từ 12 tháng tuổi. Dùng muỗng trong lon: 6 muỗng gạt ngang (6 g/muỗng) pha với 200 ml nước sạch; cho trẻ uống ngay sau khi pha, không bảo quản và bỏ phần còn thừa. Hướng dẫn trên nhãn: 1–2 cữ/ngày.</p>
        <p>Thức uống này bổ sung cho chế độ ăn đa dạng, không dùng cho trẻ dưới 12 tháng. Hãy hỏi ý kiến chuyên gia y tế trước khi sử dụng.</p>
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
