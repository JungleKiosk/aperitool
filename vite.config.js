import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig({
  // Base path for the application, useful for deployment in subdirectories
  base: '/aperitool/',
  plugins: [vue()],
})
