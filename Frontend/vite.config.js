import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit()],
	server: {
		proxy: {
		  '/api': {
			target: 'https://web-production-ceb18.up.railway.app',
			changeOrigin: true,
			rewrite: (path) => path.replace(/^\/api/, ''),
		  },
		},
	  },
});

// vite.config.js
