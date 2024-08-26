<template>
    <div class="landing-page q-mt-none">
      <div class="content">
        <h1 class="text-h2 text-weight-bold text-purple q-mb-lg q-mt-none">FoodMood</h1>
        <p class="text-h5 q-mb-lg">Get food based on your mood, time and ingridients you have</p>
        <p class="text-h5 q-mb-lg"> Cook your foods with your choosen character </p>
        <div class="character-avatars">
            <q-avatar size="100px" class="q-ma-sm">
            <img src="src/assets/gordan.jpg" alt="Gordon Ramsay">
            </q-avatar>
            <q-avatar size="100px" class="q-ma-sm">
            <img src="src/assets/mom.jpg" alt="Mom">
            </q-avatar>
            <q-avatar size="100px" class="q-ma-sm">
            <img src="src/assets/gff.jpg" alt="Liya">
            </q-avatar>
            <q-avatar size="100px" class="q-ma-sm">
            <img src="src/assets/bf.jpg" alt="John">
            </q-avatar>
            <q-avatar size="100px" class="q-ma-sm">
            <img src="src/assets/gym.jpg" alt="Mike">
            </q-avatar>
            <q-avatar size="100px" class="q-ma-sm">
            <img src="src/assets/gym.jpg" alt="Mike">
            </q-avatar>
        </div>
        <q-btn
          rounded
          color="purple"
          label="Get Started"
          size="lg"
          to="/index"
          class="q-px-xl q-py-sm"
        />
      </div>
    </div>
  </template>
  
  <script setup>
  // No additional script needed for now
  </script>
  
  <style lang="scss" scoped>
.landing-page {
  height: 100vh;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #000000, #37193e);
  color: white;
  text-align: center;
  font-family: 'Open Sans', sans-serif; // new font family
  scrollbar-width: none;
}

.content {
  max-width: 600px;
  padding: 3rem 2rem; // adjusted padding
}

header {
  background: linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.3));
  padding: 1rem;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}

.character-avatars {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  margin-bottom: 2rem; // added margin bottom
}

.character-avatars .q-avatar {
  margin: 10px; // added margin to create some space between avatars
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2); // added box shadow
}

.q-btn {
  margin-top: 2rem; // added margin top to create some space
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2); // added box shadow
}
  
  </style>
  