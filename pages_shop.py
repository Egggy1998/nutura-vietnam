# -*- coding: utf-8 -*-
"""
Trang Cửa Hàng & Các Trang Chi Tiết Sản Phẩm
shop.html, product-stage1.html, product-stage2.html, product-stage3.html, product-stage4.html,
product-smoothie.html, product-advance-kids.html, product-advance-adults.html, product-motherdaily.html
"""

from build_site import render_head, render_topbar, render_navbar, render_footer

def build_shop():
    content = render_head(
        title="Cửa Hàng Sữa Hữu Cơ Nutura | Bộ 3 Giai Đoạn Stage 1, Stage 2, Stage 3",
        description="Khám phá bộ 3 dòng sữa công thức hữu cơ Nutura Úc: Stage 1 (0 - 6 tháng), Stage 2 (6 - 12 tháng) và Stage 3 (12 - 36 tháng). 100% sữa tươi đạm A2 từ đàn bò ăn cỏ Úc.",
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
            Tất Cả (Stage 1-3)
          </button>
          <button onclick="filterByAge('0-6m')" class="filter-age-btn px-4 py-2 rounded-full text-xs font-bold bg-stone-100 text-stone-700 hover:bg-stone-200 transition" data-age="0-6m">
            Stage 1 (0 - 6 Tháng)
          </button>
          <button onclick="filterByAge('6-12m')" class="filter-age-btn px-4 py-2 rounded-full text-xs font-bold bg-stone-100 text-stone-700 hover:bg-stone-200 transition" data-age="6-12m">
            Stage 2 (6 - 12 Tháng)
          </button>
          <button onclick="filterByAge('1-3y')" class="filter-age-btn px-4 py-2 rounded-full text-xs font-bold bg-stone-100 text-stone-700 hover:bg-stone-200 transition" data-age="1-3y">
            Stage 3 (12 - 36 Tháng)
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

      <!-- PRODUCTS GRID -->
      <div id="shopProductsGrid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
        <!-- Product 1: Stage 1 -->
        <div class="product-item nutura-card flex flex-col p-6 bg-white" data-age="0-6m" data-cat="formula" data-name="Sữa Hữu Cơ Nutura Stage 1 (0-6 tháng)">
          <div class="flex items-center justify-between mb-2">
            <span class="stage-badge stage-badge-s1">0 - 6 Tháng</span>
            <span class="text-[11px] font-bold text-emerald-600">ACO Hữu Cơ</span>
          </div>
          <a href="product-stage1.html" class="my-4 block group text-center flex-1">
            <img src="assets/images/stage1.png" alt="Sữa Nutura Stage 1" class="h-60 mx-auto object-contain group-hover:scale-105 transition duration-300">
          </a>
          <h3 class="text-lg font-bold text-stone-900 mb-1 hover:text-[#FF6F78] transition">
            <a href="product-stage1.html">Sữa Hữu Cơ Nutura Stage 1</a>
          </h3>
          <p class="text-xs text-stone-500 mb-4">800g • Đạm tươi A2, Tỷ lệ đạm Whey vượt trội (60:40)</p>
          <div class="flex items-baseline justify-between mt-auto pt-3 border-t border-stone-100">
            <div>
              <span class="text-xl font-bold text-[#FF6F78]">780.000 đ</span>
              <span class="block text-[11px] text-stone-400">$46.00 AUD</span>
            </div>
            <button class="add-to-cart-btn px-4 py-2 bg-[#FF6F78] hover:bg-[#E65A63] text-white text-xs font-bold rounded-full transition shadow-sm" data-product-id="stage-1">
              + Giỏ Hàng
            </button>
          </div>
        </div>

        <!-- Product 2: Stage 2 -->
        <div class="product-item nutura-card flex flex-col p-6 bg-white" data-age="6-12m" data-cat="formula" data-name="Sữa Hữu Cơ Nutura Stage 2 (6-12 tháng)">
          <div class="flex items-center justify-between mb-2">
            <span class="stage-badge stage-badge-s2">6 - 12 Tháng</span>
            <span class="text-[11px] font-bold text-emerald-600">ACO Hữu Cơ</span>
          </div>
          <a href="product-stage2.html" class="my-4 block group text-center flex-1">
            <img src="assets/images/stage2.png" alt="Sữa Nutura Stage 2" class="h-60 mx-auto object-contain group-hover:scale-105 transition duration-300">
          </a>
          <h3 class="text-lg font-bold text-stone-900 mb-1 hover:text-[#FF6F78] transition">
            <a href="product-stage2.html">Sữa Hữu Cơ Nutura Stage 2</a>
          </h3>
          <p class="text-xs text-stone-500 mb-4">800g • Đạm Casein cân bằng, Giàu Sắt, Kẽm, DHA & GOS</p>
          <div class="flex items-baseline justify-between mt-auto pt-3 border-t border-stone-100">
            <div>
              <span class="text-xl font-bold text-[#FF6F78]">780.000 đ</span>
              <span class="block text-[11px] text-stone-400">$46.00 AUD</span>
            </div>
            <button class="add-to-cart-btn px-4 py-2 bg-[#FF6F78] hover:bg-[#E65A63] text-white text-xs font-bold rounded-full transition shadow-sm" data-product-id="stage-2">
              + Giỏ Hàng
            </button>
          </div>
        </div>

        <!-- Product 3: Stage 3 -->
        <div class="product-item nutura-card flex flex-col p-6 bg-white" data-age="1-3y" data-cat="formula" data-name="Sữa Hữu Cơ Nutura Stage 3 (12-36 tháng)">
          <div class="flex items-center justify-between mb-2">
            <span class="stage-badge stage-badge-s3">1 - 3 Tuổi</span>
            <span class="text-[11px] font-bold text-amber-600">Từ 12 tháng tuổi</span>
          </div>
          <a href="product-stage3.html" class="my-4 block group text-center flex-1">
            <img src="assets/images/stage3.png" alt="Sữa Nutura Stage 3" class="h-60 mx-auto object-contain group-hover:scale-105 transition duration-300">
          </a>
          <h3 class="text-lg font-bold text-stone-900 mb-1 hover:text-[#FF6F78] transition">
            <a href="product-stage3.html">Sữa Hữu Cơ Nutura Stage 3</a>
          </h3>
          <p class="text-xs text-stone-500 mb-4">800g • 16 Vitamin & Khoáng chất, FOS & GOS, DHA & ARA</p>
          <div class="flex items-baseline justify-between mt-auto pt-3 border-t border-stone-100">
            <div>
              <span class="text-xl font-bold text-[#FF6F78]">780.000 đ</span>
              <span class="block text-[11px] text-stone-400">$46.00 AUD</span>
            </div>
            <button class="add-to-cart-btn px-4 py-2 bg-[#FF6F78] hover:bg-[#E65A63] text-white text-xs font-bold rounded-full transition shadow-sm" data-product-id="stage-3">
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
