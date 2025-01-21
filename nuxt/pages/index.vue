<template>
    <UContainer class="flex flex-col gap-6 md:w-3/5 p-0">
        <div class="title text-green-400">Natural Language Processing</div>
        <UiLanguageTranslation />
        <UiTextSummarization />
        <UiSentimentAnalysis />
    </UContainer>
</template>

<style lang="scss" scoped>
.title {
    font-size: clamp(1rem, 6vw, 3rem);
    font-weight: 700;
}
</style>