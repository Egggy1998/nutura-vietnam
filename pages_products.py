# -*- coding: utf-8 -*-
"""
Trang chi tiết sản phẩm Stage 1
Nutura Organic A2 Protein Infant Formula Stage 1 (0 - 6 tháng)
Tuân thủ Nghị định 100/2014/NĐ-CP và tiêu chuẩn WHO
"""

from build_site import render_head, render_topbar, render_navbar, render_footer, render_breast_milk_banner

def build_product_stage1():
    content = render_head(
        title="Nutura Organic A2 Protein Infant Formula Stage 1 (0 - 6 tháng) 800g",
        description="Thông tin sản phẩm dinh dưỡng công thức Nutura Organic Stage 1 cho trẻ từ 0 đến 6 tháng tuổi; sữa hữu cơ đạm A2 từ Úc, đạm whey 60%, có chứa Lactoferrin và IgG theo TCCS.",
        canonical_url="product-stage1.html"
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
      <span class="text-stone-800 font-bold">Nutura Organic Stage 1</span>
    </div>
  </div>

  <!-- Chi tiết sản phẩm -->
  <main id="main-content" class="py-10 lg:py-14 bg-white flex-1">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-start">
        
        <!-- Cột hình ảnh sản phẩm -->
        <div class="lg:col-span-6 space-y-4">
          <div class="bg-[#FAF7F2] rounded-3xl p-6 sm:p-10 border border-stone-200/80 text-center relative overflow-hidden">
            <span class="absolute top-4 left-4 px-3 py-1 rounded-full text-xs font-bold bg-blue-50 text-blue-700 border border-blue-200">0 - 6 tháng</span>
            <span class="absolute top-4 right-4 bg-emerald-100 text-emerald-800 px-3 py-1 rounded-full text-xs font-bold">Hữu cơ ACO</span>
            <img id="mainProductImg" src="assets/images/stage1.png" alt="Lon sữa Nutura Organic Stage 1 800g" class="h-80 sm:h-96 mx-auto object-contain" loading="eager">
          </div>
          <!-- Thumbnails -->
          <div class="grid grid-cols-2 gap-3 max-w-xs mx-auto">
            <button type="button" onclick="document.getElementById('mainProductImg').src='assets/images/stage1.png'" class="p-2 bg-[#FAF7F2] rounded-2xl border border-stone-200 hover:border-[#FF6F78] transition text-center">
              <img src="assets/images/stage1.png" alt="Mặt trước lon Stage 1" class="h-14 mx-auto object-contain">
              <span class="block text-[10px] text-stone-600 mt-1 font-medium">Mặt trước lon</span>
            </button>
            <button type="button" onclick="document.getElementById('mainProductImg').src='assets/images/aco-logo.png'" class="p-2 bg-[#FAF7F2] rounded-2xl border border-stone-200 hover:border-[#FF6F78] transition text-center">
              <img src="assets/images/aco-logo.png" alt="Logo chứng nhận hữu cơ ACO" class="h-14 mx-auto object-contain">
              <span class="block text-[10px] text-stone-600 mt-1 font-medium">Chứng nhận ACO</span>
            </button>
          </div>
        </div>

        <!-- Cột thông tin nhanh & CTA tìm điểm bán (Không giá, không nút mua) -->
        <div class="lg:col-span-6 space-y-6">
          <div class="space-y-2">
            <div class="inline-block text-xs font-bold text-stone-500 uppercase tracking-wider">Thông tin sản phẩm theo nhãn & TCCS 01/2026</div>
            <h1 class="text-2xl sm:text-3xl font-bold text-stone-900 leading-tight">
              Nutura Organic A2 Protein Infant Formula Stage 1
            </h1>
            <p class="text-sm font-semibold text-[#FF6F78]">Sản phẩm dinh dưỡng công thức cho trẻ từ 0 đến 6 tháng tuổi</p>
          </div>

          <p class="text-stone-600 text-sm leading-relaxed">
            Nutura Organic Stage 1 sử dụng nguồn <strong>sữa tươi nguyên liệu farmgate đạm A2</strong> từ Úc. Công thức có tỷ lệ đạm whey chiếm 60% và đạm casein 40% theo TCCS 01/2026, đồng thời có chứa Lactoferrin và Immunoglobulin IgG tự nhiên từ sữa.
          </p>

          <!-- Khối thông tin nhanh theo quy định -->
          <div class="p-5 bg-[#FAF7F2] rounded-2xl border border-stone-200/80 space-y-4">
            <h3 class="text-xs font-bold text-stone-800 uppercase tracking-wider border-b border-stone-200 pb-2">Thông tin nhanh sản phẩm</h3>
            <div class="grid grid-cols-2 gap-3 text-xs">
              <div>
                <span class="text-stone-500 block text-[11px]">Độ tuổi áp dụng:</span>
                <strong class="text-stone-800">0 - 6 tháng tuổi</strong>
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
                <strong class="text-stone-800">9350758001271</strong>
              </div>
            </div>

            <!-- Nút CTA duy nhất: Tìm điểm bán -->
            <div class="pt-2">
              <a href="contact.html#diem-ban" class="block w-full py-3 px-6 text-center bg-[#FF6F78] hover:bg-[#E65A63] text-white font-bold rounded-full transition text-xs sm:text-sm shadow-md">
                Tìm điểm bán sản phẩm gần bạn
              </a>
              <p class="text-[11px] text-stone-500 text-center mt-2">Website chỉ cung cấp thông tin tra cứu nhãn, không bán hàng trực tuyến.</p>
            </div>
          </div>

          <!-- Nhắc nhở sữa mẹ theo luật -->
          <div class="p-3.5 bg-amber-50 rounded-xl border border-amber-200 text-xs text-stone-700 leading-relaxed">
            <strong>Khuyến cáo:</strong> Sữa mẹ là thức ăn tốt nhất cho sức khoẻ và sự phát triển toàn diện của trẻ nhỏ. Các yếu tố chống nhiễm khuẩn, đặc biệt là kháng thể chỉ có trong sữa mẹ có tác dụng giúp trẻ phòng, chống bệnh tiêu chảy, nhiễm khuẩn đường hô hấp và một số bệnh nhiễm khuẩn khác. Chỉ sử dụng sản phẩm này theo chỉ dẫn của bác sĩ. Pha chế theo đúng hướng dẫn. Cho trẻ ăn bằng cốc, thìa hợp vệ sinh.
          </div>
        </div>
      </div>

      <!-- Tabs: Thành phần & Dinh dưỡng / Cách pha / Bảo quản -->
      <div class="mt-14 pt-8 border-t border-stone-200">
        <!-- Tab Headers -->
        <div class="flex flex-wrap gap-4 border-b border-stone-200 text-xs sm:text-sm font-bold mb-6" role="tablist">
          <button type="button" onclick="switchTab('tabNutrition', this)" class="tab-btn pb-3 border-b-2 border-[#FF6F78] text-[#FF6F78] transition">
            1. Thành phần & bảng dinh dưỡng
          </button>
          <button type="button" onclick="switchTab('tabPreparation', this)" class="tab-btn pb-3 border-b-2 border-transparent text-stone-500 hover:text-stone-800 transition">
            2. Cách pha & định lượng
          </button>
          <button type="button" onclick="switchTab('tabStorage', this)" class="tab-btn pb-3 border-b-2 border-transparent text-stone-500 hover:text-stone-800 transition">
            3. Hướng dẫn bảo quản
          </button>
        </div>

        <!-- Tab 1: Thành phần & Dinh dưỡng -->
        <div id="tabNutrition" class="tab-content space-y-6">
          <div class="space-y-3">
            <h4 class="font-bold text-stone-900 text-sm sm:text-base">Thành phần nguyên liệu (theo nhãn sản phẩm):</h4>
            <p class="text-xs text-stone-700 leading-relaxed bg-stone-50 p-4 rounded-2xl border border-stone-200">
              Sữa tươi nguyên chất đạm A2 hữu cơ (Fresh Organic A2 Protein Milk), Đường lactose hữu cơ, Dầu thực vật hữu cơ (Dầu hạt cải, Dầu hướng dương, Dầu dừa), Đạm whey cô đặc hữu cơ (Organic Whey Protein Concentrate), Galacto-oligosaccharide hữu cơ (GOS), Fructo-oligosaccharide (FOS), Axit Arachidonic (ARA), Axit Docosahexaenoic (DHA từ dầu cá). <strong>Khoáng chất:</strong> Canxi cacbonat, Sắt pyrophosphat, Kẽm sulfat, Magie cacbonat, Đồng sulfat, Mangan sulfat, Natri selenit. <strong>Vitamin:</strong> Choline bitartrate, Inositol, Niacinamide (Vitamin B3), Vitamin A axetat, Vitamin E axetat, Cholecalciferol (Vitamin D3), D-Canxi pantothenate, Thiamine hydrochloride (Vitamin B1), Pyridoxine hydrochloride (Vitamin B6), Riboflavin (Vitamin B2), Phytonadione (Vitamin K1), Axit folic, D-Biotin.
            </p>
            <p class="text-xs text-rose-700 font-semibold">
              Thông tin dị ứng: Sản phẩm có chứa sữa, đậu nành và dầu cá.
            </p>
          </div>

          <!-- Bảng dinh dưỡng NIP theo nhãn & TCCS 01/2026 -->
          <div>
            <h4 class="font-bold text-stone-900 mb-2 text-sm sm:text-base">Bảng giá trị dinh dưỡng trung bình (theo nhãn Stage 1 và TCCS 01/2026):</h4>
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
                  <tr><td class="p-2.5 pl-4">Năng lượng (Energy)</td><td class="p-2.5">kJ / Cal</td><td class="p-2.5">289 / 69</td><td class="p-2.5">2141 / 512</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>
                  <tr><td class="p-2.5 pl-4">Chất đạm (Protein)</td><td class="p-2.5">g</td><td class="p-2.5">1.7</td><td class="p-2.5">12.6</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>
                  <tr><td class="p-2.5 pl-6 text-stone-600">- Đạm Whey (60%)</td><td class="p-2.5">g</td><td class="p-2.5">1.0</td><td class="p-2.5">7.5</td><td class="p-2.5 text-stone-500">TCCS 01/2026</td></tr>
                  <tr><td class="p-2.5 pl-6 text-stone-600">- Đạm Casein (40%)</td><td class="p-2.5">g</td><td class="p-2.5">0.7</td><td class="p-2.5">5.0</td><td class="p-2.5 text-stone-500">TCCS 01/2026</td></tr>
                  <tr><td class="p-2.5 pl-6 text-stone-600">- Đạm A2-β-Casein</td><td class="p-2.5">g</td><td class="p-2.5">0.2</td><td class="p-2.5">1.7</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>

                  <tr class="bg-stone-50"><td class="p-2.5 font-bold text-stone-900" colspan="5">Chất béo & Axit béo</td></tr>
                  <tr><td class="p-2.5 pl-4">Chất béo tổng số (Fat, total)</td><td class="p-2.5">g</td><td class="p-2.5">3.8</td><td class="p-2.5">28</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>
                  <tr><td class="p-2.5 pl-6 text-stone-600">- Axit béo Linoleic</td><td class="p-2.5">g</td><td class="p-2.5">0.7</td><td class="p-2.5">4.8</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>
                  <tr><td class="p-2.5 pl-6 text-stone-600">- Axit α-Linolenic</td><td class="p-2.5">mg</td><td class="p-2.5">92</td><td class="p-2.5">681</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>
                  <tr><td class="p-2.5 pl-6 text-stone-600">- DHA (Docosahexaenoic Acid)</td><td class="p-2.5">mg</td><td class="p-2.5">12.4</td><td class="p-2.5">92</td><td class="p-2.5 text-stone-500">Từ dầu cá</td></tr>
                  <tr><td class="p-2.5 pl-6 text-stone-600">- ARA (Arachidonic Acid)</td><td class="p-2.5">mg</td><td class="p-2.5">12.4</td><td class="p-2.5">92</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>

                  <tr class="bg-stone-50"><td class="p-2.5 font-bold text-stone-900" colspan="5">Carbohydrate & Prebiotics</td></tr>
                  <tr><td class="p-2.5 pl-4">Carbohydrate</td><td class="p-2.5">g</td><td class="p-2.5">7.3</td><td class="p-2.5">54</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>
                  <tr><td class="p-2.5 pl-6 text-stone-600">- Đường tự nhiên (Sugars)</td><td class="p-2.5">g</td><td class="p-2.5">6.1</td><td class="p-2.5">45</td><td class="p-2.5 text-stone-500">Lactose tự nhiên</td></tr>
                  <tr><td class="p-2.5 pl-4">Chất xơ hòa tan (Prebiotic GOS)</td><td class="p-2.5">g</td><td class="p-2.5">0.20</td><td class="p-2.5">1.5</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>
                  <tr><td class="p-2.5 pl-4">Chất xơ hòa tan (Prebiotic FOS)</td><td class="p-2.5">g</td><td class="p-2.5">0.13</td><td class="p-2.5">1.0</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>

                  <tr class="bg-stone-50"><td class="p-2.5 font-bold text-stone-900" colspan="5">Vitamin thiết yếu</td></tr>
                  <tr><td class="p-2.5 pl-4">Vitamin A</td><td class="p-2.5">µg RE</td><td class="p-2.5">75</td><td class="p-2.5">553</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>
                  <tr><td class="p-2.5 pl-4">Vitamin D</td><td class="p-2.5">µg</td><td class="p-2.5">1.3</td><td class="p-2.5">10.0</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>
                  <tr><td class="p-2.5 pl-4">Vitamin E</td><td class="p-2.5">mg α-TE</td><td class="p-2.5">0.8</td><td class="p-2.5">5.8</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>
                  <tr><td class="p-2.5 pl-4">Vitamin C</td><td class="p-2.5">mg</td><td class="p-2.5">10.8</td><td class="p-2.5">80</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>
                  <tr><td class="p-2.5 pl-4">Vitamin B1 / B2 / B6 / B12</td><td class="p-2.5">µg</td><td class="p-2.5">58 / 98 / 56 / 0.2</td><td class="p-2.5">432 / 729 / 413 / 1.6</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>

                  <tr class="bg-stone-50"><td class="p-2.5 font-bold text-stone-900" colspan="5">Khoáng chất</td></tr>
                  <tr><td class="p-2.5 pl-4">Canxi (Calcium)</td><td class="p-2.5">mg</td><td class="p-2.5">52</td><td class="p-2.5">383</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>
                  <tr><td class="p-2.5 pl-4">Sắt (Iron)</td><td class="p-2.5">mg</td><td class="p-2.5">0.7</td><td class="p-2.5">5.5</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>
                  <tr><td class="p-2.5 pl-4">Kẽm (Zinc)</td><td class="p-2.5">mg</td><td class="p-2.5">0.4</td><td class="p-2.5">3.3</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>
                  <tr><td class="p-2.5 pl-4">Iốt (Iodine)</td><td class="p-2.5">µg</td><td class="p-2.5">7.1</td><td class="p-2.5">53</td><td class="p-2.5 text-stone-500">Theo nhãn</td></tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- Tab 2: Hướng dẫn pha & Bảng định lượng -->
        <div id="tabPreparation" class="tab-content space-y-6 hidden">
          <div class="grid grid-cols-1 md:grid-cols-5 gap-3 text-center">
            <div class="p-4 bg-stone-50 rounded-2xl border border-stone-200">
              <div class="w-7 h-7 rounded-full bg-[#FF6F78] text-white flex items-center justify-center font-bold mx-auto mb-2 text-xs">1</div>
              <h5 class="font-bold text-xs text-stone-900 mb-1">Rửa tay sạch sẽ</h5>
              <p class="text-[11px] text-stone-500">Rửa tay bằng xà phòng và tiệt trùng dụng cụ pha bình.</p>
            </div>
            <div class="p-4 bg-stone-50 rounded-2xl border border-stone-200">
              <div class="w-7 h-7 rounded-full bg-[#FF6F78] text-white flex items-center justify-center font-bold mx-auto mb-2 text-xs">2</div>
              <h5 class="font-bold text-xs text-stone-900 mb-1">Đun sôi nước</h5>
              <p class="text-[11px] text-stone-500">Đun sôi nước uống trong 5 phút, để nguội đến khoảng 40–50°C.</p>
            </div>
            <div class="p-4 bg-stone-50 rounded-2xl border border-stone-200">
              <div class="w-7 h-7 rounded-full bg-[#FF6F78] text-white flex items-center justify-center font-bold mx-auto mb-2 text-xs">3</div>
              <h5 class="font-bold text-xs text-stone-900 mb-1">Rót nước vào bình</h5>
              <p class="text-[11px] text-stone-500">Rót lượng nước ấm cần thiết theo bảng khẩu phần bên dưới.</p>
            </div>
            <div class="p-4 bg-stone-50 rounded-2xl border border-stone-200">
              <div class="w-7 h-7 rounded-full bg-[#FF6F78] text-white flex items-center justify-center font-bold mx-auto mb-2 text-xs">4</div>
              <h5 class="font-bold text-xs text-stone-900 mb-1">Đong bột gạt ngang</h5>
              <p class="text-[11px] text-stone-500">1 muỗng gạt ngang (4,6 g) pha với 30 ml nước ấm.</p>
            </div>
            <div class="p-4 bg-stone-50 rounded-2xl border border-stone-200">
              <div class="w-7 h-7 rounded-full bg-[#FF6F78] text-white flex items-center justify-center font-bold mx-auto mb-2 text-xs">5</div>
              <h5 class="font-bold text-xs text-stone-900 mb-1">Lắc đều & thử ấm</h5>
              <p class="text-[11px] text-stone-500">Lắc đều cho tan hết bột, nhỏ vài giọt lên cổ tay để thử nhiệt độ.</p>
            </div>
          </div>

          <h4 class="font-bold text-stone-900 pt-2 text-sm sm:text-base">Bảng khẩu phần ăn khuyến nghị (Feeding Guide Stage 1):</h4>
          <div class="overflow-x-auto rounded-2xl border border-stone-200">
            <table class="nutrition-table text-xs w-full min-w-[540px]">
              <thead>
                <tr>
                  <th scope="col" class="p-3 bg-stone-100 text-stone-800 text-left font-bold">Độ tuổi của bé</th>
                  <th scope="col" class="p-3 bg-stone-100 text-stone-800 text-left font-bold">Lượng nước nguội (ml)</th>
                  <th scope="col" class="p-3 bg-stone-100 text-stone-800 text-left font-bold">Số muỗng gạt (4,6 g/muỗng)</th>
                  <th scope="col" class="p-3 bg-stone-100 text-stone-800 text-left font-bold">Số cữ ăn mỗi ngày</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-stone-100">
                <tr><td class="p-2.5 font-medium">0 - 2 tuần tuổi</td><td class="p-2.5">60 ml</td><td class="p-2.5">2 muỗng</td><td class="p-2.5">7 - 8 lần</td></tr>
                <tr><td class="p-2.5 font-medium">2 - 4 tuần tuổi</td><td class="p-2.5">90 ml</td><td class="p-2.5">3 muỗng</td><td class="p-2.5">6 - 7 lần</td></tr>
                <tr><td class="p-2.5 font-medium">1 - 2 tháng tuổi</td><td class="p-2.5">120 ml</td><td class="p-2.5">4 muỗng</td><td class="p-2.5">5 - 6 lần</td></tr>
                <tr><td class="p-2.5 font-medium">2 - 4 tháng tuổi</td><td class="p-2.5">150 ml</td><td class="p-2.5">5 muỗng</td><td class="p-2.5">4 - 5 lần</td></tr>
                <tr><td class="p-2.5 font-medium">4 - 6 tháng tuổi</td><td class="p-2.5">180 ml</td><td class="p-2.5">6 muỗng</td><td class="p-2.5">4 - 5 lần</td></tr>
              </tbody>
            </table>
          </div>
          <p class="text-[11px] text-stone-500 italic">*Chỉ sử dụng muỗng lường kèm theo lon. Pha đúng tỷ lệ 1 muỗng gạt ngang (4,6g) cho mỗi 30ml nước. Không tự ý thay đổi tỷ lệ trừ khi có chỉ định y tế.</p>
        </div>

        <!-- Tab 3: Hướng dẫn bảo quản -->
        <div id="tabStorage" class="tab-content space-y-4 hidden">
          <div class="bg-stone-50 p-6 rounded-2xl border border-stone-200 text-xs text-stone-700 space-y-3 leading-relaxed">
            <h4 class="font-bold text-stone-900 text-sm">Hướng dẫn bảo quản lon và sữa đã pha (theo nhãn):</h4>
            <p>• <strong>Bảo quản lon sữa:</strong> Đậy kín nắp nhựa sau mỗi lần sử dụng. Bảo quản ở nơi khô ráo, thoáng mát dưới 25°C. Tránh ánh nắng mặt trời trực tiếp và không bảo quản lon sữa trong tủ lạnh.</p>
            <p>• <strong>Thời hạn sử dụng sau mở nắp:</strong> Sử dụng hết lượng sữa trong lon trong vòng 4 tuần kể từ ngày mở nắp.</p>
            <p>• <strong>Sữa sau khi pha:</strong> Cho bé dùng ngay sau khi pha xong. Không lưu trữ bình sữa đã bú dở; đổ bỏ phần thừa sau mỗi cữ ăn để đảm bảo vệ sinh cho bé.</p>
            <p>• <strong>Kiểm tra an toàn:</strong> Không sử dụng nếu màng nhôm niêm phong hoặc nắp hộp bị hư hỏng trước khi mở.</p>
          </div>
        </div>

      </div>

    </div>
  </main>
"""

    content += render_footer()
    return content

print("pages_products.py ready")
