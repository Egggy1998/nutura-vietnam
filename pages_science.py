# -*- coding: utf-8 -*-
"""
Science & Standards Pages:
- fresh-milk-difference.html (Sữa tươi farmgate)
- certified-organic.html (Chứng nhận hữu cơ ACO)
- breast-is-best.html (Thông tin sữa mẹ theo WHO & NĐ100)
"""

from build_site import render_head, render_topbar, render_navbar, render_footer, render_breast_milk_banner

def build_fresh_milk_difference():
    content = render_head(
        title="Quy trình sữa tươi farmgate một lần sấy",
        description="Tìm hiểu quy trình chế biến sữa tươi nguyên liệu farmgate tại Victoria, Úc của Nutura: Công nghệ phối trộn ướt wet blending và sấy phun một lần theo TCCS.",
        canonical_url="fresh-milk-difference.html"
    )
    content += render_topbar()
    content += render_breast_milk_banner()
    content += render_navbar(active_page="fresh_milk")

    content += """
  <!-- Breadcrumb -->
  <div class="bg-[#FAF7F2] py-3.5 border-b border-stone-200/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-xs text-stone-500 flex items-center gap-2">
      <a href="index.html" class="hover:text-[#FF6F78]">Trang chủ</a>
      <span>/</span>
      <span class="text-stone-800 font-bold">Sữa tươi farmgate</span>
    </div>
  </div>

  <main id="main-content">
  <!-- Hero Banner -->
  <section class="bg-[#FAF7F2] py-14 lg:py-20 border-b border-stone-200/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
        <div class="lg:col-span-7 space-y-5">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-rose-100 text-[#FF6F78] text-xs font-bold uppercase tracking-wider">
            Quy trình sản xuất từ Úc
          </div>
          <h1 class="text-2xl sm:text-3xl lg:text-4xl font-bold text-stone-900 leading-tight">
            Quy trình chế biến từ sữa tươi farmgate
          </h1>
          <p class="text-stone-700 text-sm sm:text-base leading-relaxed">
            Nutura sử dụng nguồn sữa tươi thu gom trực tiếp tại các trang trại ở Victoria, Úc (farmgate milk). Quy trình phối trộn ướt (wet blending) kết hợp sấy phun một lần giúp bảo toàn cấu trúc tự nhiên của protein và giữ lại Lactoferrin cùng IgG tự nhiên theo tiêu chuẩn TCCS.
          </p>
          <div class="flex flex-wrap gap-3 pt-2">
            <a href="#so-sanh-quy-trinh" class="text-xs sm:text-sm py-2.5 px-5 rounded-full bg-[#FF6F78] hover:bg-[#E65A63] text-white font-bold transition shadow-sm text-center">
              So sánh quy trình sấy 1 lần vs 2 lần
            </a>
            <a href="contact.html#diem-ban" class="text-xs sm:text-sm py-2.5 px-5 rounded-full border border-stone-300 text-stone-700 hover:border-[#FF6F78] hover:text-[#FF6F78] font-bold transition text-center">
              Tìm điểm bán sản phẩm
            </a>
          </div>
        </div>
        <div class="lg:col-span-5 text-center">
          <img src="assets/images/banner-fresh-milk.jpg" alt="Trang trại bò sữa tại bang Victoria, Úc" class="rounded-3xl shadow-xl border-4 border-white max-h-80 mx-auto object-cover" loading="eager">
        </div>
      </div>
    </div>
  </section>

  <!-- 3 Trụ cột kỹ thuật của sữa tươi farmgate -->
  <section class="py-16 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-3xl mx-auto mb-14 space-y-3">
        <span class="text-xs font-bold text-[#FF6F78] uppercase tracking-widest">Nguồn sữa tươi nguyên liệu</span>
        <h2 class="text-2xl sm:text-3xl font-bold text-stone-900">Thu gom tại cổng trang trại bang Victoria</h2>
        <p class="text-stone-600 text-xs sm:text-sm leading-relaxed">
          Nguồn sữa tươi nguyên liệu được thu hoạch từ đàn bò ăn cỏ tự nhiên trên các thung lũng của bang Victoria, đáp ứng tiêu chuẩn vệ sinh an toàn thực phẩm FSANZ của Úc.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div class="p-6 rounded-3xl bg-[#FAF7F2] border border-stone-200/80 space-y-3">
          <div class="w-10 h-10 bg-white rounded-xl flex items-center justify-center text-xl shadow-sm">🥛</div>
          <h3 class="text-base font-bold text-stone-900">Sữa tươi farmgate</h3>
          <p class="text-stone-600 text-xs leading-relaxed">
            Sử dụng sữa tươi chuyển trực tiếp từ trang trại đến nhà máy trong vòng vài giờ, không sử dụng bột sữa gầy hoàn nguyên nhập từ nơi khác.
          </p>
        </div>

        <div class="p-6 rounded-3xl bg-[#FAF7F2] border border-stone-200/80 space-y-3">
          <div class="w-10 h-10 bg-white rounded-xl flex items-center justify-center text-xl shadow-sm">🔬</div>
          <h3 class="text-base font-bold text-stone-900">Lactoferrin và IgG tự nhiên</h3>
          <p class="text-stone-600 text-xs leading-relaxed">
            Hàm lượng Lactoferrin đạt ≥1,12 mg/100 ml và IgG đạt ≥19,6 mg/100 ml theo công bố TCCS 01/2026 và 02/2026, được bảo tồn nhờ công nghệ sấy nhiệt độ được kiểm soát.
          </p>
        </div>

        <div class="p-6 rounded-3xl bg-[#FAF7F2] border border-stone-200/80 space-y-3">
          <div class="w-10 h-10 bg-white rounded-xl flex items-center justify-center text-xl shadow-sm">🌿</div>
          <h3 class="text-base font-bold text-stone-900">Đạm A2 hữu cơ</h3>
          <p class="text-stone-600 text-xs leading-relaxed">
            Nguồn đạm tự nhiên từ giống bò chọn lọc chỉ cho đạm A2-β-casein, đạt chứng nhận hữu cơ ACO trên từng nhãn lon.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- So sánh quy trình kỹ thuật: 1 lần sấy vs 2 lần sấy -->
  <section id="so-sanh-quy-trinh" class="py-16 bg-[#FAF7F2] border-t border-b border-stone-200/60">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 space-y-10">
      <div class="text-center space-y-3">
        <span class="text-xs font-bold text-[#FF6F78] uppercase tracking-wider">Giải thích kỹ thuật</span>
        <h2 class="text-2xl sm:text-3xl font-bold text-stone-900">
          So sánh quy trình sấy một lần và sấy hai lần
        </h2>
        <p class="text-stone-600 text-xs sm:text-sm leading-relaxed max-w-2xl mx-auto">
          Bảng phân tích kỹ thuật giữa quy trình sữa tươi farmgate (Nutura) và quy trình hoàn nguyên bột thông thường.
        </p>
      </div>

      <div class="overflow-x-auto rounded-3xl border border-stone-200 bg-white shadow-sm">
        <table class="nutrition-table text-xs w-full">
          <thead>
            <tr>
              <th scope="col" class="p-3.5 bg-stone-100 text-stone-800 text-left font-bold">Tiêu chí kỹ thuật</th>
              <th scope="col" class="p-3.5 bg-rose-50 text-[#FF6F78] text-left font-bold">Quy trình Nutura (Sữa tươi farmgate)</th>
              <th scope="col" class="p-3.5 bg-stone-100 text-stone-600 text-left font-bold">Quy trình bột sữa hoàn nguyên</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-stone-100 text-stone-700">
            <tr>
              <td class="p-3 font-semibold text-stone-900">Nguồn nguyên liệu đầu vào</td>
              <td class="p-3 bg-rose-50/20 font-medium text-stone-800">Sữa tươi nguyên chất thu gom tại trang trại</td>
              <td class="p-3 text-stone-500">Bột sữa sấy khô nhập kho lưu trữ</td>
            </tr>
            <tr>
              <td class="p-3 font-semibold text-stone-900">Số lần xử lý nhiệt cao</td>
              <td class="p-3 bg-rose-50/20 font-bold text-[#FF6F78]">1 lần duy nhất (Wet blending + sấy phun)</td>
              <td class="p-3 text-stone-500">2 lần (sấy thành bột nguyên liệu, rồi hòa nước sấy lại)</td>
            </tr>
            <tr>
              <td class="p-3 font-semibold text-stone-900">Bảo tồn protein hoạt tính</td>
              <td class="p-3 bg-rose-50/20 font-medium text-stone-800">Giữ lại cấu trúc tự nhiên của Lactoferrin và IgG</td>
              <td class="p-3 text-stone-500">Nhiệt độ gia nhiệt nhiều lần làm giảm tỷ lệ protein nhạy cảm</td>
            </tr>
            <tr>
              <td class="p-3 font-semibold text-stone-900">Độ hòa tan & tơi xốp</td>
              <td class="p-3 bg-rose-50/20 font-medium text-stone-800">Hạt bột tơi xốp đồng nhất do phối trộn ở thể lỏng</td>
              <td class="p-3 text-stone-500">Có thể cần thêm phụ gia phân tán hoặc phối trộn khô</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="p-5 bg-white rounded-2xl border border-stone-200 text-xs text-stone-600 leading-relaxed">
        <strong class="text-stone-800">Lưu ý tra cứu:</strong> Các chỉ số về nồng độ Lactoferrin và IgG được xác định theo hồ sơ công bố TCCS của từng giai đoạn (Stage 1 và 2). Thông tin không có giá trị thay thế cho việc chẩn đoán hay điều trị y khoa.
      </div>
    </div>
  </section>
  </main>
"""
    content += render_footer()
    return content

def build_certified_organic():
    content = render_head(
        title="Tiêu chuẩn chứng nhận hữu cơ ACO trên nhãn Nutura Organic",
        description="Tìm hiểu tiêu chuẩn chứng nhận hữu cơ Australian Certified Organic (ACO) thể hiện trên nhãn lon Nutura Stage 1–3: Không hóa chất tổng hợp, không biến đổi gen.",
        canonical_url="certified-organic.html"
    )
    content += render_topbar()
    content += render_breast_milk_banner()
    content += render_navbar(active_page="organic")

    content += """
  <!-- Breadcrumb -->
  <div class="bg-[#FAF7F2] py-3.5 border-b border-stone-200/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-xs text-stone-500 flex items-center gap-2">
      <a href="index.html" class="hover:text-[#FF6F78]">Trang chủ</a>
      <span>/</span>
      <span class="text-stone-800 font-bold">Chứng nhận hữu cơ</span>
    </div>
  </div>

  <main id="main-content">
  <!-- Hero Banner -->
  <section class="bg-[#FAF7F2] py-14 lg:py-20 border-b border-stone-200/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
        <div class="lg:col-span-7 space-y-5">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-100 text-emerald-800 text-xs font-bold uppercase tracking-wider">
            Tiêu chuẩn hữu cơ Úc
          </div>
          <h1 class="text-2xl sm:text-3xl lg:text-4xl font-bold text-stone-900 leading-tight">
            Chứng nhận hữu cơ Australian Certified Organic (ACO)
          </h1>
          <p class="text-stone-700 text-sm sm:text-base leading-relaxed">
            Bộ sản phẩm Nutura Organic A2 Stage 1, Stage 2 và Stage 3 thể hiện logo chứng nhận <strong>ACO Certified Organic</strong> trên nhãn sản phẩm. Đây là một trong những chứng nhận hữu cơ nghiêm ngặt và uy tín hàng đầu tại Úc.
          </p>
          <div class="flex items-center gap-4 pt-1">
            <img src="assets/images/aco-logo.png" alt="Logo ACO Certified Organic" class="h-12 w-auto bg-white p-1 rounded-lg border border-stone-200 shadow-sm">
            <img src="assets/images/icon-aus-made.png" alt="Logo Australian Made" class="h-12 w-auto bg-white p-1 rounded-lg border border-stone-200 shadow-sm">
          </div>
        </div>
        <div class="lg:col-span-5 text-center">
          <img src="assets/images/banner-organic.jpg" alt="Nông trại đạt chuẩn hữu cơ tại Úc" class="rounded-3xl shadow-xl border-4 border-white max-h-80 mx-auto object-cover" loading="eager">
        </div>
      </div>
    </div>
  </section>

  <!-- Tiêu chuẩn ACO là gì -->
  <section class="py-16 bg-white">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
      <div class="space-y-4">
        <h2 class="text-2xl sm:text-3xl font-bold text-stone-900">
          Tiêu chuẩn ACO là gì?
        </h2>
        <p class="text-stone-700 text-sm sm:text-base leading-relaxed">
          Australian Certified Organic (ACO) là cơ quan chứng nhận hữu cơ lớn nhất của Úc. Tiêu chuẩn ACO yêu cầu quá trình canh tác và chế biến phải tuân thủ nghiêm ngặt các điều kiện:
        </p>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-2 text-xs text-stone-700">
          <div class="p-4 rounded-2xl bg-stone-50 border border-stone-100 flex items-start gap-3">
            <span class="text-emerald-600 font-bold text-sm">✓</span>
            <div><strong>Không thuốc trừ sâu tổng hợp:</strong> Đất trồng và đồng cỏ không sử dụng phân bón hóa học hay thuốc trừ sâu tổng hợp.</div>
          </div>
          <div class="p-4 rounded-2xl bg-stone-50 border border-stone-100 flex items-start gap-3">
            <span class="text-emerald-600 font-bold text-sm">✓</span>
            <div><strong>Không hormone tăng trưởng:</strong> Đàn bò được chăn thả tự nhiên, không sử dụng hormone kích thích tăng trưởng.</div>
          </div>
          <div class="p-4 rounded-2xl bg-stone-50 border border-stone-100 flex items-start gap-3">
            <span class="text-emerald-600 font-bold text-sm">✓</span>
            <div><strong>Không biến đổi gen (Non-GMO):</strong> Thức ăn và nguyên liệu không có nguồn gốc từ sinh vật biến đổi gen.</div>
          </div>
          <div class="p-4 rounded-2xl bg-stone-50 border border-stone-100 flex items-start gap-3">
            <span class="text-emerald-600 font-bold text-sm">✓</span>
            <div><strong>Không hương liệu & tạo ngọt nhân tạo:</strong> 100% hương vị thanh nhẹ từ đường sữa tự nhiên (lactose).</div>
          </div>
        </div>
      </div>

      <!-- Hướng dẫn đọc logo trên nhãn -->
      <div class="p-6 sm:p-8 bg-[#FAF7F2] rounded-3xl border border-stone-200/80 space-y-4">
        <h3 class="text-lg font-bold text-stone-900">Cách nhận biết chứng nhận trên nhãn lon</h3>
        <p class="text-xs sm:text-sm text-stone-600 leading-relaxed">
          Trên mỗi lon Nutura Organic phân phối chính hãng, người dùng có thể tra cứu các dấu hiệu chứng nhận sau:
        </p>
        <ul class="space-y-2 text-xs text-stone-700">
          <li class="flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
            <span><strong>Logo ACO:</strong> Thể hiện ở mặt trước và mặt sau của nhãn Stage 1, 2 và 3.</span>
          </li>
          <li class="flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
            <span><strong>Biểu tượng Australian Made:</strong> Kangaroo xanh vàng xác nhận sản xuất tại Úc với trên 69% nguyên liệu bản địa.</span>
          </li>
          <li class="flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
            <span><strong>Mã vạch EAN-13 Úc:</strong> Đầu số 935... xác nhận sản phẩm xuất xứ từ Úc.</span>
          </li>
        </ul>
      </div>
    </div>
  </section>
  </main>
"""
    content += render_footer()
    return content

def build_breast_is_best():
    content = render_head(
        title="Thông tin về nuôi con bằng sữa mẹ theo khuyến nghị WHO",
        description="Thông điệp y tế chính thức về tầm quan trọng của sữa mẹ đối với sự phát triển của trẻ nhỏ theo khuyến nghị của Tổ chức Y tế Thế giới (WHO) và Nghị định 100/2014/NĐ-CP.",
        canonical_url="breast-is-best.html"
    )
    content += render_topbar()
    content += render_breast_milk_banner()
    content += render_navbar(active_page="home")

    content += """
  <!-- Breadcrumb -->
  <div class="bg-[#FAF7F2] py-3.5 border-b border-stone-200/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-xs text-stone-500 flex items-center gap-2">
      <a href="index.html" class="hover:text-[#FF6F78]">Trang chủ</a>
      <span>/</span>
      <span class="text-stone-800 font-bold">Thông tin sữa mẹ</span>
    </div>
  </div>

  <main id="main-content" class="py-12 lg:py-16 bg-white flex-1">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
      <div class="text-center space-y-3">
        <div class="w-12 h-12 bg-rose-50 text-[#FF6F78] rounded-2xl flex items-center justify-center mx-auto text-2xl">
          ❤️
        </div>
        <h1 class="text-2xl sm:text-3xl font-bold text-stone-900">
          Thông tin về nuôi con bằng sữa mẹ
        </h1>
        <p class="text-xs uppercase font-bold tracking-widest text-[#FF6F78]">
          Theo tiêu chuẩn WHO & Nghị định 100/2014/NĐ-CP
        </p>
      </div>

      <div class="text-stone-700 text-xs sm:text-sm leading-relaxed space-y-5 bg-[#FAF7F2] p-6 sm:p-10 rounded-3xl border border-stone-200">
        <div class="p-4 bg-white rounded-2xl border-l-4 border-[#FF6F78] shadow-sm">
          <p class="font-bold text-stone-900 text-sm sm:text-base">
            Sữa mẹ là thức ăn tốt nhất cho sức khoẻ và sự phát triển toàn diện của trẻ nhỏ.
          </p>
        </div>

        <p>
          Tổ chức Y tế Thế giới (WHO) khuyến nghị nên nuôi con hoàn toàn bằng sữa mẹ trong 6 tháng đầu đời và tiếp tục cho trẻ bú mẹ kết hợp ăn dặm đầy đủ chất dinh dưỡng cho đến 2 tuổi hoặc lâu hơn. Sữa mẹ chứa các kháng thể tự nhiên chỉ có trong sữa mẹ giúp trẻ phòng ngừa các bệnh nhiễm khuẩn tiêu hóa và đường hô hấp.
        </p>

        <h3 class="text-base font-bold text-stone-900 pt-3 border-t border-stone-200">
          Khi nào cần tham vấn ý kiến chuyên gia y tế?
        </h3>
        <p>
          Sản phẩm dinh dưỡng công thức chỉ nên sử dụng khi có chỉ định của bác sĩ hoặc cán bộ y tế trong những trường hợp người mẹ không đủ sữa hoặc vì lý do y khoa không thể cho con bú:
        </p>
        <ul class="list-disc pl-5 space-y-1.5 text-stone-600">
          <li>Luôn tham khảo ý kiến bác sĩ chuyên khoa nhi trước khi quyết định đổi sang hoặc dùng bổ sung sản phẩm dinh dưỡng công thức.</li>
          <li>Việc cho trẻ bú bình có thể làm giảm phản xạ bú mẹ và làm giảm lượng sữa mẹ tự nhiên.</li>
          <li>Sản phẩm dinh dưỡng công thức phải được pha chế và sử dụng nghiêm ngặt theo hướng dẫn ghi trên lon. Việc pha không đúng hướng dẫn có thể ảnh hưởng đến sức khỏe của trẻ.</li>
        </ul>

        <div class="pt-4 border-t border-stone-200 flex flex-col sm:flex-row gap-3 items-center justify-between">
          <span class="text-[11px] text-stone-500">Nutura Việt Nam cam kết tuân thủ đạo đức truyền thông y tế và bảo vệ nguồn sữa mẹ.</span>
          <a href="index.html" class="text-xs py-2 px-4 rounded-full border border-stone-300 hover:border-[#FF6F78] hover:text-[#FF6F78] font-bold text-stone-700 transition">
            Quay lại trang chủ
          </a>
        </div>
      </div>
    </div>
  </main>
"""
    content += render_footer()
    return content

print("pages_science.py ready")
