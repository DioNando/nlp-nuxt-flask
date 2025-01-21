<template>
    <div class="mt-3">
        <p class="title text-green-600">{{ props.title }}</p>
    </div>
</template>

<script setup lang="ts">
const props = defineProps<{
    title: string
}>()
</script>

<style lang="scss" scoped>
@import "~/assets/scss/style.scss";

.title {
    font-size: clamp(1rem, 5vw, 2rem);
    font-weight: 900;
}
</style>