<template>
    <div class="flex flex-col gap-3">
      <TextsTitle :title="'Text summarization'" />
      <UCard>
        <div class="flex flex-col gap-4">
          <div class="flex-1 flex flex-col gap-3">
            <p class="text-lg font-bold">Your text</p>
            <div class="flex items-stretch gap-3">
              <UCard class="flex-auto">
                <UTextarea
                  class="h-full"
                  size="xl"
                  :rows="5"
                  :padded="false"
                  variant="none"
                  autoresize
                  placeholder="Enter your text..."
                  v-model="input_text"
                />
              </UCard>
            </div>
          </div>
          <div class="flex justify-end gap-4">
            <UButton variant="outline" @click="onReset" :disabled="loading">Reset</UButton>
            <UButton
              @click="onSummarize"
              :loading="loading"
              icon="i-heroicons-document-text"
              :disabled="!input_text.trim()"
              >Summarize
            </UButton>
          </div>
          <div v-if="error_message" class="text-red-500 text-sm">
            {{ error_message }}
          </div>
          <div v-else class="flex-1 flex flex-col gap-3">
            <p class="text-lg font-bold">Summary</p>
            <UCard class="card__summary">
              <UTextarea
                class="h-full"
                size="xl"
                :rows="2"
                :padded="false"
                variant="none"
                autoresize
                v-model="summary_text.summary"
              />
              <div>
                <ButtonsClipboard :text-to-copy="summary_text.summary" />
              </div>
            </UCard>
          </div>
        </div>
      </UCard>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref } from 'vue';
  
  const config = useRuntimeConfig();
  const input_text = ref("");
  const summary_text = ref({
    summary: "",
  });
  const loading = ref(false);
  const error_message = ref("");
  
  const onSummarize = async () => {
    error_message.value = ""; // Reset error message
  
    if (!input_text.value.trim()) {
      error_message.value = "Input text cannot be empty.";
      return;
    }
  
    loading.value = true;
  
    try {
      const response = await $fetch<any>(
        config.public.flaskApiUrl + "text_summarization",
        {
          method: "POST",
          body: {
            text: input_text.value,
          },
        }
      );
      summary_text.value.summary = response.summary || "";
    } catch (err: any) {
      console.error("Fetching error :", err);
      error_message.value = err?.data?.message || "An error occurred during summarization.";
    } finally {
      loading.value = false;
    }
  };
  
  const onReset = () => {
    input_text.value = "";
    summary_text.value.summary = "";
    error_message.value = "";
  };
  </script>
  
  <style lang="scss" scoped>
  .card__summary {
    background-color: rgba(175, 175, 175, 0.05);
    box-shadow: none;
  }
  
  .text-red-500 {
    color: #f87171;
    font-size: 0.875rem;
  }
  </style>
  