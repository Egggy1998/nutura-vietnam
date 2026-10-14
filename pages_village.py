# -*- coding: utf-8 -*-
"""
Community & Support Pages:
- about-us.html
- village.html
- subscriptions.html
- faqs.html
- contact.html
- cart.html
"""

from build_site import render_head, render_topbar, render_navbar, render_footer

def build_about_us():
    content = render_head(
        title="Về Chúng Tôi | Câu Chuyện & Đội Ngũ Chuyên Gia Nutura Village",
        description="Tìm hiểu câu chuyện Nutura Organic: Sứ mệnh tạo dựng dinh dưỡng hữu cơ thanh lành cho trẻ em và triết lý 'Takes a village to raise a child'. Gặp gỡ các chuyên gia hàng đầu.",
        canonical_url="about-us.html"
    )
    content += render_topbar()
    content += render_navbar(active_page="about")

    content += """
  <!-- HERO BANNER -->
  <section class="bg-[#FAF7F2] py-16 lg:py-24 border-b border-stone-200/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        <div class="lg:col-span-7 space-y-6">
          <span class="inline-block px-3 py-1 rounded-full bg-rose-100 text-[#FF6F78] text-xs font-bold uppercase tracking-wider">
            Câu Chuyện Của Chúng Tôi
          </span>
          <h1 class="text-3xl sm:text-4xl lg:text-5xl font-bold text-stone-900 leading-tight">
            Nuôi Dưỡng Bởi Thiên Nhiên, Kiến Tạo Bởi Chuyên Gia
          </h1>
          <p class="text-stone-700 text-base leading-relaxed">
            Hành trình của Nutura bắt nguồn từ một mong ước giản dị nhưng thiêng liêng của các bậc làm cha mẹ tại Úc: Mang đến cho con nguồn dinh dưỡng thuần khiết, an toàn nhất, đồng thời kiến tạo một cộng đồng chuyên gia tin cậy để nâng đỡ các gia đình trong suốt hành trình nuôi con.
          </p>
        </div>
        <div class="lg:col-span-5 text-center">
          <img src="assets/images/team-group.jpg" alt="Đội ngũ Nutura" class="rounded-3xl shadow-2xl border-4 border-white max-h-88 mx-auto object-cover">
        </div>
      </div>
    </div>
  </section>

  <!-- BRAND STORY & PHILOSOPHY -->
  <section class="py-16 lg:py-20 bg-white">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
      <div class="space-y-4">
        <h2 class="text-2xl sm:text-3xl font-bold text-stone-900">
          "Cần Cả Một Ngôi Làng Để Nuôi Dạy Một Đứa Trẻ"
        </h2>
        <p class="text-stone-700 text-sm sm:text-base leading-relaxed">
          Ngạn ngữ xưa có câu: <em>"It takes a village to raise a child"</em>. Trong thế giới hiện đại đầy áp lực và thông tin nhiễu loạn, việc nuôi con chưa bao giờ là hành trình đơn độc. Tại Nutura, chúng tôi xây dựng một "ngôi làng" đúng nghĩa -  Nơi các bậc phụ huynh tìm thấy sự đồng cảm, các giải pháp dinh dưỡng dựa trên bằng chứng khoa học, và lời khuyên ấm áp từ những chuyên gia giàu tâm huyết.
        </p>
      </div>

      <div class="space-y-4">
        <h2 class="text-2xl sm:text-3xl font-bold text-stone-900">
          Lịch Sử & Cam Kết Tiên Phong Đổi Mới
        </h2>
        <p class="text-stone-700 text-sm sm:text-base leading-relaxed">
          Nutura là thương hiệu sữa từ Úc. Bộ nhãn Organic A2 Stage 1–3 trong tài liệu sản phẩm thể hiện chứng nhận hữu cơ <strong>ACO</strong> và biểu tượng Made in Australia. Thông tin công thức, hướng dẫn sử dụng và chứng nhận áp dụng cần được đối chiếu theo nhãn từng sản phẩm.
        </p>
      </div>

      <!-- MEET THE VILLAGE EXPERTS -->
      <div id="team" class="pt-8 border-t border-stone-200 space-y-8">
        <div class="text-center space-y-2">
          <span class="text-xs font-bold text-[#FF6F78] uppercase tracking-widest">Đội Ngũ Đồng Hành</span>
          <h2 class="text-3xl font-bold text-stone-900">Gặp Gỡ Các Chuyên Gia Của Ngôi Làng Nutura</h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          <div class="p-6 bg-[#FAF7F2] rounded-3xl text-center space-y-3 border border-stone-200/80">
            <img src="assets/images/dr-michael.jpg" alt="Dr Michael Carr-Gregg" class="w-28 h-28 rounded-full mx-auto object-cover border-4 border-white shadow-md">
            <h3 class="font-bold text-stone-900 text-base">Dr. Michael Carr-Gregg</h3>
            <p class="text-xs text-[#FF6F78] font-bold">Chuyên Gia Tâm Lý Nhi Khoa</p>
            <p class="text-xs text-stone-600 leading-relaxed">Tiến sĩ tâm lý thiếu nhi hàng đầu nước Úc, tác giả của nhiều cuốn sách bán chạy về hành vi và sức khỏe tinh thần trẻ thơ.</p>
          </div>

          <div class="p-6 bg-[#FAF7F2] rounded-3xl text-center space-y-3 border border-stone-200/80">
            <img src="assets/images/miriam-raleigh.jpg" alt="Miriam Raleigh" class="w-28 h-28 rounded-full mx-auto object-cover border-4 border-white shadow-md">
            <h3 class="font-bold text-stone-900 text-base">Miriam Raleigh</h3>
            <p class="text-xs text-[#FF6F78] font-bold">Chuyên Gia Dinh Dưỡng Nhi</p>
            <p class="text-xs text-stone-600 leading-relaxed">Chuyên gia dinh dưỡng lâm sàng trẻ em, cố vấn hàng đầu về ăn dặm, hấp thu vi chất và phát triển chiều cao.</p>
          </div>

          <div class="p-6 bg-[#FAF7F2] rounded-3xl text-center space-y-3 border border-stone-200/80">
            <img src="assets/images/kirsty-levin.jpg" alt="Kirsty Levin" class="w-28 h-28 rounded-full mx-auto object-cover border-4 border-white shadow-md">
            <h3 class="font-bold text-stone-900 text-base">Kirsty Levin</h3>
            <p class="text-xs text-[#FF6F78] font-bold">Nhà Tâm Lý Học Gia Đình</p>
            <p class="text-xs text-stone-600 leading-relaxed">Sáng lập The Parents Village, chuyên gia đồng hành cùng người mẹ vượt qua trầm cảm sau sinh và tìm lại cân bằng cảm xúc.</p>
          </div>

          <div class="p-6 bg-[#FAF7F2] rounded-3xl text-center space-y-3 border border-stone-200/80">
            <img src="assets/images/jimmy-rees.png" alt="Jimmy Rees" class="w-28 h-28 rounded-full mx-auto object-cover border-4 border-white shadow-md">
            <h3 class="font-bold text-stone-900 text-base">Jimmy Rees</h3>
            <p class="text-xs text-[#FF6F78] font-bold">Đại Sứ Làm Cha Mẹ</p>
            <p class="text-xs text-stone-600 leading-relaxed">Nghệ sĩ hài và người bố nổi tiếng của 3 nhóc tì, mang tiếng cười và sự lạc quan truyền cảm hứng đến hàng triệu gia đình.</p>
          </div>
        </div>
      </div>
    </div>
  </section>
"""
    content += render_footer()
    return content

def build_village():
    content = render_head(
        title="Ngôi Làng Nutura & Góc Cha Mẹ | Cẩm Nang Nuôi Con Toàn Diện",
        description="Tuyển tập bài viết chia sẻ từ các chuyên gia y tế, dinh dưỡng và tâm lý học trẻ em hàng đầu của Nutura Village. Kiến thức nuôi dạy con chuẩn khoa học.",
        canonical_url="village.html"
    )
    content += render_topbar()
    content += render_navbar(active_page="village")

    content += """
  <!-- BANNER -->
  <section class="bg-[#FAF7F2] py-16 lg:py-20 border-b border-stone-200/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 md:grid-cols-12 gap-8 items-center">
        <div class="md:col-span-8 space-y-4">
          <span class="inline-block px-3 py-1 rounded-full bg-rose-100 text-[#FF6F78] text-xs font-bold uppercase tracking-wider">
            Ngôi Làng Tri Thức Nutura
          </span>
          <h1 class="text-3xl sm:text-4xl lg:text-5xl font-bold text-stone-900">
            Góc Cha Mẹ: Dinh Dưỡng, Cảm Xúc & Yêu Thương
          </h1>
          <p class="text-stone-600 text-sm sm:text-base leading-relaxed max-w-2xl">
            Nơi bạn tìm thấy sự sẻ chia ấm áp và những hướng dẫn khoa học từ đội ngũ bác sĩ nhi khoa, chuyên gia dinh dưỡng và các bậc phụ huynh giàu kinh nghiệm. Bạn không bao giờ phải đơn độc trên hành trình này!
          </p>
        </div>
        <div class="md:col-span-4 text-center">
          <img src="assets/images/banner-village.jpg" alt="Ngôi làng Nutura" class="rounded-3xl shadow-lg border-4 border-white max-h-64 mx-auto object-cover">
        </div>
      </div>
    </div>
  </section>

  <!-- ARTICLES LIST -->
  <section class="py-16 bg-white flex-1">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-16">
      
      <!-- Article 1 -->
      <article id="article-1" class="grid grid-cols-1 md:grid-cols-12 gap-8 items-center pb-12 border-b border-stone-100">
        <div class="md:col-span-5">
          <img src="assets/images/blog-baby-names.jpg" alt="Đặt tên cho bé" class="rounded-3xl w-full h-64 object-cover shadow-sm">
        </div>
        <div class="md:col-span-7 space-y-3">
          <div class="flex items-center gap-3 text-xs text-stone-400">
            <span class="font-bold text-[#FF6F78] bg-rose-50 px-2.5 py-1 rounded-full">Góc Cha Mẹ</span>
            <span>Tác giả: Nutura Organic</span>
          </div>
          <h2 class="text-2xl font-bold text-stone-900">Mẹo Và Gợi Ý Khi Đặt Tên Cho Thiên Thần Nhỏ Sắp Chào Đời</h2>
          <p class="text-stone-600 text-xs sm:text-sm leading-relaxed">
            Chúc mừng bạn sắp đón nhận một sinh linh bé bỏng! Khoảnh khắc biết mình mang thai luôn tràn ngập cảm xúc diệu kỳ xen lẫn hồi hộp. Việc lựa chọn một cái tên theo con suốt cuộc đời là quyết định quan trọng. Hãy cân nhắc ý nghĩa phong thủy, âm điệu khi gọi tên, kỷ niệm tình yêu của bố mẹ và cả sự hòa hợp giữa các thành viên trong gia đình.
          </p>
        </div>
      </article>

      <!-- Article 2 -->
      <article id="article-2" class="grid grid-cols-1 md:grid-cols-12 gap-8 items-center pb-12 border-b border-stone-100">
        <div class="md:col-span-5">
          <img src="assets/images/blog-school.jpg" alt="Ngày đầu đi học" class="rounded-3xl w-full h-64 object-cover shadow-sm">
        </div>
        <div class="md:col-span-7 space-y-3">
          <div class="flex items-center gap-3 text-xs text-stone-400">
            <span class="font-bold text-[#FF6F78] bg-rose-50 px-2.5 py-1 rounded-full">Tâm Lý Thiếu Nhi</span>
            <span>Tác giả: Dr. Michael Carr-Gregg</span>
          </div>
          <h2 class="text-2xl font-bold text-stone-900">Cách Chuẩn Bị Hành Trang Tâm Lý Cho Con Vào Ngày Đầu Tiên Đến Trường</h2>
          <p class="text-stone-600 text-xs sm:text-sm leading-relaxed">
            Bước qua cánh cổng trường học là một bước ngoặt khổng lồ đối với trẻ em. Tiến sĩ Michael Carr-Gregg khuyến nghị cha mẹ nên cùng con làm quen với đường đến trường trước ngày khai giảng, đọc những cuốn sách về bạn bè lớp học và quan trọng nhất: Hãy rèn luyện cho con kỹ năng tự phục vụ cơ bản để con cảm thấy tự tin và kiểm soát được bản thân.
          </p>
        </div>
      </article>

      <!-- Article 3 -->
      <article id="article-3" class="grid grid-cols-1 md:grid-cols-12 gap-8 items-center pb-12 border-b border-stone-100">
        <div class="md:col-span-5">
          <img src="assets/images/jimmy-rees.png" alt="Jimmy Rees" class="rounded-3xl w-full h-64 object-cover shadow-sm bg-stone-50">
        </div>
        <div class="md:col-span-7 space-y-3">
          <div class="flex items-center gap-3 text-xs text-stone-400">
            <span class="font-bold text-[#FF6F78] bg-rose-50 px-2.5 py-1 rounded-full">Góc Người Bố</span>
            <span>Tác giả: Jimmy Rees</span>
          </div>
          <h2 class="text-2xl font-bold text-stone-900">Khi Mẹ Có Một Đêm Được Nghỉ Ngơi Trọn Vẹn</h2>
          <p class="text-stone-600 text-xs sm:text-sm leading-relaxed">
            Các ông bố hãy dũng cảm bước lên nào! Nuôi con là công việc toàn thời gian không ngày nghỉ của mẹ. Một đêm mẹ được đi ngủ sớm, không phải thức dậy pha sữa hay dỗ dành con lúc 2 giờ sáng chính là món quà phục hồi tinh thần kỳ diệu nhất. Với sự hỗ trợ của một bình sữa ấm dinh dưỡng và vòng tay bố, cả nhà sẽ có một đêm êm ả.
          </p>
        </div>
      </article>

      <!-- Article 4 -->
      <article id="article-4" class="grid grid-cols-1 md:grid-cols-12 gap-8 items-center pb-12 border-b border-stone-100">
        <div class="md:col-span-5">
          <img src="assets/images/blog-lighten-load.jpg" alt="Buông bỏ gánh nặng" class="rounded-3xl w-full h-64 object-cover shadow-sm">
        </div>
        <div class="md:col-span-7 space-y-3">
          <div class="flex items-center gap-3 text-xs text-stone-400">
            <span class="font-bold text-[#FF6F78] bg-rose-50 px-2.5 py-1 rounded-full">Cảm Xúc Làm Mẹ</span>
            <span>Tác giả: Kirsty Levin</span>
          </div>
          <h2 class="text-2xl font-bold text-stone-900">Học Cách Buông Bỏ Để Nhẹ Bớt Gánh Nặng Trách Nhiệm</h2>
          <p class="text-stone-600 text-xs sm:text-sm leading-relaxed">
            Người mẹ hiện đại thường tự đặt lên vai mình áp lực phải trở thành một người mẹ hoàn hảo: Nhà cửa phải tinh tươm, con phải tăng cân chuẩn bảng, bản thân phải luôn rạng rỡ. Nhưng sự thật là: Không có người mẹ hoàn hảo, chỉ có người mẹ đủ tốt. Hãy học cách nhờ sự giúp đỡ của người thân và buông bỏ những tiêu chuẩn khắt khe không cần thiết.
          </p>
        </div>
      </article>

      <!-- Article 5 -->
      <article id="article-5" class="grid grid-cols-1 md:grid-cols-12 gap-8 items-center pb-12 border-b border-stone-100">
        <div class="md:col-span-5">
          <img src="assets/images/blog-happiness.jpg" alt="Hormone hạnh phúc" class="rounded-3xl w-full h-64 object-cover shadow-sm">
        </div>
        <div class="md:col-span-7 space-y-3">
          <div class="flex items-center gap-3 text-xs text-stone-400">
            <span class="font-bold text-[#FF6F78] bg-rose-50 px-2.5 py-1 rounded-full">Khoa Học Cảm Xúc</span>
            <span>Tác giả: Kirsty Levin</span>
          </div>
          <h2 class="text-2xl font-bold text-stone-900">Bí Quyết Kích Hoạt Các Hormone Hạnh Phúc Mỗi Ngày</h2>
          <p class="text-stone-600 text-xs sm:text-sm leading-relaxed">
            Hormone Oxytocin (hormone của tình yêu và gắn kết) được tiết ra mãnh liệt mỗi khi bạn ôm con da kề da hoặc nhìn sâu vào ánh mắt bé. Dopamine được kích hoạt khi bạn hoàn thành một mục tiêu nhỏ trong ngày. Hãy dành 10 phút tắm nắng buổi sáng để thúc đẩy Serotonin, giúp mẹ duy trì tâm trạng an vui và giàu năng lượng tích cực.
          </p>
        </div>
      </article>

      <!-- Article 6 -->
      <article id="article-6" class="grid grid-cols-1 md:grid-cols-12 gap-8 items-center pb-12 border-b border-stone-100">
        <div class="md:col-span-5">
          <img src="assets/images/blog-iron.jpg" alt="Sắt cho bé" class="rounded-3xl w-full h-64 object-cover shadow-sm">
        </div>
        <div class="md:col-span-7 space-y-3">
          <div class="flex items-center gap-3 text-xs text-stone-400">
            <span class="font-bold text-[#FF6F78] bg-rose-50 px-2.5 py-1 rounded-full">Dinh Dưỡng Trẻ Nhỏ</span>
            <span>Tác giả: Miriam Raleigh</span>
          </div>
          <h2 class="text-2xl font-bold text-stone-900">Bé Nhà Bạn Đã Nạp Đủ Lượng Sắt Cần Thiết Chưa?</h2>
          <p class="text-stone-600 text-xs sm:text-sm leading-relaxed">
            Lượng sắt dự trữ từ bụng mẹ sẽ cạn dần khi bé đạt 6 tháng tuổi. Thiếu sắt ở trẻ nhỏ có thể dẫn đến xanh xao, chậm tăng cân, mệt mỏi và giảm khả năng tập trung. Hãy bổ sung thực phẩm giàu sắt heme (thịt đỏ) kết hợp cùng vitamin C để tăng hấp thu, hoặc chọn các dòng sữa có vi chất sắt sinh học như Nutura Stage 2 & 3.
          </p>
        </div>
      </article>

      <!-- Article 7 -->
      <article id="article-7" class="grid grid-cols-1 md:grid-cols-12 gap-8 items-center pb-12 border-b border-stone-100">
        <div class="md:col-span-5">
          <img src="assets/images/blog-food.jpg" alt="Dinh dưỡng mầm non" class="rounded-3xl w-full h-64 object-cover shadow-sm">
        </div>
        <div class="md:col-span-7 space-y-3">
          <div class="flex items-center gap-3 text-xs text-stone-400">
            <span class="font-bold text-[#FF6F78] bg-rose-50 px-2.5 py-1 rounded-full">Ăn Dặm & Dinh Dưỡng</span>
            <span>Tác giả: Miriam Raleigh</span>
          </div>
          <h2 class="text-2xl font-bold text-stone-900">Trẻ Tuổi Mầm Non Và Mẫu Giáo Nên Ăn Những Nhóm Thực Phẩm Nào?</h2>
          <p class="text-stone-600 text-xs sm:text-sm leading-relaxed">
            Hai năm đầu đời là giai đoạn thể chất và não bộ phát triển vũ bão. Khi bước vào tuổi mẫu giáo (3 - 5 tuổi), trẻ cần chế độ ăn đa dạng màu sắc với ngũ cốc nguyên cám, đạm nạc, rau xanh đậm, trái cây tươi và sữa dinh dưỡng để bổ sung Canxi cho xương chắc khỏe.
          </p>
        </div>
      </article>

      <!-- Article 8 -->
      <article id="article-8" class="grid grid-cols-1 md:grid-cols-12 gap-8 items-center pb-12 border-b border-stone-100">
        <div class="md:col-span-5">
          <img src="assets/images/blog-attachment.jpg" alt="Gắn bó an toàn" class="rounded-3xl w-full h-64 object-cover shadow-sm">
        </div>
        <div class="md:col-span-7 space-y-3">
          <div class="flex items-center gap-3 text-xs text-stone-400">
            <span class="font-bold text-[#FF6F78] bg-rose-50 px-2.5 py-1 rounded-full">Tâm Lý Phát Triển</span>
            <span>Tác giả: Kirsty Levin</span>
          </div>
          <h2 class="text-2xl font-bold text-stone-900">Gắn Bó An Toàn (Secure Attachment) Là Gì Và Vì Sao Quan Trọng?</h2>
          <p class="text-stone-600 text-xs sm:text-sm leading-relaxed">
            Gắn bó an toàn được hình thành khi người chăm sóc phản hồi nhất quán, kịp thời và yêu thương trước những tín hiệu khóc, đói, cần ôm ấp của trẻ. Đây chính là 'bệ phóng' giúp con lớn lên tự tin, dễ dàng kết bạn và kiên cường vượt qua nghịch cảnh trong tương lai.
          </p>
        </div>
      </article>

      <!-- Article 9 -->
      <article id="article-9" class="grid grid-cols-1 md:grid-cols-12 gap-8 items-center">
        <div class="md:col-span-5">
          <img src="assets/images/blog-touch.jpg" alt="Khám phá xúc giác" class="rounded-3xl w-full h-64 object-cover shadow-sm">
        </div>
        <div class="md:col-span-7 space-y-3">
          <div class="flex items-center gap-3 text-xs text-stone-400">
            <span class="font-bold text-[#FF6F78] bg-rose-50 px-2.5 py-1 rounded-full">Khoa Học Não Bộ</span>
            <span>Tác giả: Dr. Michael Carr-Gregg</span>
          </div>
          <h2 class="text-2xl font-bold text-stone-900">Khám Phá Diệu Kỳ Về Xúc Giác Của Trẻ Sơ Sinh</h2>
          <p class="text-stone-600 text-xs sm:text-sm leading-relaxed">
            Xúc giác là giác quan đầu tiên phát triển trong bào thai và là phương tiện đầu tiên giúp trẻ kết nối với thế giới bên ngoài. Massage nhẹ nhàng cho bé trước giờ ngủ không chỉ giúp bé ngủ sâu mà còn thúc đẩy sản xuất hormone tăng trưởng và củng cố liên kết thần kinh.
          </p>
        </div>
      </article>

    </div>
  </section>
"""
    content += render_footer()
    return content

def build_subscriptions():
    content = render_head(
        title="Gói Giao Sữa Định Kỳ Nutura Milkman | Tiết Kiệm 15% & Freeship Tận Cửa",
        description="Đăng ký gói giao sữa định kỳ Nutura Milkman Subscription: Tiết kiệm 15% trọn đời, miễn phí vận chuyển tận nhà, linh hoạt hủy đổi bất kỳ lúc nào.",
        canonical_url="subscriptions.html"
    )
    content += render_topbar()
    content += render_navbar(active_page="subscriptions")

    content += """
  <!-- HERO BANNER -->
  <section class="bg-[#1C120D] text-white py-16 lg:py-24 border-b border-stone-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        <div class="lg:col-span-7 space-y-6">
          <span class="inline-block px-3.5 py-1 rounded-full bg-rose-500/20 text-rose-300 text-xs font-bold uppercase tracking-wider">
            Dịch Vụ Độc Quyền Nutura Milkman
          </span>
          <h1 class="text-3xl sm:text-4xl lg:text-5xl font-bold text-white leading-tight">
            Giao Sữa Định Kỳ Nutura Milkman: Tiện Lợi, Tiết Kiệm 15%
          </h1>
          <p class="text-stone-300 text-base leading-relaxed">
            Không còn nỗi lo hết sữa lúc nửa đêm hay vất vả mang vác lon sữa nặng từ siêu thị! Nutura Milkman mang lon sữa tươi hữu cơ mới xuất xưởng trực tiếp đến cửa nhà bạn đều đặn mỗi 2 tuần hoặc 4 tuần.
          </p>
          <div class="flex items-center gap-4 pt-2">
            <a href="shop.html" class="btn-nutura-primary text-sm py-3.5 px-8 shadow-lg shadow-[#FF6F78]/30">
              Chọn Sữa & Đăng Ký Ngay
            </a>
          </div>
        </div>
        <div class="lg:col-span-5 text-center">
          <img src="assets/images/milkman-lockup.png" alt="Nutura Milkman" class="max-w-xs mx-auto mb-6">
          <img src="assets/images/nutura-tin-lockups.png" alt="Lon sữa Nutura" class="w-full max-w-sm mx-auto">
        </div>
      </div>
    </div>
  </section>

  <!-- 3 SIMPLE STEPS -->
  <section class="py-16 lg:py-20 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-3xl mx-auto mb-16 space-y-3">
        <h2 class="text-3xl font-bold text-stone-900">Cách Thức Hoạt Động Cực Kỳ Đơn Giản</h2>
        <p class="text-stone-600 text-sm">3 bước để bạn thảnh thơi chăm con, việc giao sữa đã có Nutura lo chu tất:</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8 text-center">
        <div class="p-8 bg-[#FAF7F2] rounded-3xl border border-stone-200/80 space-y-3">
          <div class="w-14 h-14 bg-[#FF6F78] text-white rounded-2xl flex items-center justify-center font-bold text-xl mx-auto shadow-md">1</div>
          <h3 class="font-bold text-stone-900 text-lg">Chọn Giai Đoạn Sữa Của Bé</h3>
          <p class="text-xs text-stone-600 leading-relaxed">Chọn Stage 1, Stage 2 hoặc Stage 3 phù hợp với độ tuổi ghi trên nhãn lon.</p>
        </div>

        <div class="p-8 bg-[#FAF7F2] rounded-3xl border border-stone-200/80 space-y-3">
          <div class="w-14 h-14 bg-[#FF6F78] text-white rounded-2xl flex items-center justify-center font-bold text-xl mx-auto shadow-md">2</div>
          <h3 class="font-bold text-stone-900 text-lg">Chọn Chu Kỳ Giao Hàng</h3>
          <p class="text-xs text-stone-600 leading-relaxed">Tùy chọn giao mỗi 2 tuần hoặc mỗi 4 tuần tùy theo lượng ăn hàng ngày của bé.</p>
        </div>

        <div class="p-8 bg-[#FAF7F2] rounded-3xl border border-stone-200/80 space-y-3">
          <div class="w-14 h-14 bg-[#FF6F78] text-white rounded-2xl flex items-center justify-center font-bold text-xl mx-auto shadow-md">3</div>
          <h3 class="font-bold text-stone-900 text-lg">Nhận Sữa Tươi Mới Tận Cửa</h3>
          <p class="text-xs text-stone-600 leading-relaxed">Sữa được giao tự động, chiết khấu 15% trọn đời và hoàn toàn miễn phí vận chuyển!</p>
        </div>
      </div>
    </div>
  </section>
"""
    content += render_footer()
    return content

def build_faqs():
    content = render_head(
        title="Câu Hỏi Thường Gặp (FAQs) | Hướng Dẫn Pha Sữa Theo Nhãn",
        description="Giải đáp chi tiết mọi thắc mắc về sữa hữu cơ Nutura: Chứng nhận ACO trên nhãn, nguồn sữa tươi, hướng dẫn pha theo từng nhãn sản phẩm và thông tin giao hàng.",
        canonical_url="faqs.html"
    )
    content += render_topbar()
    content += render_navbar(active_page="faqs")

    content += """
  <!-- BANNER -->
  <section class="bg-[#FAF7F2] py-16 lg:py-20 border-b border-stone-200/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 md:grid-cols-12 gap-8 items-center">
        <div class="md:col-span-8 space-y-4">
          <span class="inline-block px-3 py-1 rounded-full bg-rose-100 text-[#FF6F78] text-xs font-bold uppercase tracking-wider">
            Trung Tâm Hỗ Trợ Khách Hàng
          </span>
          <h1 class="text-3xl sm:text-4xl lg:text-5xl font-bold text-stone-900">
            Câu Hỏi Thường Gặp (FAQs)
          </h1>
          <p class="text-stone-600 text-sm sm:text-base leading-relaxed max-w-2xl">
            Tìm câu trả lời cho những thắc mắc phổ biến nhất về sản phẩm, cách pha theo nhãn từng sản phẩm và thông tin giao hàng của Nutura Organic.
          </p>
        </div>
        <div class="md:col-span-4 text-center">
          <img src="assets/images/banner-faq.jpg" alt="FAQs Nutura" class="rounded-3xl shadow-lg border-4 border-white max-h-64 mx-auto object-cover">
        </div>
      </div>
    </div>
  </section>

  <!-- FAQ ACCORDION GROUPS -->
  <section class="py-16 bg-white flex-1">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">

      <!-- Group 1: Thông tin sản phẩm chung -->
      <div class="space-y-4">
        <h2 class="text-2xl font-bold text-stone-900 border-b border-stone-200 pb-3 flex items-center gap-2">
          <span>🌿</span> 1. Câu Hỏi Chung Về Sữa Nutura Organic
        </h2>

        <div class="faq-item">
          <button class="faq-question">
            <span>Sản phẩm Nutura Organic có chứng nhận hữu cơ chính thức không?</span>
            <span class="faq-icon">▼</span>
          </button>
          <div class="faq-answer text-sm space-y-2">
            <p>Trên nhãn Organic A2 Stage 1–3 hiện có trong thư mục tài liệu, sản phẩm thể hiện logo <strong>ACO Certified Organic</strong>. Hãy kiểm tra nhãn lô hàng thực tế để xác nhận chứng nhận áp dụng; không mặc định mọi lon đều in logo NASAA.</p>
          </div>
        </div>

        <div class="faq-item">
          <button class="faq-question">
            <span>Sữa Nutura được sản xuất ở đâu?</span>
            <span class="faq-icon">▼</span>
          </button>
          <div class="faq-answer text-sm space-y-2">
            <p>Toàn bộ dòng sản phẩm Nutura Organic được nghiên cứu, chế biến và đóng lon trực tiếp tại <strong>tiểu bang Victoria, Úc</strong>. Nutura là thương hiệu 100% sở hữu và vận hành tại Úc, đạt tiêu chuẩn khắt khe của Cơ quan Tiêu chuẩn Thực phẩm Úc & New Zealand (FSANZ).</p>
          </div>
        </div>

        <div class="faq-item">
          <button class="faq-question">
            <span>Bảng dinh dưỡng ghi có đường (sugars). Nutura có thêm đường vào sữa không?</span>
            <span class="faq-icon">▼</span>
          </button>
          <div class="faq-answer text-sm space-y-2">
            <p><strong>Hoàn toàn không.</strong> Nutura không thêm bất kỳ loại đường mía (sucrose), siro ngô hay chất tạo ngọt nhân tạo nào vào công thức. Lượng đường hiển thị trên bảng dinh dưỡng là <strong>đường tự nhiên (Lactose)</strong> vốn có sẵn trong sữa tươi nguyên chất của bò -  Tương tự như đường lactose tự nhiên trong sữa mẹ, giúp cung cấp năng lượng và hỗ trợ hệ tiêu hóa của bé.</p>
          </div>
        </div>

        <div class="faq-item">
          <button class="faq-question">
            <span>Nutura có chứa thành phần biến đổi gen (GMO) không?</span>
            <span class="faq-icon">▼</span>
          </button>
          <div class="faq-answer text-sm space-y-2">
            <p>Hãy xem danh sách thành phần và chứng nhận trên nhãn của đúng sản phẩm, đúng lô hàng. Tài liệu nhãn đã đối chiếu không đủ để xác nhận tuyên bố 100% Non-GMO cho toàn bộ chuỗi cung ứng.</p>
          </div>
        </div>
      </div>

      <!-- Group 2: Hướng dẫn pha và bảo quản -->
      <div class="space-y-4">
        <h2 class="text-2xl font-bold text-stone-900 border-b border-stone-200 pb-3 flex items-center gap-2">
          <span>🍼</span> 2. Pha Chế & Bảo Quản
        </h2>

        <div class="faq-item open">
          <button class="faq-question">
            <span>Chuyển sang sữa Nutura cho bé như thế nào?</span>
            <span class="faq-icon">▼</span>
          </button>
          <div class="faq-answer text-sm space-y-3">
            <p>Hỏi ý kiến chuyên gia y tế trước khi đổi sữa cho trẻ, đặc biệt khi trẻ có tiền sử dị ứng hoặc vấn đề tiêu hóa. Chọn đúng Stage theo độ tuổi; pha mỗi sản phẩm riêng theo hướng dẫn trên lon. Không trộn bột của hai sản phẩm hoặc tự thay đổi tỷ lệ nước và bột.</p>
          </div>
        </div>
        <div class="faq-item">
          <button class="faq-question">
            <span>Một muỗng gạt ngang bột sữa tương đương bao nhiêu gram?</span>
            <span class="faq-icon">▼</span>
          </button>
          <div class="faq-answer text-sm space-y-2">
            <p>Nhãn Stage 1 và Stage 2: <strong>1 muỗng gạt ngang (4,6 g) cho 30 ml nước đun sôi để nguội</strong>. Nhãn Stage 3: <strong>6 muỗng gạt ngang (6 g/muỗng) cho 200 ml nước sạch</strong>. Chỉ dùng muỗng đi kèm lon; làm theo nhãn đúng sản phẩm và không tự thay đổi tỷ lệ trừ khi có chỉ định y tế.</p>
          </div>
        </div>

        <div class="faq-item">
          <button class="faq-question">
            <span>Lon sữa sau khi mở nắp dùng được trong bao lâu? Có để tủ lạnh được không?</span>
            <span class="faq-icon">▼</span>
          </button>
          <div class="faq-answer text-sm space-y-2">
            <p>Đậy kín lon sau khi lấy bột. Xem điều kiện bảo quản và thời hạn sử dụng sau mở nắp trên nhãn của đúng lon đang dùng; không sử dụng quá hạn. Với sữa đã pha, làm theo hướng dẫn riêng trên nhãn từng Stage.</p>
          </div>
        </div>
      </div>

      <!-- Group 3: Đặt hàng & Vận chuyển -->
      <div class="space-y-4">
        <h2 class="text-2xl font-bold text-stone-900 border-b border-stone-200 pb-3 flex items-center gap-2">
          <span>📦</span> 3. Đặt Hàng & Giao Nhận Toàn Quốc
        </h2>

        <div class="faq-item">
          <button class="faq-question">
            <span>Phí vận chuyển và thời gian giao hàng tại Việt Nam như thế nào?</span>
            <span class="faq-icon">▼</span>
          </button>
          <div class="faq-answer text-sm space-y-2">
            <p>• <strong>Miễn phí vận chuyển</strong> toàn quốc cho đơn hàng từ 1.000.000 đ (tương đương 2 lon trở lên).<br>• Đơn hàng dưới 1.000.000 đ có phí ship tiêu chuẩn là 30.000 đ (nội thành Hà Nội & TP.HCM) và 45.000 đ (các tỉnh thành khác).<br>• Thời gian giao: 1 - 2 ngày (Hà Nội, TP.HCM), 2 - 4 ngày đối với các tỉnh thành khác.</p>
          </div>
        </div>

        <div class="faq-item">
          <button class="faq-question">
            <span>Chính sách đổi trả sản phẩm ra sao?</span>
            <span class="faq-icon">▼</span>
          </button>
          <div class="faq-answer text-sm space-y-2">
            <p>Do tính chất đặc thù của sản phẩm dinh dưỡng dành cho trẻ em, chúng tôi chỉ hỗ trợ đổi trả khi sản phẩm bị lỗi móp méo do vận chuyển hoặc tem niêm phong có dấu hiệu bất thường trước khi mở. Vui lòng quay video lúc nhận hàng và liên hệ Hotline 1800 827 957 để được xử lý nhanh chóng trong 24 giờ.</p>
          </div>
        </div>
      </div>

    </div>
  </section>
"""
    content += render_footer()
    return content

def build_contact():
    content = render_head(
        title="Liên Hệ & Tư Vấn Dinh Dưỡng | Nutura Organic Việt Nam",
        description="Kết nối với đội ngũ Nutura Organic Việt Nam. Đặt lịch tư vấn miễn phí cùng chuyên gia dinh dưỡng, hỗ trợ đơn hàng hoặc liên hệ hợp tác đại lý phân phối.",
        canonical_url="contact.html"
    )
    content += render_topbar()
    content += render_navbar(active_page="contact")

    content += """
  <!-- BANNER -->
  <section class="bg-[#FAF7F2] py-16 lg:py-20 border-b border-stone-200/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-3xl mx-auto space-y-4">
        <span class="inline-block px-3 py-1 rounded-full bg-rose-100 text-[#FF6F78] text-xs font-bold uppercase tracking-wider">
          Luôn Lắng Nghe & Đồng Hành
        </span>
        <h1 class="text-3xl sm:text-4xl lg:text-5xl font-bold text-stone-900">
          Kết Nối Với Ngôi Làng Nutura
        </h1>
        <p class="text-stone-600 text-sm sm:text-base leading-relaxed">
          Đội ngũ chuyên viên tư vấn dinh dưỡng của Nutura luôn sẵn sàng lắng nghe và giải đáp mọi băn khoăn của ba mẹ về sức khỏe của con.
        </p>
      </div>
    </div>
  </section>

  <!-- CONTACT FORM & INFO -->
  <section class="py-16 bg-white flex-1">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12">
        <!-- Contact Form -->
        <div class="lg:col-span-7 bg-[#FAF7F2] p-8 sm:p-10 rounded-3xl border border-stone-200/80">
          <h2 class="text-2xl font-bold text-stone-900 mb-6">Gửi Yêu Cầu Tư Vấn Miễn Phí</h2>
          <form onsubmit="event.preventDefault(); alert('Cảm ơn bạn! Đội ngũ chuyên gia dinh dưỡng Nutura sẽ liên hệ lại trong vòng 24 giờ làm việc.');" class="space-y-4">
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label for="contactFullName" class="block text-xs font-bold text-stone-700 mb-1">Họ Và Tên Phụ Huynh *</label>
                <input id="contactFullName" name="fullName" type="text" required placeholder="Nguyễn Văn A" class="w-full px-4 py-3 text-sm bg-white border border-stone-300 rounded-xl focus:outline-none focus:border-[#FF6F78]">
              </div>
              <div>
                <label for="contactPhone" class="block text-xs font-bold text-stone-700 mb-1">Số Điện Thoại *</label>
                <input id="contactPhone" name="phone" type="tel" required placeholder="0901 234 567" class="w-full px-4 py-3 text-sm bg-white border border-stone-300 rounded-xl focus:outline-none focus:border-[#FF6F78]">
              </div>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label for="contactEmail" class="block text-xs font-bold text-stone-700 mb-1">Địa Chỉ Email *</label>
                <input id="contactEmail" name="email" type="email" required placeholder="email@domain.com" class="w-full px-4 py-3 text-sm bg-white border border-stone-300 rounded-xl focus:outline-none focus:border-[#FF6F78]">
              </div>
              <div>
                <label for="contactBabyAge" class="block text-xs font-bold text-stone-700 mb-1">Độ Tuổi Của Bé</label>
                <select id="contactBabyAge" name="babyAge" class="w-full px-4 py-3 text-sm bg-white border border-stone-300 rounded-xl focus:outline-none focus:border-[#FF6F78]">
                  <option>Dưới 6 tháng tuổi</option>
                  <option>6 - 12 tháng tuổi</option>
                  <option>1 - 3 tuổi</option>
                  <option>Trên 3 tuổi</option>
                  <option>Chưa sinh (Đang mang thai)</option>
                </select>
              </div>
            </div>

            <div>
              <label for="contactContent" class="block text-xs font-bold text-stone-700 mb-1">Nội Dung Cần Tư Vấn *</label>
              <textarea id="contactContent" name="content" rows="4" required placeholder="Mô tả tình trạng của bé (cân nặng, hệ tiêu hóa, loại sữa đang dùng)..." class="w-full px-4 py-3 text-sm bg-white border border-stone-300 rounded-xl focus:outline-none focus:border-[#FF6F78]"></textarea>
            </div>

            <button type="submit" class="w-full py-3.5 bg-[#FF6F78] hover:bg-[#E65A63] text-white font-bold rounded-xl transition text-sm shadow-md shadow-[#FF6F78]/30">
              Gửi Thông Tin Cho Chuyên Gia
            </button>
          </form>
        </div>

        <!-- Contact Info Cards -->
        <div class="lg:col-span-5 space-y-6">
          <div class="p-6 bg-stone-50 rounded-3xl border border-stone-200 space-y-4">
            <h3 class="font-bold text-stone-900 text-lg">Thông Tin Liên Hệ Trực Tiếp</h3>
            <div class="space-y-3 text-xs text-stone-600">
              <div class="flex items-start gap-3">
                <span class="text-base text-[#FF6F78]">📞</span>
                <div>
                  <strong class="text-stone-800">Hotline Tư Vấn Miễn Phí:</strong><br>
                  <span class="text-sm font-bold text-[#FF6F78]">1800 827 957</span> (8:00 - 20:00 các ngày)
                </div>
              </div>
              <div class="flex items-start gap-3">
                <span class="text-base text-[#FF6F78]">✉️</span>
                <div>
                  <strong class="text-stone-800">Hộp Thư Điện Tử:</strong><br>
                  cskh@nutura.vn / info@nutura.com.au
                </div>
              </div>
              <div class="flex items-start gap-3">
                <span class="text-base text-[#FF6F78]">🏢</span>
                <div>
                  <strong class="text-stone-800">Văn Phòng Đại Diện Tại Việt Nam:</strong><br>
                  Tầng 12, Tòa nhà Landmark, Ba Đình, Hà Nội & Quận 1, TP. Hồ Chí Minh
                </div>
              </div>
              <div class="flex items-start gap-3">
                <span class="text-base text-[#FF6F78]">🇦🇺</span>
                <div>
                  <strong class="text-stone-800">Trụ Sở Chính Tại Úc:</strong><br>
                  Victoria, Australia
                </div>
              </div>
            </div>
          </div>

          <div class="p-6 bg-rose-50/60 rounded-3xl border border-rose-200 text-xs text-stone-700 space-y-2">
            <h4 class="font-bold text-stone-900">Hợp Tác Phân Phối & Đại Lý:</h4>
            <p>Nutura Organic mở rộng hợp tác với các hệ thống siêu thị mẹ & bé, chuỗi nhà thuốc và đại lý uy tín trên toàn quốc. Liên hệ phòng kinh doanh: <strong>kinhdoanh@nutura.vn</strong></p>
          </div>
        </div>
      </div>
    </div>
  </section>
"""
    content += render_footer()
    return content

def build_cart():
    content = render_head(
        title="Giỏ Hàng & Thanh Toán | Nutura Organic Việt Nam",
        description="Kiểm tra giỏ hàng, áp dụng mã ưu đãi voucher và thanh toán đơn hàng an toàn, tiện lợi.",
        canonical_url="cart.html"
    )
    content += render_topbar()
    content += render_navbar(active_page="shop")

    content += """
  <!-- BREADCRUMB -->
  <div class="bg-[#FAF7F2] py-4 border-b border-stone-200/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-xs text-stone-500 flex items-center gap-2">
      <a href="index.html" class="hover:text-[#FF6F78]">Trang Chủ</a>
      <span>/</span>
      <span class="text-stone-800 font-bold">Giỏ Hàng & Thanh Toán</span>
    </div>
  </div>

  <section class="py-12 lg:py-16 bg-white flex-1">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <h1 class="text-2xl sm:text-3xl font-bold text-stone-900 mb-8">Chi Tiết Giỏ Hàng Của Bạn</h1>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-start">
        <!-- Cart Items Table -->
        <div class="lg:col-span-7 space-y-6">
          <div id="fullCartItemList" class="divide-y divide-stone-200 border border-stone-200 rounded-3xl p-6 bg-white shadow-sm">
            <!-- Rendered by JS -->
          </div>

          <div class="flex items-center justify-between">
            <a href="shop.html" class="text-xs font-bold text-[#FF6F78] hover:underline inline-flex items-center gap-1">
              &larr; Tiếp Tục Mua Sắm Thêm Sản Phẩm
            </a>
            <button onclick="localStorage.removeItem('nutura_vn_cart'); window.location.reload();" class="text-xs text-stone-400 hover:text-rose-500">
              Xóa Toàn Bộ Giỏ Hàng
            </button>
          </div>
        </div>

        <!-- Checkout Summary & Form -->
        <div class="lg:col-span-5 bg-[#FAF7F2] p-6 sm:p-8 rounded-3xl border border-stone-200/80 space-y-6">
          <h3 class="text-lg font-bold text-stone-900">Tóm Tắt Đơn Hàng</h3>

          <!-- ponytail: chỉ xem giỏ hàng; bật thanh toán khi có backend nhận đơn và bảng giá đã xác minh. -->
          <!-- Discount Voucher Box -->
          <div class="flex gap-2">
            <input type="text" id="voucherCodeInput" placeholder="Mã giảm giá (ví dụ: NUTURA40)" class="flex-1 px-3 py-2 text-xs bg-white border border-stone-300 rounded-xl focus:outline-none focus:border-[#FF6F78] uppercase font-bold">
            <button onclick="applyVoucher()" class="px-4 py-2 bg-stone-900 text-white rounded-xl text-xs font-bold hover:bg-stone-800 transition">
              Áp Dụng
            </button>
          </div>
          <div id="voucherMessage" class="text-xs hidden"></div>

          <!-- Price Calculation -->
          <div class="space-y-3 text-xs text-stone-600 border-t border-b border-stone-200 py-4">
            <div class="flex justify-between">
              <span>Tạm tính hàng hóa:</span>
              <span id="cartSubtotalText" class="font-bold text-stone-800">0 đ</span>
            </div>
            <div class="flex justify-between">
              <span>Giảm giá khuyến mãi:</span>
              <span id="cartDiscountText" class="font-bold text-emerald-600">0 đ</span>
            </div>
            <div class="flex justify-between">
              <span>Phí vận chuyển:</span>
              <span id="cartShippingText" class="font-bold text-stone-800">Miễn phí</span>
            </div>
            <div class="flex justify-between text-base font-bold text-stone-900 pt-2 border-t border-stone-200">
              <span>Tổng thanh toán:</span>
              <span id="cartTotalText" class="text-[#FF6F78]">0 đ</span>
            </div>
          </div>

          <!-- Delivery Form -->
          <div class="space-y-3">
            <h4 class="font-bold text-xs uppercase tracking-wider text-stone-700">Thông Tin Giao Hàng</h4>
            <div>
              <label for="custName" class="block text-xs font-bold text-stone-700 mb-1">Họ và tên người nhận *</label>
              <input type="text" id="custName" name="custName" required placeholder="Nguyễn Văn A" class="w-full px-3 py-2 text-xs bg-white border border-stone-300 rounded-xl focus:outline-none focus:border-[#FF6F78]">
            </div>
            <div>
              <label for="custPhone" class="block text-xs font-bold text-stone-700 mb-1">Số điện thoại *</label>
              <input type="tel" id="custPhone" name="custPhone" required placeholder="0901 234 567" class="w-full px-3 py-2 text-xs bg-white border border-stone-300 rounded-xl focus:outline-none focus:border-[#FF6F78]">
            </div>
            <div>
              <label for="custAddress" class="block text-xs font-bold text-stone-700 mb-1">Địa chỉ nhận hàng *</label>
              <input type="text" id="custAddress" name="custAddress" required placeholder="Số nhà, đường, phường/xã, quận/huyện, tỉnh/thành" class="w-full px-3 py-2 text-xs bg-white border border-stone-300 rounded-xl focus:outline-none focus:border-[#FF6F78]">
            </div>
            <div>
              <label for="custNote" class="block text-xs font-medium text-stone-600 mb-1">Ghi chú giao hàng</label>
              <textarea id="custNote" name="custNote" rows="2" placeholder="Ví dụ: giao giờ hành chính, gọi trước khi giao..." class="w-full px-3 py-2 text-xs bg-white border border-stone-300 rounded-xl focus:outline-none focus:border-[#FF6F78]"></textarea>
            </div>
          </div>

          <!-- Payment Methods -->
          <div class="space-y-2 text-xs">
            <h4 class="font-bold text-stone-700">Hình Thức Thanh Toán</h4>
            <label class="flex items-center gap-2 p-2.5 bg-white rounded-xl border border-stone-200 cursor-pointer">
              <input type="radio" name="payMethod" value="cod" checked class="custom-checkbox">
              <span class="font-semibold text-stone-800">Thanh toán khi nhận hàng (COD)</span>
            </label>
            <label class="flex items-center gap-2 p-2.5 bg-white rounded-xl border border-stone-200 cursor-pointer">
              <input type="radio" name="payMethod" value="vietqr" class="custom-checkbox">
              <span class="font-semibold text-stone-800">Chuyển khoản VietQR (Momo / Ngân hàng)</span>
            </label>
          </div>

          <p role="status" class="text-sm font-semibold text-amber-900">Trang demo: chưa có máy chủ nhận đơn. Không nhập thông tin cá nhân hoặc chuyển tiền; giá và ưu đãi chưa được xác minh.</p>
           <button type="button" disabled title="Chưa có máy chủ nhận đơn" class="w-full py-3.5 bg-stone-300 text-stone-700 font-bold rounded-full text-sm cursor-not-allowed">
            Chưa thể đặt hàng
          </button>
        </div>
      </div>
    </div>
  </section>

  <!-- Checkout Logic Script -->
  <script>
    let currentDiscountPercent = 0;

    function renderFullCart() {
      const listEl = document.getElementById('fullCartItemList');
      const cart = window.nuturaCart ? window.nuturaCart.items : [];

      if (!cart || cart.length === 0) {
        listEl.innerHTML = `
          <div class="text-center py-12">
            <p class="text-stone-500 font-medium mb-4">Giỏ hàng của bạn đang trống</p>
            <a href="shop.html" class="btn-nutura-primary text-xs py-2.5 px-6">Khám Phá Cửa Hàng</a>
          </div>
        `;
        updateCalculations(0);
        return;
      }

      listEl.innerHTML = cart.map(item => `
        <div class="py-4 flex gap-4 items-center">
          <img src="${item.image}" alt="${item.name}" class="w-20 h-20 object-contain p-1 rounded-xl bg-stone-50 border border-stone-200">
          <div class="flex-1 min-w-0">
            <h4 class="font-bold text-stone-900 text-sm truncate">${item.name}</h4>
            <p class="text-xs text-stone-500">${item.weight} • ${window.nuturaCart.formatMoney(item.price)}</p>
            <div class="flex items-center gap-3 mt-3">
              <div class="flex items-center border border-stone-200 rounded-full bg-stone-50">
                <button onclick="window.nuturaCart.updateQuantity('${item.id}', -1); renderFullCart();" class="w-7 h-7 flex items-center justify-center font-bold text-xs">-</button>
                <span class="px-2 text-xs font-bold">${item.quantity}</span>
                <button onclick="window.nuturaCart.updateQuantity('${item.id}', 1); renderFullCart();" class="w-7 h-7 flex items-center justify-center font-bold text-xs">+</button>
              </div>
              <button onclick="window.nuturaCart.removeItem('${item.id}'); renderFullCart();" class="text-xs text-rose-500 hover:underline">Xóa</button>
            </div>
          </div>
          <div class="text-right">
            <span class="font-bold text-[#FF6F78] text-base">${window.nuturaCart.formatMoney(item.price * item.quantity)}</span>
          </div>
        </div>
      `).join('');

      updateCalculations(window.nuturaCart.getTotalAmount());
    }

    function updateCalculations(subtotal) {
      const discount = subtotal * currentDiscountPercent;
      const shipping = (subtotal >= 1000000 || subtotal === 0) ? 0 : 30000;
      const total = subtotal - discount + shipping;

      document.getElementById('cartSubtotalText').textContent = window.nuturaCart.formatMoney(subtotal);
      document.getElementById('cartDiscountText').textContent = discount > 0 ? `-${window.nuturaCart.formatMoney(discount)}` : '0 đ';
      document.getElementById('cartShippingText').textContent = shipping === 0 ? 'Miễn phí' : window.nuturaCart.formatMoney(shipping);
      document.getElementById('cartTotalText').textContent = window.nuturaCart.formatMoney(total);
    }

    function applyVoucher() {
      const code = (document.getElementById('voucherCodeInput').value || '').trim().toUpperCase();
      const msgEl = document.getElementById('voucherMessage');
      msgEl.classList.remove('hidden', 'text-emerald-600', 'text-rose-500');

      if (code === 'NUTURA40') {
        currentDiscountPercent = 0.4;
        msgEl.textContent = '🎉 Áp dụng thành công mã NUTURA40: Giảm 40%!';
        msgEl.classList.add('text-emerald-600');
      } else if (code === 'WELCOME10') {
        currentDiscountPercent = 0.1;
        msgEl.textContent = '🎉 Áp dụng thành công mã WELCOME10: Giảm 10%!';
        msgEl.classList.add('text-emerald-600');
      } else {
        currentDiscountPercent = 0;
        msgEl.textContent = 'Mã giảm giá không hợp lệ hoặc đã hết hạn.';
        msgEl.classList.add('text-rose-500');
      }
      renderFullCart();
    }

    function submitOrder() {
      const name = document.getElementById('custName').value.trim();
      const phone = document.getElementById('custPhone').value.trim();
      const address = document.getElementById('custAddress').value.trim();

      if (!name || !phone || !address) {
        alert('Vui lòng điền đầy đủ Họ tên, Số điện thoại và Địa chỉ nhận hàng!');
        return;
      }

      if (!window.nuturaCart || window.nuturaCart.items.length === 0) {
        alert('Giỏ hàng của bạn đang trống!');
        return;
      }

      const orderId = 'NUTURA-' + Math.floor(100000 + Math.random() * 900000);
      alert(`🎉 ĐẶT HÀNG THÀNH CÔNG!\n\nMã đơn hàng của bạn: ${orderId}\nCảm ơn ${name} đã tin chọn Nutura Organic.\nNhân viên chăm sóc khách hàng sẽ liên hệ xác nhận đơn qua số điện thoại ${phone}.`);
      localStorage.removeItem('nutura_vn_cart');
      window.location.href = 'index.html';
    }

    document.addEventListener('DOMContentLoaded', () => {
      setTimeout(renderFullCart, 100);
    });
  </script>
"""
    content += render_footer()
    return content

print("Village and support pages ready.")
