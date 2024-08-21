<template>
  <q-layout view="hHh lpR fFf" class="bg-grey-6">
    <q-header elevated class="bg-grey-7 text-black">
      <q-toolbar>
        <q-btn flat dense round icon="menu" @click="toggleLeftDrawer" />
        <q-toolbar-title>FoodMood</q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-drawer class = "bg-grey-7 text-purple" v-model="leftDrawerOpen" show-if-above bordered>
      <q-list>
        <q-item-label header>Navigation</q-item-label>
        <q-item clickable v-ripple to="/page1">
          <q-item-section>Page 1</q-item-section>
        </q-item>
        <q-item clickable v-ripple to="/page2">
          <q-item-section>Page 2</q-item-section>
        </q-item>
        <q-item clickable v-ripple to="/page3">
          <q-item-section>Page 3</q-item-section>
        </q-item>
      </q-list>
    </q-drawer>

    <q-page-container class = "bg-grey-8">
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup>
import { ref } from 'vue';

const leftDrawerOpen = ref(false);

const toggleLeftDrawer = () => {
  leftDrawerOpen.value = !leftDrawerOpen.value;
};
</script>
