/**
 * DEYAMI - Master Site Configuration
 * Single source of truth for branding, contact info, SEO, and navigation.
 * Modify values here without touching any template code.
 */

export interface SiteConfig {
  name: string;
  legalName: string;
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
      number: string; // International format without spaces or symbols for wa.me link (TODO: Replace with owner's number)
      display: string;
      defaultMessage: string;
    };
    phone: string;
    email: string;
    address: {
      street: string;
      city: string;
      state: string;
      pincode: string;
      country: string;
      mapsUrl: string;
    };
    hours: string;
  };
  socials: {
    instagram: string;
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
  legalName: 'DEYAMI Silver Studio',
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
      number: '919876543210', // TODO: Replace with real WhatsApp number (e.g. 919825000000)
      display: '+91 98765 43210', // TODO: Replace with formatted WhatsApp display number
      defaultMessage: 'Hello DEYAMI, I am interested in exploring your 925 Sterling Silver jewelry collection.',
    },
    phone: '+91 98765 43210', // TODO: Replace with real contact phone number
    email: 'hello@deyami.com', // TODO: Replace with real email address
    address: {
      street: 'Jewelry Quarter, CG Road', // TODO: Replace with real store / studio address
      city: 'Ahmedabad',
      state: 'Gujarat',
      pincode: '380009',
      country: 'India',
      mapsUrl: 'https://maps.google.com/?q=Ahmedabad+Gujarat+India', // TODO: Replace with Google Maps link
    },
    hours: 'Monday – Saturday: 10:30 AM – 8:00 PM IST',
  },
  socials: {
    instagram: 'https://instagram.com/deyami_silver', // TODO: Replace with real Instagram profile
    facebook: 'https://facebook.com/deyamisilver', // TODO: Replace with real Facebook page
    pinterest: 'https://pinterest.com/deyamisilver', // TODO: Replace with real Pinterest profile
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
