# -*- coding: utf-8 -*-
"""
Community, Company & Support Pages:
- about-us.html (Về Nutura & Nhà máy Victoria - Không ảnh/tên NVYT)
- village.html (Góc cha mẹ - 9 bài blog không nhắc sản phẩm)
- faqs.html (Hỏi đáp về pha sữa, bảo quản, hữu cơ - Bỏ FAQ giao/đặt hàng)
- contact.html (Liên hệ & Danh sách điểm bán - Pháp nhân EVA Premium Mom and Baby)
Tuân thủ Nghị định 100/2014/NĐ-CP và tiêu chuẩn WHO
"""

from build_site import render_head, render_topbar, render_navbar, render_footer, render_breast_milk_banner

def build_about_us():
    content = render_head(
        title="Câu chuyện thương hiệu Nutura & Nhà máy Victoria",
        description="Tìm hiểu câu chuyện Nutura Organic: Sứ mệnh tạo dựng dinh dưỡng hữu cơ thanh lành cho trẻ em từ sữa tươi farmgate và nhà máy tại Victoria, Úc.",
        canonical_url="about-us.html"
    )
    content += render_topbar()
    content += render_breast_milk_banner()
    content += render_navbar(active_page="about")

    content += """
  <!-- Breadcrumb -->
  <div class="bg-[#FAF7F2] py-3.5 border-b border-stone-200/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-xs text-stone-500 flex items-center gap-2">
      <a href="index.html" class="hover:text-[#FF6F78]">Trang chủ</a>
      <span>/</span>
      <span class="text-stone-800 font-bold">Về Nutura</span>
    </div>
  </div>

  <main id="main-content">
  <!-- Hero Banner -->
  <section class="bg-[#FAF7F2] py-14 lg:py-20 border-b border-stone-200/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
        <div class="lg:col-span-7 space-y-5">
          <span class="inline-block px-3 py-1 rounded-full bg-rose-100 text-[#FF6F78] text-xs font-bold uppercase tracking-wider">
            Câu chuyện thương hiệu
          </span>
          <h1 class="text-2xl sm:text-3xl lg:text-4xl font-bold text-stone-900 leading-tight">
            Dinh dưỡng tự nhiên từ đàn bò ăn cỏ nước Úc
          </h1>
          <p class="text-stone-700 text-sm sm:text-base leading-relaxed">
            Hành trình của Nutura bắt nguồn từ mong muốn mang lại nguồn dinh dưỡng thuần khiết cho trẻ nhỏ, đồng thời chia sẻ tri thức nuôi con đồng hành cùng các bậc phụ huynh.
          </p>
        </div>
        <div class="lg:col-span-5 text-center">
          <img src="assets/images/banner-scene2.jpg" alt="Nông trại Nutura tại Úc" class="rounded-3xl shadow-xl border-4 border-white max-h-80 mx-auto object-cover" loading="eager">
        </div>
      </div>
    </div>
  </section>

  <!-- Triết lý ngôi làng & Nhà máy Victoria (Không ảnh/tên nhân viên y tế) -->
  <section class="py-16 bg-white">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
      
      <div class="space-y-4">
        <h2 class="text-xl sm:text-2xl font-bold text-stone-900">
          Triết lý 'Cần cả một ngôi làng để nuôi dạy một đứa trẻ'
        </h2>
        <p class="text-stone-700 text-xs sm:text-sm leading-relaxed">
          Ngạn ngữ xưa có câu: <em>'It takes a village to raise a child'</em>. Nuôi dạy con là một hành trình dài cần sự sẻ chia, hỗ trợ từ gia đình và cộng đồng. Nutura xây dựng 'ngôi làng' của mình bằng việc cung cấp các kiến thức khoa học nuôi con bổ ích tại Góc cha mẹ, cùng các sản phẩm dinh dưỡng được kiểm định minh bạch theo tiêu chuẩn hữu cơ.
        </p>
      </div>

      <div class="space-y-4">
        <h2 class="text-xl sm:text-2xl font-bold text-stone-900">
          Nhà máy Nutura Organic tại bang Victoria, Úc
        </h2>
        <p class="text-stone-700 text-xs sm:text-sm leading-relaxed">
          Sản phẩm Nutura được sản xuất tại Mulgrave, Victoria, Australia bởi Nutura Organic Ltd. Nhà máy áp dụng quy trình kiểm soát chất lượng khép kín từ khâu tiếp nhận sữa tươi farmgate đến khâu đóng lon, đáp ứng các tiêu chuẩn nghiêm ngặt của Cơ quan Tiêu chuẩn Thực phẩm Úc & New Zealand (FSANZ).
        </p>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 pt-2 text-xs">
          <div class="p-4 rounded-2xl bg-stone-50 border border-stone-100">
            <div class="font-bold text-stone-900 mb-1">Địa điểm sản xuất</div>
            <div class="text-stone-600">Mulgrave, bang Victoria, Australia</div>
          </div>
          <div class="p-4 rounded-2xl bg-stone-50 border border-stone-100">
            <div class="font-bold text-stone-900 mb-1">Tiêu chuẩn áp dụng</div>
            <div class="text-stone-600">FSANZ Úc & Hữu cơ ACO</div>
          </div>
          <div class="p-4 rounded-2xl bg-stone-50 border border-stone-100">
            <div class="font-bold text-stone-900 mb-1">Nhập khẩu chính ngạch</div>
            <div class="text-stone-600">Phân phối bởi EVA Premium Mom and Baby</div>
          </div>
        </div>
      </div>

    </div>
  </section>
  </main>
"""
    content += render_footer()
    return content

def build_village():
    content = render_head(
        title="Góc cha mẹ | Cẩm nang nuôi dạy con chuẩn khoa học",
        description="Tuyển tập bài viết chia sẻ về tâm lý trẻ nhỏ, cẩm nang nuôi con và dinh dưỡng từ các tác giả uy tín tại Góc cha mẹ Nutura Việt Nam.",
        canonical_url="village.html"
    )
    content += render_topbar()
    content += render_breast_milk_banner()
    content += render_navbar(active_page="village")

    content += """
  <!-- Breadcrumb -->
  <div class="bg-[#FAF7F2] py-3.5 border-b border-stone-200/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-xs text-stone-500 flex items-center gap-2">
      <a href="index.html" class="hover:text-[#FF6F78]">Trang chủ</a>
      <span>/</span>
      <span class="text-stone-800 font-bold">Góc cha mẹ</span>
    </div>
  </div>

  <main id="main-content">
  <!-- Banner -->
  <section class="bg-[#FAF7F2] py-14 lg:py-18 border-b border-stone-200/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 md:grid-cols-12 gap-8 items-center">
        <div class="md:col-span-8 space-y-4">
          <span class="inline-block px-3 py-1 rounded-full bg-rose-100 text-[#FF6F78] text-xs font-bold uppercase tracking-wider">
            Cẩm nang nuôi con
          </span>
          <h1 class="text-2xl sm:text-3xl lg:text-4xl font-bold text-stone-900">
            Góc cha mẹ - Đồng hành nuôi dạy con
          </h1>
          <p class="text-stone-600 text-xs sm:text-sm leading-relaxed max-w-2xl">
            Chia sẻ các bài viết khoa học về tâm lý, cảm xúc và chế độ dinh dưỡng hàng ngày giúp ba mẹ thảnh thơi hơn trên hành trình nuôi con. Các bài viết mang tính giáo dục độc lập và không quảng bá sản phẩm.
          </p>
        </div>
        <div class="md:col-span-4 text-center">
          <img src="assets/images/banner-village.jpg" alt="Góc cha mẹ Nutura" class="rounded-3xl shadow-lg border-4 border-white max-h-60 mx-auto object-cover" loading="eager">
        </div>
      </div>
    </div>
  </section>

  <!-- Danh sách 9 bài viết blog (Không chèn link sản phẩm trong bài) -->
  <section class="py-14 bg-white flex-1">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
      
      <!-- Bài 1: Đặt tên cho bé -->
      <article id="article-1" class="grid grid-cols-1 md:grid-cols-12 gap-6 items-center pb-10 border-b border-stone-100">
        <div class="md:col-span-5">
          <img src="assets/images/blog-baby-names.jpg" alt="Đặt tên cho bé" class="rounded-2xl w-full h-56 object-cover shadow-sm" loading="lazy">
        </div>
        <div class="md:col-span-7 space-y-2.5">
          <div class="flex items-center gap-3 text-xs text-stone-400">
            <span class="font-bold text-[#FF6F78] bg-rose-50 px-2 py-0.5 rounded-full">Góc cha mẹ</span>
            <span>Tác giả: Nutura Việt Nam</span>
          </div>
          <h2 class="text-lg sm:text-xl font-bold text-stone-900">Mẹo và gợi ý khi đặt tên cho thiên thần nhỏ sắp chào đời</h2>
          <p class="text-stone-600 text-xs leading-relaxed">
            Chúc mừng bạn sắp đón nhận một sinh linh bé bỏng. Việc lựa chọn một cái tên theo con suốt cuộc đời là quyết định quan trọng. Hãy cân nhắc ý nghĩa phong thủy, âm điệu khi gọi tên, kỷ niệm tình yêu của bố mẹ và sự hòa hợp giữa các thành viên trong gia đình.
          </p>
        </div>
      </article>

      <!-- Bài 2: Ngày đầu đi học -->
      <article id="article-2" class="grid grid-cols-1 md:grid-cols-12 gap-6 items-center pb-10 border-b border-stone-100">
        <div class="md:col-span-5">
          <img src="assets/images/blog-school.jpg" alt="Ngày đầu đi học" class="rounded-2xl w-full h-56 object-cover shadow-sm" loading="lazy">
        </div>
        <div class="md:col-span-7 space-y-2.5">
          <div class="flex items-center gap-3 text-xs text-stone-400">
            <span class="font-bold text-[#FF6F78] bg-rose-50 px-2 py-0.5 rounded-full">Tâm lý thiếu nhi</span>
            <span>Tác giả: Dr. Michael Carr-Gregg</span>
          </div>
          <h2 class="text-lg sm:text-xl font-bold text-stone-900">Cách chuẩn bị hành trang tâm lý cho con vào ngày đầu tiên đến trường</h2>
          <p class="text-stone-600 text-xs leading-relaxed">
            Bước qua cánh cổng trường học là một bước ngoặt lớn đối với trẻ em. Cha mẹ nên cùng con làm quen với đường đến trường trước ngày khai giảng, đọc những cuốn sách về bạn bè lớp học và quan trọng nhất: rèn luyện cho con kỹ năng tự phục vụ cơ bản để con cảm thấy tự tin.
          </p>
        </div>
      </article>

      <!-- Bài 3: Góc người bố -->
      <article id="article-3" class="grid grid-cols-1 md:grid-cols-12 gap-6 items-center pb-10 border-b border-stone-100">
        <div class="md:col-span-5">
          <img src="assets/images/jimmy-rees.png" alt="Góc người bố Jimmy Rees" class="rounded-2xl w-full h-56 object-cover shadow-sm bg-stone-50" loading="lazy">
        </div>
        <div class="md:col-span-7 space-y-2.5">
          <div class="flex items-center gap-3 text-xs text-stone-400">
            <span class="font-bold text-[#FF6F78] bg-rose-50 px-2 py-0.5 rounded-full">Góc người bố</span>
            <span>Tác giả: Jimmy Rees</span>
          </div>
          <h2 class="text-lg sm:text-xl font-bold text-stone-900">Khi mẹ có một đêm được nghỉ ngơi trọn vẹn</h2>
          <p class="text-stone-600 text-xs leading-relaxed">
            Nuôi con là công việc toàn thời gian không ngày nghỉ của mẹ. Một đêm mẹ được đi ngủ sớm và được người bạn đời chia sẻ trách nhiệm chăm con chính là món quà phục hồi tinh thần ý nghĩa.
          </p>
        </div>
      </article>

      <!-- Bài 4: Buông bỏ gánh nặng -->
      <article id="article-4" class="grid grid-cols-1 md:grid-cols-12 gap-6 items-center pb-10 border-b border-stone-100">
        <div class="md:col-span-5">
          <img src="assets/images/blog-lighten-load.jpg" alt="Buông bỏ gánh nặng làm mẹ" class="rounded-2xl w-full h-56 object-cover shadow-sm" loading="lazy">
        </div>
        <div class="md:col-span-7 space-y-2.5">
          <div class="flex items-center gap-3 text-xs text-stone-400">
            <span class="font-bold text-[#FF6F78] bg-rose-50 px-2 py-0.5 rounded-full">Cảm xúc làm mẹ</span>
            <span>Tác giả: Kirsty Levin</span>
          </div>
          <h2 class="text-lg sm:text-xl font-bold text-stone-900">Học cách buông bỏ để nhẹ bớt gánh nặng trách nhiệm</h2>
          <p class="text-stone-600 text-xs leading-relaxed">
            Người mẹ hiện đại thường tự đặt lên vai mình áp lực phải trở thành một người mẹ hoàn hảo. Hãy học cách nhờ sự giúp đỡ của người thân và buông bỏ những tiêu chuẩn khắt khe không cần thiết để tận hưởng niềm vui làm mẹ.
          </p>
        </div>
      </article>

      <!-- Bài 5: Hormone hạnh phúc -->
      <article id="article-5" class="grid grid-cols-1 md:grid-cols-12 gap-6 items-center pb-10 border-b border-stone-100">
        <div class="md:col-span-5">
          <img src="assets/images/blog-happiness.jpg" alt="Hormone hạnh phúc" class="rounded-2xl w-full h-56 object-cover shadow-sm" loading="lazy">
        </div>
        <div class="md:col-span-7 space-y-2.5">
          <div class="flex items-center gap-3 text-xs text-stone-400">
            <span class="font-bold text-[#FF6F78] bg-rose-50 px-2 py-0.5 rounded-full">Khoa học cảm xúc</span>
            <span>Tác giả: Kirsty Levin</span>
          </div>
          <h2 class="text-lg sm:text-xl font-bold text-stone-900">Bí quyết kích hoạt các hormone hạnh phúc mỗi ngày</h2>
          <p class="text-stone-600 text-xs leading-relaxed">
            Hormone Oxytocin được kích hoạt khi bạn ôm ấp con da kề da. Dành 10 phút tắm nắng buổi sáng để thúc đẩy Serotonin, giúp mẹ duy trì tâm trạng an vui và giàu năng lượng tích cực trong ngày.
          </p>
        </div>
      </article>

      <!-- Bài 6: Sắt cho bé (Đã sửa bỏ nhắc tên sản phẩm) -->
      <article id="article-6" class="grid grid-cols-1 md:grid-cols-12 gap-6 items-center pb-10 border-b border-stone-100">
        <div class="md:col-span-5">
          <img src="assets/images/blog-iron.jpg" alt="Bổ sung sắt cho bé" class="rounded-2xl w-full h-56 object-cover shadow-sm" loading="lazy">
        </div>
        <div class="md:col-span-7 space-y-2.5">
          <div class="flex items-center gap-3 text-xs text-stone-400">
            <span class="font-bold text-[#FF6F78] bg-rose-50 px-2 py-0.5 rounded-full">Dinh dưỡng trẻ nhỏ</span>
            <span>Tác giả: Miriam Raleigh</span>
          </div>
          <h2 class="text-lg sm:text-xl font-bold text-stone-900">Bé nhà bạn đã nạp đủ lượng sắt cần thiết chưa?</h2>
          <p class="text-stone-600 text-xs leading-relaxed">
            Lượng sắt dự trữ từ giai đoạn thai kỳ sẽ giảm dần khi bé đạt 6 tháng tuổi. Thiếu sắt ở trẻ nhỏ có thể dẫn đến mệt mỏi và chậm tăng cân. Cha mẹ hãy chú trọng bổ sung thực phẩm giàu sắt tự nhiên như thịt bò, lòng đỏ trứng, kết hợp cùng các loại rau củ giàu vitamin C để hỗ trợ hấp thu sắt tốt hơn.
          </p>
        </div>
      </article>

      <!-- Bài 7: Dinh dưỡng mầm non -->
      <article id="article-7" class="grid grid-cols-1 md:grid-cols-12 gap-6 items-center pb-10 border-b border-stone-100">
        <div class="md:col-span-5">
          <img src="assets/images/blog-food.jpg" alt="Dinh dưỡng mầm non" class="rounded-2xl w-full h-56 object-cover shadow-sm" loading="lazy">
        </div>
        <div class="md:col-span-7 space-y-2.5">
          <div class="flex items-center gap-3 text-xs text-stone-400">
            <span class="font-bold text-[#FF6F78] bg-rose-50 px-2 py-0.5 rounded-full">Ăn dặm & dinh dưỡng</span>
            <span>Tác giả: Miriam Raleigh</span>
          </div>
          <h2 class="text-lg sm:text-xl font-bold text-stone-900">Trẻ tuổi mầm non và mẫu giáo nên ăn những nhóm thực phẩm nào?</h2>
          <p class="text-stone-600 text-xs leading-relaxed">
            Giai đoạn mẫu giáo trẻ vận động rất nhiều. Trẻ cần chế độ ăn đa dạng với các nhóm: tinh bột nguyên cám, chất đạm nạc, rau xanh đậm và trái cây tươi để cung cấp đầy đủ vitamin và khoáng chất thiết yếu.
          </p>
        </div>
      </article>

      <!-- Bài 8: Gắn bó an toàn -->
      <article id="article-8" class="grid grid-cols-1 md:grid-cols-12 gap-6 items-center pb-10 border-b border-stone-100">
        <div class="md:col-span-5">
          <img src="assets/images/blog-attachment.jpg" alt="Gắn bó an toàn với con" class="rounded-2xl w-full h-56 object-cover shadow-sm" loading="lazy">
        </div>
        <div class="md:col-span-7 space-y-2.5">
          <div class="flex items-center gap-3 text-xs text-stone-400">
            <span class="font-bold text-[#FF6F78] bg-rose-50 px-2 py-0.5 rounded-full">Tâm lý phát triển</span>
            <span>Tác giả: Kirsty Levin</span>
          </div>
          <h2 class="text-lg sm:text-xl font-bold text-stone-900">Gắn bó an toàn (Secure Attachment) là gì và vì sao quan trọng?</h2>
          <p class="text-stone-600 text-xs leading-relaxed">
            Gắn bó an toàn được hình thành khi cha mẹ phản hồi nhất quán, kịp thời và yêu thương trước những tín hiệu khóc hay cần ôm ấp của trẻ. Đây chính là điểm tựa cảm xúc giúp con lớn lên tự tin và kiên cường.
          </p>
        </div>
      </article>

      <!-- Bài 9: Khám phá xúc giác -->
      <article id="article-9" class="grid grid-cols-1 md:grid-cols-12 gap-6 items-center">
        <div class="md:col-span-5">
          <img src="assets/images/blog-touch.jpg" alt="Khám phá xúc giác của trẻ" class="rounded-2xl w-full h-56 object-cover shadow-sm" loading="lazy">
        </div>
        <div class="md:col-span-7 space-y-2.5">
          <div class="flex items-center gap-3 text-xs text-stone-400">
            <span class="font-bold text-[#FF6F78] bg-rose-50 px-2 py-0.5 rounded-full">Khoa học cảm giác</span>
            <span>Tác giả: Dr. Michael Carr-Gregg</span>
          </div>
          <h2 class="text-lg sm:text-xl font-bold text-stone-900">Khám phá xúc giác của trẻ sơ sinh</h2>
          <p class="text-stone-600 text-xs leading-relaxed">
            Xúc giác là giác quan đầu tiên phát triển trong thai kỳ. Massage nhẹ nhàng cho bé trước giờ ngủ giúp bé thư giãn, ngủ sâu và tăng cường sự gắn kết mật thiết giữa cha mẹ và con nhỏ.
          </p>
        </div>
      </article>

    </div>
  </section>
  </main>
"""
    content += render_footer()
    return content

def build_faqs():
    content = render_head(
        title="Câu hỏi thường gặp về sản phẩm & cách pha sữa Nutura",
        description="Giải đáp các câu hỏi thường gặp về sản phẩm Nutura Organic: Nguồn gốc sữa tươi farmgate, chứng nhận hữu cơ ACO, đạm A2 và hướng dẫn pha theo nhãn.",
        canonical_url="faqs.html"
    )
    content += render_topbar()
    content += render_breast_milk_banner()
    content += render_navbar(active_page="village")

    content += """
  <!-- Breadcrumb -->
  <div class="bg-[#FAF7F2] py-3.5 border-b border-stone-200/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-xs text-stone-500 flex items-center gap-2">
      <a href="index.html" class="hover:text-[#FF6F78]">Trang chủ</a>
      <span>/</span>
      <span class="text-stone-800 font-bold">Câu hỏi thường gặp</span>
    </div>
  </div>

  <main id="main-content">
  <!-- Banner -->
  <section class="bg-[#FAF7F2] py-14 lg:py-18 border-b border-stone-200/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 md:grid-cols-12 gap-8 items-center">
        <div class="md:col-span-8 space-y-4">
          <span class="inline-block px-3 py-1 rounded-full bg-rose-100 text-[#FF6F78] text-xs font-bold uppercase tracking-wider">
            Tra cứu thông tin
          </span>
          <h1 class="text-2xl sm:text-3xl lg:text-4xl font-bold text-stone-900">
            Câu hỏi thường gặp (FAQs)
          </h1>
          <p class="text-stone-600 text-xs sm:text-sm leading-relaxed max-w-2xl">
            Giải đáp những thắc mắc phổ biến về nguồn gốc sữa tươi farmgate, chứng nhận hữu cơ ACO và cách pha theo nhãn từng giai đoạn.
          </p>
        </div>
        <div class="md:col-span-4 text-center">
          <img src="assets/images/banner-faq.jpg" alt="FAQs Nutura" class="rounded-3xl shadow-lg border-4 border-white max-h-56 mx-auto object-cover" loading="eager">
        </div>
      </div>
    </div>
  </section>

  <!-- FAQ Accordion (Chỉ giữ nhóm sản phẩm, pha chế, bảo quản - Đã bỏ hẳn nhóm đặt hàng / vận chuyển) -->
  <section class="py-14 bg-white flex-1">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 space-y-10">

      <!-- Nhóm 1: Sản phẩm & Nguồn gốc -->
      <div class="space-y-4">
        <h2 class="text-lg sm:text-xl font-bold text-stone-900 border-b border-stone-200 pb-2 flex items-center gap-2">
          <span>🌿</span> 1. Thông tin sản phẩm & chứng nhận
        </h2>

        <div class="faq-item">
          <button class="faq-question text-xs sm:text-sm">
            <span>Sản phẩm Nutura Organic có chứng nhận hữu cơ chính thức không?</span>
            <span class="faq-icon">▼</span>
          </button>
          <div class="faq-answer text-xs space-y-2 text-stone-600">
            <p>Bộ nhãn Nutura Organic A2 Stage 1, 2 và 3 thể hiện logo chứng nhận hữu cơ <strong>ACO Certified Organic</strong>. Tiêu chuẩn này xác nhận sản phẩm không chứa hóa chất tổng hợp, phân bón hóa học hay hormone tăng trưởng theo chuẩn hữu cơ của Úc.</p>
          </div>
        </div>

        <div class="faq-item">
          <button class="faq-question text-xs sm:text-sm">
            <span>Sữa Nutura được sản xuất ở đâu?</span>
            <span class="faq-icon">▼</span>
          </button>
          <div class="faq-answer text-xs space-y-2 text-stone-600">
            <p>Sản phẩm được nghiên cứu, chế biến và đóng lon tại <strong>Mulgrave, tiểu bang Victoria, Úc</strong> bởi Nutura Organic Ltd, tuân thủ tiêu chuẩn an toàn thực phẩm FSANZ.</p>
          </div>
        </div>

        <div class="faq-item">
          <button class="faq-question text-xs sm:text-sm">
            <span>Bảng dinh dưỡng ghi có đường (sugars), sữa có thêm đường không?</span>
            <span class="faq-icon">▼</span>
          </button>
          <div class="faq-answer text-xs space-y-2 text-stone-600">
            <p>Sản phẩm <strong>không thêm đường mía (sucrose)</strong> hay chất tạo ngọt nhân tạo. Lượng đường trên bảng dinh dưỡng là <strong>đường lactose tự nhiên</strong> vốn có trong sữa bò tươi.</p>
          </div>
        </div>

        <div class="faq-item">
          <button class="faq-question text-xs sm:text-sm">
            <span>Thành phần có chứa biến đổi gen (GMO) không?</span>
            <span class="faq-icon">▼</span>
          </button>
          <div class="faq-answer text-xs space-y-2 text-stone-600">
            <p>Nhãn lon thể hiện biểu tượng No GMO Ingredients. Quy trình kiểm tra nguyên liệu và chuỗi cung ứng hữu cơ ACO không cho phép sử dụng thành phần biến đổi gen.</p>
          </div>
        </div>
      </div>

      <!-- Nhóm 2: Cách pha & bảo quản -->
      <div class="space-y-4">
        <h2 class="text-lg sm:text-xl font-bold text-stone-900 border-b border-stone-200 pb-2 flex items-center gap-2">
          <span>🍼</span> 2. Pha chế & bảo quản theo nhãn
        </h2>

        <div class="faq-item open">
          <button class="faq-question text-xs sm:text-sm">
            <span>Một muỗng gạt ngang bột sữa tương đương bao nhiêu gram?</span>
            <span class="faq-icon">▼</span>
          </button>
          <div class="faq-answer text-xs space-y-2 text-stone-600">
            <p>Theo nhãn từng sản phẩm:</p>
            <p>• <strong>Stage 1:</strong> 1 muỗng gạt ngang = 4,6 g bột, pha với 30 ml nước ấm.</p>
            <p>• <strong>Stage 2:</strong> 1 muỗng gạt ngang = 4,5 g bột, pha với 30 ml nước ấm.</p>
            <p>• <strong>Stage 3:</strong> 1 muỗng gạt ngang = 6 g bột (pha 6 muỗng với 200 ml nước ấm).</p>
            <p>Chỉ sử dụng muỗng lường có sẵn trong lon và không tự ý thay đổi tỷ lệ trừ khi có chỉ định của cán bộ y tế.</p>
          </div>
        </div>

        <div class="faq-item">
          <button class="faq-question text-xs sm:text-sm">
            <span>Lon sữa sau khi mở nắp dùng được trong bao lâu? Có để tủ lạnh được không?</span>
            <span class="faq-icon">▼</span>
          </button>
          <div class="faq-answer text-xs space-y-2 text-stone-600">
            <p>Lon sữa sau khi mở nắp cần đậy kín nắp nhựa và sử dụng hết trong vòng <strong>4 tuần</strong>. Bảo quản nơi khô ráo, thoáng mát dưới 25°C. <strong>Không bảo quản lon sữa bột trong tủ lạnh</strong> vì độ ẩm có thể làm bột vón cục.</p>
          </div>
        </div>

        <div class="faq-item">
          <button class="faq-question text-xs sm:text-sm">
            <span>Sữa đã pha để được bao lâu?</span>
            <span class="faq-icon">▼</span>
          </button>
          <div class="faq-answer text-xs space-y-2 text-stone-600">
            <p>Nên cho trẻ uống ngay sau khi pha xong. Không lưu trữ bình sữa bé đã uống dở; cần đổ bỏ lượng sữa còn lại sau mỗi cữ ăn để đảm bảo vệ sinh an toàn cho trẻ.</p>
          </div>
        </div>
      </div>

    </div>
  </section>
  </main>
"""
    content += render_footer()
    return content

def build_contact():
    content = render_head(
        title="Liên hệ & Thông tin điểm bán | Nutura Việt Nam",
        description="Thông tin liên hệ chính thức của Nutura Việt Nam và danh sách điểm bán. Đơn vị chịu trách nhiệm nội dung: Công ty TNHH EVA Premium Mom and Baby.",
        canonical_url="contact.html"
    )
    content += render_topbar()
    content += render_breast_milk_banner()
    content += render_navbar(active_page="contact")

    content += """
  <!-- Breadcrumb -->
  <div class="bg-[#FAF7F2] py-3.5 border-b border-stone-200/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-xs text-stone-500 flex items-center gap-2">
      <a href="index.html" class="hover:text-[#FF6F78]">Trang chủ</a>
      <span>/</span>
      <span class="text-stone-800 font-bold">Liên hệ & điểm bán</span>
    </div>
  </div>

  <main id="main-content">
  <!-- Banner -->
  <section class="bg-[#FAF7F2] py-14 lg:py-18 border-b border-stone-200/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-3xl mx-auto space-y-3">
        <span class="inline-block px-3 py-1 rounded-full bg-rose-100 text-[#FF6F78] text-xs font-bold uppercase tracking-wider">
          Hỗ trợ thông tin
        </span>
        <h1 class="text-2xl sm:text-3xl lg:text-4xl font-bold text-stone-900">
          Liên hệ & điểm phân phối
        </h1>
        <p class="text-stone-600 text-xs sm:text-sm leading-relaxed">
          Giải đáp thắc mắc về tra cứu nhãn, hướng dẫn sử dụng sản phẩm và thông tin hệ thống phân phối Nutura Việt Nam.
        </p>
      </div>
    </div>
  </section>

  <!-- Danh sách điểm bán & Form liên hệ -->
  <section class="py-14 bg-white flex-1">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">

      <!-- Khối tra cứu điểm bán -->
      <div id="diem-ban" class="p-6 sm:p-10 rounded-3xl bg-[#FAF7F2] border border-stone-200/80 space-y-4">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-2xl bg-[#FF6F78] text-white flex items-center justify-center font-bold text-lg">
            📍
          </div>
          <div>
            <h2 class="text-xl font-bold text-stone-900">Hệ thống điểm phân phối Nutura</h2>
            <p class="text-xs text-stone-500">Tra cứu điểm bán chính hãng gần bạn</p>
          </div>
        </div>

        <div class="p-5 bg-white rounded-2xl border border-stone-200 space-y-3 text-xs text-stone-700 leading-relaxed">
          <p class="font-medium text-stone-900">
            Danh sách các chuỗi cửa hàng mẹ & bé và điểm bán lẻ ủy quyền đang được cập nhật chính thức.
          </p>
          <p>
            Để biết cửa hàng phân phối sản phẩm Nutura chính hãng gần bạn nhất hoặc tìm hiểu phương thức hợp tác đại lý, vui lòng liên hệ trực tiếp với bộ phận chăm sóc khách hàng qua hotline hoặc email bên dưới.
          </p>
          <div class="pt-2 flex flex-wrap gap-4 text-xs">
            <div><strong>Hotline hỗ trợ:</strong> <span class="text-[#FF6F78] font-bold">1800 827 957</span> (8:00 - 17:00, Thứ 2 - Thứ 6)</div>
            <div><strong>Email hỗ trợ:</strong> lienhe@nuturavietnam.vn</div>
          </div>
        </div>
      </div>

      <!-- Form gửi câu hỏi & Thông tin pháp nhân -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10">
        <!-- Form gửi thắc mắc -->
        <div class="lg:col-span-7 bg-[#FAF7F2] p-6 sm:p-8 rounded-3xl border border-stone-200/80">
          <h2 class="text-lg font-bold text-stone-900 mb-4">Gửi câu hỏi về thông tin sản phẩm</h2>
          <form onsubmit="event.preventDefault(); alert('Cảm ơn bạn đã gửi thông tin. Bộ phận chăm sóc khách hàng sẽ phản hồi qua email hoặc số điện thoại của bạn.');" class="space-y-3 text-xs">
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
              <div>
                <label for="contactName" class="block font-bold text-stone-700 mb-1">Họ và tên *</label>
                <input id="contactName" required placeholder="Nguyễn Văn A" class="w-full px-3.5 py-2.5 bg-white border border-stone-300 rounded-xl focus:outline-none focus:border-[#FF6F78]">
              </div>
              <div>
                <label for="contactPhone" class="block font-bold text-stone-700 mb-1">Số điện thoại *</label>
                <input id="contactPhone" required type="tel" placeholder="0901 234 567" class="w-full px-3.5 py-2.5 bg-white border border-stone-300 rounded-xl focus:outline-none focus:border-[#FF6F78]">
              </div>
            </div>

            <div>
              <label for="contactEmail" class="block font-bold text-stone-700 mb-1">Địa chỉ email *</label>
              <input id="contactEmail" required type="email" placeholder="email@domain.com" class="w-full px-3.5 py-2.5 bg-white border border-stone-300 rounded-xl focus:outline-none focus:border-[#FF6F78]">
            </div>

            <div>
              <label for="contactSubject" class="block font-bold text-stone-700 mb-1">Nội dung cần hỗ trợ *</label>
              <textarea id="contactSubject" required rows="4" placeholder="Nhập nội dung bạn cần hỗ trợ về nhãn, thành phần hoặc điểm bán..." class="w-full px-3.5 py-2.5 bg-white border border-stone-300 rounded-xl focus:outline-none focus:border-[#FF6F78]"></textarea>
            </div>

            <button type="submit" class="w-full py-3 bg-[#FF6F78] hover:bg-[#E65A63] text-white font-bold rounded-xl transition shadow-md">
              Gửi câu hỏi
            </button>
          </form>
        </div>

        <!-- Thông tin pháp nhân EVA Premium Mom and Baby -->
        <div class="lg:col-span-5 space-y-5 text-xs text-stone-600">
          <div class="p-6 bg-stone-50 rounded-3xl border border-stone-200 space-y-3">
            <h3 class="font-bold text-stone-900 text-sm">Pháp nhân chịu trách nhiệm nội dung</h3>
            <p class="font-semibold text-stone-800 text-xs">Công ty TNHH EVA Premium Mom and Baby</p>
            <p>EVA Premium Mom and Baby Co., Ltd.</p>
            <p><strong>Địa chỉ:</strong> Tỉnh Lâm Đồng, Việt Nam</p>
            <p><strong>Mã số thuế:</strong> Đang cập nhật (chưa xác minh)</p>
            <p><strong>Hotline:</strong> 1800 827 957</p>
            <p><strong>Email chính thức:</strong> lienhe@nuturavietnam.vn</p>
          </div>

          <div class="p-6 bg-stone-50 rounded-3xl border border-stone-200 space-y-2">
            <h3 class="font-bold text-stone-900 text-sm">Thông tin nhà sản xuất</h3>
            <p class="font-semibold text-stone-800">Nutura Organic Ltd</p>
            <p>Mulgrave, Victoria, Australia</p>
            <p>100% sản xuất và đóng lon tại Úc</p>
          </div>
        </div>
      </div>

    </div>
  </section>
  </main>
"""
    content += render_footer()
    return content

print("pages_village.py ready")
