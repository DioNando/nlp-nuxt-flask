<template>
  <div class="flex flex-col gap-3">
    <TextsTitle :title="'Sentiment analysis'" />
    <UCard>
      <div class="flex flex-col gap-4">
        <div class="flex-1 flex flex-col gap-3">
          <p class="text-lg font-bold">Your text</p>
          <div class="flex items-stretch gap-3">
            <UCard class="flex-auto">
              <UTextarea
                size="xl"
                :rows="2"
                :padded="false"
                variant="none"
                autoresize
                placeholder="Enter your text..."
                v-model="input_text"
                @input="debouncedAnalyseSentiment"
              />
            </UCard>
            <UCard class="flex items-center justify-center card__sentiment">
              <div class="card__emoji">
                <img
                  v-if="result.sentiment_score >= scores[index_zero + 2].value"
                  :src="scores[index_zero + 2].image"
                  :alt="scores[index_zero + 2].alt"
                />
                <img
                  v-else-if="
                    result.sentiment_score >= scores[index_zero + 1].value
                  "
                  :src="scores[index_zero + 1].image"
                  :alt="scores[index_zero + 1].alt"
                />
                <img
                  v-else-if="
                    result.sentiment_score === scores[index_zero].value
                  "
                  :src="scores[index_zero].image"
                  :alt="scores[index_zero].alt"
                />
                <img
                  v-else-if="
                    result.sentiment_score <= scores[index_zero - 1].value
                  "
                  :src="scores[index_zero - 1].image"
                  :alt="scores[index_zero - 1].alt"
                />
                <img
                  v-else-if="
                    result.sentiment_score <= scores[index_zero - 2].value
                  "
                  :src="scores[index_zero - 2].image"
                  :alt="scores[index_zero - 2].alt"
                />
                <img
                  v-else
                  :src="scores[index_zero].image"
                  :alt="scores[index_zero].alt"
                />
              </div>
            </UCard>
          </div>
        </div>
        <div class="flex justify-start gap-4">
          <UButton variant="outline" @click="onReset" :disabled="loading"
            >Reset</UButton
          >
          <UButton
            @click="analyseSentiment"
            :loading="loading"
            icon="i-heroicons-face-smile"
            :disabled="!input_text.trim()"
            >Analyse sentiment
          </UButton>
        </div>
        <div v-if="error_message" class="text-red-500 text-sm">
          {{ error_message }}
        </div>
        <div v-else class="flex flex-col gap-1 text-gray-400 text-sm">
          <span>Sentiment : {{ result.sentiment }}</span>
          <span>Score : {{ result.sentiment_score }}</span>
        </div>
      </div>
    </UCard>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import debounce from "lodash/debounce";

const input_text = ref("");
const result = ref({
  sentiment: "Neutral",
  sentiment_score: 0,
});
const loading = ref(false);
const error_message = ref("");
const config = useRuntimeConfig();

const scores = [
  {
    value: -0.7,
    image:
      "https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Loudly%20Crying%20Face.png",
    alt: "Loudly Crying Face",
  },
  {
    value: -0.1,
    image:
      "https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Disappointed%20Face.png",
    alt: "Disappointed Face",
  },
  {
    value: 0,
    image:
      "https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Face%20Without%20Mouth.png",
    alt: "Face Without Mouth",
  },
  {
    value: 0.1,
    image:
      "https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Beaming%20Face%20with%20Smiling%20Eyes.png",
    alt: "Beaming Face with Smiling Eyes",
  },
  {
    value: 0.7,
    image:
      "https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Face%20with%20Tears%20of%20Joy.png",
    alt: "Face with Tears of Joy",
  },
];

const index_zero = scores.findIndex((e) => e.value === 0);

const debouncedAnalyseSentiment = debounce(async () => {
  await analyseSentiment();
}, 500);

const analyseSentiment = async () => {
  error_message.value = ""; // Reset error message

  if (!input_text.value.trim()) {
    error_message.value = "Input text cannot be empty.";
    return;
  }

  loading.value = true;
  try {
    const response = await $fetch<any>(
      config.public.flaskApiUrl + "sentiment_analysis",
      {
        method: "POST",
        body: JSON.stringify({ text: input_text.value }),
      }
    );
    result.value = {
      sentiment: response.sentiment || "Neutral",
      sentiment_score: response.sentiment_score || 0,
    };
  } catch (err: any) {
    console.error("Fetching error:", err);
    error_message.value =
      err?.data?.message || "An error occurred during sentiment analysis.";
  } finally {
    loading.value = false;
  }
};

const onReset = () => {
  input_text.value = "";
  result.value = {
    sentiment: "Neutral",
    sentiment_score: 0,
  };
  error_message.value = "";
};
</script>

<style lang="scss" scoped>
.card__sentiment {
  background-color: rgba(175, 175, 175, 0.05);
  box-shadow: none;

  .card__emoji img {
    width: 4rem;
    aspect-ratio: 1/1;
  }
}

.text-red-500 {
  color: #f87171;
  font-size: 0.875rem;
}
</style>
