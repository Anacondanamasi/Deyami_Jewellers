import { siteConfig } from '../config/site';

export function getOrganizationSchema() {
  return {
    '@context': 'https://schema.org',
    '@type': 'JewelryStore',
    name: siteConfig.name,
    legalName: siteConfig.legalName,
    url: siteConfig.url,
    logo: `${siteConfig.url}${siteConfig.logo.transparent}`,
    image: `${siteConfig.url}${siteConfig.ogImage}`,
    description: siteConfig.seo.defaultDescription,
    telephone: siteConfig.contact.phone,
    email: siteConfig.contact.email,
    address: {
      '@type': 'PostalAddress',
      streetAddress: siteConfig.contact.address.street,
      addressLocality: siteConfig.contact.address.city,
      addressRegion: siteConfig.contact.address.state,
      postalCode: siteConfig.contact.address.pincode,
      addressCountry: siteConfig.contact.address.country,
    },
    openingHoursSpecification: [
      {
        '@type': 'OpeningHoursSpecification',
        dayOfWeek: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
        opens: '10:30',
        closes: '20:00',
      },
    ],
    sameAs: [
      siteConfig.socials.instagram,
      siteConfig.socials.facebook,
      siteConfig.socials.pinterest,
    ],
    priceRange: '₹₹',
  };
}

export function getProductSchema(product: {
  name: string;
  description: string;
  images: string[];
  sku: string;
  price?: number;
  slug: string;
  category: string;
}) {
  const schema: any = {
    '@context': 'https://schema.org',
    '@type': 'Product',
    name: product.name,
    description: product.description,
    image: product.images.map((img) => `${siteConfig.url}${img}`),
    sku: product.sku,
    category: product.category,
    brand: {
      '@type': 'Brand',
      name: siteConfig.name,
    },
    material: '925 Sterling Silver',
  };

  // Only include price offer if showPrices is active and product has a price
  if (siteConfig.settings.showPrices && product.price) {
    schema.offers = {
      '@type': 'Offer',
      price: product.price,
      priceCurrency: siteConfig.settings.currencyCode,
      availability: 'https://schema.org/InStock',
      url: `${siteConfig.url}/products/${product.slug}`,
      itemCondition: 'https://schema.org/NewCondition',
      seller: {
        '@type': 'JewelryStore',
        name: siteConfig.name,
      },
    };
  }

  return schema;
}

export function getBreadcrumbSchema(items: Array<{ name: string; url: string }>) {
  return {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: items.map((item, index) => ({
      '@type': 'ListItem',
      position: index + 1,
      name: item.name,
      item: item.url.startsWith('http') ? item.url : `${siteConfig.url}${item.url}`,
    })),
  };
}

export function getFaqSchema(faqs: Array<{ question: string; answer: string }>) {
  return {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: faqs.map((faq) => ({
      '@type': 'Question',
      name: faq.question,
      acceptedAnswer: {
        '@type': 'Answer',
        text: faq.answer,
      },
    })),
  };
}
