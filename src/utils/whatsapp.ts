import { siteConfig } from '../config/site';

export interface WhatsAppEnquiryParams {
  productName?: string;
  productSku?: string;
  productUrl?: string;
  collectionName?: string;
  customMessage?: string;
}

/**
 * Generates a direct WhatsApp click-to-chat URL with pre-filled message.
 */
export function getWhatsAppUrl(params?: WhatsAppEnquiryParams): string {
  const number = siteConfig.contact.whatsapp.number;
  let text = siteConfig.contact.whatsapp.defaultMessage;

  if (params?.productName) {
    text = `Hello DEYAMI, I am enquiring about the *${params.productName}*`;
    if (params.productSku) {
      text += ` (SKU: ${params.productSku})`;
    }
    if (params.productUrl) {
      text += `.\n\nProduct Link: ${params.productUrl}`;
    }
    text += `\n\nCould you please share availability, sizing details, and price?`;
  } else if (params?.collectionName) {
    text = `Hello DEYAMI, I would like to enquire about your *${params.collectionName}* collection.`;
  } else if (params?.customMessage) {
    text = params.customMessage;
  }

  const encoded = encodeURIComponent(text);
  return `https://wa.me/${number}?text=${encoded}`;
}
