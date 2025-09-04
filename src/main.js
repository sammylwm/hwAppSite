import {createApp} from 'vue'
import './style.css'
import App from './App.vue'
import {autoAnimatePlugin} from "@formkit/auto-animate/vue";
import {createRouter, createWebHistory} from "vue-router";
import VueCookies from 'vue-cookies'

const pages = import.meta.glob('./pages/*.vue');

const routes = Object.entries(pages).map(([path, componentImport]) => {
    const name = path
        .split('/')
        .pop()
        ?.replace('.vue', '')

    return {
        path: name.toLowerCase() === 'home' ? '/' : `/${name.toLowerCase()}`,
        name,
        component: componentImport,
    };
});

const router = createRouter({
    history: createWebHistory(),
    routes,
});

const app = createApp(App);
app.use(autoAnimatePlugin);
app.use(router);
app.use(VueCookies);
app.mount('#app');
