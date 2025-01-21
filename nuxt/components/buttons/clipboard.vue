<template>
    <div class="flex items-center justify-end gap-2">
        <p v-if="copied" class="text-sm text-gray-400">Copied to clipboard</p>
        <UButton :icon="copied ? 'i-heroicons-check' : 'i-heroicons-document-duplicate'"
            :color="copied ? 'gray' : 'primary'" variant="link" @click="copyToClipBoard" />
    </div>
</template>

<script setup lang="ts">
const props = defineProps<{
    textToCopy: string
}>()

const copied = ref(false)

const copyToClipBoard = () => {
    navigator.clipboard.writeText(props.textToCopy);
    copied.value = true
    setTimeout(() => {
        copied.value = false
    }, 4000);
}
</script>