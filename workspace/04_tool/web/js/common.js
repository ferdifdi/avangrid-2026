/* Shared UI helpers */
const COLORS = {
  bus: '#f5b301', busDark: '#b98500', charge: '#0ea371', discharge: '#f06a1d',
  grid: '#2f6fe4', reserve: '#8b5cf6', ink: '#111827', ink2: '#4b5563', ink3: '#8a93a3', line: '#e6e3da'
};

if (window.Chart) {
  Chart.defaults.font.family = "'Inter', system-ui, sans-serif";
  Chart.defaults.font.size = 12;
  Chart.defaults.color = COLORS.ink2;
  Chart.defaults.borderColor = '#ece9e0';
  Chart.defaults.plugins.legend.labels.boxWidth = 12;
  Chart.defaults.plugins.legend.labels.boxHeight = 12;
  Chart.defaults.plugins.tooltip.backgroundColor = '#111827';
  Chart.defaults.plugins.tooltip.padding = 10;
  Chart.defaults.animation.duration = 450;
  Chart.defaults.maintainAspectRatio = false;
}

const HOUR_LABELS = HOURS.map((h) => hourLabel(h));

/* Shade route hours behind a chart + optional "now" line. */
const routeShadePlugin = {
  id: 'routeShade',
  beforeDatasetsDraw(chart, args, opts) {
    if (!opts || !opts.on) return;
    const { ctx, chartArea, scales } = chart;
    const x = scales.x;
    if (!x) return;
    ctx.save();
    ROUTE_BLOCKS.forEach((b) => {
      const w = (x.getPixelForValue(1) - x.getPixelForValue(0));
      const x0 = opts.edge ? x.getPixelForValue(b[0]) : x.getPixelForValue(b[0]) - w / 2;
      const x1 = opts.edge ? x.getPixelForValue(b[b.length - 1] + 1) : x.getPixelForValue(b[b.length - 1]) + w / 2;
      ctx.fillStyle = 'rgba(245,179,1,.12)';
      ctx.fillRect(x0, chartArea.top, x1 - x0, chartArea.bottom - chartArea.top);
    });
    if (opts.peak) {
      const w = (x.getPixelForValue(1) - x.getPixelForValue(0));
      const x0 = x.getPixelForValue(16) - w / 2, x1 = x.getPixelForValue(20) + w / 2;
      ctx.fillStyle = 'rgba(240,106,29,.06)';
      ctx.fillRect(x0, chartArea.top, x1 - x0, chartArea.bottom - chartArea.top);
    }
    ctx.restore();
  },
  afterDatasetsDraw(chart, args, opts) {
    if (!opts || opts.now == null) return;
    const { ctx, chartArea, scales } = chart;
    const x = scales.x;
    const px = x.getPixelForValue(0) + (x.getPixelForValue(1) - x.getPixelForValue(0)) * (opts.edge ? opts.now : opts.now - 0.5);
    ctx.save();
    ctx.strokeStyle = COLORS.ink; ctx.lineWidth = 1.5; ctx.setLineDash([4, 3]);
    ctx.beginPath(); ctx.moveTo(px, chartArea.top); ctx.lineTo(px, chartArea.bottom); ctx.stroke();
    ctx.restore();
  }
};
if (window.Chart) Chart.register(routeShadePlugin);

/* Scroll progress + reveal on scroll */
document.addEventListener('DOMContentLoaded', () => {
  const bar = document.getElementById('progress');
  if (bar) {
    const upd = () => {
      const h = document.documentElement;
      bar.style.width = (100 * h.scrollTop / Math.max(1, h.scrollHeight - h.clientHeight)) + '%';
    };
    window.addEventListener('scroll', upd, { passive: true }); upd();
  }
  const els = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver((ents) => ents.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { threshold: 0.12 });
    els.forEach((el) => io.observe(el));
  } else els.forEach((el) => el.classList.add('in'));
});

function debounce(fn, ms) { let t; return (...a) => { clearTimeout(t); t = setTimeout(() => fn(...a), ms); }; }
