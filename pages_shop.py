# -*- coding: utf-8 -*-
"""
Trang Cửa Hàng & Các Trang Chi Tiết Sản Phẩm
shop.html, product-stage1.html, product-stage2.html, product-stage3.html, product-stage4.html,
product-smoothie.html, product-advance-kids.html, product-advance-adults.html, product-motherdaily.html
"""

from build_site import render_head, render_topbar, render_navbar, render_footer

def build_shop():
    content = render_head(
        title="Cửa Hàng Sữa Hữu Cơ Nutura | Dòng Sản Phẩm Hoàn Chỉnh Cho Cả Gia Đình",
        description="Khám phá đầy đủ dòng sữa hữu cơ Nutura Úc: Sữa công thức Stage 1, 2, 3, 4, Sữa bột chức năng The Good Smoothie, Nutura Advance và Combo ưu đãi MotherDaily.",
        canonical_url="shop.html"
    )
    content += render_topbar()
    content += render_navbar(active_page="shop")

    content += """
  <!-- SHOP HEADER BANNER -->
  <section class="bg-[#FAF7F2] py-12 lg:py-16 border-b border-stone-200/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 md:grid-cols-12 gap-8 items-center">
        <div class="md:col-span-8 space-y-4">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-rose-100 text-[#FF6F78] text-xs font-bold uppercase tracking-wider">
            Cửa Hàng Trực Tuyến Chính Thức
          </div>
          <h1 class="text-3xl sm:text-4xl lg:text-5xl font-bold text-stone-900 tracking-tight">
            Dòng Sản Phẩm Nutura Organic
          </h1>
          <p class="text-stone-600 text-sm sm:text-base leading-relaxed max-w-2xl">
            Toàn bộ dòng sản phẩm sữa hữu cơ cao cấp sản xuất 100% tại Úc. Được tạo nên bởi các chuyên gia dinh dưỡng, nông dân và nhà khoa học hàng đầu với tâm huyết đặt sự phát triển khỏe mạnh của con bạn lên vị trí ưu tiên số 1.
          </p>
        </div>
        <div class="md:col-span-4 text-center">
          <img src="assets/images/banner-shop.jpg" alt="Dòng sản phẩm Nutura" class="rounded-3xl shadow-lg border-4 border-white max-h-56 mx-auto object-cover">
        </div>
      </div>
    </div>
  </section>

  <!-- SHOP FILTER & PRODUCTS GRID -->
  <section class="py-12 bg-white flex-1">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <!-- Search & Age Filter Tabs -->
      <div class="flex flex-col lg:flex-row items-center justify-between gap-6 pb-8 border-b border-stone-100 mb-8">
        <!-- Age Filter Buttons -->
        <div class="flex flex-wrap items-center gap-2 w-full lg:w-auto">
          <span class="text-xs font-bold text-stone-400 uppercase tracking-wider mr-2">Độ Tuổi:</span>
          <button onclick="filterByAge('all')" class="filter-age-btn px-4 py-2 rounded-full text-xs font-bold bg-[#FF6F78] text-white transition" data-age="all">
            Tất Cả
          </button>
          <button onclick="filterByAge('0-6m')" class="filter-age-btn px-4 py-2 rounded-full text-xs font-bold bg-stone-100 text-stone-700 hover:bg-stone-200 transition" data-age="0-6m">
            0 - 6 Tháng
          </button>
          <button onclick="filterByAge('6-12m')" class="filter-age-btn px-4 py-2 rounded-full text-xs font-bold bg-stone-100 text-stone-700 hover:bg-stone-200 transition" data-age="6-12m">
            6 - 12 Tháng
          </button>
          <button onclick="filterByAge('1-3y')" class="filter-age-btn px-4 py-2 rounded-full text-xs font-bold bg-stone-100 text-stone-700 hover:bg-stone-200 transition" data-age="1-3y">
            1 - 3 Tuổi
          </button>
          <button onclick="filterByAge('3y+')" class="filter-age-btn px-4 py-2 rounded-full text-xs font-bold bg-stone-100 text-stone-700 hover:bg-stone-200 transition" data-age="3y+">
            3+ Tuổi
          </button>
          <button onclick="filterByAge('adult')" class="filter-age-btn px-4 py-2 rounded-full text-xs font-bold bg-stone-100 text-stone-700 hover:bg-stone-200 transition" data-age="adult">
            Người Lớn
          </button>
        </div>

        <!-- Quick Search Bar -->
        <div class="relative w-full lg:w-72">
          <label for="productSearchInput" class="sr-only">Tìm theo tên sản phẩm</label>
          <input type="text" id="productSearchInput" onkeyup="searchProducts()" placeholder="Tìm theo tên sản phẩm..." class="w-full pl-9 pr-4 py-2 text-xs border border-stone-300 rounded-full focus:outline-none focus:border-[#FF6F78]">
          <svg class="w-4 h-4 text-stone-400 absolute left-3 top-2.5" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
          </svg>
        </div>
      </div>

      <!-- Category Filter Pills -->
      <div class="flex flex-wrap gap-2 mb-8 text-xs font-semibold">
        <button onclick="filterByCategory('all')" class="category-pill px-3 py-1.5 rounded-lg border border-stone-300 bg-stone-900 text-white" data-cat="all">Tất Cả Danh Mục</button>
        <button onclick="filterByCategory('formula')" class="category-pill px-3 py-1.5 rounded-lg border border-stone-200 bg-white text-stone-700 hover:bg-stone-50" data-cat="formula">Sữa Công Thức Hữu Cơ</button>
        <button onclick="filterByCategory('smoothie')" class="category-pill px-3 py-1.5 rounded-lg border border-stone-200 bg-white text-stone-700 hover:bg-stone-50" data-cat="smoothie">The Good Smoothie</button>
        <button onclick="filterByCategory('collab')" class="category-pill px-3 py-1.5 rounded-lg border border-stone-200 bg-white text-stone-700 hover:bg-rose-50 text-rose-600" data-cat="collab">Combo Nutura x MotherDaily (-40%)</button>
        <button onclick="filterByCategory('advance')" class="category-pill px-3 py-1.5 rounded-lg border border-stone-200 bg-white text-stone-700 hover:bg-stone-50" data-cat="advance">Dòng Nutura Advance</button>
        <button onclick="filterByCategory('trial')" class="category-pill px-3 py-1.5 rounded-lg border border-stone-200 bg-white text-stone-700 hover:bg-stone-50" data-cat="trial">Gói Dùng Thử Sachet</button>
      </div>

      <!-- PRODUCTS GRID -->
      <div id="shopProductsGrid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
        <!-- Product 1: Stage 1 -->
        <div class="product-item nutura-card flex flex-col p-5 bg-white" data-age="0-6m" data-cat="formula" data-name="Sữa Hữu Cơ Nutura Stage 1 (0-6 tháng)">
          <div class="flex items-center justify-between mb-2">
            <span class="stage-badge stage-badge-s1">0 - 6 Tháng</span>
            <span class="text-[11px] font-bold text-emerald-600">ACO Hữu Cơ</span>
          </div>
          <a href="product-stage1.html" class="my-3 block group text-center flex-1">
            <img src="assets/images/stage1.png" alt="Sữa Nutura Stage 1" class="h-48 mx-auto object-contain group-hover:scale-105 transition duration-300">
          </a>
          <h3 class="text-base font-bold text-stone-900 mb-1 hover:text-[#FF6F78] transition">
            <a href="product-stage1.html">Sữa Hữu Cơ Nutura Stage 1</a>
          </h3>
          <p class="text-xs text-stone-500 mb-3">800g • Đạm tươi A2, Tỷ lệ đạm Whey vượt trội</p>
          <div class="flex items-baseline justify-between mt-auto pt-2 border-t border-stone-100">
            <div>
              <span class="text-lg font-bold text-[#FF6F78]">780.000 đ</span>
              <span class="block text-[11px] text-stone-400">$46.00 AUD</span>
            </div>
            <button class="add-to-cart-btn px-3 py-2 bg-[#FF6F78] hover:bg-[#E65A63] text-white text-xs font-bold rounded-full transition shadow-sm" data-product-id="stage-1">
              + Giỏ Hàng
            </button>
          </div>
        </div>

        <!-- Product 2: Stage 2 -->
        <div class="product-item nutura-card flex flex-col p-5 bg-white" data-age="6-12m" data-cat="formula" data-name="Sữa Hữu Cơ Nutura Stage 2 (6-12 tháng)">
          <div class="flex items-center justify-between mb-2">
            <span class="stage-badge stage-badge-s2">6 - 12 Tháng</span>
            <span class="text-[11px] font-bold text-emerald-600">ACO Hữu Cơ</span>
          </div>
          <a href="product-stage2.html" class="my-3 block group text-center flex-1">
            <img src="assets/images/stage2.png" alt="Sữa Nutura Stage 2" class="h-48 mx-auto object-contain group-hover:scale-105 transition duration-300">
          </a>
          <h3 class="text-base font-bold text-stone-900 mb-1 hover:text-[#FF6F78] transition">
            <a href="product-stage2.html">Sữa Hữu Cơ Nutura Stage 2</a>
          </h3>
          <p class="text-xs text-stone-500 mb-3">800g • Đạm Casein cân bằng, Giàu DHA & GOS</p>
          <div class="flex items-baseline justify-between mt-auto pt-2 border-t border-stone-100">
            <div>
              <span class="text-lg font-bold text-[#FF6F78]">780.000 đ</span>
              <span class="block text-[11px] text-stone-400">$46.00 AUD</span>
            </div>
            <button class="add-to-cart-btn px-3 py-2 bg-[#FF6F78] hover:bg-[#E65A63] text-white text-xs font-bold rounded-full transition shadow-sm" data-product-id="stage-2">
              + Giỏ Hàng
            </button>
          </div>
        </div>

        <!-- Product 3: Stage 3 -->
        <div class="product-item nutura-card flex flex-col p-5 bg-white" data-age="1-3y" data-cat="formula" data-name="Sữa Hữu Cơ Nutura Stage 3 (12-36 tháng)">
          <div class="flex items-center justify-between mb-2">
            <span class="stage-badge stage-badge-s3">1 - 3 Tuổi</span>
            <span class="text-[11px] font-bold text-amber-600">Số 1 Nước Úc</span>
          </div>
          <a href="product-stage3.html" class="my-3 block group text-center flex-1">
            <img src="assets/images/stage3.png" alt="Sữa Nutura Stage 3" class="h-48 mx-auto object-contain group-hover:scale-105 transition duration-300">
          </a>
          <h3 class="text-base font-bold text-stone-900 mb-1 hover:text-[#FF6F78] transition">
            <a href="product-stage3.html">Sữa Hữu Cơ Nutura Stage 3</a>
          </h3>
          <p class="text-xs text-stone-500 mb-3">800g • 16 Vitamin & Khoáng chất, FOS & GOS</p>
          <div class="flex items-baseline justify-between mt-auto pt-2 border-t border-stone-100">
            <div>
              <span class="text-lg font-bold text-[#FF6F78]">780.000 đ</span>
              <span class="block text-[11px] text-stone-400">$46.00 AUD</span>
            </div>
            <button class="add-to-cart-btn px-3 py-2 bg-[#FF6F78] hover:bg-[#E65A63] text-white text-xs font-bold rounded-full transition shadow-sm" data-product-id="stage-3">
              + Giỏ Hàng
            </button>
          </div>
        </div>

        <!-- Product 4: Stage 4 -->
        <div class="product-item nutura-card flex flex-col p-5 bg-white" data-age="3y+" data-cat="formula" data-name="Sữa Dinh Dưỡng Nutura Stage 4 (3 tuổi trở lên)">
          <div class="flex items-center justify-between mb-2">
            <span class="stage-badge bg-indigo-50 text-indigo-700">3+ Tuổi</span>
            <span class="text-[11px] font-bold text-stone-500">Junior Milk</span>
          </div>
          <a href="product-stage4.html" class="my-3 block group text-center flex-1">
            <img src="assets/images/stage4.jpg" alt="Sữa Nutura Stage 4" class="h-48 mx-auto object-contain group-hover:scale-105 transition duration-300">
          </a>
          <h3 class="text-base font-bold text-stone-900 mb-1 hover:text-[#FF6F78] transition">
            <a href="product-stage4.html">Sữa Dinh Dưỡng Nutura Stage 4</a>
          </h3>
          <p class="text-xs text-stone-500 mb-3">800g • Dinh dưỡng vàng cho trẻ mẫu giáo & tiểu học</p>
          <div class="flex items-baseline justify-between mt-auto pt-2 border-t border-stone-100">
            <div>
              <span class="text-lg font-bold text-[#FF6F78]">560.000 đ</span>
              <span class="block text-[11px] text-stone-400">$33.00 AUD</span>
            </div>
            <button class="add-to-cart-btn px-3 py-2 bg-[#FF6F78] hover:bg-[#E65A63] text-white text-xs font-bold rounded-full transition shadow-sm" data-product-id="stage-4">
              + Giỏ Hàng
            </button>
          </div>
        </div>

        <!-- Product 5: The Good Smoothie Cognitive -->
        <div class="product-item nutura-card flex flex-col p-5 bg-white" data-age="1-3y" data-cat="smoothie" data-name="The Good Smoothie Cognitive Trí Não">
          <div class="flex items-center justify-between mb-2">
            <span class="stage-badge stage-badge-smoothie">Trí Não</span>
            <span class="text-[11px] font-bold text-rose-500">Giảm 30%</span>
          </div>
          <a href="product-smoothie.html" class="my-3 block group text-center flex-1">
            <img src="assets/images/smoothie-cognitive.png" alt="Smoothie Cognitive" class="h-48 mx-auto object-contain group-hover:scale-105 transition duration-300">
          </a>
          <h3 class="text-base font-bold text-stone-900 mb-1 hover:text-[#FF6F78] transition">
            <a href="product-smoothie.html">The Good Smoothie - Cognitive</a>
          </h3>
          <p class="text-xs text-stone-500 mb-3">300g • Phospholipids, Tyrosine, DHA & B-Vitamins</p>
          <div class="flex items-baseline justify-between mt-auto pt-2 border-t border-stone-100">
            <div>
              <span class="text-lg font-bold text-[#FF6F78]">410.000 đ</span>
              <span class="block text-[11px] text-stone-400 line-through">590.000 đ</span>
            </div>
            <button class="add-to-cart-btn px-3 py-2 bg-[#FF6F78] hover:bg-[#E65A63] text-white text-xs font-bold rounded-full transition shadow-sm" data-product-id="smoothie-cognitive">
              + Giỏ Hàng
            </button>
          </div>
        </div>

        <!-- Product 6: The Good Smoothie Calm -->
        <div class="product-item nutura-card flex flex-col p-5 bg-white" data-age="1-3y" data-cat="smoothie" data-name="The Good Smoothie Calm Ngủ Ngon">
          <div class="flex items-center justify-between mb-2">
            <span class="stage-badge bg-amber-50 text-amber-700">Ngủ Ngon</span>
            <span class="text-[11px] font-bold text-rose-500">Giảm 30%</span>
          </div>
          <a href="product-smoothie.html" class="my-3 block group text-center flex-1">
            <img src="assets/images/smoothie-calm.png" alt="Smoothie Calm" class="h-48 mx-auto object-contain group-hover:scale-105 transition duration-300">
          </a>
          <h3 class="text-base font-bold text-stone-900 mb-1 hover:text-[#FF6F78] transition">
            <a href="product-smoothie.html">The Good Smoothie - Calm</a>
          </h3>
          <p class="text-xs text-stone-500 mb-3">300g • Cúc La Mã, Yến mạch, Magie & Chuối</p>
          <div class="flex items-baseline justify-between mt-auto pt-2 border-t border-stone-100">
            <div>
              <span class="text-lg font-bold text-[#FF6F78]">410.000 đ</span>
              <span class="block text-[11px] text-stone-400 line-through">590.000 đ</span>
            </div>
            <button class="add-to-cart-btn px-3 py-2 bg-[#FF6F78] hover:bg-[#E65A63] text-white text-xs font-bold rounded-full transition shadow-sm" data-product-id="smoothie-calm">
              + Giỏ Hàng
            </button>
          </div>
        </div>

        <!-- Product 7: The Good Smoothie Immunity -->
        <div class="product-item nutura-card flex flex-col p-5 bg-white" data-age="1-3y" data-cat="smoothie" data-name="The Good Smoothie Immunity Đề Kháng">
          <div class="flex items-center justify-between mb-2">
            <span class="stage-badge bg-rose-50 text-rose-700">Đề Kháng</span>
            <span class="text-[11px] font-bold text-rose-500">Giảm 30%</span>
          </div>
          <a href="product-smoothie.html" class="my-3 block group text-center flex-1">
            <img src="assets/images/smoothie-immunity.png" alt="Smoothie Immunity" class="h-48 mx-auto object-contain group-hover:scale-105 transition duration-300">
          </a>
          <h3 class="text-base font-bold text-stone-900 mb-1 hover:text-[#FF6F78] transition">
            <a href="product-smoothie.html">The Good Smoothie - Immunity</a>
          </h3>
          <p class="text-xs text-stone-500 mb-3">300g • Lactoferrin, Cơm cháy Elderberry, Kẽm & C</p>
          <div class="flex items-baseline justify-between mt-auto pt-2 border-t border-stone-100">
            <div>
              <span class="text-lg font-bold text-[#FF6F78]">410.000 đ</span>
              <span class="block text-[11px] text-stone-400 line-through">590.000 đ</span>
            </div>
            <button class="add-to-cart-btn px-3 py-2 bg-[#FF6F78] hover:bg-[#E65A63] text-white text-xs font-bold rounded-full transition shadow-sm" data-product-id="smoothie-immunity">
              + Giỏ Hàng
            </button>
          </div>
        </div>

        <!-- Product 8: Collab MotherDaily Stage 1 -->
        <div class="product-item nutura-card flex flex-col p-5 bg-rose-50/40 border-rose-200" data-age="0-6m" data-cat="collab" data-name="Combo Nutura Stage 1 x MotherDaily">
          <div class="flex items-center justify-between mb-2">
            <span class="stage-badge bg-rose-100 text-rose-700">Combo Mẹ & Bé</span>
            <span class="text-[11px] font-bold text-rose-600 bg-white px-2 py-0.5 rounded-full border border-rose-200">-40% Collab</span>
          </div>
          <a href="product-motherdaily.html" class="my-3 block group text-center flex-1">
            <img src="assets/images/motherdaily-pack.png" alt="Nutura x MotherDaily" class="h-48 mx-auto object-contain group-hover:scale-105 transition duration-300">
          </a>
          <h3 class="text-base font-bold text-stone-900 mb-1 hover:text-[#FF6F78] transition">
            <a href="product-motherdaily.html">Nutura S1 x MotherDaily</a>
          </h3>
          <p class="text-xs text-stone-500 mb-3">Bộ phục hồi cho mẹ sau sinh + Sữa hữu cơ Stage 1</p>
          <div class="flex items-baseline justify-between mt-auto pt-2 border-t border-rose-200/60">
            <div>
              <span class="text-lg font-bold text-[#FF6F78]">1.330.000 đ</span>
              <span class="block text-[11px] text-stone-400 line-through">2.220.000 đ</span>
            </div>
            <button class="add-to-cart-btn px-3 py-2 bg-[#FF6F78] hover:bg-[#E65A63] text-white text-xs font-bold rounded-full transition shadow-sm" data-product-id="collab-stage1">
              + Giỏ Hàng
            </button>
          </div>
        </div>

        <!-- Product 9: Advance Smart Grow for Kids -->
        <div class="product-item nutura-card flex flex-col p-5 bg-white" data-age="3y+" data-cat="advance" data-name="Nutura Advance Smart Grow for Kids">
          <div class="flex items-center justify-between mb-2">
            <span class="stage-badge bg-blue-50 text-blue-700">3+ Tuổi</span>
            <span class="text-[11px] font-bold text-stone-500">Advance Range</span>
          </div>
          <a href="product-advance-kids.html" class="my-3 block group text-center flex-1">
            <img src="assets/images/smart-grow-kids.jpg" alt="Nutura Smart Grow" class="h-48 mx-auto object-contain group-hover:scale-105 transition duration-300">
          </a>
          <h3 class="text-base font-bold text-stone-900 mb-1 hover:text-[#FF6F78] transition">
            <a href="product-advance-kids.html">Advance Smart Grow Kids</a>
          </h3>
          <p class="text-xs text-stone-500 mb-3">800g • Dinh dưỡng cao cấp bứt phá chiều cao & thể chất</p>
          <div class="flex items-baseline justify-between mt-auto pt-2 border-t border-stone-100">
            <div>
              <span class="text-lg font-bold text-[#FF6F78]">780.000 đ</span>
              <span class="block text-[11px] text-stone-400">$46.00 AUD</span>
            </div>
            <button class="add-to-cart-btn px-3 py-2 bg-[#FF6F78] hover:bg-[#E65A63] text-white text-xs font-bold rounded-full transition shadow-sm" data-product-id="smart-grow-kids">
              + Giỏ Hàng
            </button>
          </div>
        </div>

        <!-- Product 10: Advance Active Adults -->
        <div class="product-item nutura-card flex flex-col p-5 bg-white" data-age="adult" data-cat="advance" data-name="Nutura Advance Active Adults Người Lớn">
          <div class="flex items-center justify-between mb-2">
            <span class="stage-badge bg-stone-100 text-stone-700">Người Lớn</span>
            <span class="text-[11px] font-bold text-stone-500">Advance Range</span>
          </div>
          <a href="product-advance-adults.html" class="my-3 block group text-center flex-1">
            <img src="assets/images/active-adults.jpg" alt="Nutura Active Adults" class="h-48 mx-auto object-contain group-hover:scale-105 transition duration-300">
          </a>
          <h3 class="text-base font-bold text-stone-900 mb-1 hover:text-[#FF6F78] transition">
            <a href="product-advance-adults.html">Advance Active Adults</a>
          </h3>
          <p class="text-xs text-stone-500 mb-3">800g • Canxi sinh học & đạm tươi tái tạo năng lượng</p>
          <div class="flex items-baseline justify-between mt-auto pt-2 border-t border-stone-100">
            <div>
              <span class="text-lg font-bold text-[#FF6F78]">780.000 đ</span>
              <span class="block text-[11px] text-stone-400">$46.00 AUD</span>
            </div>
            <button class="add-to-cart-btn px-3 py-2 bg-[#FF6F78] hover:bg-[#E65A63] text-white text-xs font-bold rounded-full transition shadow-sm" data-product-id="active-adults">
              + Giỏ Hàng
            </button>
          </div>
        </div>

        <!-- Product 11: Trial Pack Stage 1 -->
        <div class="product-item nutura-card flex flex-col p-5 bg-white" data-age="0-6m" data-cat="trial" data-name="Gói Dùng Thử Stage 1 Trial Pack">
          <div class="flex items-center justify-between mb-2">
            <span class="stage-badge bg-stone-100 text-stone-600">Dùng Thử</span>
            <span class="text-[11px] font-bold text-emerald-600">2 Gói Nhỏ</span>
          </div>
          <a href="product-stage1.html" class="my-3 block group text-center flex-1">
            <img src="assets/images/sachet-stage1.jpg" alt="Trial Pack Stage 1" class="h-48 mx-auto object-contain group-hover:scale-105 transition duration-300">
          </a>
          <h3 class="text-base font-bold text-stone-900 mb-1 hover:text-[#FF6F78] transition">
            <a href="product-stage1.html">Gói Dùng Thử Stage 1 (Twin Pack)</a>
          </h3>
          <p class="text-xs text-stone-500 mb-3">2 x 20g • Tiện lợi mang đi chơi hoặc cho bé trải nghiệm</p>
          <div class="flex items-baseline justify-between mt-auto pt-2 border-t border-stone-100">
            <div>
              <span class="text-lg font-bold text-[#FF6F78]">85.000 đ</span>
              <span class="block text-[11px] text-stone-400">$4.99 AUD</span>
            </div>
            <button class="add-to-cart-btn px-3 py-2 bg-[#FF6F78] hover:bg-[#E65A63] text-white text-xs font-bold rounded-full transition shadow-sm" data-product-id="trial-stage1">
              + Giỏ Hàng
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Client-side filter script -->
  <script>
    function filterByAge(age) {
      document.querySelectorAll('.filter-age-btn').forEach(btn => {
        if (btn.dataset.age === age) {
          btn.classList.remove('bg-stone-100', 'text-stone-700');
          btn.classList.add('bg-[#FF6F78]', 'text-white');
        } else {
          btn.classList.remove('bg-[#FF6F78]', 'text-white');
          btn.classList.add('bg-stone-100', 'text-stone-700');
        }
      });

      document.querySelectorAll('.product-item').forEach(item => {
        if (age === 'all' || item.dataset.age === age) {
          item.style.display = 'flex';
        } else {
          item.style.display = 'none';
        }
      });
    }

    function filterByCategory(cat) {
      document.querySelectorAll('.category-pill').forEach(btn => {
        if (btn.dataset.cat === cat) {
          btn.classList.add('bg-stone-900', 'text-white');
          btn.classList.remove('bg-white', 'text-stone-700');
        } else {
          btn.classList.remove('bg-stone-900', 'text-white');
          btn.classList.add('bg-white', 'text-stone-700');
        }
      });

      document.querySelectorAll('.product-item').forEach(item => {
        if (cat === 'all' || item.dataset.cat === cat) {
          item.style.display = 'flex';
        } else {
          item.style.display = 'none';
        }
      });
    }

    function searchProducts() {
      const q = document.getElementById('productSearchInput').value.toLowerCase().trim();
      document.querySelectorAll('.product-item').forEach(item => {
        const name = (item.dataset.name || '').toLowerCase();
        if (name.includes(q)) {
          item.style.display = 'flex';
        } else {
          item.style.display = 'none';
        }
      });
    }
  </script>
"""

    content += render_footer()
    return content

print("Shop page builder ready.")
