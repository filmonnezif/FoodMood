<template>
    <div class="landing-page q-mt-none">
      <div class="content">
        <q-avatar size="150px" class="q-ma-sm">
            <img src='https://ucarecdn.com/7710d474-c049-4897-ac48-9e2cf83fe64e/-/preview/500x500/' alt="Liya">
        </q-avatar>
        <h1 class="text-h3 text-weight-bold text-purple q-mb-lg q-mt-none">FoodMood</h1>
        <p class="text-h5 q-mb-lg">Get food based on your mood, time and ingridients you have</p>
        <p class="text-h5 q-mb-lg"> Cook your foods with your choosen character </p>
        <div class="character-avatars">
            <q-avatar size="100px" class="q-ma-sm">
            <img src='https://ucarecdn.com/fdc181ff-1093-4e52-95e9-2a818131831e/-/preview/980x1000/' alt="Gordon Ramsay">
            </q-avatar>
            <q-avatar size="100px" class="q-ma-sm">
            <img src='https://ucarecdn.com/68e18db6-f3b7-466a-8728-6f9fc410bec1/-/preview/916x1000/' alt="Mom">
            </q-avatar>
            <q-avatar size="100px" class="q-ma-sm">
            <img src='https://ucarecdn.com/7ddc4286-42c3-489b-8baa-5ac6f6f1eac6/-/preview/300x300/' alt="Liya">
            </q-avatar>
            <q-avatar size="100px" class="q-ma-sm">
            <img src='https://ucarecdn.com/c950e8b5-c236-45a8-a8c7-250a88b6c54d/-/preview/1000x950/' alt="John">
            </q-avatar>
            <q-avatar size="100px" class="q-ma-sm">
            <img src='https://ucarecdn.com/15478e0d-606a-43c9-858c-40753ab0e162/-/preview/959x1000/' alt="Mike">
            </q-avatar>
            <q-avatar size="100px" class="q-ma-sm">
            <img src= 'https://ucarecdn.com/1c0e418a-2b23-499d-aa3b-bc1cb424ab4b/-/preview/640x640/' alt="Mike">
            </q-avatar>
        </div>
        <q-btn
          rounded
          color="purple"
          label="Get Started"
          size="lg"
          to="/index"
          class="q-px-xl q-py-sm q-mb-lg"
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
  padding: 3rem 2rem; 
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
  margin-bottom: 1rem; // 
}

.character-avatars .q-avatar {
  margin: 10px; 
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2); 
}

.q-btn {
  margin-top: 1rem; 
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}
  
  </style>
  