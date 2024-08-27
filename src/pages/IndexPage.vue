<template>
  <q-page class="q-pa-md">
    <q-stepper
      v-model="step"
      ref="stepper"
      class = "bg-grey-10"
      animated
      flat
      header-nav
      @update:model-value="onStepChange"
      >
      <q-step :name="1" title="Mood" icon="sentiment_satisfied_alt" :done="step > 1" >
        <div class="flex justify-center">
        <q-card class="q-ma-md bg-grey-9 modern-card" >
          <div class="text-h5 flex justify-center">Mood</div>
          <q-card-section>
            <q-radio v-model="mood" val="tired" label="Tired 😴" color="purple" />
            <q-radio v-model="mood" val="happy" label="Happy 😃" color="purple" />
            <q-radio v-model="mood" val="sad" label="Sad 😔" color="purple" />
            <q-radio v-model="mood" val="bored" label="Bored 😒" color="purple" />
            <q-radio v-model="mood" val="angry" label="Angry 😠" color="purple" />
            <q-radio v-model="mood" val="relaxed" label="Relaxed 😌" color="purple" />
            <q-radio v-model="mood" val="lazy" label="Lazy 🥱" color="purple" />
            <q-radio v-model="mood" val="sleepy" label="Sleepy 😴" color="purple" />
            <q-radio v-model="mood" val="anxious" label="Anxious 😰" color="purple" />
            <q-radio v-model="mood" val="fancy" label="Fancy 😎" color="purple" />
            <q-radio v-model="mood" val="content" label="Content 😊" color="purple" />
            <q-radio v-model="mood" val="Not specified" label="None of your bizznes" color="purple" />
          </q-card-section>
        </q-card>
      </div>
      <q-card class="q-ma-md bg-grey-9 modern-card" >
          <div class="text-h5 flex justify-center">Time</div>
          <q-card-section>
            <q-slider
              v-model="duration"
              :min="15"
              :max="60"
              :step="5"
              label
              label-always
              color="purple"
              :label-value="`${duration} min`"
            />
          </q-card-section>
          <div class="q-pa-md text-white">How much time do you have to cook?</div>

        </q-card>
        <q-card class="q-ma-md bg-grey-9 modern-card">
          <div class="text-h5 flex justify-center">Ingridients</div>
          <q-card-section>
            <div v-for="(item, index) in items" :key="index" class="q-pa-sm">
              {{ item }}
              <q-btn round color="purple" flat dense icon="close" @click="removeItem(index)" class="float-right" />
            </div>
          </q-card-section>

          <q-card-section>
            <div class="q-pa-sm">
              <q-input
                  v-model="newItem"
                  light
                  dense
                  outlined
                  rounded
                  label="Add the ingredients you have"
                  label-color="white"
                  color="purple"
                  input-class="text-white"
                  @keyup.enter="addItem"
                  class="bg-grey-9 rounded-borders text-white"
                >
                  <template v-slot:append>
                    <q-btn color="white" round dense flat icon="add" @click="addItem" />
                  </template>
                </q-input>
                <div class="text-purple">To add your ingredients click Enter or the plus icon!</div>
            </div>
          </q-card-section>
        </q-card>
        <q-card class="q-ma-md bg-grey-9 modern-card" >
          <div class="text-h5 flex justify-center">Type</div>
          <q-card-section>
            <q-option-group
                v-model="foodType"
                :options="[
                  { label: 'Breakfast', value: 'breakfast' },
                  { label: 'Lunch', value: 'lunch' },
                  { label: 'Dinner', value: 'dinner' },
                  { label: 'Snack', value: 'snack' },
                  { label: 'I just wanna eat', value: 'Not specified' }
                ]"
                color="purple"
                type="radio"
                inline
              />          
          </q-card-section>
        </q-card>
        <div class="flex justify-center">
        <q-btn color="purple" rounded label="Done" @click="handleDoneClick" />
        </div>
      </q-step>
      <q-step :name="2" title="Food" icon="assignment">
        <q-card class="bg-grey-9 modern-card" v-if="recipes.length === 0">
          <q-item>
            <q-item-section>
              <q-item-label>
                <q-skeleton type="text-h5" />
              </q-item-label>
              <q-item-label caption>
                <q-skeleton type="text" />
                <q-skeleton type="text" />
              </q-item-label>
            </q-item-section>
          </q-item>

          <q-skeleton height="200px" square />
          <q-item>
            <q-item-section>
              <q-item-label caption>
                <q-skeleton type="text" />
                <q-skeleton type="text" />
              </q-item-label>
            </q-item-section>
          </q-item>

          <q-card-actions align="center" class="q-gutter-md">
            <q-skeleton type="QBtn" />
          </q-card-actions>
        </q-card>

        <q-card v-else class="bg-grey-9 modern-card">
          <q-carousel
              v-model="currentRecipeIndex"
              transition-prev="slide-right"
              transition-next="slide-left"
              swipeable
              animated
              control-color="purple"
              navigation
              padding
              arrows
              height="70vh"
              class="bg-grey-9 shadow-1 rounded-borders"
            >
            <q-carousel-slide v-for="(recipe, index) in recipes" :key="index" :name="index" class="column no-wrap bg-grey-9">
              <div class="text-h5 flex justify-center">{{ recipe.name }}</div>
              <q-card-section >
                <div class="q-pt-md q-pb-none">
                  <p>{{ recipe.description }}</p>
                  <q-img  class= 'rounded-borders' :src="recipe.image" style="height: 200px; max-width: 100%; object-fit: cover;" />
                  <p>Time to cook: {{ recipe.cookTime }}</p>
                  <p>Nutrition: {{ recipe.nutrition }}</p>
                </div>
              </q-card-section>
            </q-carousel-slide>
          </q-carousel>
          <q-card-actions align="center">
            <q-btn color="primary" label="Cook This!" @click="cookRecipe" />
          </q-card-actions>
        </q-card>
        <q-card v-if="isLoading" class="q-mt-md bg-grey-9 modern-card">
          <q-card-section>
            <div class="text-h6"><q-skeleton type="text" width="200px" /></div>
            <q-skeleton type="text" class="q-mb-md" />
            <q-skeleton type="text" width="90%" class="q-mb-xs" />
            <q-skeleton type="text" width="80%" class="q-mb-xs" />
            <q-skeleton type="text" width="95%" class="q-mb-xs" />
            <q-skeleton type="text" width="75%" class="q-mb-xs" />
          </q-card-section>
        </q-card>
        <q-card v-if="avatarResponse" class="q-mt-md bg-grey-9 modern-card">
          <q-card-section>
            <div class="text-h6">
              <q-item>
                <q-item-section avatar>
                  <q-avatar>
                    <img :src="selectedAvatar.image">
                  </q-avatar>
                </q-item-section>
                <q-item-section>{{ selectedAvatar.name }}</q-item-section>
              </q-item>
            </div>
            <p>{{ avatarResponse.small_talk }}</p>
            <q-list>
              <q-expansion-item
                group="steps"
                v-for="(step, index) in avatarResponse.steps"
                :key="index"
                :label="`Step ${index + 1}: ${step.short_instruction}`"
                header-class="text-white"
                :default-opened="index === 0"
                :ref="el => { if (el) stepRefs[`step${index}`] = el }"
                >
                <q-card class="bg-grey-10 modern-card">
                  <q-card-section>
                    <p>{{ step.detailed_instruction }}</p>
                    <q-checkbox v-model="step.completed" label="Mark as completed" color="purple" keep-color @click="handleStepCompletion(index)"
                    />
                  </q-card-section>
                </q-card>
              </q-expansion-item>
            </q-list>
            <p v-if="allStepsCompleted">{{ avatarResponse.congratulation }}</p>
          </q-card-section>
        </q-card>
        <div ref="pageBottom"></div>
      </q-step>


    </q-stepper>

    <q-dialog v-model="showAvatarDialog">
      <q-card class="bg-grey-10 text-white" style="width: 700px; max-width: 80vw;">
        <q-card-section>
          <div class="text-h6">Cook with:</div>
        </q-card-section>
        <q-card-section class="q-pt-none">
          <div class="row q-col-gutter-md">
            <div v-for="avatar in avatars" :key="avatar.name" class="col-12 col-sm-6">
              <q-item clickable v-ripple @click="selectAvatar(avatar.value)">
                <q-item-section avatar>
                  <q-avatar>
                    <img :src="avatar.image">
                  </q-avatar>
                </q-item-section>
                <q-item-section>
                  <q-item-label>{{ avatar.name }}</q-item-label>
                  <q-item-label class= "text-white" caption>{{ avatar.description }}</q-item-label>
                </q-item-section>
              </q-item>
            </div>
          </div>
        </q-card-section>
      </q-card>
    </q-dialog>

    <q-dialog v-model="showIncompleteFieldsDialog" persistent rounded>
      <q-card class="bg-grey-10 text-white">
        <q-card-section>
          <div class="text-h6">Incomplete Fields</div>
        </q-card-section>
        <q-card-section class="q-pt-none">
          Please fill in the following fields:
          <ul>
            <li v-for="field in incompleteFields" :key="field">{{ field }}</li>
          </ul>
        </q-card-section>
        <q-card-actions align="right" class="bg-grey-10 text-white" >
          <q-btn color="purple" label="OK" v-close-popup />
        </q-card-actions>
      </q-card>
    </q-dialog>


  </q-page>

</template>

<script setup>
import { ref, computed, nextTick } from 'vue';
import { api } from 'boot/axios'

defineOptions({
  name: 'IndexPage'
});

const step = ref(1);
const mood = ref(null);
const duration = ref(15);
const foodType = ref(null);
const items = ref([]);
const newItem = ref('');
const recipes = ref([]);
const currentRecipeIndex = ref(0);
const showIncompleteFieldsDialog = ref(false);
const incompleteFields = ref([]);

const checkAllFieldsFilled = () => {
  incompleteFields.value = [];
  if (!mood.value) incompleteFields.value.push('Mood');
  if (items.value.length === 0) incompleteFields.value.push('Ingredients');
  if (!foodType.value) incompleteFields.value.push('Food Type');
  return incompleteFields.value.length === 0;
};

const handleDoneClick = () => {
  if (checkAllFieldsFilled()) {
    getRecipe();
    step.value = 2;
  } else {
    showIncompleteFieldsDialog.value = true;
  }
};

const onStepChange = (newStep) => {
  if (newStep === 2) {
    if (checkAllFieldsFilled()) {
      step.value = 2;
    } else {
      showIncompleteFieldsDialog.value = true;
      nextTick(() => {
        step.value = 1;
      });
    }
  }
}


const getRecipe = async () => {
  recipes.value = [];
  try {
    const response = await api.post('/get_recipe', {
      mood: mood.value,
      duration: duration.value,
      ingredients: items.value,
      foodType: foodType.value
    });
    console.log(response.data);
    recipes.value = response.data.recipes;
;

  } catch (error) {
    console.error('Error fetching recipe:', error);
    recipes.value = [];
  } 
};


const showAvatarDialog = ref(false);
const avatars = [
  { name:"Gordan Ramsey",value: 'Gordon_Ramsey', image: 'https://ucarecdn.com/fdc181ff-1093-4e52-95e9-2a818131831e/-/preview/980x1000/', description: 'The world-renowned chef' },
  { name: "Hareg", value: 'Habeshan_Mom', image: 'https://ucarecdn.com/68e18db6-f3b7-466a-8728-6f9fc410bec1/-/preview/916x1000/', description: 'Loving Ethiopian mother with traditional cooking wisdom' },
  { name: "Liya", value: 'Supportive_GF', image: 'https://ucarecdn.com/7ddc4286-42c3-489b-8baa-5ac6f6f1eac6/-/preview/300x300/', description: 'Your imaginary habesha girlfriend who loves cooking' },
  { name: "John", value: 'Supportive_BF', image: 'https://ucarecdn.com/c950e8b5-c236-45a8-a8c7-250a88b6c54d/-/preview/1000x950/', description: 'Your imaginary habesha boyfriend who enjoys helping in the kitchen' },
  { name: "Mike", value: 'Gym_Bro', image: 'https://ucarecdn.com/15478e0d-606a-43c9-858c-40753ab0e162/-/preview/959x1000/', description: 'A gym bro who loves cooking and woking out' },
  { name: "Filmon", value: 'Filmon', image: 'https://ucarecdn.com/1c0e418a-2b23-499d-aa3b-bc1cb424ab4b/-/preview/640x640/', description: 'A lazy college student who hates cooking' },
];
const selectedAvatar = ref('');
const avatarResponse = ref(null);
const isLoading = ref(false);
const pageBottom = ref(null);
const avatarName = ref('');
const stepRefs = ref({});

    
const cookRecipe = async () => {
  showAvatarDialog.value = true;
};

const allStepsCompleted = computed(() => {
  return avatarResponse.value && avatarResponse.value.steps.every(step => step.completed);
});

const selectAvatar = async (avatar) => {
  selectedAvatar.value = avatars.find(a => a.value === avatar);
  showAvatarDialog.value = false;
  avatarResponse.value = null;
  isLoading.value = true;
  await nextTick();
  pageBottom.value?.scrollIntoView({ behavior: 'smooth' });
  
  try {
    const selectedRecipe = recipes.value[currentRecipeIndex.value];
    const response = await api.post('/cook_with_avatar', {
      avatar: selectedAvatar.value.value,
      mood: mood.value,
      duration: duration.value,
      ingredients: items.value,
      foodType: foodType.value,
      recipe: selectedRecipe
    });
    avatarResponse.value = response.data;
    avatarResponse.value.steps.forEach(step => step.completed = false);
    console.log(response.data);

  } catch (error) {
    console.error('Error cooking with avatar:', error);
    avatarResponse.value = null;
  } finally {
    isLoading.value = false;
    await nextTick();
    pageBottom.value?.scrollIntoView({ behavior: 'smooth' });
  }
};

const addItem = () => {
  if (newItem.value.trim()) {
    items.value.unshift(newItem.value.trim())
    newItem.value = ''
  }
}

const removeItem = (index) => {
  items.value.splice(index, 1)
}
const handleStepCompletion = (index) => {
  nextTick(() => {
    avatarResponse.value.steps[index].completed = true;
    
    if (index < avatarResponse.value.steps.length - 1) {
      const nextStepRef = `step${index + 1}`;
      if (stepRefs.value[nextStepRef]) {
        stepRefs.value[nextStepRef].show();
      }
    }
  });
};

</script>
<style lang="scss">
.q-stepper__tab--active {
    color: white;
    .q-stepper__dot {
    background: purple;
    }
  }
.q-stepper__tab--done {
    color: purple;
    
    .q-stepper__dot {
      background: purple;
    }
  }
.modern-card {
  border-radius: 16px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  transition: all 0.3s ease;
  color: rgb(228, 225, 225);
  &:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
  }

  .q-card-section {
    padding: 20px;
  }

  .q-radio {
    margin-bottom: 10px;
  }
}
.q-stepper {
  .q-stepper__step-inner {
    padding: 20px;
  }
}

</style>

