# -*- coding: utf-8 -*-
"""
Trang chi tiết sản phẩm Stage 2 & Stage 3
- Stage 2: Nutura Organic A2 Protein Follow-on Formula (6 - 12 tháng)
- Stage 3: Nutura Organic A2 Protein Toddler Milk Drink (12 - 36 tháng)
Tuân thủ Nghị định 100/2014/NĐ-CP và tiêu chuẩn WHO
"""

from build_site import render_head, render_topbar, render_navbar, render_footer, render_breast_milk_banner

def build_product_stage2():
    content = render_head(
        title="Nutura Organic A2 Protein Follow-on Formula Stage 2 (6 - 12 tháng) 800g",
        description="Thông tin sản phẩm dinh dưỡng công thức Nutura Organic Stage 2 cho bé từ 6 đến 12 tháng tuổi; đạm A2 từ Úc, đạm casein 60%, có bổ sung DHA, ARA và chất xơ GOS/FOS.",
        canonical_url="product-stage2.html"
    )
    content += render_topbar()
    content += render_breast_milk_banner()
    content += render_navbar(active_page="products")

    content += """
  <!-- Breadcrumb -->
  <div class="bg-[#FAF7F2] py-3.5 border-b border-stone-200/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-xs text-stone-500 flex items-center gap-2">
      <a href="index.html" class="hover:text-[#FF6F78]">Trang chủ</a>
      <span>/</span>
      <span class="text-stone-400">Sản phẩm</span>
      <span>/</span>
      <span class="text-stone-800 font-bold">Nutura Organic Stage 2</span>
    </div>
  </div>

  <!-- Chi tiết sản phẩm -->
  <main id="main-content" class="py-10 lg:py-14 bg-white flex-1">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-start">
        
        <!-- Gallery -->
        <div class="lg:col-span-6 space-y-4">
          <div class="bg-[#FAF7F2] rounded-3xl p-6 sm:p-10 border border-stone-200/80 text-center relative overflow-hidden">
            <span class="absolute top-4 left-4 px-3 py-1 rounded-full text-xs font-bold bg-amber-50 text-amber-700 border border-amber-200">6 - 12 tháng</span>
            <span class="absolute top-4 right-4 bg-emerald-100 text-emerald-800 px-3 py-1 rounded-full text-xs font-bold">Hữu cơ ACO</span>
            <img id="mainProductImg2" src="assets/images/stage2.png" alt="Lon sữa Nutura Organic Stage 2 800g" class="h-80 sm:h-96 mx-auto object-contain" loading="eager">
          </div>
          <div class="grid grid-cols-2 gap-3 max-w-xs mx-auto">
            <button type="button" onclick="document.getElementById('mainProductImg2').src='assets/images/stage2.png'" class="p-2 bg-[#FAF7F2] rounded-2xl border border-stone-200 hover:border-[#FF6F78] transition text-center">
              <img src="assets/images/stage2.png" alt="Mặt trước lon Stage 2" class="h-14 mx-auto object-contain">
              <span class="block text-[10px] text-stone-600 mt-1 font-medium">Mặt trước lon</span>
            </button>
            <button type="button" onclick="document.getElementById('mainProductImg2').src='assets/images/aco-logo.png'" class="p-2 bg-[#FAF7F2] rounded-2xl border border-stone-200 hover:border-[#FF6F78] transition text-center">
              <img src="assets/images/aco-logo.png" alt="Logo chứng nhận hữu cơ ACO" class="h-14 mx-auto object-contain">
              <span class="block text-[10px] text-stone-600 mt-1 font-medium">Chứng nhận ACO</span>
            </button>
          </div>
        </div>

        <!-- Thông tin nhanh & CTA tìm điểm bán -->
        <div class="lg:col-span-6 space-y-6">
          <div class="space-y-2">
            <div class="inline-block text-xs font-bold text-stone-500 uppercase tracking-wider">Thông tin sản phẩm theo nhãn & TCCS 02/2026</div>
            <h1 class="text-2xl sm:text-3xl font-bold text-stone-900 leading-tight">
              Nutura Organic A2 Protein Follow-on Formula Stage 2
            </h1>
            <p class="text-sm font-semibold text-[#FF6F78]">Sản phẩm dinh dưỡng công thức tiếp theo cho trẻ từ 6 đến 12 tháng tuổi</p>
          </div>

          <p class="text-stone-600 text-sm leading-relaxed">
            Nutura Organic Stage 2 được nghiên cứu dành riêng cho giai đoạn bé tập ăn dặm. Tỷ lệ đạm Casein 60% và Whey 40% theo TCCS 02/2026, bổ sung hàm lượng sắt, kẽm, DHA, ARA cùng prebiotic kép GOS và FOS.
          </p>

          <!-- Khối thông tin nhanh -->
          <div class="p-5 bg-[#FAF7F2] rounded-2xl border border-stone-200/80 space-y-4">
            <h3 class="text-xs font-bold text-stone-800 uppercase tracking-wider border-b border-stone-200 pb-2">Thông tin nhanh sản phẩm</h3>
            <div class="grid grid-cols-2 gap-3 text-xs">
              <div>
                <span class="text-stone-500 block text-[11px]">Độ tuổi áp dụng:</span>
                <strong class="text-stone-800">6 - 12 tháng tuổi</strong>
              </div>
              <div>
                <span class="text-stone-500 block text-[11px]">Khối lượng tịnh:</span>
                <strong class="text-stone-800">800g / lon</strong>
              </div>
              <div>
                <span class="text-stone-500 block text-[11px]">Xuất xứ:</span>
                <strong class="text-stone-800">Victoria, Australia</strong>
              </div>
              <div>
                <span class="text-stone-500 block text-[11px]">Chứng nhận:</span>
                <strong class="text-emerald-700">ACO Certified Organic</strong>
              </div>
              <div>
                <span class="text-stone-500 block text-[11px]">Dạng bào chế:</span>
                <strong class="text-stone-800">Bột dinh dưỡng công thức</strong>
              </div>
              <div>
                <span class="text-stone-500 block text-[11px]">Mã vạch (Barcode):</span>
                <strong class="text-stone-800">9350758001288</strong>
              </div>
            </div>

            <div class="pt-2">
              <a href="contact.html#diem-ban" class="block w-full py-3 px-6 text-center bg-[#FF6F78] hover:bg-[#E65A63] text-white font-bold rounded-full transition text-xs sm:text-sm shadow-md">
                Tìm điểm bán sản phẩm gần bạn
              </a>
              <p class="text-[11px] text-stone-500 text-center mt-2">Website chỉ cung cấp thông tin tra cứu nhãn, không bán hàng trực tuyến.</p>
            </div>
          </div>

          <div class="p-3.5 bg-amber-50 rounded-xl border border-amber-200 text-xs text-stone-700 leading-relaxed">
            <strong>Khuyến cáo:</strong> Sữa mẹ là thức ăn tốt nhất cho sức khoẻ và sự phát triển toàn diện của trẻ nhỏ. Từ 6 tháng tuổi, trẻ cần được ăn bổ sung các thực phẩm dinh dưỡng khác bên cạnh sữa mẹ hoặc sản phẩm dinh dưỡng công thức theo chỉ dẫn của bác sĩ.
          </div>
        </div>
      </div>

      <!-- Tabs chi tiết -->
      <div class="mt-14 pt-8 border-t border-stone-200">
        <div class="flex flex-wrap gap-4 border-b border-stone-200 text-xs sm:text-sm font-bold mb-6" role="tablist">
          <button type="button" onclick="switchTab('tabNutrition2', this)" class="tab-btn pb-3 border-b-2 border-[#FF6F78] text-[#FF6F78] transition">
            1. Thành phần & bảng dinh dưỡng
          </button>
          <button type="button" onclick="switchTab('tabPreparation2', this)" class="tab-btn pb-3 border-b-2 border-transparent text-stone-500 hover:text-stone-800 transition">
            2. Cách pha & định lượng
          </button>
          <button type="button" onclick="switchTab('tabStorage2', this)" class="tab-btn pb-3 border-b-2 border-transparent text-stone-500 hover:text-stone-800 transition">
            3. Hướng dẫn bảo quản
          </button>
        </div>

        <!-- Tab 1: Thành phần & Dinh dưỡng Stage 2 -->
        <div id="tabNutrition2" class="tab-content space-y-6">
          <div class="space-y-3">
            <h4 class="font-bold text-stone-900 text-sm sm:text-base">Thành phần nguyên liệu (theo nhãn sản phẩm Stage 2):</h4>
            <p class="text-xs text-stone-700 leading-relaxed bg-stone-50 p-4 rounded-2xl border border-stone-200">
              Sữa tươi nguyên chất đạm A2 hữu cơ (Fresh Organic A2 Protein Milk), Đường lactose hữu cơ, Dầu thực vật hữu cơ (Dầu hạt cải, Dầu hướng dương, Dầu dừa), Đạm whey cô đặc hữu cơ (Organic Whey Protein Concentrate), Galacto-oligosaccharide hữu cơ (GOS), Fructo-oligosaccharide (FOS), Axit Arachidonic (ARA), Axit Docosahexaenoic (DHA từ dầu cá). <strong>Khoáng chất:</strong> Kali clorua, Natri citrat, Canxi cacbonat, Sắt pyrophosphat, Magie cacbonat, Kẽm sulfat, Đồng sulfat, Mangan sulfat, Natri selenit. <strong>Vitamin:</strong> Choline bitartrate, Inositol, Niacinamide (Vitamin B3), Vitamin A axetat, Vitamin E axetat, Cholecalciferol (Vitamin D3), D-Canxi pantothenate, Thiamine hydrochloride (Vitamin B1), Pyridoxine hydrochloride (Vitamin B6), Riboflavin (Vitamin B2), Phytonadione (Vitamin K1), Axit folic, D-Biotin.
            </p>
            <p class="text-xs text-rose-700 font-semibold">
              Thông tin dị ứng: Sản phẩm có chứa sữa, đậu nành và dầu cá.
            </p>
          </div>

          <div>
            <h4 class="font-bold text-stone-900 mb-2 text-sm sm:text-base">Bảng giá trị dinh dưỡng trung bình (theo nhãn Stage 2 và TCCS 02/2026):</h4>
            <div class="overflow-x-auto rounded-2xl border border-stone-200">
              <table class="nutrition-table text-xs w-full min-w-[540px]">
                <thead>
                  <tr>
                    <th scope="col" class="p-3 bg-stone-100 text-stone-800 text-left font-bold">Chỉ số dinh dưỡng</th>
                    <th scope="col" class="p-3 bg-stone-100 text-stone-800 text-left font-bold">Đơn vị</th>
                    <th scope="col" class="p-3 bg-stone-100 text-stone-800 text-left font-bold">Trong 100 ml sữa đã pha</th>
                    <th scope="col" class="p-3 bg-stone-100 text-stone-800 text-left font-bold">Trong 100 g bột sữa</th>
                    <th scope="col" class="p-3 bg-stone-100 text-stone-800 text-left font-bold">Ghi chú</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-stone-100">
                  <tr class="bg-rose-50/40"><td class="p-2.5 font-bold text-stone-900" colspan="5">Thành phần hoạt tính sinh học tự nhiên</td></tr>
                  <tr><td class="p-2.5 pl-4 font-semibold text-stone-800">Lactoferrin</td><td class="p-2.5">mg</td><td class="p-2.5 font-bold text-[#FF6F78]">1.4</td><td class="p-2.5">10</td><td class="p-2.5 text-stone-500">TCCS: ≥ 1,12 mg/100 ml</td></tr>
                  <tr><td class="p-2.5 pl-4 font-semibold text-stone-800">Immunoglobulins (IgG)</td><td class="p-2.5">mg</td><td class="p-2.5 font-bold text-[#FF6F78]">28</td><td class="p-2.5">200</td><td class="p-2.5 text-stone-500">TCCS: ≥ 19,6 mg/100 ml</td></tr>

                  <tr class="bg-stone-50"><td class="p-2.5 font-bold text-stone-900" colspan="5">Năng lượng & Đạm</td></tr>
                  <tr><td class="p-2.5 pl-4">Năng lượng (Energy)</td><td class="p-2.5">kJ / Cal</td><td class="p-2.5">283 / 68</td><td class="p-2.5">2098 / 501</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>
                  <tr><td class="p-2.5 pl-4">Chất đạm (Protein)</td><td class="p-2.5">g</td><td class="p-2.5">1.7</td><td class="p-2.5">12.9</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>
                  <tr><td class="p-2.5 pl-6 text-stone-600">- Đạm Whey (40%)</td><td class="p-2.5">g</td><td class="p-2.5">0.7</td><td class="p-2.5">5.1</td><td class="p-2.5 text-stone-500">TCCS 02/2026</td></tr>
                  <tr><td class="p-2.5 pl-6 text-stone-600">- Đạm Casein (60%)</td><td class="p-2.5">g</td><td class="p-2.5">1.0</td><td class="p-2.5">7.7</td><td class="p-2.5 text-stone-500">TCCS 02/2026</td></tr>
                  <tr><td class="p-2.5 pl-6 text-stone-600">- Đạm A2-β-Casein</td><td class="p-2.5">g</td><td class="p-2.5">0.4</td><td class="p-2.5">2.7</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>

                  <tr class="bg-stone-50"><td class="p-2.5 font-bold text-stone-900" colspan="5">Chất béo & Axit béo</td></tr>
                  <tr><td class="p-2.5 pl-4">Chất béo tổng số (Fat, total)</td><td class="p-2.5">g</td><td class="p-2.5">3.6</td><td class="p-2.5">27</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>
                  <tr><td class="p-2.5 pl-6 text-stone-600">- DHA</td><td class="p-2.5">mg</td><td class="p-2.5">11.6</td><td class="p-2.5">86</td><td class="p-2.5 text-stone-500">Từ dầu cá</td></tr>
                  <tr><td class="p-2.5 pl-6 text-stone-600">- ARA</td><td class="p-2.5">mg</td><td class="p-2.5">11.6</td><td class="p-2.5">86</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>

                  <tr class="bg-stone-50"><td class="p-2.5 font-bold text-stone-900" colspan="5">Khoáng chất nổi bật cho ăn dặm</td></tr>
                  <tr><td class="p-2.5 pl-4">Canxi (Calcium)</td><td class="p-2.5">mg</td><td class="p-2.5">63</td><td class="p-2.5">464</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>
                  <tr><td class="p-2.5 pl-4">Sắt (Iron)</td><td class="p-2.5">mg</td><td class="p-2.5">0.9</td><td class="p-2.5">6.5</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>
                  <tr><td class="p-2.5 pl-4">Kẽm (Zinc)</td><td class="p-2.5">mg</td><td class="p-2.5">0.5</td><td class="p-2.5">3.9</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>
                  <tr><td class="p-2.5 pl-4">Iốt (Iodine)</td><td class="p-2.5">µg</td><td class="p-2.5">7.1</td><td class="p-2.5">53</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- Tab 2: Hướng dẫn pha Stage 2 -->
        <div id="tabPreparation2" class="tab-content space-y-6 hidden">
          <div class="grid grid-cols-1 md:grid-cols-5 gap-3 text-center">
            <div class="p-4 bg-stone-50 rounded-2xl border border-stone-200">
              <div class="w-7 h-7 rounded-full bg-[#FF6F78] text-white flex items-center justify-center font-bold mx-auto mb-2 text-xs">1</div>
              <h5 class="font-bold text-xs text-stone-900 mb-1">Rửa tay & tiệt trùng</h5>
              <p class="text-[11px] text-stone-500">Rửa tay và tiệt trùng dụng cụ cốc/bình trước khi pha.</p>
            </div>
            <div class="p-4 bg-stone-50 rounded-2xl border border-stone-200">
              <div class="w-7 h-7 rounded-full bg-[#FF6F78] text-white flex items-center justify-center font-bold mx-auto mb-2 text-xs">2</div>
              <h5 class="font-bold text-xs text-stone-900 mb-1">Đun sôi nước uống</h5>
              <p class="text-[11px] text-stone-500">Đun sôi 5 phút và để nguội xuống khoảng 40–50°C.</p>
            </div>
            <div class="p-4 bg-stone-50 rounded-2xl border border-stone-200">
              <div class="w-7 h-7 rounded-full bg-[#FF6F78] text-white flex items-center justify-center font-bold mx-auto mb-2 text-xs">3</div>
              <h5 class="font-bold text-xs text-stone-900 mb-1">Rót nước vào bình</h5>
              <p class="text-[11px] text-stone-500">Rót lượng nước ấm cần thiết theo bảng khẩu phần bên dưới.</p>
            </div>
            <div class="p-4 bg-stone-50 rounded-2xl border border-stone-200">
              <div class="w-7 h-7 rounded-full bg-[#FF6F78] text-white flex items-center justify-center font-bold mx-auto mb-2 text-xs">4</div>
              <h5 class="font-bold text-xs text-stone-900 mb-1">Đong bột gạt ngang</h5>
              <p class="text-[11px] text-stone-500">1 muỗng gạt ngang (4,5 g) pha với 30 ml nước ấm.</p>
            </div>
            <div class="p-4 bg-stone-50 rounded-2xl border border-stone-200">
              <div class="w-7 h-7 rounded-full bg-[#FF6F78] text-white flex items-center justify-center font-bold mx-auto mb-2 text-xs">5</div>
              <h5 class="font-bold text-xs text-stone-900 mb-1">Lắc đều & thử nhiệt</h5>
              <p class="text-[11px] text-stone-500">Lắc đều cho tan hết bột, kiểm tra độ ấm trước khi cho bé dùng.</p>
            </div>
          </div>

          <h4 class="font-bold text-stone-900 pt-2 text-sm sm:text-base">Bảng khẩu phần ăn khuyến nghị (Feeding Guide Stage 2):</h4>
          <div class="overflow-x-auto rounded-2xl border border-stone-200">
            <table class="nutrition-table text-xs w-full min-w-[540px]">
              <thead>
                <tr>
                  <th scope="col" class="p-3 bg-stone-100 text-stone-800 text-left font-bold">Độ tuổi của bé</th>
                  <th scope="col" class="p-3 bg-stone-100 text-stone-800 text-left font-bold">Lượng nước ấm (ml)</th>
                  <th scope="col" class="p-3 bg-stone-100 text-stone-800 text-left font-bold">Số muỗng gạt (4,5 g/muỗng)</th>
                  <th scope="col" class="p-3 bg-stone-100 text-stone-800 text-left font-bold">Số cữ ăn mỗi ngày</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-stone-100">
                <tr><td class="p-2.5 font-medium">6 - 9 tháng tuổi</td><td class="p-2.5">180 ml</td><td class="p-2.5">6 muỗng</td><td class="p-2.5">4 lần</td></tr>
                <tr><td class="p-2.5 font-medium">9 - 12 tháng tuổi</td><td class="p-2.5">240 ml</td><td class="p-2.5">8 muỗng</td><td class="p-2.5">3 lần</td></tr>
              </tbody>
            </table>
          </div>
          <p class="text-[11px] text-stone-500 italic">*Chỉ sử dụng muỗng lường kèm theo lon. Pha đúng tỷ lệ theo nhãn. Trẻ từ 6 tháng cần chế độ ăn dặm đa dạng kết hợp.</p>
        </div>

        <!-- Tab 3: Bảo quản Stage 2 -->
        <div id="tabStorage2" class="tab-content space-y-4 hidden">
          <div class="bg-stone-50 p-6 rounded-2xl border border-stone-200 text-xs text-stone-700 space-y-3 leading-relaxed">
            <h4 class="font-bold text-stone-900 text-sm">Hướng dẫn bảo quản lon và sữa đã pha:</h4>
            <p>• <strong>Bảo quản lon sữa:</strong> Đậy kín nắp nhựa sau mỗi lần sử dụng. Bảo quản ở nơi khô ráo, thoáng mát dưới 25°C. Không bảo quản trong tủ lạnh.</p>
            <p>• <strong>Thời hạn sử dụng sau mở nắp:</strong> Sử dụng hết lượng sữa trong lon trong vòng 4 tuần kể từ ngày mở nắp.</p>
            <p>• <strong>Sữa sau khi pha:</strong> Cho bé dùng ngay sau khi pha xong. Đổ bỏ phần sữa còn thừa sau mỗi cữ ăn.</p>
          </div>
        </div>

      </div>

    </div>
  </main>
"""
    content += render_footer()
    return content

def build_product_stage3():
    content = render_head(
        title="Nutura Organic A2 Protein Toddler Milk Drink Stage 3 (12 - 36 tháng) 800g",
        description="Thông tin sản phẩm dinh dưỡng công thức Nutura Organic Stage 3 cho trẻ từ 1 đến 3 tuổi; đạm A2 hữu cơ từ Úc, cung cấp 16 vitamin và khoáng chất thiết yếu theo nhãn.",
        canonical_url="product-stage3.html"
    )
    content += render_topbar()
    content += render_breast_milk_banner()
    content += render_navbar(active_page="products")

    content += """
  <!-- Breadcrumb -->
  <div class="bg-[#FAF7F2] py-3.5 border-b border-stone-200/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-xs text-stone-500 flex items-center gap-2">
      <a href="index.html" class="hover:text-[#FF6F78]">Trang chủ</a>
      <span>/</span>
      <span class="text-stone-400">Sản phẩm</span>
      <span>/</span>
      <span class="text-stone-800 font-bold">Nutura Organic Stage 3</span>
    </div>
  </div>

  <!-- Chi tiết sản phẩm Stage 3 -->
  <main id="main-content" class="py-10 lg:py-14 bg-white flex-1">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-start">
        
        <!-- Gallery -->
        <div class="lg:col-span-6 space-y-4">
          <div class="bg-[#FAF7F2] rounded-3xl p-6 sm:p-10 border border-stone-200/80 text-center relative overflow-hidden">
            <span class="absolute top-4 left-4 px-3 py-1 rounded-full text-xs font-bold bg-emerald-50 text-emerald-800 border border-emerald-200">12 - 36 tháng</span>
            <span class="absolute top-4 right-4 bg-emerald-100 text-emerald-800 px-3 py-1 rounded-full text-xs font-bold">Hữu cơ ACO</span>
            <img id="mainProductImg3" src="assets/images/stage3.png" alt="Lon sữa Nutura Organic Stage 3 800g" class="h-80 sm:h-96 mx-auto object-contain" loading="eager">
          </div>
          <div class="grid grid-cols-2 gap-3 max-w-xs mx-auto">
            <button type="button" onclick="document.getElementById('mainProductImg3').src='assets/images/stage3.png'" class="p-2 bg-[#FAF7F2] rounded-2xl border border-stone-200 hover:border-[#FF6F78] transition text-center">
              <img src="assets/images/stage3.png" alt="Mặt trước lon Stage 3" class="h-14 mx-auto object-contain">
              <span class="block text-[10px] text-stone-600 mt-1 font-medium">Mặt trước lon</span>
            </button>
            <button type="button" onclick="document.getElementById('mainProductImg3').src='assets/images/aco-logo.png'" class="p-2 bg-[#FAF7F2] rounded-2xl border border-stone-200 hover:border-[#FF6F78] transition text-center">
              <img src="assets/images/aco-logo.png" alt="Logo chứng nhận hữu cơ ACO" class="h-14 mx-auto object-contain">
              <span class="block text-[10px] text-stone-600 mt-1 font-medium">Chứng nhận ACO</span>
            </button>
          </div>
        </div>

        <!-- Thông tin nhanh & CTA -->
        <div class="lg:col-span-6 space-y-6">
          <div class="space-y-2">
            <div class="inline-block text-xs font-bold text-stone-500 uppercase tracking-wider">Thông tin sản phẩm theo nhãn & TCCS 03/2026</div>
            <h1 class="text-2xl sm:text-3xl font-bold text-stone-900 leading-tight">
              Nutura Organic A2 Protein Toddler Milk Drink Stage 3
            </h1>
            <p class="text-sm font-semibold text-[#FF6F78]">Sản phẩm dinh dưỡng cho trẻ từ 12 đến 36 tháng tuổi</p>
          </div>

          <p class="text-stone-600 text-sm leading-relaxed">
            Nutura Organic Stage 3 bổ sung 16 vitamin và khoáng chất thiết yếu cho giai đoạn trẻ tập đi. Nền tảng sữa tươi farmgate đạm A2 hữu cơ, có chứa DHA, ARA, GOS và FOS theo tiêu chuẩn TCCS 03/2026.
          </p>

          <!-- Khối thông tin nhanh -->
          <div class="p-5 bg-[#FAF7F2] rounded-2xl border border-stone-200/80 space-y-4">
            <h3 class="text-xs font-bold text-stone-800 uppercase tracking-wider border-b border-stone-200 pb-2">Thông tin nhanh sản phẩm</h3>
            <div class="grid grid-cols-2 gap-3 text-xs">
              <div>
                <span class="text-stone-500 block text-[11px]">Độ tuổi áp dụng:</span>
                <strong class="text-stone-800">12 - 36 tháng tuổi (1 - 3 tuổi)</strong>
              </div>
              <div>
                <span class="text-stone-500 block text-[11px]">Khối lượng tịnh:</span>
                <strong class="text-stone-800">800g / lon</strong>
              </div>
              <div>
                <span class="text-stone-500 block text-[11px]">Xuất xứ:</span>
                <strong class="text-stone-800">Victoria, Australia</strong>
              </div>
              <div>
                <span class="text-stone-500 block text-[11px]">Chứng nhận:</span>
                <strong class="text-emerald-700">ACO Certified Organic</strong>
              </div>
              <div>
                <span class="text-stone-500 block text-[11px]">Dạng bào chế:</span>
                <strong class="text-stone-800">Bột dinh dưỡng</strong>
              </div>
              <div>
                <span class="text-stone-500 block text-[11px]">Mã vạch (Barcode):</span>
                <strong class="text-stone-800">9350758001295</strong>
              </div>
            </div>

            <div class="pt-2">
              <a href="contact.html#diem-ban" class="block w-full py-3 px-6 text-center bg-[#FF6F78] hover:bg-[#E65A63] text-white font-bold rounded-full transition text-xs sm:text-sm shadow-md">
                Tìm điểm bán sản phẩm gần bạn
              </a>
              <p class="text-[11px] text-stone-500 text-center mt-2">Website chỉ cung cấp thông tin tra cứu nhãn, không bán hàng trực tuyến.</p>
            </div>
          </div>

          <div class="p-3.5 bg-amber-50 rounded-xl border border-amber-200 text-xs text-stone-700 leading-relaxed">
            <strong>Khuyến cáo:</strong> Sữa mẹ là thức ăn tốt nhất cho sức khoẻ và sự phát triển toàn diện của trẻ nhỏ. Sản phẩm dinh dưỡng công thức dùng bổ sung cho chế độ ăn của trẻ trên 1 tuổi.
          </div>
        </div>
      </div>

      <!-- Tabs chi tiết Stage 3 -->
      <div class="mt-14 pt-8 border-t border-stone-200">
        <div class="flex flex-wrap gap-4 border-b border-stone-200 text-xs sm:text-sm font-bold mb-6" role="tablist">
          <button type="button" onclick="switchTab('tabNutrition3', this)" class="tab-btn pb-3 border-b-2 border-[#FF6F78] text-[#FF6F78] transition">
            1. Thành phần & bảng dinh dưỡng
          </button>
          <button type="button" onclick="switchTab('tabPreparation3', this)" class="tab-btn pb-3 border-b-2 border-transparent text-stone-500 hover:text-stone-800 transition">
            2. Cách pha & định lượng
          </button>
          <button type="button" onclick="switchTab('tabStorage3', this)" class="tab-btn pb-3 border-b-2 border-transparent text-stone-500 hover:text-stone-800 transition">
            3. Hướng dẫn bảo quản
          </button>
        </div>

        <!-- Tab 1: Thành phần & Dinh dưỡng Stage 3 -->
        <div id="tabNutrition3" class="tab-content space-y-6">
          <div class="space-y-3">
            <h4 class="font-bold text-stone-900 text-sm sm:text-base">Thành phần nguyên liệu (theo nhãn sản phẩm Stage 3):</h4>
            <p class="text-xs text-stone-700 leading-relaxed bg-stone-50 p-4 rounded-2xl border border-stone-200">
              Sữa tươi nguyên chất đạm A2 hữu cơ (Fresh Organic A2 Protein Milk), Đường lactose hữu cơ, Dầu thực vật hữu cơ (Dầu hạt cải, Dầu hướng dương, Dầu dừa), Đạm whey cô đặc hữu cơ (Organic Whey Protein Concentrate), Galacto-oligosaccharide hữu cơ (GOS), Fructo-oligosaccharide hữu cơ (FOS), Axit Arachidonic (ARA), Axit Docosahexaenoic (DHA từ dầu cá). <strong>Vitamin:</strong> Axit Ascorbic (Vitamin C), Niacinamide (Vitamin B3), Vitamin A axetat, Vitamin E axetat, Cholecalciferol (Vitamin D3), Thiamine hydrochloride (Vitamin B1), Pyridoxine hydrochloride (Vitamin B6), Riboflavin (Vitamin B2), Axit folic, Cyanocobalamin (Vitamin B12). <strong>Khoáng chất:</strong> Canxi photphat, Kali clorua, Natri citrat, Magie sulfat, Sắt sulfat, Kẽm sulfat.
            </p>
            <p class="text-xs text-rose-700 font-semibold">
              Thông tin dị ứng: Sản phẩm có chứa sữa, đậu nành và dầu cá.
            </p>
          </div>

          <div>
            <h4 class="font-bold text-stone-900 mb-2 text-sm sm:text-base">Bảng giá trị dinh dưỡng trung bình (theo nhãn Stage 3 và TCCS 03/2026):</h4>
            <div class="overflow-x-auto rounded-2xl border border-stone-200">
              <table class="nutrition-table text-xs w-full min-w-[540px]">
                <thead>
                  <tr>
                    <th scope="col" class="p-3 bg-stone-100 text-stone-800 text-left font-bold">Chỉ số dinh dưỡng</th>
                    <th scope="col" class="p-3 bg-stone-100 text-stone-800 text-left font-bold">Đơn vị</th>
                    <th scope="col" class="p-3 bg-stone-100 text-stone-800 text-left font-bold">Trong 100 ml sữa đã pha</th>
                    <th scope="col" class="p-3 bg-stone-100 text-stone-800 text-left font-bold">Trong 100 g bột sữa</th>
                    <th scope="col" class="p-3 bg-stone-100 text-stone-800 text-left font-bold">Ghi chú</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-stone-100">
                  <tr class="bg-rose-50/40"><td class="p-2.5 font-bold text-stone-900" colspan="5">Thành phần hoạt tính sinh học tự nhiên</td></tr>
                  <tr><td class="p-2.5 pl-4 font-semibold text-stone-800">Lactoferrin</td><td class="p-2.5">mg</td><td class="p-2.5 font-bold text-[#FF6F78]">1.6</td><td class="p-2.5">10</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>
                  <tr><td class="p-2.5 pl-4 font-semibold text-stone-800">Immunoglobulins (IgG)</td><td class="p-2.5">mg</td><td class="p-2.5 font-bold text-[#FF6F78]">31</td><td class="p-2.5">200</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>

                  <tr class="bg-stone-50"><td class="p-2.5 font-bold text-stone-900" colspan="5">Năng lượng & Đạm</td></tr>
                  <tr><td class="p-2.5 pl-4">Năng lượng (Energy)</td><td class="p-2.5">kJ / Cal</td><td class="p-2.5">302 / 72</td><td class="p-2.5">1933 / 462</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>
                  <tr><td class="p-2.5 pl-4">Chất đạm (Protein)</td><td class="p-2.5">g</td><td class="p-2.5">2.1</td><td class="p-2.5">14</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>
                  <tr><td class="p-2.5 pl-6 text-stone-600">- Đạm A2-β-Casein</td><td class="p-2.5">g</td><td class="p-2.5">0.5</td><td class="p-2.5">3.0</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>

                  <tr class="bg-stone-50"><td class="p-2.5 font-bold text-stone-900" colspan="5">Chất béo & Axit béo</td></tr>
                  <tr><td class="p-2.5 pl-4">Chất béo tổng số (Fat, total)</td><td class="p-2.5">g</td><td class="p-2.5">2.9</td><td class="p-2.5">19</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>
                  <tr><td class="p-2.5 pl-6 text-stone-600">- DHA</td><td class="p-2.5">mg</td><td class="p-2.5">14.4</td><td class="p-2.5">92</td><td class="p-2.5 text-stone-500">Từ dầu cá</td></tr>
                  <tr><td class="p-2.5 pl-6 text-stone-600">- ARA</td><td class="p-2.5">mg</td><td class="p-2.5">14.4</td><td class="p-2.5">92</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>

                  <tr class="bg-stone-50"><td class="p-2.5 font-bold text-stone-900" colspan="5">Carbohydrate & Prebiotics</td></tr>
                  <tr><td class="p-2.5 pl-4">Carbohydrate</td><td class="p-2.5">g</td><td class="p-2.5">9.7</td><td class="p-2.5">62</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>
                  <tr><td class="p-2.5 pl-6 text-stone-600">- Đường tự nhiên (Sugars)</td><td class="p-2.5">g</td><td class="p-2.5">9.2</td><td class="p-2.5">59</td><td class="p-2.5 text-stone-500">Lactose tự nhiên</td></tr>
                  <tr><td class="p-2.5 pl-4">Prebiotic GOS / FOS</td><td class="p-2.5">g</td><td class="p-2.5">0.15 / 0.15</td><td class="p-2.5">1.0 / 1.0</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>

                  <tr class="bg-stone-50"><td class="p-2.5 font-bold text-stone-900" colspan="5">Khoáng chất tiêu biểu</td></tr>
                  <tr><td class="p-2.5 pl-4">Canxi (Calcium)</td><td class="p-2.5">mg</td><td class="p-2.5">94</td><td class="p-2.5">600</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>
                  <tr><td class="p-2.5 pl-4">Sắt (Iron)</td><td class="p-2.5">mg</td><td class="p-2.5">1.3</td><td class="p-2.5">8.6</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>
                  <tr><td class="p-2.5 pl-4">Kẽm (Zinc)</td><td class="p-2.5">mg</td><td class="p-2.5">0.5</td><td class="p-2.5">2.9</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>
                  <tr><td class="p-2.5 pl-4">Vitamin D</td><td class="p-2.5">µg</td><td class="p-2.5">1.5</td><td class="p-2.5">9.7</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>
                  <tr><td class="p-2.5 pl-4">Vitamin C</td><td class="p-2.5">mg</td><td class="p-2.5">15.5</td><td class="p-2.5">99</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- Tab 2: Hướng dẫn pha Stage 3 -->
        <div id="tabPreparation3" class="tab-content space-y-6 hidden">
          <div class="grid grid-cols-1 md:grid-cols-5 gap-3 text-center">
            <div class="p-4 bg-stone-50 rounded-2xl border border-stone-200">
              <div class="w-7 h-7 rounded-full bg-[#FF6F78] text-white flex items-center justify-center font-bold mx-auto mb-2 text-xs">1</div>
              <h5 class="font-bold text-xs text-stone-900 mb-1">Rửa tay sạch sẽ</h5>
              <p class="text-[11px] text-stone-500">Rửa sạch tay và tiệt trùng cốc uống nước của bé.</p>
            </div>
            <div class="p-4 bg-stone-50 rounded-2xl border border-stone-200">
              <div class="w-7 h-7 rounded-full bg-[#FF6F78] text-white flex items-center justify-center font-bold mx-auto mb-2 text-xs">2</div>
              <h5 class="font-bold text-xs text-stone-900 mb-1">Chuẩn bị nước sạch</h5>
              <p class="text-[11px] text-stone-500">Đun sôi nước uống và để nguội xuống nhiệt độ ấm thích hợp.</p>
            </div>
            <div class="p-4 bg-stone-50 rounded-2xl border border-stone-200">
              <div class="w-7 h-7 rounded-full bg-[#FF6F78] text-white flex items-center justify-center font-bold mx-auto mb-2 text-xs">3</div>
              <h5 class="font-bold text-xs text-stone-900 mb-1">Đo lượng nước</h5>
              <p class="text-[11px] text-stone-500">Rót 200 ml nước ấm vào cốc uống.</p>
            </div>
            <div class="p-4 bg-stone-50 rounded-2xl border border-stone-200">
              <div class="w-7 h-7 rounded-full bg-[#FF6F78] text-white flex items-center justify-center font-bold mx-auto mb-2 text-xs">4</div>
              <h5 class="font-bold text-xs text-stone-900 mb-1">Đong bột gạt ngang</h5>
              <p class="text-[11px] text-stone-500">Thêm 6 muỗng gạt ngang (khoảng 6g/muỗng) vào 200 ml nước.</p>
            </div>
            <div class="p-4 bg-stone-50 rounded-2xl border border-stone-200">
              <div class="w-7 h-7 rounded-full bg-[#FF6F78] text-white flex items-center justify-center font-bold mx-auto mb-2 text-xs">5</div>
              <h5 class="font-bold text-xs text-stone-900 mb-1">Khuấy đều cho tan</h5>
              <p class="text-[11px] text-stone-500">Khuấy đều cho bột tan hoàn toàn và cho bé uống ngay.</p>
            </div>
          </div>

          <h4 class="font-bold text-stone-900 pt-2 text-sm sm:text-base">Bảng khẩu phần khuyến nghị (Feeding Guide Stage 3):</h4>
          <div class="overflow-x-auto rounded-2xl border border-stone-200">
            <table class="nutrition-table text-xs w-full min-w-[540px]">
              <thead>
                <tr>
                  <th scope="col" class="p-3 bg-stone-100 text-stone-800 text-left font-bold">Độ tuổi của trẻ</th>
                  <th scope="col" class="p-3 bg-stone-100 text-stone-800 text-left font-bold">Lượng nước ấm (ml)</th>
                  <th scope="col" class="p-3 bg-stone-100 text-stone-800 text-left font-bold">Số muỗng gạt (6g/muỗng)</th>
                  <th scope="col" class="p-3 bg-stone-100 text-stone-800 text-left font-bold">Số cữ uống mỗi ngày</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-stone-100">
                <tr><td class="p-2.5 font-medium">Từ 12 tháng tuổi trở lên</td><td class="p-2.5">200 ml</td><td class="p-2.5">6 muỗng</td><td class="p-2.5">1 - 2 lần</td></tr>
              </tbody>
            </table>
          </div>
          <p class="text-[11px] text-stone-500 italic">*Chỉ sử dụng muỗng lường kèm theo lon. Pha đúng tỷ lệ theo nhãn. Sản phẩm dinh dưỡng dùng kết hợp với bữa ăn hàng ngày của bé.</p>
        </div>

        <!-- Tab 3: Bảo quản Stage 3 -->
        <div id="tabStorage3" class="tab-content space-y-4 hidden">
          <div class="bg-stone-50 p-6 rounded-2xl border border-stone-200 text-xs text-stone-700 space-y-3 leading-relaxed">
            <h4 class="font-bold text-stone-900 text-sm">Hướng dẫn bảo quản lon và sữa đã pha:</h4>
            <p>• <strong>Bảo quản lon sữa:</strong> Đậy kín nắp nhựa sau mỗi lần sử dụng. Bảo quản ở nơi khô ráo, thoáng mát dưới 25°C. Không để trong tủ lạnh.</p>
            <p>• <strong>Thời hạn sử dụng sau mở nắp:</strong> Sử dụng hết trong vòng 4 tuần kể từ ngày mở nắp lon.</p>
            <p>• <strong>Sữa sau khi pha:</strong> Cho bé uống ngay sau khi pha xong. Không bảo quản lại phần sữa bé uống dở.</p>
          </div>
        </div>

      </div>

    </div>
  </main>
"""
    content += render_footer()
    return content

print("pages_products_stage2_3_4.py ready")
