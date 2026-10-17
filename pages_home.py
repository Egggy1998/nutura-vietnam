# -*- coding: utf-8 -*-
"""
Trang chủ - index.html
Trang thương hiệu, khoa học dinh dưỡng & tra cứu nhãn sản phẩm Nutura Việt Nam
Tuân thủ Nghị định 100/2014/NĐ-CP và tiêu chuẩn WHO
"""

from build_site import render_head, render_topbar, render_navbar, render_footer, render_breast_milk_banner

def build_home():
    content = render_head(
        title="Trang thông tin sản phẩm & dinh dưỡng hữu cơ từ Úc",
        description="Nutura Organic Việt Nam - Sản phẩm dinh dưỡng công thức hữu cơ đạm A2 từ sữa tươi farmgate bang Victoria, Úc. Tra cứu thông tin theo nhãn sản phẩm và TCCS.",
        canonical_url="index.html"
    )
    content += render_topbar()
    content += render_breast_milk_banner()
    content += render_navbar(active_page="home")

    content += """
  <!-- Nội dung chính -->
  <main id="main-content">

  <!-- Hero Section -->
  <section class="relative bg-[#FAF7F2] overflow-hidden pt-8 pb-16 lg:py-20 border-b border-stone-200/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
        <!-- Nội dung giới thiệu -->
        <div class="lg:col-span-7 space-y-6 text-center lg:text-left">
          <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-rose-100 text-[#FF6F78] text-xs font-bold uppercase tracking-wider">
            <span class="w-2 h-2 rounded-full bg-[#FF6F78]"></span>
            Chứng nhận hữu cơ ACO trên nhãn • 100% sản xuất tại Úc
          </div>

          <h1 class="text-3xl sm:text-4xl lg:text-5xl font-bold text-stone-900 tracking-tight leading-tight">
            Sản phẩm dinh dưỡng công thức hữu cơ từ sữa tươi farmgate nước Úc
          </h1>

          <p class="text-base sm:text-lg text-stone-600 max-w-2xl mx-auto lg:mx-0 leading-relaxed">
            Nutura Việt Nam giới thiệu dòng sản phẩm dinh dưỡng chế biến từ <strong>sữa tươi nguyên liệu farmgate</strong> tại Victoria, Úc. Quy trình sấy phun một lần giúp giữ lại các thành phần tự nhiên trong sữa theo tiêu chuẩn TCCS.
          </p>

          <div class="flex flex-col sm:flex-row items-center justify-center lg:justify-start gap-3.5 pt-2">
            <a href="#san-pham" class="w-full sm:w-auto text-sm py-3 px-6 rounded-full bg-[#FF6F78] hover:bg-[#E65A63] text-white font-bold transition shadow-md text-center">
              <span>Xem thông tin 3 giai đoạn</span>
            </a>
            <a href="fresh-milk-difference.html" class="w-full sm:w-auto text-sm py-3 px-6 rounded-full border border-stone-300 text-stone-700 hover:border-[#FF6F78] hover:text-[#FF6F78] font-bold transition text-center">
              <span>Tìm hiểu sữa tươi farmgate</span>
            </a>
          </div>

          <!-- 4 đặc điểm minh bạch -->
          <div class="pt-6 border-t border-stone-200/80 grid grid-cols-2 sm:grid-cols-4 gap-4 text-center lg:text-left">
            <div>
              <div class="text-xs font-bold text-stone-900">Sữa tươi farmgate</div>
              <div class="text-[11px] text-stone-500">Quy trình một lần sấy</div>
            </div>
            <div>
              <div class="text-xs font-bold text-stone-900">Đạm A2 tự nhiên</div>
              <div class="text-[11px] text-stone-500">Từ đàn bò ăn cỏ tự nhiên</div>
            </div>
            <div>
              <div class="text-xs font-bold text-stone-900">Hữu cơ ACO</div>
              <div class="text-[11px] text-stone-500">Chứng nhận trên nhãn</div>
            </div>
            <div>
              <div class="text-xs font-bold text-stone-900">Không biến đổi gen</div>
              <div class="text-[11px] text-stone-500">Non-GMO theo tiêu chuẩn Úc</div>
            </div>
          </div>
        </div>

        <!-- Ảnh lon sữa thật trên nền đồng cỏ -->
        <div class="lg:col-span-5 relative">
          <div class="relative mx-auto max-w-md lg:max-w-none">
            <div class="rounded-3xl overflow-hidden shadow-xl border-4 border-white bg-gradient-to-b from-[#FFF5F6] to-[#FAF7F2] p-6 text-center">
              <img src="assets/images/nutura-tin-lockups.png" alt="Bộ sản phẩm dinh dưỡng công thức Nutura Organic Stage 1, Stage 2 và Stage 3" class="w-full h-auto object-contain mx-auto transition-transform hover:scale-105 duration-300" loading="eager">
              <p class="mt-3 text-xs text-stone-500 italic">Bộ 3 lon Nutura Organic A2 Protein chính hãng sản xuất tại Victoria, Úc</p>
            </div>
            <!-- Huy hiệu chứng nhận hữu cơ ACO -->
            <div class="absolute -bottom-4 -left-4 bg-white p-3 rounded-2xl shadow-lg border border-stone-100 flex items-center gap-3">
              <img src="assets/images/aco-logo.png" alt="Chứng nhận hữu cơ ACO" class="w-10 h-10 object-contain">
              <div>
                <div class="text-xs font-bold text-stone-900">Chứng nhận hữu cơ ACO</div>
                <div class="text-[11px] text-emerald-600 font-semibold">Thể hiện trên nhãn lon</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Sự khác biệt sữa tươi farmgate -->
  <section class="py-16 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        <!-- Ảnh minh họa quy trình -->
        <div class="lg:col-span-5 text-center">
          <div class="relative inline-block">
            <img src="assets/images/fresh-milk-circle.jpg" alt="Sữa tươi nguyên liệu farmgate tại bang Victoria, Úc" class="rounded-3xl shadow-xl w-72 sm:w-80 h-72 sm:h-80 object-cover mx-auto border-4 border-stone-100" loading="lazy">
            <div class="absolute -bottom-3 right-0 bg-white py-2 px-3.5 rounded-2xl shadow-md border border-stone-100 text-left">
              <div class="text-xs font-bold text-stone-900">Quy trình sấy phun 1 lần</div>
              <div class="text-[11px] text-stone-500">Từ sữa tươi farmgate</div>
            </div>
          </div>
        </div>

        <!-- Nội dung giải thích kỹ thuật -->
        <div class="lg:col-span-7 space-y-5">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-rose-100 text-[#FF6F78] text-xs font-bold uppercase tracking-wider">
            Khoa học công nghệ
          </div>
          <h2 class="text-2xl sm:text-3xl lg:text-4xl font-bold text-stone-900 leading-tight">
            Quy trình sấy 1 lần từ sữa tươi farmgate
          </h2>
          <p class="text-stone-700 text-sm sm:text-base leading-relaxed">
            Khác với quy trình dùng bột sữa hoàn nguyên phải qua 2 lần gia nhiệt sấy khô, Nutura sử dụng nguồn <strong>sữa tươi thu gom trực tiếp tại trang trại (farmgate milk)</strong> và tiến hành phối trộn ướt (wet blending), sau đó sấy phun một lần duy nhất.
          </p>
          <p class="text-stone-600 text-sm leading-relaxed">
            Quy trình này giúp giữ lại Lactoferrin và IgG tự nhiên trong sữa theo tiêu chuẩn TCCS đã công bố, đồng thời bảo toàn cấu trúc đạm A2 tự nhiên từ đàn bò ăn cỏ.
          </p>

          <!-- 3 thẻ tính năng tiếng Việt thay thế cho ảnh tiếng Anh -->
          <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 pt-2">
            <div class="p-3.5 rounded-2xl bg-stone-50 border border-stone-100">
              <div class="text-base mb-1">🥛</div>
              <div class="text-xs font-bold text-stone-900">Sữa tươi farmgate</div>
              <div class="text-[11px] text-stone-500 mt-0.5">100% sữa tươi từ trang trại Victoria</div>
            </div>
            <div class="p-3.5 rounded-2xl bg-stone-50 border border-stone-100">
              <div class="text-base mb-1">🔬</div>
              <div class="text-xs font-bold text-stone-900">Lactoferrin & IgG</div>
              <div class="text-[11px] text-stone-500 mt-0.5">Giữ lại tự nhiên theo TCCS</div>
            </div>
            <div class="p-3.5 rounded-2xl bg-stone-50 border border-stone-100">
              <div class="text-base mb-1">🌿</div>
              <div class="text-xs font-bold text-stone-900">Đạm A2 hữu cơ</div>
              <div class="text-[11px] text-stone-500 mt-0.5">Không hóa chất tổng hợp</div>
            </div>
          </div>

          <div class="pt-2">
            <a href="fresh-milk-difference.html" class="text-xs sm:text-sm font-bold text-[#FF6F78] hover:underline inline-flex items-center gap-1">
              <span>Tìm hiểu chi tiết về quy trình sấy 1 lần</span>
              <span>&rarr;</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- 3 Giai đoạn sản phẩm theo nhãn -->
  <section id="san-pham" class="py-16 lg:py-20 bg-[#FAF7F2] border-t border-b border-stone-200/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-3xl mx-auto mb-12 space-y-3">
        <span class="text-xs font-bold uppercase tracking-widest text-[#FF6F78]">Thông tin theo nhãn sản phẩm</span>
        <h2 class="text-2xl sm:text-3xl lg:text-4xl font-bold text-stone-900">3 giai đoạn sản phẩm Nutura Organic</h2>
        <p class="text-stone-600 text-xs sm:text-sm leading-relaxed">
          Sản phẩm dinh dưỡng công thức sản xuất tại bang Victoria, Úc. Thành phần và hàm lượng dinh dưỡng được ghi rõ trên nhãn và hồ sơ TCCS tương ứng.
        </p>
      </div>

      <!-- Grid 3 sản phẩm -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 lg:gap-8">
        <!-- Stage 1 Card -->
        <div class="bg-white rounded-3xl p-6 border border-stone-200/80 shadow-sm flex flex-col h-full">
          <div class="text-center flex-1 flex flex-col items-center">
            <span class="inline-block px-3 py-1 rounded-full text-[11px] font-bold bg-blue-50 text-blue-700 mb-2">Stage 1</span>
            <h3 class="text-xl font-bold text-stone-900">Nutura Organic Stage 1</h3>
            <p class="text-xs text-stone-500 mb-4">Dành cho trẻ 0 - 6 tháng tuổi • Lon 800g</p>
            
            <a href="product-stage1.html" class="my-2 block group">
              <img src="assets/images/stage1.png" alt="Sữa công thức Nutura Stage 1 800g" class="h-56 object-contain group-hover:scale-105 transition duration-300" loading="lazy">
            </a>

            <ul class="text-xs text-stone-600 space-y-2 text-left w-full my-4 border-t border-b border-stone-100 py-4 leading-relaxed">
              <li class="flex items-start gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-blue-500 mt-1.5 flex-shrink-0"></span>
                <span><strong>Tỷ lệ đạm:</strong> Đạm whey chiếm 60% theo TCCS 01/2026</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-blue-500 mt-1.5 flex-shrink-0"></span>
                <span><strong>Kháng thể tự nhiên:</strong> Có chứa Lactoferrin và IgG</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-blue-500 mt-1.5 flex-shrink-0"></span>
                <span><strong>Nguồn đạm:</strong> Đạm A2 từ sữa bò ăn cỏ tự nhiên</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-blue-500 mt-1.5 flex-shrink-0"></span>
                <span><strong>Chứng nhận:</strong> Logo hữu cơ ACO trên nhãn</span>
              </li>
            </ul>

            <div class="mt-auto w-full pt-2">
              <a href="product-stage1.html" class="block w-full py-2.5 px-4 rounded-full border border-stone-300 hover:border-[#FF6F78] hover:text-[#FF6F78] text-xs font-bold text-stone-700 text-center transition">
                Xem thông tin nhãn & thành phần
              </a>
            </div>
          </div>
        </div>

        <!-- Stage 2 Card -->
        <div class="bg-white rounded-3xl p-6 border border-stone-200/80 shadow-sm flex flex-col h-full">
          <div class="text-center flex-1 flex flex-col items-center">
            <span class="inline-block px-3 py-1 rounded-full text-[11px] font-bold bg-amber-50 text-amber-700 mb-2">Stage 2</span>
            <h3 class="text-xl font-bold text-stone-900">Nutura Organic Stage 2</h3>
            <p class="text-xs text-stone-500 mb-4">Dành cho trẻ 6 - 12 tháng tuổi • Lon 800g</p>
            
            <a href="product-stage2.html" class="my-2 block group">
              <img src="assets/images/stage2.png" alt="Sữa công thức Nutura Stage 2 800g" class="h-56 object-contain group-hover:scale-105 transition duration-300" loading="lazy">
            </a>

            <ul class="text-xs text-stone-600 space-y-2 text-left w-full my-4 border-t border-b border-stone-100 py-4 leading-relaxed">
              <li class="flex items-start gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-amber-500 mt-1.5 flex-shrink-0"></span>
                <span><strong>Tỷ lệ đạm:</strong> Đạm casein chiếm 60% theo TCCS 02/2026</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-amber-500 mt-1.5 flex-shrink-0"></span>
                <span><strong>Axit béo & xơ:</strong> Có bổ sung DHA, ARA, GOS và FOS</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-amber-500 mt-1.5 flex-shrink-0"></span>
                <span><strong>Khoáng chất:</strong> Có bổ sung sắt và kẽm cho bé tập ăn dặm</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-amber-500 mt-1.5 flex-shrink-0"></span>
                <span><strong>Chứng nhận:</strong> Logo hữu cơ ACO trên nhãn</span>
              </li>
            </ul>

            <div class="mt-auto w-full pt-2">
              <a href="product-stage2.html" class="block w-full py-2.5 px-4 rounded-full border border-stone-300 hover:border-[#FF6F78] hover:text-[#FF6F78] text-xs font-bold text-stone-700 text-center transition">
                Xem thông tin nhãn & thành phần
              </a>
            </div>
          </div>
        </div>

        <!-- Stage 3 Card -->
        <div class="bg-white rounded-3xl p-6 border border-stone-200/80 shadow-sm flex flex-col h-full">
          <div class="text-center flex-1 flex flex-col items-center">
            <span class="inline-block px-3 py-1 rounded-full text-[11px] font-bold bg-emerald-50 text-emerald-700 mb-2">Stage 3</span>
            <h3 class="text-xl font-bold text-stone-900">Nutura Organic Stage 3</h3>
            <p class="text-xs text-stone-500 mb-4">Dành cho trẻ 12 - 36 tháng tuổi • Lon 800g</p>
            
            <a href="product-stage3.html" class="my-2 block group">
              <img src="assets/images/stage3.png" alt="Sữa dinh dưỡng Nutura Stage 3 800g" class="h-56 object-contain group-hover:scale-105 transition duration-300" loading="lazy">
            </a>

            <ul class="text-xs text-stone-600 space-y-2 text-left w-full my-4 border-t border-b border-stone-100 py-4 leading-relaxed">
              <li class="flex items-start gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 mt-1.5 flex-shrink-0"></span>
                <span><strong>Vi chất dinh dưỡng:</strong> 16 vitamin và khoáng chất thiết yếu</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 mt-1.5 flex-shrink-0"></span>
                <span><strong>Dưỡng chất bổ sung:</strong> Chứa DHA và ARA theo TCCS 03/2026</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 mt-1.5 flex-shrink-0"></span>
                <span><strong>Prebiotics:</strong> Bổ sung chất xơ hòa tan GOS và FOS</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 mt-1.5 flex-shrink-0"></span>
                <span><strong>Hương vị:</strong> Vị thanh nhẹ tự nhiên, không thêm đường mía</span>
              </li>
            </ul>

            <div class="mt-auto w-full pt-2">
              <a href="product-stage3.html" class="block w-full py-2.5 px-4 rounded-full border border-stone-300 hover:border-[#FF6F78] hover:text-[#FF6F78] text-xs font-bold text-stone-700 text-center transition">
                Xem thông tin nhãn & thành phần
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Triết lý thương hiệu & Nhà máy Victoria (Thay cho section đội ngũ y tế) -->
  <section class="py-16 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
        <div class="lg:col-span-7 space-y-5">
          <span class="text-xs font-bold uppercase tracking-widest text-[#FF6F78]">Nguồn gốc sản xuất</span>
          <h2 class="text-2xl sm:text-3xl lg:text-4xl font-bold text-stone-900 leading-tight">
            Nhà máy Nutura Organic tại bang Victoria, Úc
          </h2>
          <p class="text-stone-700 text-sm sm:text-base leading-relaxed">
            Nutura Organic được nghiên cứu, phát triển và sản xuất bởi Nutura Organic Ltd tại Mulgrave, Victoria, Australia. Nhà máy đặt gần các vùng nông trại chăn thả tự nhiên, giúp tiếp nhận nguồn sữa tươi farmgate trong thời gian ngắn và đưa vào quy trình sấy một lần.
          </p>
          <p class="text-stone-600 text-xs sm:text-sm leading-relaxed">
            Mọi lô sản phẩm đều tuân thủ các quy định an toàn thực phẩm khắt khe của Cơ quan Tiêu chuẩn Thực phẩm Úc và New Zealand (FSANZ) cùng chứng nhận hữu cơ ACO trên từng nhãn lon.
          </p>
          <div class="pt-2">
            <a href="about-us.html" class="text-xs sm:text-sm font-bold text-[#FF6F78] hover:underline inline-flex items-center gap-1">
              <span>Tìm hiểu câu chuyện Nutura và nhà máy Victoria</span>
              <span>&rarr;</span>
            </a>
          </div>
        </div>

        <div class="lg:col-span-5">
          <div class="rounded-3xl overflow-hidden shadow-lg border-4 border-stone-100 bg-[#FAF7F2] p-6 space-y-4">
            <div class="text-xs font-bold text-stone-900 uppercase tracking-wider text-rose-500">Thông tin nhà máy & chứng nhận</div>
            <div class="space-y-3 text-xs text-stone-600">
              <div class="p-3 bg-white rounded-2xl border border-stone-100">
                <div class="font-bold text-stone-800">Nhà sản xuất</div>
                <div class="text-stone-500 mt-0.5">Nutura Organic Ltd, Mulgrave VIC, Australia</div>
              </div>
              <div class="p-3 bg-white rounded-2xl border border-stone-100">
                <div class="font-bold text-stone-800">Chứng nhận hữu cơ</div>
                <div class="text-stone-500 mt-0.5">Australian Certified Organic (ACO)</div>
              </div>
              <div class="p-3 bg-white rounded-2xl border border-stone-100">
                <div class="font-bold text-stone-800">Xuất xứ nguồn sữa</div>
                <div class="text-stone-500 mt-0.5">100% sữa tươi farmgate từ đàn bò ăn cỏ Úc</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Góc cha mẹ: 3 bài viết nổi bật -->
  <section class="py-16 bg-[#FAF7F2] border-t border-stone-200/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex flex-col sm:flex-row sm:items-end justify-between mb-10 gap-3">
        <div>
          <span class="text-xs font-bold uppercase tracking-widest text-[#FF6F78]">Cẩm nang nuôi con</span>
          <h2 class="text-2xl sm:text-3xl font-bold text-stone-900 mt-1">Bài viết nổi bật tại Góc cha mẹ</h2>
        </div>
        <a href="village.html" class="text-xs sm:text-sm font-bold text-[#FF6F78] hover:underline inline-flex items-center gap-1">
          <span>Xem tất cả bài viết</span>
          <span>&rarr;</span>
        </a>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <!-- Bài 1: Đặt tên cho bé -->
        <article class="bg-white rounded-3xl overflow-hidden border border-stone-200/80 shadow-sm flex flex-col">
          <a href="village.html#article-1" class="block h-44 overflow-hidden bg-stone-100">
            <img src="assets/images/blog-baby-names.jpg" alt="Đặt tên cho bé" class="w-full h-full object-cover hover:scale-105 transition duration-300" loading="lazy">
          </a>
          <div class="p-5 flex-1 flex flex-col space-y-2">
            <div class="text-[11px] font-bold text-[#FF6F78]">Góc cha mẹ</div>
            <h3 class="text-sm sm:text-base font-bold text-stone-900 leading-snug">
              <a href="village.html#article-1" class="hover:text-[#FF6F78] transition">Mẹo và gợi ý khi đặt tên cho thiên thần nhỏ sắp chào đời</a>
            </h3>
            <p class="text-xs text-stone-600 line-clamp-3 leading-relaxed">
              Khoảnh khắc biết mình mang thai luôn tràn ngập cảm xúc diệu kỳ. Cùng tham khảo những gợi ý ý nghĩa khi chọn tên cho bé yêu.
            </p>
            <div class="mt-auto pt-2">
              <a href="village.html#article-1" class="text-xs font-bold text-[#FF6F78] hover:underline">&rarr; Đọc bài viết</a>
            </div>
          </div>
        </article>

        <!-- Bài 2: Ngày đầu đi học -->
        <article class="bg-white rounded-3xl overflow-hidden border border-stone-200/80 shadow-sm flex flex-col">
          <a href="village.html#article-2" class="block h-44 overflow-hidden bg-stone-100">
            <img src="assets/images/blog-school.jpg" alt="Chuẩn bị tâm lý cho con vào ngày đầu đi học" class="w-full h-full object-cover hover:scale-105 transition duration-300" loading="lazy">
          </a>
          <div class="p-5 flex-1 flex flex-col space-y-2">
            <div class="text-[11px] font-bold text-[#FF6F78]">Tâm lý thiếu nhi • Tác giả: Dr. Michael Carr-Gregg</div>
            <h3 class="text-sm sm:text-base font-bold text-stone-900 leading-snug">
              <a href="village.html#article-2" class="hover:text-[#FF6F78] transition">Chuẩn bị hành trang tâm lý cho con vào ngày đầu đến trường</a>
            </h3>
            <p class="text-xs text-stone-600 line-clamp-3 leading-relaxed">
              Bước qua cánh cổng trường học là bước ngoặt lớn với con. Những bước chuẩn bị cảm xúc giúp con tự tin và vững vàng hơn.
            </p>
            <div class="mt-auto pt-2">
              <a href="village.html#article-2" class="text-xs font-bold text-[#FF6F78] hover:underline">&rarr; Đọc bài viết</a>
            </div>
          </div>
        </article>

        <!-- Bài 3: Sắt cho bé -->
        <article class="bg-white rounded-3xl overflow-hidden border border-stone-200/80 shadow-sm flex flex-col">
          <a href="village.html#article-6" class="block h-44 overflow-hidden bg-stone-100">
            <img src="assets/images/blog-iron.jpg" alt="Bổ sung sắt cho bé" class="w-full h-full object-cover hover:scale-105 transition duration-300" loading="lazy">
          </a>
          <div class="p-5 flex-1 flex flex-col space-y-2">
            <div class="text-[11px] font-bold text-[#FF6F78]">Dinh dưỡng trẻ nhỏ • Tác giả: Miriam Raleigh</div>
            <h3 class="text-sm sm:text-base font-bold text-stone-900 leading-snug">
              <a href="village.html#article-6" class="hover:text-[#FF6F78] transition">Bé nhà bạn đã nạp đủ lượng sắt cần thiết mỗi ngày?</a>
            </h3>
            <p class="text-xs text-stone-600 line-clamp-3 leading-relaxed">
              Sắt là vi chất dinh dưỡng thiết yếu cho trẻ nhỏ. Hướng dẫn nhận biết dấu hiệu và bổ sung thực phẩm giàu sắt đúng cách cho bé.
            </p>
            <div class="mt-auto pt-2">
              <a href="village.html#article-6" class="text-xs font-bold text-[#FF6F78] hover:underline">&rarr; Đọc bài viết</a>
            </div>
          </div>
        </article>
      </div>
    </div>
  </section>

  <!-- 4 Tiêu chuẩn chất lượng minh bạch -->
  <section class="py-12 bg-white border-t border-stone-200/80">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-8">
        <h3 class="text-lg font-bold text-stone-900">Tiêu chuẩn kiểm nghiệm chất lượng Nutura Organic</h3>
      </div>
      <div class="grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
        <div class="flex flex-col items-center">
          <img src="assets/images/icon-aus-made.png" alt="100% sản xuất tại Úc" class="h-12 w-auto mb-2 object-contain" loading="lazy">
          <h4 class="text-xs font-bold text-stone-900">100% sản xuất tại Úc</h4>
          <p class="text-[11px] text-stone-500">Australian Made & Owned</p>
        </div>
        <div class="flex flex-col items-center">
          <img src="assets/images/icon-cert-organic.png" alt="Chứng nhận hữu cơ ACO" class="h-12 w-auto mb-2 object-contain" loading="lazy">
          <h4 class="text-xs font-bold text-stone-900">Chứng nhận hữu cơ ACO</h4>
          <p class="text-[11px] text-stone-500">Theo nhãn Stage 1–3</p>
        </div>
        <div class="flex flex-col items-center">
          <img src="assets/images/icon-no-artificial-flav.png" alt="Không hương vị nhân tạo" class="h-12 w-auto mb-2 object-contain" loading="lazy">
          <h4 class="text-xs font-bold text-stone-900">Không hương vị nhân tạo</h4>
          <p class="text-[11px] text-stone-500">Vị thanh thuần từ sữa tươi</p>
        </div>
        <div class="flex flex-col items-center">
          <img src="assets/images/icon-no-gmo.png" alt="Không biến đổi gen" class="h-12 w-auto mb-2 object-contain" loading="lazy">
          <h4 class="text-xs font-bold text-stone-900">Không biến đổi gen</h4>
          <p class="text-[11px] text-stone-500">Non-GMO ingredients</p>
        </div>
      </div>
    </div>
  </section>

  </main>
"""
    content += render_footer()
    return content

print("pages_home.py ready")
