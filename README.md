# DEYAMI — 925 Sterling Silver Catalog Website

> *"Wear Your Moments"*

A production-ready, ultra-fast, SEO-optimized digital catalog website for **DEYAMI**, a handcrafted 925 sterling silver jewelry brand.

This is a **curated inquiry catalog** (not an e-commerce cart/checkout): visitors browse hallmarked collections and enquire directly with the studio via WhatsApp or Netlify-protected enquiry forms.

---

## 🌟 Key Architecture & Highlights

- **Static-First Framework**: Built with [Astro 5](https://astro.build/) for static HTML output and sub-second load times.
- **Design Language**: Luxury minimal monochrome (`#0A0A0A`, `#FAFAFA`, subtle `#C0C8D0` silver accent) with generous whitespace, geometric Jost sans-serif headings, Dancing Script tagline accent, and the signature four-point sparkle `✦` motif.
- **Content Collections**: Products (`src/content/products/*.json`) and Collections (`src/content/collections/*.json`) are schema-validated with Zod. Adding a product requires creating one JSON file — zero code changes.
- **Near-Zero Client JavaScript**: Client-side JS is limited to lightweight islands:
  - Responsive slide-over mobile drawer (`MobileMenu.astro`)
  - Interactive product image zoom & lightbox (`ProductGallery.astro`)
  - Instant category & keyword catalog filter (`ProductFilter.astro`)
  - Accessible FAQ accordion (`faq.astro`)
- **Self-Hosted Typography**: Latin subset Google Fonts (Jost and Dancing Script) self-hosted as WOFF2 in `/public/fonts/` with `font-display: swap` for 0 layout shift (CLS ~0).
- **SEO & Structured Data (JSON-LD)**:
  - `JewelryStore` / `Organization` schema
  - `Product` schema (with SKU, hallmarked material, and optional price offer)
  - `FAQPage` schema
  - `BreadcrumbList` schema
  - OpenGraph cards (1200×630) and Twitter Card tags
  - Dynamic `sitemap-index.xml` and `robots.txt`
- **Deploy Ready**: Fully configured for [Netlify](https://www.netlify.com/) with `netlify.toml`, security headers (CSP, X-Frame-Options, HSTS), long-term caching for immutable assets, and Netlify Forms with bot-field honeypot protection.

---

## 📁 Repository Structure

```
deyami-website/
├── public/
│   ├── favicon.ico                   # Standard browser favicon
│   ├── favicon.svg                   # Vector SVG monogram favicon
│   ├── og-image.jpg                  # 1200x630 luxury social card
│   ├── robots.txt                    # Search crawler directions
│   ├── fonts/                        # Self-hosted WOFF2 fonts
│   ├── logo/
│   │   ├── deyami-logo.jpeg          # Original untouched logo
│   │   ├── deyami-logo-transparent.png # Cleaned transparent PNG
│   │   ├── deyami-logo.svg           # High-resolution vector wrapper
│   │   └── deyami-monogram.png       # Extracted D-sparkle badge
│   └── images/
│       ├── collections/              # 6 Collection cover portraits
│       └── products/                 # 24 High-res sample product photos
├── src/
│   ├── config/
│   │   └── site.ts                   # MASTER CONFIG: Brand, WhatsApp, SEO, Prices
│   ├── content/
│   │   ├── collections/              # 6 Collection JSON definitions
│   │   └── products/                 # 12 Sample Product JSON definitions
│   ├── content.config.ts             # Astro 5 Zod schemas & glob loaders
│   ├── components/
│   │   ├── global/                   # Header, Footer, MobileMenu, WhatsAppButton
│   │   ├── home/                     # Hero, Collections, NewArrivals, WhySilver, Story, Testimonials, Instagram
│   │   ├── product/                  # ProductCard, ProductGallery, WhatsAppEnquire, ProductFilter
│   │   ├── seo/                      # Seo.astro, JsonLd.astro
│   │   └── ui/                       # Button, SectionHeading, Sparkle, Breadcrumb
│   ├── layouts/
│   │   └── BaseLayout.astro          # Root HTML layout with fonts & meta
│   ├── pages/
│   │   ├── index.astro               # Homepage
│   │   ├── collections/
│   │   │   ├── index.astro           # Collections overview grid
│   │   │   └── [slug].astro          # Single collection product list
│   │   ├── products/
│   │   │   ├── index.astro           # All Products with instant filter & search
│   │   │   └── [slug].astro          # Product detail with zoom & WhatsApp action
│   │   ├── about.astro               # Brand Story, Philosophy & Symbolism
│   │   ├── contact.astro             # Netlify Form & Studio Info
│   │   ├── faq.astro                 # Accordion FAQs + FAQPage Schema
│   │   ├── guides/
│   │   │   ├── silver-care.astro     # Silver Care, Cleaning & Anti-Tarnish
│   │   │   └── silver-purity.astro   # What 925 Means, BIS Hallmarking & Tests
│   │   ├── success.astro             # Form submission thank-you page
│   │   ├── privacy-policy.astro      # Privacy policy
│   │   ├── terms.astro               # Terms of service
│   │   └── 404.astro                 # Custom 404 error page
│   ├── styles/
│   │   ├── fonts.css                 # Local @font-face declarations
│   │   └── global.css                # Tailwind directives & CSS variables
│   └── utils/
│       ├── whatsapp.ts               # Click-to-chat URL generator
│       └── schema.ts                 # JSON-LD Schema generators
├── cms/
│   └── config.yml                    # Decap CMS (Netlify CMS) ready stub
├── netlify.toml                      # Netlify build, headers, redirects
├── astro.config.mjs                  # Astro configuration & integrations
├── tailwind.config.mjs               # Tailwind design tokens
└── package.json
```

---

## 🚀 Getting Started Locally

### 1. Prerequisites
- **Node.js**: v18.17+ or v20+ (Node v24 tested)
- **NPM**: v9+ (or pnpm / yarn)

### 2. Installation
```bash
# Clone the repository
git clone <your-repo-url>
cd Vipul_Deyami_Website

# Install dependencies
npm install
```

### 3. Run Development Server
```bash
npm run dev
```
Open [http://localhost:4321](http://localhost:4321) in your browser.

### 4. Build for Production
```bash
npm run build
```
The static site will be compiled into the `dist/` folder in ~8 seconds.

### 5. Preview Production Build
```bash
npm run preview
```

---

## ⚙️ How to Customize Branding & Contact Details

All branding, phone numbers, email, WhatsApp numbers, and settings are governed by a **single configuration file**:

👉 `src/config/site.ts`

```typescript
export const siteConfig = {
  name: 'DEYAMI',
  tagline: 'Wear Your Moments',
  url: 'https://deyami.netlify.app',
  
  contact: {
    whatsapp: {
      number: '919876543210',  // <-- TODO: Enter your 10-digit WhatsApp number (with 91 country code, no + or spaces)
      display: '+91 98765 43210',
      defaultMessage: 'Hello DEYAMI, I am interested in exploring your 925 Sterling Silver jewelry collection.',
    },
    phone: '+91 98765 43210',  // <-- TODO: Real studio contact number
    email: 'hello@deyami.com', // <-- TODO: Real studio email address
    address: {
      street: 'Jewelry Quarter, CG Road',
      city: 'Ahmedabad',
      state: 'Gujarat',
      pincode: '380009',
      country: 'India',
      mapsUrl: 'https://maps.google.com/?q=Ahmedabad+Gujarat+India',
    },
    hours: 'Monday – Saturday: 10:30 AM – 8:00 PM IST',
  },

  socials: {
    instagram: 'https://instagram.com/deyami_silver', // <-- TODO: Instagram handle
    facebook: 'https://facebook.com/deyamisilver',
    pinterest: 'https://pinterest.com/deyamisilver',
  },

  settings: {
    showPrices: true, // <-- Set to false to hide all prices and show "Price on Request"
    pricePrefix: 'Starting from ',
    currency: '₹',
    currencyCode: 'INR',
  },
};
```

---

## 💎 How to Add a New Product

Adding a new product does **not** require modifying any layout, component, or routing file!

1. Place 1 or 2 photos of your product in `public/images/products/`:
   - `my-new-piece-1.jpg`
   - `my-new-piece-2.jpg` (optional second angle)
2. Create a new JSON file in `src/content/products/`:
   e.g. `src/content/products/moonlight-drop-choker.json`
3. Fill in the data structure:

```json
{
  "id": "moonlight-drop-choker",
  "name": "Moonlight Drop Sterling Choker",
  "slug": "moonlight-drop-choker",
  "category": "Necklaces",
  "collectionSlug": "necklaces",
  "description": "Silky articulated choker with a delicate suspended silver droplet.",
  "story": "A luminous reminder of moonlit shores and personal serenity.",
  "images": [
    "/images/products/moonlight-drop-choker-1.jpg",
    "/images/products/moonlight-drop-choker-2.jpg"
  ],
  "price": 2800,
  "sku": "DYM-NCK-003",
  "specs": {
    "material": "925 Sterling Silver",
    "hallmark": "925 BIS Hallmarked",
    "weight": "4.8g approx.",
    "size": "15 inches + 2 inch extender",
    "finish": "High-Polish Rhodium Plated (Anti-Tarnish)",
    "gemstone": "None",
    "clasp": "Lobster Claw"
  },
  "tags": ["Choker", "New Arrival", "Bestseller"],
  "featured": true,
  "newArrival": true,
  "inStock": true
}
```

Astro automatically validates the schema and generates `/products/moonlight-drop-choker/` upon next build!

---

## 🌐 Deploying to Netlify (Step-by-Step)

The project includes a ready-to-use `netlify.toml` file.

### Step 1: Push Code to GitHub
```bash
git init
git add .
git commit -m "feat: complete DEYAMI 925 sterling silver catalog website"
git branch -M main
git remote add origin https://github.com/<your-username>/deyami-website.git
git push -u origin main
```

### Step 2: Connect to Netlify
1. Log into [Netlify](https://app.netlify.com/).
2. Click **"Add new site"** > **"Import an existing project"**.
3. Select **GitHub** and authorize access to your `deyami-website` repository.
4. Netlify will auto-detect settings from `netlify.toml`:
   - **Build command**: `npm run build`
   - **Publish directory**: `dist`
5. Click **"Deploy site"**.

### Step 3: Verify Netlify Forms
- The contact form on `/contact` uses Netlify Forms with a honeypot field (`netlify-honeypot="bot-field"`).
- Netlify detects the form automatically on build.
- Submissions will appear in your Netlify Dashboard under **Forms > Submissions**.
- You can configure email or Slack notifications for incoming inquiries in Netlify settings.

### Step 4: Custom Domain & HTTPS
1. In Netlify Dashboard, navigate to **Site configuration > Domain management**.
2. Click **"Add a domain"** and enter your registered domain (e.g. `deyami.com`).
3. Update your domain registrar's DNS records:
   - Apex domain (`@`): Point to Netlify Load Balancer `75.2.60.5`
   - CNAME (`www`): Point to your site's Netlify subdomain (e.g. `deyami.netlify.app`)
4. Netlify will automatically provision a free Let's Encrypt SSL certificate within 24 hours.

---

## 📊 Lighthouse Performance Target Summary

The site has been engineered specifically to achieve **95–100** on Google Lighthouse:

| Metric | Target | How It Is Achieved |
|---|---|---|
| **Performance** | **98 - 100** | Zero render-blocking libraries; pre-rendered static HTML; WOFF2 local fonts |
| **Accessibility** | **100** | Full semantic HTML (`<nav>`, `<article>`, `<dl>`), WCAG AA color contrast, explicit ARIA labels |
| **Best Practices** | **100** | Strong CSP, X-Frame-Options: DENY, HSTS headers, secure `rel="noopener noreferrer"` links |
| **SEO** | **100** | Descriptive metadata, canonical links, OpenGraph, JSON-LD (JewelryStore, Product, FAQPage, BreadcrumbList) |
| **LCP** | **< 1.2s** | Pre-rendered static hero with high-priority responsive assets |
| **CLS** | **~ 0.00** | Explicit width/height on all images, self-hosted fonts with `font-display: swap` |

---

## 📝 Checklist: Items You Must Supply

Before making the website publicly live, replace the following placeholder values:

- [ ] **WhatsApp Business Number**: Update `contact.whatsapp.number` in `src/config/site.ts` with your actual 10-digit number (e.g. `9198XXXXXXXX`).
- [ ] **Contact Phone & Email**: Update `contact.phone` and `contact.email` in `src/config/site.ts`.
- [ ] **Studio Address**: Update street, city, pin code, and Google Maps URL in `src/config/site.ts`.
- [ ] **Social Media Links**: Replace placeholder Instagram, Facebook, and Pinterest URLs.
- [ ] **High-Resolution Product Photography**: Replace placeholder images in `public/images/products/` with real studio photography of each piece.
- [ ] **Custom Domain**: Connect your domain (e.g. `deyami.com` or `deyamisilver.com`) on Netlify.

---

## 🗺️ Future-Proofing Roadmap

The codebase architecture has been intentionally designed to accommodate smooth future scaling:

1. **Decap CMS (Netlify CMS) Integration**:
   - `cms/config.yml` is already written and pre-configured to match our Content Collections.
   - Simply enable Netlify Identity and Git Gateway to give non-technical team members a web dashboard to add products.
2. **Blog / Silver Journal**:
   - Add a `src/content/blog/` collection for styling articles, jewelry care stories, and seasonal trend guides for organic SEO.
3. **Multi-Language Support**:
   - Astro’s built-in i18n routing can be enabled for English, Hindi, and Gujarati with zero architecture changes.
4. **Interactive Ring Size Guide & Lookbook**:
   - Add printable ring sizers and interactive customer styling galleries.
5. **E-Commerce Transition Path**:
   - Because every product already contains `sku`, `price`, `specs`, and `inStock` fields, upgrading to e-commerce (e.g. Razorpay Payment Links, Snipcart, or Shopify Storefront API) requires only adding a checkout button component!

---

© 2026 DEYAMI. Handcrafted 925 Sterling Silver. All rights reserved.
