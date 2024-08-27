<template>
  <q-layout view="hHh lpR fFf" class="bg-grey-10">
    <q-header v-if="!isLandingPage" elevated class="modern-header">
      <q-toolbar>
        <!--<q-btn flat dense round icon="menu" @click="toggleLeftDrawer" />-->
        <q-avatar size="50px" class="q-ma-sm">
            <img src='https://ucarecdn.com/7710d474-c049-4897-ac48-9e2cf83fe64e/-/preview/500x500/' alt="Liya">
        </q-avatar>
        <q-toolbar-title>FoodMood</q-toolbar-title>
      </q-toolbar>
    </q-header>

    <!--<q-drawer v-if="!isLandingPage" v-model="leftDrawerOpen" show-if-above bordered class="bg-grey-10">
      <q-list>
        <q-item-label header>Navigation</q-item-label>
        <q-item clickable v-ripple to="/page1">
          <q-item-section>Page 1</q-item-section>
        </q-item>
        <q-item clickable v-ripple to="/page2">
          <q-item-section>This is ugly</q-item-section>
        </q-item>
        <q-item clickable v-ripple to="/page3">
          <q-item-section>This navigation will be changed</q-item-section>
        </q-item>
      </q-list>
    </q-drawer>-->

    <q-page-container :class="[isLandingPage ? 'fullscreen-container' : '']">
      <div :class="[isLandingPage ? '' : 'cont']">
        <router-view />
      </div>
    </q-page-container>
  </q-layout>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useRoute } from 'vue-router';

const leftDrawerOpen = ref(false);
const route = useRoute();

const isLandingPage = computed(() => route.name === 'landing');

const toggleLeftDrawer = () => {
  leftDrawerOpen.value = !leftDrawerOpen.value;
};
</script>

<style lang="scss">
.modern-header {
  background: linear-gradient(135deg, #171717, #402840);
  border-radius: 10px 10px 0 0;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);

  .q-toolbar {
    height: 70px;
  }

  .menu-btn {
    color: white;
    font-size: 1.2rem;
  }

  .header-title {
    font-weight: 600;
    color: white;
    font-size: 1.5rem;
    letter-spacing: 0.5px;
  }
}

.fullscreen-container {
  height: 100vh;
  width: 100vw;
  overflow-y: auto;
  padding: 0;
  margin: 0;
}

.cont {
  max-width: 600px;
  margin: 0 auto;
  padding: 0;
}

.q-drawer {
  .q-list {
    padding: 0;
  }

  .q-item {
    padding: 10px 16px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);

    &:last-child {
      border-bottom: none;
    }

    .q-item-section {
      font-size: 1.1rem;
      font-weight: 500;
      color: white;
    }
  }
}

@media screen and (max-width: 600px) {
  .q-layout {
    height: 100vh;
    width: 100vw;
    overflow: auto;
  }

  .cont {
    max-width: 100vw;
    margin: 0;
    padding: 0;
  }
}
</style>