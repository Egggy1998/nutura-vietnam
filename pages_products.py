# -*- coding: utf-8 -*-
"""
Generators for All Product Detail Pages
- product-stage1.html
- product-stage2.html
- product-stage3.html
- product-stage4.html
- product-smoothie.html
- product-advance-kids.html
- product-advance-adults.html
- product-motherdaily.html
"""

from build_site import render_head, render_topbar, render_navbar, render_footer

def build_product_stage1():
    content = render_head(
        title="Sữa Hữu Cơ Nutura Stage 1 (0 - 6 tháng) 800g | Đạm A2 Úc",
        description="Sữa công thức hữu cơ Nutura Stage 1 dành cho trẻ từ 0 đến 6 tháng tuổi; sữa hữu cơ đạm A2, tỷ lệ Whey : Casein 60 : 40, GOS và FOS theo nhãn sản phẩm.",
        canonical_url="product-stage1.html"
    )
    content += render_topbar()
    content += render_navbar(active_page="shop")

    content += """
  <!-- BREADCRUMB -->
  <div class="bg-[#FAF7F2] py-4 border-b border-stone-200/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-xs text-stone-500 flex items-center gap-2">
      <a href="index.html" class="hover:text-[#FF6F78]">Trang Chủ</a>
      <span>/</span>
      <a href="shop.html" class="hover:text-[#FF6F78]">Sản Phẩm</a>
      <span>/</span>
      <span class="text-stone-800 font-bold">Sữa Hữu Cơ Nutura Stage 1</span>
    </div>
  </div>

  <!-- PRODUCT OVERVIEW SECTION -->
  <section class="py-12 lg:py-16 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-start">
        <!-- Gallery Images -->
        <div class="lg:col-span-6 space-y-4">
          <div class="bg-[#FAF7F2] rounded-3xl p-8 border border-stone-200/80 text-center relative overflow-hidden">
            <span class="absolute top-4 left-4 stage-badge stage-badge-s1">0 - 6 Tháng</span>
            <span class="absolute top-4 right-4 bg-emerald-100 text-emerald-800 px-3 py-1 rounded-full text-xs font-bold">ACO Hữu Cơ</span>
            <img id="mainProductImg" src="assets/images/stage1.png" alt="Sữa Nutura Stage 1" class="h-96 mx-auto object-contain hover:scale-105 transition duration-300">
          </div>
          <div class="grid grid-cols-3 gap-3">
            <button onclick="document.getElementById('mainProductImg').src='assets/images/stage1.png'" class="p-2 bg-[#FAF7F2] rounded-2xl border border-stone-200 hover:border-[#FF6F78] transition">
              <img src="assets/images/stage1.png" alt="Mặt trước lon sữa" class="h-16 mx-auto object-contain">
            </button>
            <button onclick="document.getElementById('mainProductImg').src='assets/images/sachet-stage1.jpg'" class="p-2 bg-[#FAF7F2] rounded-2xl border border-stone-200 hover:border-[#FF6F78] transition">
              <img src="assets/images/sachet-stage1.jpg" alt="Gói dùng thử sachet" class="h-16 mx-auto object-contain">
            </button>
            <button onclick="document.getElementById('mainProductImg').src='assets/images/aco-logo.png'" class="p-2 bg-[#FAF7F2] rounded-2xl border border-stone-200 hover:border-[#FF6F78] transition">
              <img src="assets/images/aco-logo.png" alt="Chứng nhận hữu cơ" class="h-16 mx-auto object-contain">
            </button>
          </div>
        </div>

        <!-- Purchase Info -->
        <div class="lg:col-span-6 space-y-6">
          <div class="space-y-2">
            <div class="flex items-center gap-2">
              <span class="text-xs text-stone-500 font-semibold">Thông tin sản phẩm theo nhãn Stage 1</span>
            </div>
            <h1 class="text-3xl sm:text-4xl font-bold text-stone-900 leading-tight">
              Sữa Công Thức Hữu Cơ Nutura Stage 1
            </h1>
            <p class="text-sm font-semibold text-[#FF6F78]">Dành cho trẻ sơ sinh từ 0 đến 6 tháng tuổi • Khối lượng tịnh: 800g</p>
          </div>

          <p class="text-stone-600 text-sm leading-relaxed">
            Nutura Stage 1 sử dụng <strong>sữa hữu cơ đạm A2 từ Úc</strong>, kết hợp đạm Whey và Casein theo tỷ lệ 60 : 40 cùng chất xơ GOS, FOS. Sữa mẹ là thức ăn tốt nhất cho trẻ sơ sinh và trẻ nhỏ; hãy hỏi ý kiến chuyên gia y tế trước khi dùng sữa công thức.
          </p>

          <!-- Price & Options Box -->
          <div class="p-5 bg-[#FAF7F2] rounded-2xl border border-stone-200/80 space-y-4">
            <div class="flex items-baseline justify-between">
              <div>
                <span class="text-3xl font-bold text-[#FF6F78]">780.000 đ</span>
                <span class="text-xs text-stone-400 ml-2">≈ $46.00 AUD (Giá niêm yết tại Úc)</span>
              </div>
              <span class="text-xs bg-emerald-100 text-emerald-800 font-bold px-2.5 py-1 rounded-full">Còn hàng</span>
            </div>

            <!-- Purchase Options -->
            <div class="space-y-2 text-xs">
              <label class="flex items-center justify-between p-3 bg-white rounded-xl border-2 border-[#FF6F78] cursor-pointer">
                <div class="flex items-center gap-2">
                  <input type="radio" name="buyOption" checked class="custom-checkbox">
                  <span class="font-bold text-stone-800">Mua lẻ từng lon (800g)</span>
                </div>
                <span class="font-bold text-[#FF6F78]">780.000 đ</span>
              </label>

              <label class="flex items-center justify-between p-3 bg-white rounded-xl border border-stone-200 hover:border-stone-400 cursor-pointer">
                <div class="flex items-center gap-2">
                  <input type="radio" name="buyOption" class="custom-checkbox">
                  <span class="font-bold text-stone-800">Đăng ký giao định kỳ Milkman (Tiết kiệm 15%)</span>
                </div>
                <div class="text-right">
                  <span class="font-bold text-emerald-600">663.000 đ</span>
                  <span class="block text-[10px] text-stone-400">+ Miễn phí ship</span>
                </div>
              </label>
            </div>

            <!-- Action buttons -->
            <div class="flex items-center gap-4 pt-2">
              <div class="flex items-center border border-stone-300 rounded-full bg-white">
                <button aria-label="Giảm số lượng" onclick="let q=document.getElementById('prodQty'); if(parseInt(q.value)>1) q.value=parseInt(q.value)-1;" class="w-10 h-10 flex items-center justify-center text-stone-600 hover:text-black font-bold min-h-[44px] min-w-[44px]">-</button>
                <label for="prodQty" class="sr-only">Số lượng sản phẩm</label>
                <input type="number" id="prodQty" value="1" min="1" aria-label="Số lượng sản phẩm" class="w-12 text-center text-sm font-bold border-none focus:outline-none">
                <button aria-label="Tăng số lượng" onclick="let q=document.getElementById('prodQty'); q.value=parseInt(q.value)+1;" class="w-10 h-10 flex items-center justify-center text-stone-600 hover:text-black font-bold min-h-[44px] min-w-[44px]">+</button>
              </div>

              <button onclick="const q=parseInt(document.getElementById('prodQty').value||1); window.nuturaCart.addItem('stage-1', q);" class="flex-1 py-3 px-6 bg-[#FF6F78] hover:bg-[#E65A63] text-white font-bold rounded-full transition shadow-lg shadow-[#FF6F78]/30 text-sm flex items-center justify-center gap-2">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"/>
                </svg>
                <span>Thêm Vào Giỏ Hàng</span>
              </button>
            </div>
          </div>

          <!-- Feature Highlights Checklist -->
          <div class="grid grid-cols-2 gap-3 pt-2 text-xs text-stone-700">
            <div class="flex items-center gap-2">
              <span class="text-emerald-500 font-bold">✓</span> Đạm tươi A2 từ bò ăn cỏ Úc
            </div>
            <div class="flex items-center gap-2">
              <span class="text-emerald-500 font-bold">✓</span> Đạm Whey chiếm ưu thế (60:40)
            </div>
            <div class="flex items-center gap-2">
              <span class="text-emerald-500 font-bold">✓</span> Bổ sung Prebiotics kép GOS & FOS
            </div>
            <div class="flex items-center gap-2">
              <span class="text-emerald-500 font-bold">✓</span> Giàu DHA & ARA phát triển thị giác
            </div>
            <div class="flex items-center gap-2">
              <span class="text-emerald-500 font-bold">✓</span> Chứng nhận hữu cơ ACO theo nhãn
            </div>
            <div class="flex items-center gap-2">
              <span class="text-emerald-500 font-bold">✓</span> Xem thành phần và chứng nhận trên nhãn lon
            </div>
          </div>
        </div>
      </div>

      <!-- DETAILED TABS SECTION -->
      <div class="mt-16 border-t border-stone-200 pt-12">
        <div class="flex border-b border-stone-200 gap-8 overflow-x-auto text-sm font-bold mb-8">
          <button onclick="switchTab('tabNutrition', this)" class="tab-btn pb-3 border-b-2 border-[#FF6F78] text-[#FF6F78]">
            Thành Phần & Dinh Dưỡng
          </button>
          <button onclick="switchTab('tabPreparation', this)" class="tab-btn pb-3 border-b-2 border-transparent text-stone-500 hover:text-stone-800">
            Hướng Dẫn Pha & Bảng Định Lượng
          </button>
          <button onclick="switchTab('tabStorage', this)" class="tab-btn pb-3 border-b-2 border-transparent text-stone-500 hover:text-stone-800">
            Bảo Quản & Lưu Ý An Toàn
          </button>
        </div>

        <!-- Tab 1: Thành phần & Dinh dưỡng -->
        <div id="tabNutrition" class="tab-content space-y-6">
          <div class="bg-stone-50 p-6 rounded-2xl border border-stone-200">
            <h4 class="font-bold text-stone-900 mb-2">Danh Sách Thành Phần Nguyên Liệu:</h4>
            <p class="text-xs text-stone-700 leading-relaxed">
              <strong>Sữa tươi hữu cơ đạm A2</strong>, Đường Lactose hữu cơ, Dầu thực vật hữu cơ (Dầu hạt cải Canola, Dầu hoa hướng dương, Dầu dừa), Đạm Whey cô đặc hữu cơ, Galacto-Oligosaccharides hữu cơ (GOS), Fructo-Oligosaccharides (FOS), Axit Arachidonic (ARA), Axit Docosahexaenoic (DHA - chiết xuất từ dầu cá ngừ tự nhiên).
            </p>
            <h4 class="font-bold text-stone-900 mt-4 mb-2">Hệ Vi Chất Vitamins & Khoáng Chất:</h4>
            <p class="text-xs text-stone-600 leading-relaxed">
              <strong>Vitamins:</strong> Choline Bitartrate, Inositol, Niacinamide (Vitamin B3), Vitamin A Acetate, Vitamin E Acetate, Cholecalciferol (Vitamin D3), D-Calcium Pantothenate (Vitamin B5), Thiamine Hydrochloride (Vitamin B1), Pyridoxine Hydrochloride (Vitamin B6), Riboflavin (Vitamin B2), Phytonadione (Vitamin K1), Axit Folic, D-Biotin.<br>
              <strong>Khoáng chất:</strong> Canxi Carbonate, Ferric Pyrophosphate (Sắt sinh học), Kẽm Sulphate, Magie Carbonate, Đồng Sulphate, Mangan Sulphate, Natri Selenite.<br>
              <em>*Thông tin dị ứng trên nhãn: chứa sữa, đậu nành và dầu cá.</em>
            </p>
          </div>

          <!-- Bảng NIP chuẩn -->
          <div>
            <h4 class="font-bold text-stone-900 mb-3 text-base">Bảng Giá Trị Dinh Dưỡng Trung Bình (Nutrition Information Panel - NIP):</h4>
            <div class="overflow-x-auto rounded-2xl border border-stone-200">
              <table class="nutrition-table">
                <thead>
                  <tr>
                    <th scope="col">Chỉ Số Dinh Dưỡng</th>
                    <th scope="col">Đơn Vị</th>
                    <th scope="col">Trong 100ml Sữa Đã Pha</th>
                    <th scope="col">Trong 100g Bột Sữa</th>
                  </tr>
                </thead>
                <tbody>
                  <tr><td>Năng lượng (Energy)</td><td>kJ / kcal</td><td>293 / 70</td><td>2122 / 507</td></tr>
                  <tr><td>Chất đạm (Protein)</td><td>g</td><td>1.7</td><td>12.6</td></tr>
                  <tr><td>- Whey / Casein</td><td>g</td><td>1.0 / 0.7</td><td>7.5 / 5.0</td></tr>
                  <tr><td>Chất béo (Fat, total)</td><td>g</td><td>3.8</td><td>28</td></tr>
                  <tr><td>- Axit béo Linoleic</td><td>g</td><td>0.7</td><td>4.8</td></tr>
                  <tr><td>- DHA (Docosahexaenoic Acid)</td><td>mg</td><td>12.7</td><td>92</td></tr>
                  <tr><td>- ARA (Arachidonic Acid)</td><td>mg</td><td>12.7</td><td>92</td></tr>
                  <tr><td>Carbohydrate</td><td>g</td><td>7.4</td><td>54</td></tr>
                  <tr><td>Prebiotic GOS</td><td>g</td><td>0.21</td><td>1.5</td></tr>
                  <tr><td>Prebiotic FOS</td><td>g</td><td>0.13</td><td>1.0</td></tr>
                  <tr><td>Vitamin A</td><td>µg RE</td><td>76</td><td>553</td></tr>
                  <tr><td>Vitamin D</td><td>µg</td><td>1.4</td><td>10.0</td></tr>
                  <tr><td>Vitamin E</td><td>mg α-TE</td><td>0.8</td><td>5.8</td></tr>
                  <tr><td>Vitamin C</td><td>mg</td><td>11.1</td><td>80</td></tr>
                  <tr><td>Canxi (Calcium)</td><td>mg</td><td>53</td><td>383</td></tr>
                  <tr><td>Sắt (Iron)</td><td>mg</td><td>0.8</td><td>5.5</td></tr>
                  <tr><td>Kẽm (Zinc)</td><td>mg</td><td>0.5</td><td>3.3</td></tr>
                  <tr><td>Choline</td><td>mg</td><td>14.7</td><td>107</td></tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- Tab 2: Hướng dẫn pha & Bảng định lượng -->
        <div id="tabPreparation" class="tab-content space-y-6 hidden">
          <div class="grid grid-cols-1 md:grid-cols-5 gap-4 text-center">
            <div class="p-4 bg-stone-50 rounded-2xl border border-stone-200">
              <div class="w-8 h-8 rounded-full bg-[#FF6F78] text-white flex items-center justify-center font-bold mx-auto mb-2 text-xs">1</div>
              <h5 class="font-bold text-xs text-stone-900 mb-1">Rửa Tay Sạch Sẽ</h5>
              <p class="text-[11px] text-stone-500">Rửa tay bằng xà phòng và tiệt trùng dụng cụ pha sữa.</p>
            </div>
            <div class="p-4 bg-stone-50 rounded-2xl border border-stone-200">
              <div class="w-8 h-8 rounded-full bg-[#FF6F78] text-white flex items-center justify-center font-bold mx-auto mb-2 text-xs">2</div>
              <h5 class="font-bold text-xs text-stone-900 mb-1">Đun Nước & Làm Nguội</h5>
              <p class="text-[11px] text-stone-500">Đun sôi nước uống trong 5 phút rồi để nguội; làm theo hướng dẫn trên lon.</p>
            </div>
            <div class="p-4 bg-stone-50 rounded-2xl border border-stone-200">
              <div class="w-8 h-8 rounded-full bg-[#FF6F78] text-white flex items-center justify-center font-bold mx-auto mb-2 text-xs">3</div>
              <h5 class="font-bold text-xs text-stone-900 mb-1">Rót Nước Vào Bình</h5>
              <p class="text-[11px] text-stone-500">Rót đúng lượng nước cần thiết theo bảng khẩu phần.</p>
            </div>
            <div class="p-4 bg-stone-50 rounded-2xl border border-stone-200">
              <div class="w-8 h-8 rounded-full bg-[#FF6F78] text-white flex items-center justify-center font-bold mx-auto mb-2 text-xs">4</div>
              <h5 class="font-bold text-xs text-stone-900 mb-1">Đong Bột Gạt Ngang</h5>
              <p class="text-[11px] text-stone-500">1 muỗng gạt ngang (4,6 g) cho 30 ml nước đun sôi để nguội.</p>
            </div>
            <div class="p-4 bg-stone-50 rounded-2xl border border-stone-200">
              <div class="w-8 h-8 rounded-full bg-[#FF6F78] text-white flex items-center justify-center font-bold mx-auto mb-2 text-xs">5</div>
              <h5 class="font-bold text-xs text-stone-900 mb-1">Lắc Đều & Thử Nhiệt</h5>
              <p class="text-[11px] text-stone-500">Lắc nhẹ cho tan hết bột, nhỏ vài giọt lên cổ tay thử ấm.</p>
            </div>
          </div>

          <h4 class="font-bold text-stone-900 pt-4 mb-3 text-base">Bảng Khẩu Phần Ăn Khuyến Nghị (Feeding Guide):</h4>
          <div class="overflow-x-auto rounded-2xl border border-stone-200">
            <table class="nutrition-table">
              <thead>
                <tr>
                  <th scope="col">Độ Tuổi Của Bé</th>
                  <th scope="col">Lượng Nước Nguội (ml)</th>
                  <th scope="col">Số Muỗng Gạt (4,6 g/muỗng)</th>
                  <th scope="col">Số Bữa Ăn Mỗi Ngày</th>
                </tr>
              </thead>
              <tbody>
                <tr><td>0 - 2 tuần tuổi</td><td>60 ml</td><td>2 muỗng</td><td>7 - 8 lần</td></tr>
                <tr><td>2 - 4 tuần tuổi</td><td>90 ml</td><td>3 muỗng</td><td>6 - 7 lần</td></tr>
                <tr><td>1 - 2 tháng tuổi</td><td>120 ml</td><td>4 muỗng</td><td>5 - 6 lần</td></tr>
                <tr><td>2 - 4 tháng tuổi</td><td>150 ml</td><td>5 muỗng</td><td>4 - 5 lần</td></tr>
                <tr><td>4 - 6 tháng tuổi</td><td>180 ml</td><td>6 muỗng</td><td>4 - 5 lần</td></tr>
              </tbody>
            </table>
          </div>
          <p class="text-[11px] text-stone-500 italic">*Chỉ dùng muỗng kèm trong lon. Pha đúng tỷ lệ 1 muỗng gạt ngang/30 ml nước; không tự ý thay đổi tỷ lệ trừ khi có chỉ định y tế. Sữa mẹ là thức ăn tốt nhất cho trẻ sơ sinh và trẻ nhỏ. Tham khảo chuyên gia y tế trước khi dùng sữa công thức.</p>
        </div>

        <!-- Tab 3: Bảo quản -->
        <div id="tabStorage" class="tab-content space-y-4 hidden">
          <div class="bg-amber-50 p-6 rounded-2xl border border-amber-200 text-xs text-stone-700 space-y-3">
            <h4 class="font-bold text-amber-900 text-sm">Hướng Dẫn Bảo Quản Đúng Cách Để Đảm Bảo Dinh Dưỡng:</h4>
            <p>• <strong>Thời hạn sau mở nắp:</strong> Đậy kín lon và dùng trong thời hạn ghi trên nhãn thực tế.</p>
            <p>• <strong>Điều kiện bảo quản:</strong> Bảo quản lon sữa ở nơi khô ráo, thoáng mát tránh ánh nắng trực tiếp hoặc khu vực có độ ẩm cao như bồn rửa chén.</p>
            <p>• <strong>Không để trong tủ lạnh:</strong> Độ ẩm trong tủ lạnh có thể khiến bột sữa bị vón cục và mất đi tính tơi xốp tự nhiên.</p>
            <p>• <strong>Sữa đã pha:</strong> Cho bé dùng ngay sau khi pha. Nếu chưa dùng, đậy kín bình để trong ngăn mát tủ lạnh và dùng hết trong 24 giờ. Bỏ phần sữa còn lại trong bình sau khi bé bú; không dùng lại.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Script for Switching Tabs -->
  <script>
    function switchTab(tabId, btn) {
      document.querySelectorAll('.tab-content').forEach(tab => tab.classList.add('hidden'));
      document.querySelectorAll('.tab-btn').forEach(b => {
        b.classList.remove('border-[#FF6F78]', 'text-[#FF6F78]');
        b.classList.add('border-transparent', 'text-stone-500');
      });

      const target = document.getElementById(tabId);
      if (target) target.classList.remove('hidden');
      if (btn) {
        btn.classList.add('border-[#FF6F78]', 'text-[#FF6F78]');
        btn.classList.remove('border-transparent', 'text-stone-500');
      }
    }
  </script>
"""

    content += render_footer()
    return content

print("Product Stage 1 builder ready.")
