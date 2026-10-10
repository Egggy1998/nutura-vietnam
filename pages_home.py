# -*- coding: utf-8 -*-
"""
Trang Chủ - index.html
Clone đầy đủ toàn bộ các section của Nutura Organic sang tiếng Việt
"""

from build_site import render_head, render_topbar, render_navbar, render_footer

def build_home():
    content = render_head(
        title="Sữa Hữu Cơ Úc Chuẩn Farmgate | Nuôi Dưỡng Tự Nhiên, Đồng Hành Cùng Ngôi Làng Của Bạn",
        description="Nutura Organic - Dòng sữa dinh dưỡng và sữa công thức hữu cơ cao cấp sản xuất 100% tại Úc từ sữa tươi nguyên liệu farmgate. Chứng nhận kép ACO & NASAA Organic.",
        canonical_url="index.html"
    )
    content += render_topbar()
    content += render_navbar(active_page="home")

    content += """
  <!-- MAIN CONTENT CONTAINER -->
  <main id="main-content">
  <!-- HERO BANNER SECTION -->
  <section class="relative bg-[#FAF7F2] overflow-hidden pt-8 pb-16 lg:py-24">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        <!-- Text Content -->
        <div class="lg:col-span-7 space-y-6 text-center lg:text-left">
          <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-rose-100 text-[#FF6F78] text-xs font-bold uppercase tracking-wider">
            <span class="w-2 h-2 rounded-full bg-[#FF6F78]"></span>
            Chứng Nhận Hữu Cơ Kép ACO & NASAA • 100% Sản Xuất Tại Úc
          </div>

          <h1 class="text-3xl sm:text-4xl lg:text-5xl xl:text-6xl font-bold text-stone-900 tracking-tight leading-tight">
            Sữa Công Thức & Dinh Dưỡng Hữu Cơ Nuôi Dưỡng Từ Đồng Cỏ Úc
          </h1>

          <p class="text-base sm:text-lg text-stone-600 max-w-2xl mx-auto lg:mx-0 leading-relaxed">
            Công thức chế biến độc quyền từ <strong>sữa tươi nguyên liệu farmgate</strong> giữ trọn vẹn dưỡng chất sinh học tự nhiên quý giá. Được tạo nên bởi các chuyên gia dinh dưỡng, nông dân và nhà khoa học để hỗ trợ ngôi làng nuôi con của bạn.
          </p>

          <div class="flex flex-col sm:flex-row items-center justify-center lg:justify-start gap-4 pt-2">
            <a href="shop.html" class="btn-nutura-primary w-full sm:w-auto text-base py-3.5 px-8 shadow-lg shadow-[#FF6F78]/30">
              <span>Mua Sắm Ngay</span>
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/>
              </svg>
            </a>
            <a href="breast-is-best.html" class="btn-nutura-outline w-full sm:w-auto text-sm py-3 px-6">
              <span>Thông Tin Quan Trọng Về Sữa Mẹ</span>
            </a>
          </div>

          <!-- Trust Badges Under Hero -->
          <div class="pt-6 border-t border-stone-200/80 grid grid-cols-2 sm:grid-cols-4 gap-4 text-center lg:text-left">
            <div>
              <div class="text-xs font-bold text-stone-900">100% Sữa Bò Ăn Cỏ</div>
              <div class="text-[11px] text-stone-500">Đạm tươi A2 tự nhiên</div>
            </div>
            <div>
              <div class="text-xs font-bold text-stone-900">Chuẩn Hữu Cơ Kép</div>
              <div class="text-[11px] text-stone-500">ACO & NASAA Certified</div>
            </div>
            <div>
              <div class="text-xs font-bold text-stone-900">Không Biến Đổi Gen</div>
              <div class="text-[11px] text-stone-500">Non-GMO 100% sạch</div>
            </div>
            <div>
              <div class="text-xs font-bold text-stone-900">Bình Chọn Số 1</div>
              <div class="text-[11px] text-stone-500">ProductReview 2022-2023</div>
            </div>
          </div>
        </div>

        <!-- Hero Image -->
        <div class="lg:col-span-5 relative">
          <div class="relative mx-auto max-w-md lg:max-w-none">
            <div class="rounded-3xl overflow-hidden shadow-2xl border-4 border-white bg-white">
              <img src="assets/images/hero-dad-bub.jpg" alt="Khoảnh khắc cha và con cùng Nutura Organic" class="w-full h-auto object-cover transform hover:scale-102 transition duration-500">
            </div>
            <!-- Floating Badge -->
            <div class="absolute -bottom-6 -left-6 bg-white p-4 rounded-2xl shadow-xl border border-stone-100 flex items-center gap-3">
              <img src="assets/images/icon-cert-organic.png" alt="Chứng nhận hữu cơ" class="w-12 h-12 object-contain">
              <div>
                <div class="text-xs font-bold text-stone-900">Chứng Nhận Kép Hữu Cơ</div>
                <div class="text-[11px] text-emerald-600 font-semibold">ACO & NASAA Australia</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- WAVE DIVIDER -->
  <div class="wave-divider bg-[#FAF7F2]">
    <img src="assets/images/wave-white.svg" alt="" class="w-full">
  </div>

  <!-- COLLAB EXCLUSIVE SECTION: NUTURA x MOTHERDAILY -->
  <section class="py-16 lg:py-20 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="bg-gradient-to-br from-rose-50 via-amber-50/40 to-rose-100/60 rounded-3xl p-8 sm:p-12 border border-rose-100 shadow-sm">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
          <div class="lg:col-span-7 space-y-4">
            <span class="inline-block px-3 py-1 rounded-full bg-[#FF6F78] text-white text-xs font-bold uppercase tracking-wider">
              Ưu Đãi Hợp Tác Độc Quyền
            </span>
            <h2 class="text-2xl sm:text-3xl lg:text-4xl font-bold text-stone-900">
              Sự Hợp Tác Đầy Hứng Khởi: Nutura x MotherDaily
            </h2>
            <p class="text-stone-700 text-sm sm:text-base leading-relaxed">
              Nuôi dưỡng cả bạn và thiên thần nhỏ với sự chăm sóc trọn vẹn nhất từ bộ đôi đặc quyền <strong>Nutura x MotherDaily</strong>. Trong thời gian giới hạn, sở hữu ngay cặp đôi hoàn hảo cho mẹ và bé và tận hưởng <strong>ưu đãi giảm giá sâu 40%</strong> khi mua trọn bộ cả Nutura và MotherDaily!
            </p>
            <div class="pt-2 flex flex-wrap gap-4 items-center">
              <a href="product-motherdaily.html" class="btn-nutura-primary text-sm py-3 px-6 shadow-md">
                Khám Phá Bộ Đôi Giảm 40%
              </a>
              <span class="text-xs text-stone-500 italic">*Áp dụng có hạn cho phụ huynh tại Việt Nam & Úc</span>
            </div>
          </div>
          <div class="lg:col-span-5 text-center">
            <img src="assets/images/motherdaily-pack.png" alt="Bộ sản phẩm Nutura x MotherDaily" class="max-h-80 mx-auto object-contain hover:scale-105 transition duration-300">
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- FRESH MILK DIFFERENCE SECTION -->
  <section class="py-16 lg:py-24 bg-[#FAF7F2]">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        <!-- Visual Column -->
        <div class="lg:col-span-5 order-2 lg:order-1 text-center">
          <div class="relative inline-block">
            <img src="assets/images/fresh-milk-circle.jpg" alt="Sự khác biệt của sữa tươi Farmgate" class="rounded-full shadow-2xl w-72 sm:w-88 h-72 sm:h-88 object-cover mx-auto border-8 border-white">
            <div class="absolute -bottom-4 right-0 bg-white p-3 rounded-2xl shadow-lg border border-stone-100 flex items-center gap-2">
              <span class="text-2xl font-bold text-[#FF6F78]">1</span>
              <span class="text-xs text-left font-bold text-stone-800 leading-tight">Lần Sấy Duy Nhất<br><span class="text-stone-500 font-normal">Wet Blending Tươi</span></span>
            </div>
          </div>
        </div>

        <!-- Copy Column -->
        <div class="lg:col-span-7 order-1 lg:order-2 space-y-6">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-rose-100 text-[#FF6F78] text-xs font-bold uppercase tracking-wider">
            Công Nghệ Farmgate Tươi Mới
          </div>
          <h2 class="text-3xl sm:text-4xl font-bold text-stone-900 leading-tight">
            Sự Khác Biệt Của Sữa Tươi Nutura: Giữ Trọn Dưỡng Chất Sinh Học
          </h2>
          <p class="text-stone-700 leading-relaxed">
            Người xưa thường nói: <em>"Cần cả một ngôi làng để nuôi dạy một đứa trẻ"</em>. Ngôi làng gồm các chuyên gia tận tâm của Nutura đã cùng hội tụ để sáng tạo nên quy trình chế biến độc bản từ <strong>sữa tươi nguyên liệu tại cổng trang trại (farmgate milk)</strong>.
          </p>
          <p class="text-stone-600 text-sm leading-relaxed">
            Khác với các dòng sữa công thức thông thường sử dụng bột sữa hoàn nguyên phải qua 2 lần gia nhiệt sấy khô, Nutura sử dụng nền tảng <strong>sữa tươi nguyên chất 1 lần sấy</strong>. Quy trình này bảo toàn tối đa các protein hoạt tính sinh học quý giá bao gồm <strong>Lactoferrin</strong> và <strong>Kháng thể IgG</strong>, kết hợp cùng Kẽm, Sắt và Vitamin C tạo nên lá chắn miễn dịch tự nhiên giúp bé lớn khôn khỏe mạnh.
          </p>

          <div class="pt-2">
            <img src="assets/images/fresh-milk-icons.png" alt="Biểu tượng lợi ích sữa tươi Nutura" class="max-w-md w-full h-auto">
          </div>

          <div>
            <a href="fresh-milk-difference.html" class="btn-nutura-primary text-sm py-3 px-6">
              Tìm Hiểu Sự Khác Biệt Sữa Tươi &rarr;
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- CERTIFIED ORGANIC PEACE OF MIND -->
  <section class="py-16 lg:py-24 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        <!-- Text Column -->
        <div class="lg:col-span-7 space-y-6">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-100 text-emerald-800 text-xs font-bold uppercase tracking-wider">
            Thuần Khiết Từ Tự Nhiên
          </div>
          <h2 class="text-3xl sm:text-4xl font-bold text-stone-900 leading-tight">
            An Tâm Tuyệt Đối Với Chứng Nhận Hữu Cơ Kép
          </h2>
          <h3 class="text-lg font-semibold text-[#FF6F78]">
            Phương pháp tiếp cận toàn diện cho dinh dưỡng trẻ sơ sinh & trẻ nhỏ.
          </h3>
          <p class="text-stone-700 text-sm sm:text-base leading-relaxed">
            Các sản phẩm hữu cơ có chứng nhận của chúng tôi mang lại nguồn dưỡng chất vượt trội, toàn diện, nuôi nấng các gia đình bằng sự thanh lành của mẹ thiên nhiên. Sản phẩm Nutura tự hào đạt chứng nhận hữu cơ độc lập từ cả hai tổ chức kiểm định khắt khe nhất nước Úc: <strong>ACO (Australian Certified Organic)</strong> và <strong>NASAA Organic</strong>.
          </p>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-2">
            <div class="flex items-start gap-3 p-3 bg-stone-50 rounded-2xl border border-stone-100">
              <div class="w-6 h-6 rounded-full bg-emerald-500 text-white flex items-center justify-center font-bold text-xs flex-shrink-0 mt-0.5">✓</div>
              <div class="text-xs text-stone-700"><strong>Không hóa chất độc hại:</strong> Không thuốc trừ sâu tổng hợp hay phân bón hóa học.</div>
            </div>
            <div class="flex items-start gap-3 p-3 bg-stone-50 rounded-2xl border border-stone-100">
              <div class="w-6 h-6 rounded-full bg-emerald-500 text-white flex items-center justify-center font-bold text-xs flex-shrink-0 mt-0.5">✓</div>
              <div class="text-xs text-stone-700"><strong>Không hormone tăng trưởng:</strong> Bò được chăn thả tự nhiên, không kháng sinh phòng bệnh.</div>
            </div>
            <div class="flex items-start gap-3 p-3 bg-stone-50 rounded-2xl border border-stone-100">
              <div class="w-6 h-6 rounded-full bg-emerald-500 text-white flex items-center justify-center font-bold text-xs flex-shrink-0 mt-0.5">✓</div>
              <div class="text-xs text-stone-700"><strong>Không biến đổi gen (Non-GMO):</strong> Toàn bộ chuỗi cung ứng được kiểm toán nghiêm ngặt.</div>
            </div>
            <div class="flex items-start gap-3 p-3 bg-stone-50 rounded-2xl border border-stone-100">
              <div class="w-6 h-6 rounded-full bg-emerald-500 text-white flex items-center justify-center font-bold text-xs flex-shrink-0 mt-0.5">✓</div>
              <div class="text-xs text-stone-700"><strong>Không hương vị & chất tạo ngọt nhân tạo:</strong> 100% vị thanh nhạt tự nhiên từ đường sữa lactose.</div>
            </div>
          </div>
          <div>
            <a href="certified-organic.html" class="btn-nutura-outline text-sm py-3 px-6">
              Xem Tiêu Chuẩn Chứng Nhận Hữu Cơ
            </a>
          </div>
        </div>

        <!-- Image Column -->
        <div class="lg:col-span-5 text-center">
          <div class="relative inline-block">
            <img src="assets/images/organic-circle.jpg" alt="Chứng nhận hữu cơ Nutura" class="rounded-full shadow-2xl w-72 sm:w-88 h-72 sm:h-88 object-cover mx-auto border-8 border-white">
            <div class="mt-6">
              <img src="assets/images/cert-logos.png" alt="ACO & NASAA Logos" class="max-w-xs mx-auto h-auto">
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- MEET THE NUTURA FAMILY (SẢN PHẨM CHỦ LỰC) -->
  <section class="py-16 lg:py-24 bg-[#FAF7F2]">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-3xl mx-auto mb-16 space-y-3">
        <span class="text-xs font-bold uppercase tracking-widest text-[#FF6F78]">Được Phụ Huynh Úc Tin Yêu</span>
        <h2 class="text-3xl sm:text-4xl font-bold text-stone-900">Gia Đình Sản Phẩm Nutura</h2>
        <p class="text-stone-600 text-sm sm:text-base leading-relaxed">
          Dòng sữa công thức và sữa dinh dưỡng sản xuất trực tiếp tại bang Victoria, Úc - Nổi danh với tiêu chuẩn an toàn sản xuất tương đương cấp dược phẩm. Công thức hữu cơ cải tiến từ sữa tươi bò ăn cỏ tự nhiên.
        </p>
      </div>

      <!-- 3 Primary Formula Cards -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <!-- Stage 1 Card -->
        <div class="nutura-card flex flex-col h-full bg-white">
          <div class="p-6 text-center flex-1 flex flex-col items-center">
            <span class="stage-badge stage-badge-s1 mb-2">Sữa Cho Trẻ Sơ Sinh</span>
            <h3 class="text-2xl font-bold text-stone-900">Giai Đoạn 1</h3>
            <p class="text-xs text-stone-500 font-semibold mb-4">0 - 6 Tháng Tuổi • 800g</p>
            
            <a href="product-stage1.html" class="my-4 block group">
              <img src="assets/images/stage1.png" alt="Sữa Nutura Stage 1" class="h-64 object-contain group-hover:scale-105 transition duration-300">
            </a>

            <ul class="text-xs text-stone-600 space-y-2 text-left w-full my-4 border-t border-b border-stone-100 py-4">
              <li class="flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-blue-500"></span>
                <strong>Đạm Whey chiếm ưu thế:</strong> Dễ tiêu hóa như sữa mẹ
              </li>
              <li class="flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-blue-500"></span>
                Thành phần 100% không biến đổi gen (Non-GMO)
              </li>
              <li class="flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-blue-500"></span>
                Sản xuất & sở hữu 100% tại Úc
              </li>
              <li class="flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-blue-500"></span>
                Chứng nhận hữu cơ kép ACO & NASAA
              </li>
              <li class="flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-blue-500"></span>
                Làm từ sữa bò ăn cỏ tự nhiên đạm A2
              </li>
            </ul>

            <div class="mt-auto w-full pt-2">
              <div class="flex items-baseline justify-between mb-4">
                <span class="text-xl font-bold text-[#FF6F78]">780.000 đ</span>
                <span class="text-xs text-stone-400 font-medium">$46.00 AUD</span>
              </div>
              <div class="grid grid-cols-2 gap-2">
                <a href="product-stage1.html" class="py-2.5 px-3 rounded-full border border-stone-300 text-stone-700 text-xs font-bold hover:bg-stone-50 text-center transition">
                  Chi Tiết
                </a>
                <button class="add-to-cart-btn py-2.5 px-3 rounded-full bg-[#FF6F78] hover:bg-[#E65A63] text-white text-xs font-bold transition shadow-md shadow-[#FF6F78]/20 flex items-center justify-center gap-1" data-product-id="stage-1">
                  <span>+ Giỏ Hàng</span>
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- Stage 2 Card -->
        <div class="nutura-card flex flex-col h-full bg-white">
          <div class="p-6 text-center flex-1 flex flex-col items-center">
            <span class="stage-badge stage-badge-s2 mb-2">Sữa Tiếp Theo (Ăn Dặm)</span>
            <h3 class="text-2xl font-bold text-stone-900">Giai Đoạn 2</h3>
            <p class="text-xs text-stone-500 font-semibold mb-4">6 - 12 Tháng Tuổi • 800g</p>
            
            <a href="product-stage2.html" class="my-4 block group">
              <img src="assets/images/stage2.png" alt="Sữa Nutura Stage 2" class="h-64 object-contain group-hover:scale-105 transition duration-300">
            </a>

            <ul class="text-xs text-stone-600 space-y-2 text-left w-full my-4 border-t border-b border-stone-100 py-4">
              <li class="flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-amber-500"></span>
                <strong>Đạm Casein cân bằng:</strong> No lâu, phát triển thể chất
              </li>
              <li class="flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-amber-500"></span>
                Tăng cường Sắt, Kẽm cho giai đoạn tập ăn dặm
              </li>
              <li class="flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-amber-500"></span>
                Bổ sung DHA & ARA từ dầu cá tự nhiên
              </li>
              <li class="flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-amber-500"></span>
                Chứng nhận hữu cơ kép ACO & NASAA
              </li>
              <li class="flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-amber-500"></span>
                Làm từ sữa bò ăn cỏ tự nhiên đạm A2
              </li>
            </ul>

            <div class="mt-auto w-full pt-2">
              <div class="flex items-baseline justify-between mb-4">
                <span class="text-xl font-bold text-[#FF6F78]">780.000 đ</span>
                <span class="text-xs text-stone-400 font-medium">$46.00 AUD</span>
              </div>
              <div class="grid grid-cols-2 gap-2">
                <a href="product-stage2.html" class="py-2.5 px-3 rounded-full border border-stone-300 text-stone-700 text-xs font-bold hover:bg-stone-50 text-center transition">
                  Chi Tiết
                </a>
                <button class="add-to-cart-btn py-2.5 px-3 rounded-full bg-[#FF6F78] hover:bg-[#E65A63] text-white text-xs font-bold transition shadow-md shadow-[#FF6F78]/20 flex items-center justify-center gap-1" data-product-id="stage-2">
                  <span>+ Giỏ Hàng</span>
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- Stage 3 Card -->
        <div class="nutura-card flex flex-col h-full bg-white">
          <div class="p-6 text-center flex-1 flex flex-col items-center">
            <span class="stage-badge stage-badge-s3 mb-2">Sữa Cho Trẻ Tập Đi</span>
            <h3 class="text-2xl font-bold text-stone-900">Giai Đoạn 3</h3>
            <p class="text-xs text-stone-500 font-semibold mb-4">12 - 36 Tháng Tuổi • 800g</p>
            
            <a href="product-stage3.html" class="my-4 block group">
              <img src="assets/images/stage3.png" alt="Sữa Nutura Stage 3" class="h-64 object-contain group-hover:scale-105 transition duration-300">
            </a>

            <ul class="text-xs text-stone-600 space-y-2 text-left w-full my-4 border-t border-b border-stone-100 py-4">
              <li class="flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
                <strong>16 Vitamin & Khoáng chất thiết yếu</strong>
              </li>
              <li class="flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
                Bổ sung Prebiotics FOS & GOS hỗ trợ hệ vi sinh
              </li>
              <li class="flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
                Chứa DHA & ARA phát triển trí não vượt trội
              </li>
              <li class="flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
                Chứng nhận hữu cơ kép ACO & NASAA
              </li>
              <li class="flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
                Vị ngọt thanh tự nhiên, bé hợp tác ngay
              </li>
            </ul>

            <div class="mt-auto w-full pt-2">
              <div class="flex items-baseline justify-between mb-4">
                <span class="text-xl font-bold text-[#FF6F78]">780.000 đ</span>
                <span class="text-xs text-stone-400 font-medium">$46.00 AUD</span>
              </div>
              <div class="grid grid-cols-2 gap-2">
                <a href="product-stage3.html" class="py-2.5 px-3 rounded-full border border-stone-300 text-stone-700 text-xs font-bold hover:bg-stone-50 text-center transition">
                  Chi Tiết
                </a>
                <button class="add-to-cart-btn py-2.5 px-3 rounded-full bg-[#FF6F78] hover:bg-[#E65A63] text-white text-xs font-bold transition shadow-md shadow-[#FF6F78]/20 flex items-center justify-center gap-1" data-product-id="stage-3">
                  <span>+ Giỏ Hàng</span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Stage 4 Banner Link -->
      <div class="mt-8 bg-white p-6 rounded-2xl border border-stone-200/80 flex flex-col sm:flex-row items-center justify-between gap-4">
        <div class="flex items-center gap-4">
          <img src="assets/images/stage4.jpg" alt="Nutura Stage 4" class="w-16 h-16 object-contain rounded-xl bg-stone-50">
          <div>
            <h4 class="font-bold text-stone-900 text-base">Bé đã trên 3 tuổi? Khám phá Nutura Stage 4 Junior Milk Drink</h4>
            <p class="text-xs text-stone-500">Dinh dưỡng hoàn hảo cho giai đoạn mầm non và chuẩn bị bước vào tiểu học. Giá chỉ 560.000 đ ($33 AUD).</p>
          </div>
        </div>
        <a href="product-stage4.html" class="btn-nutura-outline text-xs py-2.5 px-5 flex-shrink-0">
          Xem Stage 4 &rarr;
        </a>
      </div>
    </div>
  </section>

  <!-- AWARD WINNING BANNER -->
  <section class="py-12 bg-white border-t border-b border-stone-100">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex flex-col md:flex-row items-center justify-between gap-8 text-center md:text-left">
        <div class="flex-shrink-0 mx-auto md:mx-0">
          <img src="assets/images/product-review.png" alt="Product Review Award Winner 2022 & 2023" class="h-28 sm:h-32 w-auto">
        </div>
        <div class="space-y-2 flex-1">
          <div class="inline-block px-3 py-1 bg-amber-100 text-amber-900 rounded-full text-xs font-bold uppercase tracking-wider">
            Giải Thưởng Danh Giá Nhất Nước Úc
          </div>
          <h2 class="text-2xl sm:text-3xl font-bold text-stone-900">
            Được Các Bậc Cha Mẹ Úc Bình Chọn Số 1
          </h2>
          <p class="text-sm text-stone-600 leading-relaxed max-w-3xl">
            *Người chiến thắng Giải thưởng <strong>Product Review Awards 2022 & 2023</strong> tại hạng mục Sữa Dinh Dưỡng Cho Trẻ Tập Đi (Toddler Milk Drink) -  Nền tảng đánh giá sản phẩm tiêu dùng số 1 nước Úc. Hàng ngàn đánh giá 5 sao từ phụ huynh trên khắp các bang Victoria, New South Wales, Queensland...
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- THE GOOD SMOOTHIE MILK POWDER -->
  <section class="py-16 lg:py-24 bg-gradient-to-b from-[#FAF7F2] to-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-3xl mx-auto mb-16 space-y-3">
        <span class="inline-block px-3.5 py-1 rounded-full bg-purple-100 text-purple-700 text-xs font-bold uppercase tracking-wider">
          Đột Phá Mới Nhất
        </span>
        <h2 class="text-3xl sm:text-4xl font-bold text-stone-900">
          Sữa Bột The Good Smoothie: Dinh Dưỡng Chuyên Sâu
        </h2>
        <p class="text-stone-600 text-sm sm:text-base leading-relaxed">
          Dòng sữa bột Smoothie của Nutura được sản xuất từ 100% sữa tươi bò ăn cỏ tự nhiên của Úc, bổ sung các vi chất dinh dưỡng hướng đích đóng vai trò then chốt cho: <strong>Trí Não</strong>, <strong>Thư Giãn Giấc Ngủ</strong>, hoặc <strong>Đề Kháng Toàn Diện</strong>. Dễ dàng pha cùng nước ấm hoặc xay cùng hoa quả tươi thành ly sinh tố thơm ngon bổ dưỡng!
        </p>
      </div>

      <!-- 3 Smoothie Products -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <!-- Cognitive -->
        <div class="nutura-card bg-white p-6 flex flex-col text-center">
          <span class="stage-badge stage-badge-smoothie mb-3 self-center">Phát Triển Trí Não</span>
          <h3 class="text-2xl font-bold text-stone-900 mb-1">Cognitive</h3>
          <p class="text-xs text-stone-500 mb-4">Tập trung, ghi nhớ và tư duy sáng tạo</p>
          
          <a href="product-smoothie.html" class="my-4 block group">
            <img src="assets/images/smoothie-cognitive.png" alt="Smoothie Cognitive" class="h-60 mx-auto object-contain group-hover:scale-105 transition duration-300">
          </a>

          <div class="bg-purple-50/60 p-4 rounded-2xl text-left my-4 text-xs space-y-2">
            <div class="font-bold text-purple-900">Thành phần vi chất vàng:</div>
            <div class="flex items-center gap-2 text-stone-700"><span>🧠</span> Phospholipids màng tế bào thần kinh</div>
            <div class="flex items-center gap-2 text-stone-700"><span>⚡</span> Tyrosine kích thích phản xạ nhạy bén</div>
            <div class="flex items-center gap-2 text-stone-700"><span>🐟</span> DHA tinh khiết cho mắt sáng thông minh</div>
            <div class="flex items-center gap-2 text-stone-700"><span>✨</span> Vitamin nhóm B (B1, B6, B12)</div>
          </div>

          <div class="mt-auto pt-2">
            <div class="flex items-baseline justify-between mb-4">
              <div>
                <span class="text-xl font-bold text-[#FF6F78]">410.000 đ</span>
                <span class="text-xs text-stone-400 line-through ml-1">590.000 đ</span>
              </div>
              <span class="text-xs text-stone-400 font-medium">$17.00 AUD</span>
            </div>
            <div class="grid grid-cols-2 gap-2">
              <a href="product-smoothie.html" class="py-2.5 px-3 rounded-full border border-stone-300 text-stone-700 text-xs font-bold hover:bg-stone-50 text-center transition">
                Chi Tiết
              </a>
              <button class="add-to-cart-btn py-2.5 px-3 rounded-full bg-[#FF6F78] hover:bg-[#E65A63] text-white text-xs font-bold transition shadow-md shadow-[#FF6F78]/20 flex items-center justify-center gap-1" data-product-id="smoothie-cognitive">
                <span>+ Giỏ Hàng</span>
              </button>
            </div>
          </div>
        </div>

        <!-- Calm -->
        <div class="nutura-card bg-white p-6 flex flex-col text-center">
          <span class="stage-badge bg-amber-50 text-amber-700 mb-3 self-center">Thư Giãn & Giấc Ngủ</span>
          <h3 class="text-2xl font-bold text-stone-900 mb-1">Calm</h3>
          <p class="text-xs text-stone-500 mb-4">Vỗ về cảm xúc, ngủ sâu giấc tự nhiên</p>
          
          <a href="product-smoothie.html" class="my-4 block group">
            <img src="assets/images/smoothie-calm.png" alt="Smoothie Calm" class="h-60 mx-auto object-contain group-hover:scale-105 transition duration-300">
          </a>

          <div class="bg-amber-50/60 p-4 rounded-2xl text-left my-4 text-xs space-y-2">
            <div class="font-bold text-amber-900">Thành phần thảo mộc êm dịu:</div>
            <div class="flex items-center gap-2 text-stone-700"><span>🌼</span> Hoa cúc La Mã (Chamomile) thư giãn</div>
            <div class="flex items-center gap-2 text-stone-700"><span>🌾</span> Yến mạch Avena Sativa xoa dịu tinh thần</div>
            <div class="flex items-center gap-2 text-stone-700"><span>🌙</span> Magie hữu cơ hỗ trợ giãn cơ sâu</div>
            <div class="flex items-center gap-2 text-stone-700"><span>🍌</span> Chuối tự nhiên giàu Kali</div>
          </div>

          <div class="mt-auto pt-2">
            <div class="flex items-baseline justify-between mb-4">
              <div>
                <span class="text-xl font-bold text-[#FF6F78]">410.000 đ</span>
                <span class="text-xs text-stone-400 line-through ml-1">590.000 đ</span>
              </div>
              <span class="text-xs text-stone-400 font-medium">$17.00 AUD</span>
            </div>
            <div class="grid grid-cols-2 gap-2">
              <a href="product-smoothie.html" class="py-2.5 px-3 rounded-full border border-stone-300 text-stone-700 text-xs font-bold hover:bg-stone-50 text-center transition">
                Chi Tiết
              </a>
              <button class="add-to-cart-btn py-2.5 px-3 rounded-full bg-[#FF6F78] hover:bg-[#E65A63] text-white text-xs font-bold transition shadow-md shadow-[#FF6F78]/20 flex items-center justify-center gap-1" data-product-id="smoothie-calm">
                <span>+ Giỏ Hàng</span>
              </button>
            </div>
          </div>
        </div>

        <!-- Immunity -->
        <div class="nutura-card bg-white p-6 flex flex-col text-center">
          <span class="stage-badge bg-rose-50 text-rose-700 mb-3 self-center">Tăng Cường Đề Kháng</span>
          <h3 class="text-2xl font-bold text-stone-900 mb-1">Immunity</h3>
          <p class="text-xs text-stone-500 mb-4">Lá chắn miễn dịch vững vàng mỗi ngày</p>
          
          <a href="product-smoothie.html" class="my-4 block group">
            <img src="assets/images/smoothie-immunity.png" alt="Smoothie Immunity" class="h-60 mx-auto object-contain group-hover:scale-105 transition duration-300">
          </a>

          <div class="bg-rose-50/60 p-4 rounded-2xl text-left my-4 text-xs space-y-2">
            <div class="font-bold text-rose-900">Kháng thể tự nhiên bảo vệ bé:</div>
            <div class="flex items-center gap-2 text-stone-700"><span>🛡️</span> Lactoferrin hoạt tính sinh học cao</div>
            <div class="flex items-center gap-2 text-stone-700"><span>🫐</span> Chiết xuất quả cơm cháy Elderberry</div>
            <div class="flex items-center gap-2 text-stone-700"><span>🌿</span> Kẽm sinh học tăng miễn dịch tế bào</div>
            <div class="flex items-center gap-2 text-stone-700"><span>🍊</span> Vitamin C tự nhiên chống oxy hóa</div>
          </div>

          <div class="mt-auto pt-2">
            <div class="flex items-baseline justify-between mb-4">
              <div>
                <span class="text-xl font-bold text-[#FF6F78]">410.000 đ</span>
                <span class="text-xs text-stone-400 line-through ml-1">590.000 đ</span>
              </div>
              <span class="text-xs text-stone-400 font-medium">$17.00 AUD</span>
            </div>
            <div class="grid grid-cols-2 gap-2">
              <a href="product-smoothie.html" class="py-2.5 px-3 rounded-full border border-stone-300 text-stone-700 text-xs font-bold hover:bg-stone-50 text-center transition">
                Chi Tiết
              </a>
              <button class="add-to-cart-btn py-2.5 px-3 rounded-full bg-[#FF6F78] hover:bg-[#E65A63] text-white text-xs font-bold transition shadow-md shadow-[#FF6F78]/20 flex items-center justify-center gap-1" data-product-id="smoothie-immunity">
                <span>+ Giỏ Hàng</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- MISSION & THE NUTURA VILLAGE -->
  <section class="py-16 lg:py-24 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        <div class="lg:col-span-6 space-y-6">
          <span class="text-xs font-bold uppercase tracking-widest text-[#FF6F78]">Triết Lý Thương Hiệu</span>
          <h2 class="text-3xl sm:text-4xl font-bold text-stone-900 leading-tight">
            Đặt Dinh Dưỡng Lành Mạnh Vào Trái Tim Ngôi Làng Của Bạn
          </h2>
          <p class="text-stone-700 leading-relaxed text-sm sm:text-base">
            Tại Nutura Organic, chúng tôi tin rằng những quyết định dinh dưỡng và nuôi dạy con tốt nhất luôn đạt kết quả mỹ mãn hơn khi chúng ta cùng đồng hành. Đội ngũ chuyên gia của chúng tôi là tập hợp của những bộ óc xuất sắc nhất trong ngành -  Từ các kỹ sư nông nghiệp hữu cơ đến các nhà khoa học dinh dưỡng và bác sĩ tâm lý nhi khoa hàng đầu nước Úc.
          </p>
          <p class="text-stone-600 text-sm leading-relaxed">
            Chúng tôi không chỉ cung cấp một sản phẩm sữa, mà còn trao gửi giải pháp tự nhiên và sự nâng đỡ tinh thần vững chắc, tiếp thêm sức mạnh để mọi gia đình tự tin đưa ra những lựa chọn thông thái nhất cho con yêu.
          </p>
          <div class="pt-2">
            <a href="about-us.html" class="btn-nutura-primary text-sm py-3.5 px-8">
              Tìm Hiểu Về Ngôi Làng Nutura &rarr;
            </a>
          </div>
        </div>

        <div class="lg:col-span-6">
          <div class="rounded-3xl overflow-hidden shadow-2xl border-4 border-[#FAF7F2]">
            <img src="assets/images/team-group.jpg" alt="Đội ngũ chuyên gia Nutura Village" class="w-full h-auto object-cover">
          </div>
          <div class="grid grid-cols-4 gap-3 mt-4 text-center">
            <div class="p-2 bg-stone-50 rounded-xl">
              <img src="assets/images/dr-michael.jpg" alt="Dr Michael Carr-Gregg" class="w-14 h-14 rounded-full mx-auto object-cover mb-1 border-2 border-white shadow">
              <div class="text-[11px] font-bold text-stone-800">Dr. Michael</div>
              <div class="text-[9px] text-stone-500">Tâm Lý Nhi Khoa</div>
            </div>
            <div class="p-2 bg-stone-50 rounded-xl">
              <img src="assets/images/miriam-raleigh.jpg" alt="Miriam Raleigh" class="w-14 h-14 rounded-full mx-auto object-cover mb-1 border-2 border-white shadow">
              <div class="text-[11px] font-bold text-stone-800">Miriam Raleigh</div>
              <div class="text-[9px] text-stone-500">Chuyên Gia Dinh Dưỡng</div>
            </div>
            <div class="p-2 bg-stone-50 rounded-xl">
              <img src="assets/images/kirsty-levin.jpg" alt="Kirsty Levin" class="w-14 h-14 rounded-full mx-auto object-cover mb-1 border-2 border-white shadow">
              <div class="text-[11px] font-bold text-stone-800">Kirsty Levin</div>
              <div class="text-[9px] text-stone-500">Tâm Lý Học Gia Đình</div>
            </div>
            <div class="p-2 bg-stone-50 rounded-xl">
              <img src="assets/images/jimmy-rees.png" alt="Jimmy Rees" class="w-14 h-14 rounded-full mx-auto object-cover mb-1 border-2 border-white shadow">
              <div class="text-[11px] font-bold text-stone-800">Jimmy Rees</div>
              <div class="text-[9px] text-stone-500">Đại Sứ Làm Cha Mẹ</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SUBSCRIBE AND SAVE: THE NUTURA MILKMAN -->
  <section class="py-16 lg:py-24 bg-[#1C120D] text-white relative overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        <div class="lg:col-span-7 space-y-6">
          <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-rose-500/20 text-rose-300 text-xs font-bold uppercase tracking-wider">
            Dịch Vụ Độc Quyền Nutura Milkman
          </div>
          <h2 class="text-3xl sm:text-4xl lg:text-5xl font-bold tracking-tight text-white leading-tight">
            Đăng Ký Định Kỳ & Tiết Kiệm 15% Trọn Đời
          </h2>
          <p class="text-stone-300 text-sm sm:text-base leading-relaxed">
            Chương trình đăng ký giao sữa định kỳ <strong>Nutura Milkman</strong> mang lại sự an tâm tuyệt đối, tiện lợi tối đa và mức giá tốt nhất cho các bậc cha mẹ. Sữa tươi mới sản xuất được chuyển giao trực tiếp đến tận ngưỡng cửa nhà bạn định kỳ 2 tuần hoặc 4 tuần/lần.
          </p>
          <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 pt-2">
            <div class="bg-stone-800/80 p-4 rounded-2xl border border-stone-700 text-left">
              <div class="text-xl font-bold text-[#FF6F78] mb-1">Giảm 15%</div>
              <div class="text-xs text-stone-300">Tiết kiệm trực tiếp trên mỗi lon sữa giao định kỳ.</div>
            </div>
            <div class="bg-stone-800/80 p-4 rounded-2xl border border-stone-700 text-left">
              <div class="text-xl font-bold text-[#FF6F78] mb-1">Miễn Phí Ship</div>
              <div class="text-xs text-stone-300">Giao hàng tận nhà không phát sinh bất kỳ phụ phí nào.</div>
            </div>
            <div class="bg-stone-800/80 p-4 rounded-2xl border border-stone-700 text-left">
              <div class="text-xl font-bold text-[#FF6F78] mb-1">Linh Hoạt 100%</div>
              <div class="text-xs text-stone-300">Tạm hoãn, đổi giai đoạn sữa hoặc hủy bất cứ lúc nào.</div>
            </div>
          </div>
          <div class="pt-4 flex flex-wrap gap-4">
            <a href="subscriptions.html" class="btn-nutura-primary text-sm py-3.5 px-8 shadow-lg shadow-[#FF6F78]/30">
              Đăng Ký Gói Milkman Ngay
            </a>
            <a href="faqs.html#subscription" class="btn-nutura-white text-sm py-3.5 px-6">
              Tìm Hiểu Cách Thức Hoạt Động
            </a>
          </div>
        </div>

        <div class="lg:col-span-5 text-center">
          <div class="relative">
            <img src="assets/images/milkman-lockup.png" alt="Nutura Milkman" class="max-w-xs mx-auto mb-6">
            <img src="assets/images/nutura-tin-lockups.png" alt="Nutura Tins Subscription" class="w-full max-w-md mx-auto">
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- FEATURED ARTICLES / GÓC CHA MẸ -->
  <section class="py-16 lg:py-24 bg-[#FAF7F2]">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex flex-col md:flex-row md:items-end justify-between mb-12 gap-4">
        <div>
          <span class="text-xs font-bold uppercase tracking-widest text-[#FF6F78]">Cẩm Nang & Lời Khuyên</span>
          <h2 class="text-3xl sm:text-4xl font-bold text-stone-900 mt-1">Bài Viết Nổi Bật Từ Chuyên Gia</h2>
        </div>
        <a href="village.html" class="inline-flex items-center gap-2 text-sm font-bold text-[#FF6F78] hover:underline">
          <span>Xem Toàn Bộ 9+ Bài Viết</span>
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/>
          </svg>
        </a>
      </div>

      <!-- Article Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <!-- Article 1 -->
        <article class="nutura-card bg-white flex flex-col">
          <a href="village.html#article-1" class="block overflow-hidden h-48 bg-stone-100">
            <img src="assets/images/blog-baby-names.jpg" alt="Đặt tên cho bé" class="w-full h-full object-cover hover:scale-105 transition duration-500">
          </a>
          <div class="p-6 flex-1 flex flex-col">
            <div class="flex items-center justify-between text-xs text-stone-400 mb-2">
              <span class="font-bold text-[#FF6F78]">Góc Cha Mẹ</span>
              <span>Nutura Organic</span>
            </div>
            <h3 class="text-lg font-bold text-stone-900 mb-2 hover:text-[#FF6F78] transition">
              <a href="village.html#article-1">Mẹo & Gợi Ý Thú Vị Khi Đặt Tên Cho Thiên Thần Nhỏ</a>
            </h3>
            <p class="text-xs text-stone-600 line-clamp-3 leading-relaxed mb-4">
              Chúc mừng bạn chuẩn bị đón chào một mầm sống mới! Vô vàn cảm xúc vỡ òa khi hay tin mang thai. Tâm trí bạn bắt đầu tìm kiếm những cái tên ý nghĩa nhất...
            </p>
            <div class="mt-auto pt-2">
              <a href="village.html#article-1" class="text-xs font-bold text-[#FF6F78] hover:underline inline-flex items-center gap-1">
                Đọc Tiếp &rarr;
              </a>
            </div>
          </div>
        </article>

        <!-- Article 2 -->
        <article class="nutura-card bg-white flex flex-col">
          <a href="village.html#article-2" class="block overflow-hidden h-48 bg-stone-100">
            <img src="assets/images/blog-school.jpg" alt="Ngày đầu đi học" class="w-full h-full object-cover hover:scale-105 transition duration-500">
          </a>
          <div class="p-6 flex-1 flex flex-col">
            <div class="flex items-center justify-between text-xs text-stone-400 mb-2">
              <span class="font-bold text-[#FF6F78]">Tâm Lý Trẻ Em</span>
              <span>Dr. Michael Carr-Gregg</span>
            </div>
            <h3 class="text-lg font-bold text-stone-900 mb-2 hover:text-[#FF6F78] transition">
              <a href="village.html#article-2">Bí Quyết Chuẩn Bị Tâm Lý Cho Con Vào Ngày Đầu Đi Học</a>
            </h3>
            <p class="text-xs text-stone-600 line-clamp-3 leading-relaxed mb-4">
              Chuyển tiếp từ gia đình sang môi trường học đường là một bước ngoặt lớn với con nhỏ. Bác sĩ tâm lý chia sẻ những bước chuẩn bị hành trang cảm xúc vững vàng...
            </p>
            <div class="mt-auto pt-2">
              <a href="village.html#article-2" class="text-xs font-bold text-[#FF6F78] hover:underline inline-flex items-center gap-1">
                Đọc Tiếp &rarr;
              </a>
            </div>
          </div>
        </article>

        <!-- Article 3 -->
        <article class="nutura-card bg-white flex flex-col">
          <a href="village.html#article-3" class="block overflow-hidden h-48 bg-stone-100">
            <img src="assets/images/jimmy-rees.png" alt="Jimmy Rees" class="w-full h-full object-cover hover:scale-105 transition duration-500">
          </a>
          <div class="p-6 flex-1 flex flex-col">
            <div class="flex items-center justify-between text-xs text-stone-400 mb-2">
              <span class="font-bold text-[#FF6F78]">Góc Người Bố</span>
              <span>Jimmy Rees</span>
            </div>
            <h3 class="text-lg font-bold text-stone-900 mb-2 hover:text-[#FF6F78] transition">
              <a href="village.html#article-3">Khi Mẹ Có Một Đêm Được Nghỉ Ngơi Trọn Vẹn</a>
            </h3>
            <p class="text-xs text-stone-600 line-clamp-3 leading-relaxed mb-4">
              Các ông bố lên tiếng nào! Tất cả chúng ta đều hiểu rằng cần cả một ngôi làng để nuôi dạy một đứa trẻ. Chia sẻ chân thật và hài hước từ ông bố nổi tiếng người Úc...
            </p>
            <div class="mt-auto pt-2">
              <a href="village.html#article-3" class="text-xs font-bold text-[#FF6F78] hover:underline inline-flex items-center gap-1">
                Đọc Tiếp &rarr;
              </a>
            </div>
          </div>
        </article>

        <!-- Article 4 -->
        <article class="nutura-card bg-white flex flex-col">
          <a href="village.html#article-4" class="block overflow-hidden h-48 bg-stone-100">
            <img src="assets/images/blog-lighten-load.jpg" alt="Buông bỏ gánh nặng" class="w-full h-full object-cover hover:scale-105 transition duration-500">
          </a>
          <div class="p-6 flex-1 flex flex-col">
            <div class="flex items-center justify-between text-xs text-stone-400 mb-2">
              <span class="font-bold text-[#FF6F78]">Tâm Lý Làm Mẹ</span>
              <span>Kirsty Levin</span>
            </div>
            <h3 class="text-lg font-bold text-stone-900 mb-2 hover:text-[#FF6F78] transition">
              <a href="village.html#article-4">Học Cách Buông Bỏ Để Nhẹ Bớt Gánh Nặng Nuôi Con</a>
            </h3>
            <p class="text-xs text-stone-600 line-clamp-3 leading-relaxed mb-4">
              Trong tất cả những bài học về thiên chức làm mẹ, một trong những bài học quý giá nhất chính là nghệ thuật tha thứ cho bản thân và sẻ chia trách nhiệm...
            </p>
            <div class="mt-auto pt-2">
              <a href="village.html#article-4" class="text-xs font-bold text-[#FF6F78] hover:underline inline-flex items-center gap-1">
                Đọc Tiếp &rarr;
              </a>
            </div>
          </div>
        </article>

        <!-- Article 5 -->
        <article class="nutura-card bg-white flex flex-col">
          <a href="village.html#article-5" class="block overflow-hidden h-48 bg-stone-100">
            <img src="assets/images/blog-happiness.jpg" alt="Kích hoạt hormone hạnh phúc" class="w-full h-full object-cover hover:scale-105 transition duration-500">
          </a>
          <div class="p-6 flex-1 flex flex-col">
            <div class="flex items-center justify-between text-xs text-stone-400 mb-2">
              <span class="font-bold text-[#FF6F78]">Khoa Học Cảm Xúc</span>
              <span>Kirsty Levin</span>
            </div>
            <h3 class="text-lg font-bold text-stone-900 mb-2 hover:text-[#FF6F78] transition">
              <a href="village.html#article-5">Kích Hoạt Các Hormone Hạnh Phúc Trong Hành Trình Làm Mẹ</a>
            </h3>
            <p class="text-xs text-stone-600 line-clamp-3 leading-relaxed mb-4">
              Đón nhận một em bé chào đời là khoảnh khắc kỳ diệu và biến đổi sâu sắc. Khám phá cách nuôi dưỡng Oxytocin, Dopamine và Serotonin mỗi ngày...
            </p>
            <div class="mt-auto pt-2">
              <a href="village.html#article-5" class="text-xs font-bold text-[#FF6F78] hover:underline inline-flex items-center gap-1">
                Đọc Tiếp &rarr;
              </a>
            </div>
          </div>
        </article>

        <!-- Article 6 -->
        <article class="nutura-card bg-white flex flex-col">
          <a href="village.html#article-6" class="block overflow-hidden h-48 bg-stone-100">
            <img src="assets/images/blog-iron.jpg" alt="Bổ sung sắt cho bé" class="w-full h-full object-cover hover:scale-105 transition duration-500">
          </a>
          <div class="p-6 flex-1 flex flex-col">
            <div class="flex items-center justify-between text-xs text-stone-400 mb-2">
              <span class="font-bold text-[#FF6F78]">Dinh Dưỡng Nhi</span>
              <span>Miriam Raleigh</span>
            </div>
            <h3 class="text-lg font-bold text-stone-900 mb-2 hover:text-[#FF6F78] transition">
              <a href="village.html#article-6">Bé Nhà Bạn Đã Nạp Đủ Lượng Sắt Cần Thiết Mỗi Ngày?</a>
            </h3>
            <p class="text-xs text-stone-600 line-clamp-3 leading-relaxed mb-4">
              Sắt là vi chất dinh dưỡng thiết yếu cho mọi đứa trẻ trên 6 tháng tuổi. Từ 7 đến 12 tháng tuổi, nhu cầu sắt của trẻ thậm chí còn cao hơn cả người lớn...
            </p>
            <div class="mt-auto pt-2">
              <a href="village.html#article-6" class="text-xs font-bold text-[#FF6F78] hover:underline inline-flex items-center gap-1">
                Đọc Tiếp &rarr;
              </a>
            </div>
          </div>
        </article>
      </div>
    </div>
  </section>

  <!-- QUALITY PROMISE BADGES SECTION -->
  <section class="py-14 bg-white border-t border-stone-200/80">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-8">
        <h3 class="text-xl font-bold text-stone-900">Cam Kết 5 Tiêu Chuẩn Vàng Của Nutura Organic</h3>
      </div>
      <div class="grid grid-cols-2 md:grid-cols-5 gap-6 text-center">
        <div class="flex flex-col items-center">
          <img src="assets/images/icon-aus-made.png" alt="Australian Made" class="h-16 w-auto mb-2 object-contain">
          <h4 class="text-xs font-bold text-stone-900">100% Sản Xuất Tại Úc</h4>
          <p class="text-[11px] text-stone-500">Australian Made & Owned</p>
        </div>
        <div class="flex flex-col items-center">
          <img src="assets/images/icon-cert-organic.png" alt="Certified Organic" class="h-16 w-auto mb-2 object-contain">
          <h4 class="text-xs font-bold text-stone-900">Chứng Nhận Hữu Cơ Kép</h4>
          <p class="text-[11px] text-stone-500">ACO & NASAA Standards</p>
        </div>
        <div class="flex flex-col items-center">
          <img src="assets/images/icon-no-artificial-flav.png" alt="No Artificial Flavours" class="h-16 w-auto mb-2 object-contain">
          <h4 class="text-xs font-bold text-stone-900">Không Hương Vị Nhân Tạo</h4>
          <p class="text-[11px] text-stone-500">Vị thanh thuần từ sữa tươi</p>
        </div>
        <div class="flex flex-col items-center">
          <img src="assets/images/icon-no-artificial-sweet.png" alt="No Artificial Sweeteners" class="h-16 w-auto mb-2 object-contain">
          <h4 class="text-xs font-bold text-stone-900">Không Chất Tạo Ngọt</h4>
          <p class="text-[11px] text-stone-500">Chỉ dùng lactose tự nhiên</p>
        </div>
        <div class="flex flex-col items-center col-span-2 md:col-span-1">
          <img src="assets/images/icon-no-gmo.png" alt="No GMO" class="h-16 w-auto mb-2 object-contain">
          <h4 class="text-xs font-bold text-stone-900">Không Biến Đổi Gen</h4>
          <p class="text-[11px] text-stone-500">Non-GMO Ingredients</p>
        </div>
      </div>
    </div>
  </section>
  </main>
"""

    content += render_footer()
    return content

print("Home page builder ready.")
