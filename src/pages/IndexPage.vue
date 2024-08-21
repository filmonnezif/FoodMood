<template>
  <q-page class="q-pa-md">
    <q-stepper
      v-model="step"
      ref="stepper"
      class = "bg-grey-8"
      animated
      flat
      header-nav
      contracted

    >
      <q-step :name="1" title="Mood" icon="sentiment_satisfied_alt" :done="step > 1" >
        <div class="flex justify-center">
        <q-card class="q-ma-md bg-grey-7" >
          <div class="text-h5 flex justify-center">Mood</div>
          <q-card-section>
            <q-radio v-model="mood" val="happy" label="Happy" color="purple" />
            <q-radio v-model="mood" val="sad" label="Sad" color="purple" />
            <q-radio v-model="mood" val="excited" label="Excited" color="purple" />
            <q-radio v-model="mood" val="tired" label="Tired" color="purple" />
            <q-radio v-model="mood" val="angry" label="Angry" color="purple" />
            <q-radio v-model="mood" val="relaxed" label="Relaxed" color="purple" />
            <q-radio v-model="mood" val="stressed" label="Stressed" color="purple" />
            <q-radio v-model="mood" val="bored" label="Bored" color="purple" />
            <q-radio v-model="mood" val="anxious" label="Anxious" color="purple" />
            <q-radio v-model="mood" val="content" label="Content" color="purple" />
            <q-radio v-model="mood" val="x" label="None of your bizznes" color="purple" />
          </q-card-section>
        </q-card>
      </div>
        <q-stepper-navigation>
          <div class="flex justify-center">
          <q-btn @click="$refs.stepper.next()" color="primary" label="Next" />
          </div>
        </q-stepper-navigation>
      </q-step>

      <q-step :name="2" title="Time" icon="access_time" :done="step > 2">
        <q-card class="q-ma-md bg-grey-7" >
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
        </q-card>
        <q-stepper-navigation>
          <q-btn @click="$refs.stepper.next()" color="primary" label="Next" />
          <q-btn flat @click="$refs.stepper.previous()" color="primary" label="Back" class="q-ml-sm" />
        </q-stepper-navigation>
      </q-step>

      <q-step :name="3" title="Food Type" icon="restaurant_menu" :done="step > 3">
        <q-card class="q-ma-md bg-grey-7" >
          <div class="text-h5 flex justify-center">Type</div>
          <q-card-section>
            <q-option-group
                v-model="foodType"
                :options="[
                  { label: 'Breakfast', value: 'breakfast' },
                  { label: 'Lunch', value: 'lunch' },
                  { label: 'Dinner', value: 'dinner' },
                  { label: 'Snack', value: 'snack' }
                ]"
                color="purple"
                type="radio"
              />          
          </q-card-section>
        </q-card>
        <q-stepper-navigation>
          <q-btn @click="processMood(); $refs.stepper.next()" color="primary" label="Next" />
          <q-btn flat @click="$refs.stepper.previous()" color="primary" label="Back" class="q-ml-sm" />
        </q-stepper-navigation>
      </q-step>

      <q-step :name="4" title="Summary" icon="assignment">
        <q-card class="q-ma-md bg-grey-7">
          <div class="text-h5 flex justify-center">Summary</div>
          <q-card-section>
            <p v-if="result">{{ result }}</p>
            <p v-else>Processing...</p>
          </q-card-section>
        </q-card>
        <q-stepper-navigation>
          <q-btn color="primary" label="Finish" />
          <q-btn flat @click="$refs.stepper.previous()" color="primary" label="Back" class="q-ml-sm" />
        </q-stepper-navigation>
      </q-step>

    </q-stepper>
  </q-page>
</template>

<script setup>
import { ref } from 'vue';
import { api } from 'boot/axios'

defineOptions({
  name: 'IndexPage'
});

const step = ref(1);
const mood = ref(null);
const duration = ref(15);
const foodType = ref(null);

const result = ref('')

const processMood = async () => {
  try {
    const response = await api.post('/process_mood', JSON.stringify({
      mood: mood.value,
      time: duration.value.toString(),
      type: foodType.value
    }), {
      headers: {
        'Content-Type': 'application/json'
      }
    });
    result.value = response.data.result;
  } catch (error) {
    console.error('Error processing mood:', error);
  }
};

</script>
