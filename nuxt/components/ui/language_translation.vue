<template>
  <div class="flex flex-col gap-3">
    <TextsTitle :title="'Language translation'" />
    <UCard>
      <div class="flex flex-col md:flex-row gap-4 items-stretch">
        <div class="flex-1 flex flex-col gap-3">
          <p class="text-lg font-bold">English</p>
          <UCard class="h-auto">
            <div class="flex flex-col justify-between gap-3">
              <UTextarea
                variant="none"
                :rows="4"
                size="xl"
                :padded="false"
                autoresize
                placeholder="Enter your text..."
                v-model="input_text"
                @input="debouncedTranslate"
              />
              <div class="flex justify-between">
                <UButton
                  icon="i-heroicons-x-mark"
                  color="gray"
                  variant="solid"
                  @click="onReset"
                  :disabled="loading"
                />
                <ButtonsClipboard :text-to-copy="input_text" />
              </div>
            </div>
          </UCard>
        </div>
        <div class="flex-1 flex flex-col gap-3 card">
          <p class="text-lg font-bold">Français</p>
          <UCard class="h-auto card__translated">
            <div class="flex flex-col justify-between gap-3">
              <UTextarea
                readonly
                variant="none"
                :rows="4"
                size="xl"
                :padded="false"
                autoresize
                placeholder="Traduction..."
                v-model="result_text.translated"
              />
              <div class="flex justify-between">
                <UButton :loading="loading" color="gray" variant="link" />
                <ButtonsClipboard :text-to-copy="result_text.translated" />
              </div>
            </div>
          </UCard>
        </div>
      </div>
    </UCard>
    <p v-if="error_message" class="text-red-500">{{ error_message }}</p>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import debounce from "lodash/debounce";

const config = useRuntimeConfig();
const input_text = ref("");
const result_text = ref({
  original: "",
  translated: "",
});
const loading = ref(false);
const error_message = ref("");

const debouncedTranslate = debounce(async () => {
  await onTranslate();
}, 500);

const onTranslate = async () => {
  error_message.value = ""; // Reset error message
  if (!input_text.value.trim()) {
    error_message.value = "Input text cannot be empty.";
    return;
  }

  loading.value = true;
  try {
    const response = await $fetch<any>(
      config.public.flaskApiUrl + "language_translation",
      {
        method: "POST",
        body: JSON.stringify({ text: input_text.value }),
      }
    );
    result_text.value.translated = response.translated || "";
  } catch (err: any) {
    console.error("Fetching error:", err);
    error_message.value =
      err?.data?.message || "An error occurred while translating.";
  } finally {
    loading.value = false;
  }
};

const onReset = () => {
  input_text.value = "";
  result_text.value.translated = "";
  error_message.value = "";
};
</script>

<style lang="scss" scoped>
.card__translated {
  background-color: rgba(175, 175, 175, 0.05);
  box-shadow: none;
}

.text-red-500 {
  color: #f87171;
  font-size: 0.875rem;
}
</style>
