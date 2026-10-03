/**
 * DEYAMI - Master Site Configuration
 * Single source of truth for branding, contact info, SEO, and navigation.
 * Modify values here without touching any template code.
 */

export interface SiteConfig {
  name: string;
  legalName: string;
  gstin?: string;
  descriptor: string;
  tagline: string;
  subtagline: string;
  url: string;
  ogImage: string;
  logo: {
    original: string;
    transparent: string;
    svg: string;
    monogram: string;
  };
  contact: {
    whatsapp: {
      number: string; // International format without spaces or symbols for wa.me link
      display: string;
      defaultMessage: string;
    };
    phone: string; // Customer care display
    phoneRaw: string; // tel: link format
    email: string;
    address: {
      building: string;
      street: string;
      locality: string;
      landmark: string;
      city: string;
      district: string;
      state: string;
      pincode: string;
      country: string;
      formatted: string;
      mapsUrl: string;
    };
    hours: string;
  };
  socials: {
    instagram: string;
    instagramHandle: string;
    facebook: string;
    pinterest: string;
  };
  settings: {
    showPrices: boolean; // Set to false to hide prices globally and only show "Enquire for Price"
    pricePrefix: string;
    currency: string;
    currencyCode: string;
    enableAnalytics: boolean; // Optional GA4 / Plausible integration
    analyticsId?: string;
  };
  nav: Array<{
    title: string;
    href: string;
  }>;
  seo: {
    defaultTitle: string;
    titleTemplate: string;
    defaultDescription: string;
    keywords: string[];
  };
}

export const siteConfig: SiteConfig = {
  name: 'DEYAMI',
  legalName: 'DEYAMI JEWELS PRIVATE LIMITED',
  gstin: '24AALCD9183H1ZA',
  descriptor: '925 Sterling Silver',
  tagline: 'Wear Your Moments',
  subtagline: 'Timeless handcrafted 925 sterling silver jewelry made for life’s everyday and milestone moments.',
  url: 'https://deyami.netlify.app',
  ogImage: '/og-image.jpg',
  logo: {
    original: '/logo/deyami-logo.jpeg',
    transparent: '/logo/deyami-logo-transparent.png',
    svg: '/logo/deyami-logo.svg',
    monogram: '/logo/deyami-monogram.png',
  },
  contact: {
    whatsapp: {
      number: '918511725925',
      display: '+91 8511 725 925',
      defaultMessage: 'Hello DEYAMI, I am interested in exploring your 925 Sterling Silver jewelry collection.',
    },
    phone: '+91 7383 792 592',
    phoneRaw: '+917383792592',
    email: 'Deyamijewels@gmail.com',
    address: {
      building: '49, YASH GREEN',
      street: '49, Yash Green, Opp. Yash Kutir, Padmnabh Chokdi, Ved Township Road',
      locality: 'Opp. Yash Kutir',
      landmark: 'Ved Township Road',
      city: 'Patan',
      district: 'Patan',
      state: 'Gujarat',
      pincode: '384265',
      country: 'India',
      formatted: '49, Yash Green, Opp. Yash Kutir, Padmnabh Chokdi, Ved Township Road, Patan, Gujarat — 384265, India',
      mapsUrl: 'https://maps.app.goo.gl/5RVo2x2NjUp9eCSh6',
    },
    hours: 'Monday – Saturday: 10:30 AM – 8:00 PM IST',
  },
  socials: {
    instagram: 'https://www.instagram.com/deyamijewels?utm_source=qr&stkn=NTViajIzYzgxemtl',
    instagramHandle: '@deyamijewels',
    facebook: 'https://www.facebook.com/share/1CVeHKBwMU/',
    pinterest: 'https://pinterest.com/deyamijewels',
  },
  settings: {
    showPrices: true, // Toggle true/false to show/hide "Starting from ₹X"
    pricePrefix: 'Starting from ',
    currency: '₹',
    currencyCode: 'INR',
    enableAnalytics: false, // Turn on via env variable or config
    analyticsId: '',
  },
  nav: [
    { title: 'Home', href: '/' },
    { title: 'Collections', href: '/collections' },
    { title: 'All Jewelry', href: '/products' },
    { title: 'Silver Care', href: '/guides/silver-care' },
    { title: 'Purity 925', href: '/guides/silver-purity' },
    { title: 'About Us', href: '/about' },
    { title: 'FAQ', href: '/faq' },
    { title: 'Contact', href: '/contact' },
  ],
  seo: {
    defaultTitle: 'DEYAMI | 925 Sterling Silver Jewelry — Wear Your Moments',
    titleTemplate: '%s | DEYAMI 925 Sterling Silver',
    defaultDescription:
      'Explore handcrafted 925 sterling silver rings, earrings, necklaces, bracelets, anklets, and curated gift sets by DEYAMI. Hallmarked purity, hypoallergenic everyday luxury.',
    keywords: [
      'DEYAMI',
      '925 sterling silver jewelry',
      'silver rings',
      'silver earrings',
      'silver necklaces',
      'silver bracelets',
      'silver anklets',
      'hallmarked 925 silver',
      'hypoallergenic jewelry',
      'silver gifts India',
      'Wear Your Moments',
    ],
  },
};
