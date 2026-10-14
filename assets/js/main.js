/**
 * Nutura Organic Vietnam - Main JavaScript Engine
 */

const NUTURA_PRODUCTS = {
  'stage-1': {
    id: 'stage-1',
    name: 'Sữa Hữu Cơ Nutura Stage 1 (0 - 6 tháng)',
    subtitle: 'Sữa hữu cơ đạm A2, Whey : Casein 60 : 40, logo ACO trên nhãn',
    price: 780000,
    priceAud: 46.00,
    weight: '800g',
    image: 'assets/images/stage1.png',
    stage: 'Giai đoạn 1',
    category: 'formula',
    age: '0-6m',
    url: 'product-stage1.html'
  },
  'stage-2': {
    id: 'stage-2',
    name: 'Sữa Hữu Cơ Nutura Stage 2 (6 - 12 tháng)',
    subtitle: 'Whey : Casein 40 : 60, DHA, GOS và FOS theo nhãn',
    price: 780000,
    priceAud: 46.00,
    weight: '800g',
    image: 'assets/images/stage2.png',
    stage: 'Giai đoạn 2',
    category: 'formula',
    age: '6-12m',
    url: 'product-stage2.html'
  },
  'stage-3': {
    id: 'stage-3',
    name: 'Sữa Hữu Cơ Nutura Stage 3 (12 - 36 tháng)',
    subtitle: 'Sữa dinh dưỡng cho trẻ 1–3 tuổi, GOS/FOS và DHA',
    price: 780000,
    priceAud: 46.00,
    weight: '800g',
    image: 'assets/images/stage3.png',
    stage: 'Giai đoạn 3',
    category: 'formula',
    age: '1-3y',
    url: 'product-stage3.html'
  }
};

// Cart Management System
class NuturaCart {
  constructor() {
    this.storageKey = 'nutura_vn_cart';
    this.items = this.loadCart();
    this.initUI();
  }

  loadCart() {
    try {
      const data = localStorage.getItem(this.storageKey);
      return data ? JSON.parse(data) : [];
    } catch (e) {
      console.error('Lỗi tải giỏ hàng:', e);
      return [];
    }
  }

  saveCart() {
    try {
      localStorage.setItem(this.storageKey, JSON.stringify(this.items));
      this.updateBadges();
      this.renderDrawer();
      window.dispatchEvent(new CustomEvent('nutura_cart_updated', { detail: { items: this.items } }));
    } catch (e) {
      console.error('Lỗi lưu giỏ hàng:', e);
    }
  }

  addItem(productId, quantity = 1) {
    const product = NUTURA_PRODUCTS[productId];
    if (!product) return;

    const existingIndex = this.items.findIndex(item => item.id === productId);
    if (existingIndex > -1) {
      this.items[existingIndex].quantity += quantity;
    } else {
      this.items.push({
        id: product.id,
        name: product.name,
        price: product.price,
        image: product.image,
        weight: product.weight,
        url: product.url,
        quantity: quantity
      });
    }

    this.saveCart();
    this.showToast(`Đã thêm "${product.name}" vào giỏ hàng!`);
    this.openDrawer();
  }

  updateQuantity(productId, delta) {
    const itemIndex = this.items.findIndex(item => item.id === productId);
    if (itemIndex > -1) {
      this.items[itemIndex].quantity += delta;
      if (this.items[itemIndex].quantity <= 0) {
        this.items.splice(itemIndex, 1);
      }
      this.saveCart();
    }
  }

  removeItem(productId) {
    this.items = this.items.filter(item => item.id !== productId);
    this.saveCart();
  }

  getTotalCount() {
    return this.items.reduce((sum, item) => sum + item.quantity, 0);
  }

  getTotalAmount() {
    return this.items.reduce((sum, item) => sum + (item.price * item.quantity), 0);
  }

  formatMoney(num) {
    return new Intl.NumberFormat('vi-VN', { style: 'currency', currency: 'VND' }).format(num);
  }

  initUI() {
    this.updateBadges();
    this.createDrawerDOM();
    this.renderDrawer();
    this.bindEvents();
  }

  updateBadges() {
    const count = this.getTotalCount();
    document.querySelectorAll('.cart-count-badge').forEach(el => {
      el.textContent = count;
      el.style.display = count > 0 ? 'inline-flex' : 'none';
    });
  }

  createDrawerDOM() {
    if (document.getElementById('nuturaCartDrawer')) return;

    const drawerHTML = `
      <div id="cartDrawerOverlay" class="cart-drawer-overlay"></div>
      <aside id="nuturaCartDrawer" class="cart-drawer" role="dialog" aria-modal="true" aria-label="Giỏ hàng của bạn">
        <div class="p-5 border-b border-stone-200 flex items-center justify-between bg-stone-50">
          <div class="flex items-center gap-2">
            <svg class="w-6 h-6 text-[#FF6F78]" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"/>
            </svg>
            <h3 class="text-lg font-bold text-stone-900">Giỏ Hàng Của Bạn</h3>
          </div>
          <button id="closeCartDrawerBtn" aria-label="Đóng giỏ hàng" class="text-stone-400 hover:text-stone-700 p-1.5 rounded-full hover:bg-stone-200 transition min-h-[44px] min-w-[44px] flex items-center justify-center">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
            </svg>
          </button>
        </div>

        <div id="cartDrawerItemList" data-lenis-prevent class="flex-1 overflow-y-auto p-5 divide-y divide-stone-100">
          <!-- Item list rendered by JS -->
        </div>

        <div class="p-5 border-t border-stone-200 bg-stone-50">
          <div class="flex justify-between items-center mb-2 text-sm text-stone-500">
            <span>Tạm tính:</span>
            <span id="cartDrawerSubtotal" class="font-bold text-stone-900 text-base">0 đ</span>
          </div>
          <div class="flex justify-between items-center mb-4 text-xs text-emerald-700 font-medium bg-emerald-50 p-2 rounded-lg">
            <span>🎉 Miễn phí vận chuyển cho đơn từ 1.000.000 đ</span>
          </div>
          <div class="grid grid-cols-2 gap-3">
            <a href="cart.html" class="w-full text-center py-3 px-4 rounded-full border border-stone-300 font-semibold text-stone-800 hover:bg-stone-100 transition text-sm">
              Xem Giỏ Hàng
            </a>
            <a href="cart.html?checkout=true" class="w-full text-center py-3 px-4 rounded-full bg-[#FF6F78] hover:bg-[#E65A63] text-white font-semibold transition text-sm shadow-md shadow-[#FF6F78]/30">
              Thanh Toán Ngay
            </a>
          </div>
        </div>
      </aside>
    `;
    document.body.insertAdjacentHTML('beforeend', drawerHTML);
  }

  renderDrawer() {
    const listEl = document.getElementById('cartDrawerItemList');
    const subtotalEl = document.getElementById('cartDrawerSubtotal');
    if (!listEl || !subtotalEl) return;

    if (this.items.length === 0) {
      listEl.innerHTML = `
        <div class="text-center py-12">
          <div class="w-20 h-20 mx-auto mb-4 bg-stone-100 rounded-full flex items-center justify-center text-stone-400">
            <svg class="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"/>
            </svg>
          </div>
          <p class="text-stone-500 font-medium mb-3">Giỏ hàng của bạn đang trống</p>
          <a href="shop.html" class="inline-block px-5 py-2 rounded-full bg-[#FF6F78] text-white text-sm font-semibold hover:bg-[#E65A63] transition">
            Khám phá sản phẩm
          </a>
        </div>
      `;
      subtotalEl.textContent = '0 đ';
      return;
    }

    listEl.innerHTML = this.items.map(item => `
      <div class="py-4 flex gap-4 items-center">
        <img src="${item.image}" alt="${item.name}" class="w-16 h-16 object-contain bg-stone-50 p-1 rounded-xl border border-stone-200">
        <div class="flex-1 min-w-0">
          <h4 class="text-sm font-bold text-stone-900 truncate">${item.name}</h4>
          <p class="text-xs text-stone-500">${item.weight} | ${this.formatMoney(item.price)}</p>
          <div class="flex items-center gap-2 mt-2">
            <div class="flex items-center border border-stone-200 rounded-full bg-stone-50">
              <button onclick="window.nuturaCart.updateQuantity('${item.id}', -1)" class="w-6 h-6 flex items-center justify-center text-stone-600 hover:text-black font-bold text-xs">-</button>
              <span class="px-2 text-xs font-semibold">${item.quantity}</span>
              <button onclick="window.nuturaCart.updateQuantity('${item.id}', 1)" class="w-6 h-6 flex items-center justify-center text-stone-600 hover:text-black font-bold text-xs">+</button>
            </div>
            <button onclick="window.nuturaCart.removeItem('${item.id}')" class="text-xs text-rose-500 hover:underline ml-2">Xóa</button>
          </div>
        </div>
        <div class="text-right">
          <span class="text-sm font-bold text-[#FF6F78]">${this.formatMoney(item.price * item.quantity)}</span>
        </div>
      </div>
    `).join('');

    subtotalEl.textContent = this.formatMoney(this.getTotalAmount());
  }

  openDrawer() {
    const drawer = document.getElementById('nuturaCartDrawer');
    const overlay = document.getElementById('cartDrawerOverlay');
    if (drawer && overlay) {
      drawer.classList.add('active');
      overlay.classList.add('active');
      document.body.style.overflow = 'hidden';
      if (window.nuturaLenis) window.nuturaLenis.stop();
    }
  }

  closeDrawer() {
    const drawer = document.getElementById('nuturaCartDrawer');
    const overlay = document.getElementById('cartDrawerOverlay');
    if (drawer && overlay) {
      drawer.classList.remove('active');
      overlay.classList.remove('active');
      document.body.style.overflow = '';
      if (window.nuturaLenis) window.nuturaLenis.start();
    }
  }

  bindEvents() {
    document.addEventListener('click', (e) => {
      if (e.target.closest('#openCartBtn') || e.target.closest('.open-cart-btn')) {
        e.preventDefault();
        this.openDrawer();
      }
      if (e.target.closest('#closeCartDrawerBtn') || e.target.id === 'cartDrawerOverlay') {
        this.closeDrawer();
      }
      const addBtn = e.target.closest('.add-to-cart-btn');
      if (addBtn) {
        e.preventDefault();
        const pId = addBtn.dataset.productId;
        const qty = parseInt(addBtn.dataset.quantity || 1, 10);
        if (pId) this.addItem(pId, qty);
      }
    });
  }

  showToast(message) {
    let toast = document.getElementById('nuturaToast');
    if (!toast) {
      toast = document.createElement('div');
      toast.id = 'nuturaToast';
      toast.className = 'toast-notice';
      document.body.appendChild(toast);
    }
    toast.innerHTML = `
      <svg class="w-5 h-5 text-emerald-400 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
      </svg>
      <span>${message}</span>
    `;
    toast.classList.add('show');
    clearTimeout(this.toastTimeout);
    this.toastTimeout = setTimeout(() => {
      toast.classList.remove('show');
    }, 3200);
  }
}

// Breastfeeding Medical Disclaimer System (Tuân thủ y tế quốc tế & WHO)
function initBreastfeedingModal() {
  const DISCLAIMER_KEY = 'nutura_breastfeeding_accepted';
  const hasAccepted = localStorage.getItem(DISCLAIMER_KEY);
  if (hasAccepted) return;

  const modalHTML = `
    <div id="disclaimerModalOverlay" class="disclaimer-modal-overlay" role="dialog" aria-modal="true" aria-labelledby="disclaimerModalTitle">
      <div class="disclaimer-modal-content p-6 sm:p-8" data-lenis-prevent>
        <div class="w-14 h-14 bg-rose-50 text-[#FF6F78] rounded-2xl flex items-center justify-center mb-5" aria-hidden="true">
          <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
          </svg>
        </div>
        <h3 id="disclaimerModalTitle" class="text-xl sm:text-2xl font-bold text-stone-900 mb-3">Thông Báo Quan Trọng Về Sức Khỏe Trẻ Sơ Sinh</h3>
        <p class="text-stone-700 text-sm sm:text-base leading-relaxed mb-4">
          <strong>Sữa mẹ là thức ăn tốt nhất cho sức khỏe và sự phát triển toàn diện của trẻ sơ sinh và trẻ nhỏ.</strong> Sữa mẹ chứa các kháng thể tự nhiên giúp bảo vệ bé trước các bệnh nhiễm khuẩn. Việc tham vấn ý kiến chuyên gia y tế trước khi quyết định phương pháp nuôi dưỡng là điều cần thiết.
        </p>
        <p class="text-stone-600 text-xs sm:text-sm leading-relaxed mb-6">
          Sữa công thức là giải pháp thay thế khi người mẹ không thể cho con bú. Khi sử dụng bình sữa, mẹ nên tham khảo ý kiến bác sĩ hoặc chuyên viên y tế. Việc bổ sung sữa công thức có thể làm giảm lượng sữa mẹ tự nhiên. Bằng cách nhấn nút <strong>"Tôi Đồng Ý & Tiếp Tục"</strong>, bạn xác nhận truy cập website để tham khảo thông tin khoa học và dinh dưỡng giáo dục.
        </p>
        <div class="flex flex-col sm:flex-row gap-3">
          <button id="acceptDisclaimerBtn" class="flex-1 py-3.5 px-6 rounded-full bg-[#FF6F78] hover:bg-[#E65A63] text-white font-bold transition text-sm sm:text-base shadow-lg shadow-[#FF6F78]/30">
            Tôi Đồng Ý & Tiếp Tục
          </button>
          <a href="https://vi.wikipedia.org/wiki/Nu%C3%B4i_con_b%E1%BA%B1ng_s%E1%BB%AFa_m%E1%BA%B9" class="py-3.5 px-6 rounded-full border border-stone-300 font-semibold text-stone-700 hover:bg-stone-100 transition text-sm text-center">
            Tìm Hiểu Về Sữa Mẹ
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
  }, 600);

  if (btn) {
    btn.addEventListener('click', () => {
      localStorage.setItem(DISCLAIMER_KEY, 'true');
      overlay.classList.remove('active');
      if (window.nuturaLenis) window.nuturaLenis.start();
      setTimeout(() => overlay.remove(), 400);
    });
  }
}

// Mobile Menu Navigation Toggle
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

  // Tôn trọng thiết lập hạn chế chuyển động (Accessibility WCAG 2.1 AA)
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

  // Cuộn mượt khi click anchor links #
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

// Global Init on DOM Loaded
document.addEventListener('DOMContentLoaded', () => {
  initLenis();
  window.nuturaCart = new NuturaCart();
  initBreastfeedingModal();
  initMobileMenu();
  initFaqAccordion();
});
