/**
 * Nutura Organic Vietnam - Main JavaScript Engine
 * Bản cập nhật tuân thủ Nghị định 100/2014/NĐ-CP & tiêu chuẩn WHO
 * Không giỏ hàng, không thanh toán, không giao dịch thương mại
 */

// Tab Navigation cho trang chi tiết sản phẩm
window.switchTab = function(tabId, btn) {
  document.querySelectorAll('.tab-content').forEach(tab => tab.classList.add('hidden'));
  document.querySelectorAll('.tab-btn').forEach(b => {
    b.classList.remove('border-[#FF6F78]', 'text-[#FF6F78]');
    b.classList.add('border-transparent', 'text-stone-500');
  });
  const target = document.getElementById(tabId);
  if (target) {
    target.classList.remove('hidden');
  }
  if (btn) {
    btn.classList.remove('border-transparent', 'text-stone-500');
    btn.classList.add('border-[#FF6F78]', 'text-[#FF6F78]');
  }
};

// Thông báo y tế bắt buộc đầu phiên (Tuân thủ Nghị định 100 & WHO)
function initBreastfeedingModal() {
  const DISCLAIMER_KEY = 'nutura_breastfeeding_accepted';
  const hasAccepted = localStorage.getItem(DISCLAIMER_KEY);
  if (hasAccepted) return;

  const modalHTML = `
    <div id="disclaimerModalOverlay" class="disclaimer-modal-overlay" role="dialog" aria-modal="true" aria-labelledby="disclaimerModalTitle">
      <div class="disclaimer-modal-content p-5 sm:p-8" data-lenis-prevent>
        <div class="w-12 h-12 sm:w-14 sm:h-14 bg-rose-50 text-[#FF6F78] rounded-2xl flex items-center justify-center mb-4" aria-hidden="true">
          <svg class="w-7 h-7 sm:w-8 sm:h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
          </svg>
        </div>
        <h3 id="disclaimerModalTitle" class="text-lg sm:text-2xl font-bold text-stone-900 mb-3">Thông báo quan trọng về dinh dưỡng trẻ nhỏ</h3>
        <p class="text-stone-700 text-xs sm:text-sm leading-relaxed mb-3">
          <strong>Sữa mẹ là thức ăn tốt nhất cho sức khoẻ và sự phát triển toàn diện của trẻ nhỏ.</strong> Sữa mẹ chứa các kháng thể tự nhiên giúp bảo vệ bé trước các bệnh nhiễm khuẩn. Việc tham vấn ý kiến chuyên gia y tế trước khi quyết định phương pháp nuôi dưỡng là điều cần thiết.
        </p>
        <p class="text-stone-600 text-[11px] sm:text-xs leading-relaxed mb-5">
          Sản phẩm dinh dưỡng công thức chỉ được sử dụng theo chỉ dẫn của bác sĩ hoặc cán bộ y tế khi người mẹ không thể cho con bú. Website Nutura Việt Nam là trang thông tin khoa học và tra cứu thông tin theo nhãn sản phẩm, không thực hiện bán hàng trực tuyến.
        </p>
        <div class="flex flex-col sm:flex-row gap-2.5">
          <button id="acceptDisclaimerBtn" class="flex-1 py-3 px-5 rounded-full bg-[#FF6F78] hover:bg-[#E65A63] text-white font-bold transition text-xs sm:text-sm shadow-md">
            Tôi đồng ý & tiếp tục
          </button>
          <a href="breast-is-best.html" class="py-3 px-5 rounded-full border border-stone-300 font-semibold text-stone-700 hover:bg-stone-50 transition text-xs sm:text-sm text-center">
            Tìm hiểu về sữa mẹ
          </a>
        </div>
      </div>
    </div>
  `;

  document.body.insertAdjacentHTML('beforeend', modalHTML);
  const overlay = document.getElementById('disclaimerModalOverlay');
  const btn = document.getElementById('acceptDisclaimerBtn');

  setTimeout(() => {
    if (overlay) {
      overlay.classList.add('active');
      if (window.nuturaLenis) window.nuturaLenis.stop();
    }
  }, 400);

  if (btn) {
    btn.addEventListener('click', () => {
      localStorage.setItem(DISCLAIMER_KEY, 'true');
      overlay.classList.remove('active');
      if (window.nuturaLenis) window.nuturaLenis.start();
      setTimeout(() => overlay.remove(), 300);
    });
  }
}

// Menu điều hướng di động
function initMobileMenu() {
  const toggleBtn = document.getElementById('mobileMenuToggleBtn');
  const mobileMenu = document.getElementById('mobileNavDrawer');
  const overlay = document.getElementById('mobileNavOverlay');
  const closeBtn = document.getElementById('closeMobileNavBtn');

  if (!toggleBtn || !mobileMenu) return;

  function openMenu() {
    mobileMenu.classList.add('translate-x-0');
    mobileMenu.classList.remove('-translate-x-full');
    if (overlay) overlay.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
    if (window.nuturaLenis) window.nuturaLenis.stop();
  }

  function closeMenu() {
    mobileMenu.classList.remove('translate-x-0');
    mobileMenu.classList.add('-translate-x-full');
    if (overlay) overlay.classList.add('hidden');
    document.body.style.overflow = '';
    if (window.nuturaLenis) window.nuturaLenis.start();
  }

  toggleBtn.addEventListener('click', openMenu);
  if (closeBtn) closeBtn.addEventListener('click', closeMenu);
  if (overlay) overlay.addEventListener('click', closeMenu);
}

// FAQs Accordion
function initFaqAccordion() {
  document.querySelectorAll('.faq-question').forEach(btn => {
    btn.addEventListener('click', () => {
      const item = btn.closest('.faq-item');
      if (item) {
        const isOpen = item.classList.contains('open');
        document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('open'));
        if (!isOpen) {
          item.classList.add('open');
        }
      }
    });
  });
}

// Lenis Smooth Scroll Engine
function initLenis() {
  if (typeof Lenis === 'undefined') return;

  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    return;
  }

  const lenis = new Lenis({
    duration: 1.2,
    easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
    orientation: 'vertical',
    gestureOrientation: 'vertical',
    smoothWheel: true,
    wheelMultiplier: 1,
    touchMultiplier: 1.5,
    infinite: false,
  });

  window.nuturaLenis = lenis;

  function raf(time) {
    lenis.raf(time);
    requestAnimationFrame(raf);
  }
  requestAnimationFrame(raf);

  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const targetId = this.getAttribute('href');
      if (targetId && targetId !== '#') {
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
          e.preventDefault();
          lenis.scrollTo(targetElement, { offset: -80 });
        }
      }
    });
  });
}

// Khởi chạy khi DOM sẵn sàng
document.addEventListener('DOMContentLoaded', () => {
  initLenis();
  initBreastfeedingModal();
  initMobileMenu();
  initFaqAccordion();
});
