# -*- coding: utf-8 -*-
"""
Science & Standards Pages:
- fresh-milk-difference.html
- certified-organic.html
- breast-is-best.html
"""

from build_site import render_head, render_topbar, render_navbar, render_footer

def build_fresh_milk_difference():
    content = render_head(
        title="Sự Khác Biệt Của Sữa Tươi Nutura | Công Nghệ Farmgate Wet-Blending",
        description="Khám phá khoa học đằng sau quy trình sữa tươi của Nutura Organic: Giữ trọn vẹn các protein hoạt tính sinh học tự nhiên như Lactoferrin và Kháng thể IgG từ cổng trang trại.",
        canonical_url="fresh-milk-difference.html"
    )
    content += render_topbar()
    content += render_navbar(active_page="fresh_milk")

    content += """
  <!-- HERO BANNER -->
  <section class="bg-[#FAF7F2] py-16 lg:py-24 border-b border-stone-200/60 relative overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        <div class="lg:col-span-7 space-y-6">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-rose-100 text-[#FF6F78] text-xs font-bold uppercase tracking-wider">
            Khoa Học Dinh Dưỡng Đột Phá
          </div>
          <h1 class="text-3xl sm:text-4xl lg:text-5xl font-bold text-stone-900 leading-tight">
            Sự Khác Biệt Của Sữa Tươi Farmgate Nutura
          </h1>
          <p class="text-base sm:text-lg text-stone-700 leading-relaxed">
            Công thức sữa tươi hữu cơ cao cấp từ Úc giúp <strong>giữ trọn vẹn sự tinh túy tự nhiên</strong> trong từng giọt sữa! Quy trình chế biến độc quyền bảo toàn các protein hoạt tính sinh học quý giá như <strong>Lactoferrin</strong> và <strong>Kháng thể tự nhiên Immunoglobulins (IgG)</strong>.
          </p>
          <div class="flex flex-wrap gap-4 pt-2">
            <a href="shop.html" class="btn-nutura-primary text-sm py-3 px-6">Mua Sắm Ngay</a>
            <a href="#science" class="btn-nutura-outline text-sm py-3 px-6">Khám Phá Nghiên Cứu Y Khoa</a>
          </div>
        </div>
        <div class="lg:col-span-5 text-center">
          <img src="assets/images/banner-fresh-milk.jpg" alt="Đồng cỏ nông trại Úc" class="rounded-3xl shadow-2xl border-4 border-white max-h-96 mx-auto object-cover">
        </div>
      </div>
    </div>
  </section>

  <!-- 3 CORE PILLARS OF FRESH MILK -->
  <section class="py-16 lg:py-20 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-3xl mx-auto mb-16 space-y-3">
        <span class="text-xs font-bold text-[#FF6F78] uppercase tracking-widest">Từ Cổng Trang Trại Đến Lon Sữa</span>
        <h2 class="text-3xl sm:text-4xl font-bold text-stone-900">Bắt Đầu Từ Nguồn Sữa Tươi Tinh Khiết Nhất Nước Úc</h2>
        <p class="text-stone-600 text-sm sm:text-base leading-relaxed">
          Tất cả bắt đầu từ những người nông dân Úc uy tín và nguồn sữa tươi thu hoạch từ đàn bò ăn cỏ tự nhiên trên các thung lũng xanh mướt của bang Victoria. Nguồn sữa chất lượng hàng đầu thế giới, được kiểm định nghiêm ngặt không chứa bất kỳ tạp chất hóa học nào.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="p-8 rounded-3xl bg-[#FAF7F2] border border-stone-200/80 space-y-4">
          <div class="w-12 h-12 bg-white rounded-2xl flex items-center justify-center text-2xl shadow-sm">🥛</div>
          <h3 class="text-xl font-bold text-stone-900">Nền Tảng Sữa Tươi Nguyên Chất</h3>
          <p class="text-stone-600 text-xs sm:text-sm leading-relaxed">
            Nutura sử dụng nền tảng là sữa tươi thu hoạch trực tiếp tại trang trại (Farmgate Milk), <strong>hoàn toàn KHÔNG dùng sữa bột hoàn nguyên sấy 2 lần</strong> như hầu hết các dòng sữa công thức công nghiệp thông thường. Điều này giúp bảo toàn tối đa cấu trúc tự nhiên của protein và hạt cầu chất béo.
          </p>
        </div>

        <div class="p-8 rounded-3xl bg-[#FAF7F2] border border-stone-200/80 space-y-4">
          <div class="w-12 h-12 bg-white rounded-2xl flex items-center justify-center text-2xl shadow-sm">🛡️</div>
          <h3 class="text-xl font-bold text-stone-900">Bảo Tồn Protein Hoạt Tính Sinh Học</h3>
          <p class="text-stone-600 text-xs sm:text-sm leading-relaxed">
            Quy trình trộn ướt Wet Blending và sấy phun 1 lần ở nhiệt độ tối ưu giúp giữ lại <strong>Lactoferrin</strong> và <strong>Kháng thể IgG</strong> tự nhiên. Kết hợp cùng Vitamin C, Kẽm và Sắt, Nutura mang lại hệ miễn dịch kiên cố giúp bé tự do khám phá thế giới.
          </p>
        </div>

        <div class="p-8 rounded-3xl bg-[#FAF7F2] border border-stone-200/80 space-y-4">
          <div class="w-12 h-12 bg-white rounded-2xl flex items-center justify-center text-2xl shadow-sm">🔬</div>
          <h3 class="text-xl font-bold text-stone-900">Được Chứng Thực Bởi Khoa Học Độc Lập</h3>
          <p class="text-stone-600 text-xs sm:text-sm leading-relaxed">
            Nutura Organic sở hữu dữ liệu phân tích độc lập chứng minh rằng quy trình 'Nutura Fresh Milk' bảo tồn nhiều protein có hoạt tính sinh học hơn đáng kể so với quy trình sản xuất sữa công thức truyền thống.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- SCIENTIFIC RESEARCH & COMPARISON (APAF Macquarie University) -->
  <section id="science" class="py-16 lg:py-24 bg-[#FAF7F2] border-t border-b border-stone-200/80">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-16">
      <!-- Section Intro -->
      <div class="text-center max-w-3xl mx-auto space-y-3">
        <span class="inline-block px-3 py-1 rounded-full bg-emerald-100 text-emerald-800 text-xs font-bold uppercase">
          Báo Cáo Nghiên Cứu Khoa Học
        </span>
        <h2 class="text-3xl sm:text-4xl font-bold text-stone-900">
          Phân Tích Của Trung Tâm Nghiên Cứu Proteome Úc (APAF)
        </h2>
        <p class="text-stone-600 text-sm leading-relaxed">
          Nghiên cứu độc lập được thực hiện bởi <strong>The Australian Proteome Analysis Facility (APAF) tại Đại học Macquarie (Úc)</strong> đã xác nhận nồng độ vượt trội của các protein sinh học tự nhiên trong sữa Nutura.
        </p>
      </div>

      <!-- Deep Dive 1: Lactoferrin -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center bg-white p-8 sm:p-12 rounded-3xl shadow-sm border border-stone-100">
        <div class="lg:col-span-5 text-center">
          <div class="w-24 h-24 bg-rose-50 text-[#FF6F78] rounded-3xl flex items-center justify-center text-4xl mx-auto mb-4 font-bold">
            LF
          </div>
          <h3 class="text-2xl font-bold text-stone-900">Lactoferrin</h3>
          <p class="text-xs text-stone-500 font-semibold mt-1">Kháng thể tự nhiên bảo vệ trẻ sơ sinh khỏi nhiễm khuẩn</p>
        </div>
        <div class="lg:col-span-7 space-y-4 text-xs sm:text-sm text-stone-700 leading-relaxed">
          <p>
            <strong>Lactoferrin là gì?</strong> Đây là một glycoprotein liên kết sắt đa chức năng được tìm thấy tự nhiên trong sữa mẹ và sữa non của động vật có vú. Nồng độ Lactoferrin trong sữa non của mẹ rất cao (7 - 9 g/L) và duy trì ở mức 1 - 3 g/L trong các tháng tiếp theo. Vai trò sinh học tiên quyết của Lactoferrin là <strong>bảo vệ em bé sơ sinh khỏi vi khuẩn, virus và kích hoạt hệ miễn dịch ban sơ</strong>.
          </p>
          <div class="space-y-2 bg-[#FAF7F2] p-4 rounded-2xl">
            <h4 class="font-bold text-stone-900 text-xs">3 Đặc Tính Cốt Lõi Của Lactoferrin Trong Sữa Nutura:</h4>
            <ul class="space-y-1.5 text-stone-600">
              <li>1. <strong>Liên kết & vận chuyển Sắt:</strong> Giúp trẻ hấp thu sắt tối đa, đồng thời tước đi nguồn sắt mà vi khuẩn gây hại cần để sinh sôi.</li>
              <li>2. <strong>Bề mặt tích điện dương:</strong> Cho phép Lactoferrin phá vỡ màng tế bào của vi sinh vật gây bệnh, vô hiệu hóa vi khuẩn.</li>
              <li>3. <strong>Tương thích với thụ thể tiêu hóa:</strong> Đường ruột con người sở hữu các thụ thể nhận diện Lactoferrin -  Khi gắn kết, nó kích hoạt tín hiệu phòng vệ miễn dịch niêm mạc.</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Deep Dive 2: Immunoglobulins (IgG) -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center bg-white p-8 sm:p-12 rounded-3xl shadow-sm border border-stone-100">
        <div class="lg:col-span-5 text-center">
          <div class="w-24 h-24 bg-blue-50 text-blue-600 rounded-3xl flex items-center justify-center text-4xl mx-auto mb-4 font-bold">
            IgG
          </div>
          <h3 class="text-2xl font-bold text-stone-900">Immunoglobulins (IgGs)</h3>
          <p class="text-xs text-stone-500 font-semibold mt-1">Kháng thể miễn dịch bảo vệ đường ruột non nớt của trẻ</p>
        </div>
        <div class="lg:col-span-7 space-y-4 text-xs sm:text-sm text-stone-700 leading-relaxed">
          <p>
            <strong>Kháng thể IgG là gì?</strong> Immunoglobulin (kháng thể) là các phân tử protein phức hợp lớn do tế bào bạch cầu tạo ra để nhận diện, khóa chặt và tiêu diệt các kháng nguyên ngoại lai (vi khuẩn, virus gây bệnh). Trong sữa bò tươi và sữa mẹ, IgG chiếm tỷ lệ cao nhất và có ý nghĩa sống còn đối với miễn dịch thụ động của trẻ nhỏ.
          </p>
          <p>
            Nhờ công nghệ sấy phun 1 lần ở nhiệt độ kiểm soát chính xác, các phân tử IgG trong sữa Nutura giữ nguyên được cấu trúc 3 chiều nhạy cảm, không bị phá hủy hay biến tính như trong quá trình sấy khô 2 lần ở các loại sữa bột thông thường.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- CTA BOTTOM -->
  <section class="py-16 bg-white text-center">
    <div class="max-w-4xl mx-auto px-4 space-y-6">
      <h2 class="text-3xl font-bold text-stone-900">
        Trao Cho Con Sự Tinh Khiết Nguyên Bản Của Sữa Tươi Trong Từng Lon Sữa
      </h2>
      <p class="text-stone-600 text-sm max-w-2xl mx-auto">
        Hãy để bé yêu khởi đầu với nguồn dinh dưỡng thanh mát chuẩn tự nhiên nhất.
      </p>
      <div>
        <a href="shop.html" class="btn-nutura-primary text-sm py-3.5 px-8">
          Khám Phá Các Dòng Sữa Nutura &rarr;
        </a>
      </div>
    </div>
  </section>
"""
    content += render_footer()
    return content

def build_certified_organic():
    content = render_head(
        title="Chứng Nhận Hữu Cơ ACO Trên Nhãn Nutura Organic A2",
        description="Tìm hiểu logo chứng nhận hữu cơ ACO thể hiện trên bộ nhãn Nutura Organic A2 Stage 1–3; kiểm tra nhãn thực tế để xác nhận sản phẩm.",
        canonical_url="certified-organic.html"
    )
    content += render_topbar()
    content += render_navbar(active_page="organic")

    content += """
  <!-- HERO BANNER -->
  <section class="bg-[#FAF7F2] py-16 lg:py-24 border-b border-stone-200/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        <div class="lg:col-span-7 space-y-6">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-100 text-emerald-800 text-xs font-bold uppercase tracking-wider">
            Tiêu Chuẩn Khắt Khe Hàng Đầu Thế Giới
          </div>
          <h1 class="text-3xl sm:text-4xl lg:text-5xl font-bold text-stone-900 leading-tight">
            Chứng Nhận Hữu Cơ Trên Nhãn Sản Phẩm
          </h1>
          <p class="text-base sm:text-lg text-stone-700 leading-relaxed">
            Bộ nhãn Nutura Organic A2 Stage 1–3 trong tài liệu sản phẩm hiển thị logo <strong>ACO Certified Organic</strong>. Đối chiếu nhãn trên lon bạn mua để xác nhận chứng nhận và thông tin thành phần của đúng sản phẩm.
          </p>
          <div class="flex items-center gap-4 pt-2">
            <img src="assets/images/aco-logo.png" alt="ACO" class="h-14 w-auto bg-white p-2 rounded-xl border border-stone-200 shadow-sm">
          </div>
        </div>
        <div class="lg:col-span-5 text-center">
          <img src="assets/images/banner-organic.jpg" alt="Chứng nhận hữu cơ" class="rounded-3xl shadow-2xl border-4 border-white max-h-96 mx-auto object-cover">
        </div>
      </div>
    </div>
  </section>

  <!-- CARBON NEUTRAL & VALUES -->
  <section class="py-16 lg:py-20 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <!-- Carbon neutral highlight -->
      <div class="bg-gradient-to-r from-emerald-50 via-teal-50 to-emerald-100 p-8 sm:p-12 rounded-3xl border border-emerald-200 mb-16">
        <div class="max-w-3xl space-y-4">
          <span class="inline-block px-3 py-1 rounded-full bg-emerald-700 text-white text-xs font-bold uppercase">
            Thông Tin Trên Nhãn
          </span>
          <h2 class="text-2xl sm:text-3xl font-bold text-emerald-950">
            Kiểm Tra Thông Tin Trên Nhãn Sản Phẩm
          </h2>
          <p class="text-stone-700 text-sm sm:text-base leading-relaxed">
            Nhãn các sản phẩm Stage 1–3 thể hiện logo ACO và thông tin thành phần, dinh dưỡng, cách pha, bảo quản. Hãy đọc nhãn của đúng sản phẩm trước khi sử dụng.
          </p>
        </div>
      </div>

      <div class="text-center max-w-3xl mx-auto mb-12 space-y-3">
        <h2 class="text-3xl font-bold text-stone-900">Đọc Thành Phần Trên Nhãn Sản Phẩm</h2>
        <p class="text-stone-600 text-sm leading-relaxed">Kiểm tra thành phần, chất gây dị ứng và hướng dẫn pha trên nhãn của đúng sản phẩm trước khi sử dụng. Tham khảo chuyên gia y tế khi cần tư vấn cho trẻ.</p>
      </div>
    </div>
  </section>
"""
    content += render_footer()
    return content

def build_breast_is_best():
    content = render_head(
        title="Thông Tin Quan Trọng Về Nuôi Con Bằng Sữa Mẹ | Cam Kết Y Tế WHO",
        description="Thông điệp y tế chính thức về tầm quan trọng của sữa mẹ đối với sự phát triển toàn diện của trẻ sơ sinh và trẻ nhỏ. Khuyến nghị khoa học từ WHO và chuyên gia y tế.",
        canonical_url="breast-is-best.html"
    )
    content += render_topbar()
    content += render_navbar(active_page="home")

    content += """
  <!-- BREADCRUMB -->
  <div class="bg-[#FAF7F2] py-4 border-b border-stone-200/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-xs text-stone-500 flex items-center gap-2">
      <a href="index.html" class="hover:text-[#FF6F78]">Trang Chủ</a>
      <span>/</span>
      <span class="text-stone-800 font-bold">Thông Tin Sữa Mẹ</span>
    </div>
  </div>

  <section class="py-16 lg:py-24 bg-white flex-1">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
      <div class="text-center space-y-3">
        <div class="w-16 h-16 bg-rose-50 text-[#FF6F78] rounded-full flex items-center justify-center mx-auto text-3xl">
          ❤️
        </div>
        <h1 class="text-3xl sm:text-4xl font-bold text-stone-900">
          Nuôi Con Bằng Sữa Mẹ: Nền Tảng Dinh Dưỡng Vàng
        </h1>
        <p class="text-xs uppercase font-bold tracking-widest text-[#FF6F78]">
          Thông Điệp Y Tế Theo Tiêu Chuẩn WHO & Quy Định Pháp Luật Việt Nam
        </p>
      </div>

      <div class="prose max-w-none text-stone-700 text-sm sm:text-base leading-relaxed space-y-6 bg-stone-50 p-8 sm:p-10 rounded-3xl border border-stone-200">
        <p class="font-bold text-stone-900 text-lg">
          Sữa mẹ là thức ăn tốt nhất cho sức khỏe và sự phát triển toàn diện của trẻ sơ sinh và trẻ nhỏ.
        </p>
        <p>
          Tổ chức Y tế Thế giới (WHO) khuyến nghị nên nuôi con hoàn toàn bằng sữa mẹ trong 6 tháng đầu đời và tiếp tục cho trẻ bú mẹ kết hợp ăn dặm đầy đủ chất dinh dưỡng cho đến 2 tuổi hoặc lâu hơn. Sữa mẹ cung cấp mọi dưỡng chất với tỷ lệ hoàn hảo, đồng thời chứa vô vàn kháng thể sống giúp bảo vệ em bé trước các bệnh nhiễm khuẩn tiêu hóa và đường hô hấp.
        </p>

        <h3 class="text-xl font-bold text-stone-900 pt-4 border-t border-stone-200">
          Khi Nào Cần Tham Vấn Chuyên Gia Y Tế?
        </h3>
        <p>
          Sữa công thức được nghiên cứu để thay thế sữa mẹ trong những trường hợp người mẹ không đủ sữa, có bệnh lý chỉ định hoặc vì lý do sức khỏe không thể cho con bú. Trước khi quyết định chuyển sang hoặc bổ sung sữa công thức:
        </p>
        <ul class="list-disc pl-5 space-y-2 text-stone-600">
          <li>Luôn tham khảo ý kiến bác sĩ chuyên khoa nhi, nữ hộ sinh hoặc chuyên gia dinh dưỡng để được tư vấn chính xác.</li>
          <li>Việc cho trẻ bú bình có thể làm giảm phản xạ bú mẹ và làm suy giảm lượng sữa mẹ tự nhiên. Quyết định ngừng cho con bú mẹ thường rất khó đảo ngược.</li>
          <li>Cần xem xét kỹ các yếu tố về kinh tế và xã hội khi lựa chọn phương pháp nuôi dưỡng cho con.</li>
          <li>Sữa công thức phải được pha chế và sử dụng nghiêm ngặt theo hướng dẫn trên lon sữa. Việc pha không đúng cách có thể gây nguy cơ nghiêm trọng cho sức khỏe của bé.</li>
        </ul>

        <div class="mt-8 pt-6 border-t border-stone-200 flex flex-col sm:flex-row gap-4 items-center justify-between">
          <span class="text-xs text-stone-500">Nutura Organic Việt Nam cam kết tuân thủ đạo đức truyền thông y tế và bảo vệ nguồn sữa mẹ.</span>
          <a href="shop.html" class="btn-nutura-primary text-xs py-3 px-6 whitespace-nowrap">
            Truy Cập Trang Sản Phẩm
          </a>
        </div>
      </div>
    </div>
  </section>
"""
    content += render_footer()
    return content

print("Science & standards pages ready.")
