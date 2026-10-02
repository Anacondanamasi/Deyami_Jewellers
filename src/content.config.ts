import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const products = defineCollection({
  loader: glob({ pattern: '**/*.json', base: './src/content/products' }),
  schema: z.object({
    id: z.string(),
    name: z.string(),
    slug: z.string(),
    category: z.string(),
    collectionSlug: z.string(),
    description: z.string(),
    story: z.string().optional(),
    images: z.array(z.string()),
    price: z.number().optional(),
    sku: z.string(),
    specs: z.object({
      material: z.string().default('925 Sterling Silver'),
      hallmark: z.string().default('925 BIS Hallmarked'),
      weight: z.string(),
      size: z.string(),
      finish: z.string(),
      gemstone: z.string().optional(),
      clasp: z.string().optional(),
    }),
    tags: z.array(z.string()).default([]),
    featured: z.boolean().default(false),
    newArrival: z.boolean().default(false),
    inStock: z.boolean().default(true),
  }),
});

const collectionsList = defineCollection({
  loader: glob({ pattern: '**/*.json', base: './src/content/collections' }),
  schema: z.object({
    id: z.string(),
    name: z.string(),
    slug: z.string(),
    tagline: z.string(),
    description: z.string(),
    image: z.string(),
    featured: z.boolean().default(true),
    order: z.number().default(1),
  }),
});

export const collections = {
  products,
  collections: collectionsList,
};
